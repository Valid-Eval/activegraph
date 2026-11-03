class RefreshJob
  include Sidekiq::Job

  def perform(kind)
    Checklist.new.item_total
  end
end
