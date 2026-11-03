class RefreshService
  %w[alpha beta].each do |kind|
    define_method("run_#{kind}") { perform_kind(kind) }
  end

  def perform_kind(kind)
    RefreshJob.perform_async(kind)
  end

  def start
    run_alpha
    send(:perform_kind, 'gamma')
    Object.const_get('Checklist').new.item_total
    Stage.where(name: 'x').first
    ActiveGraph::Base.query('MATCH (p:Stage)-[:HAS_CHECKLIST]->(r) RETURN r')
  end
end
