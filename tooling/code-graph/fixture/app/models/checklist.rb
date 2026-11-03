class Checklist
  include ActiveGraph::Node
  has_one :in, :stage, type: :HAS_CHECKLIST

  def item_total
    42
  end
end
