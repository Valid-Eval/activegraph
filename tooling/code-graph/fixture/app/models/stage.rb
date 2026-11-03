class Stage < BaseRecord
  include ActiveGraph::Node
  include Trackable
  include Taggable

  property :name
  has_many :out, :checklists, type: :HAS_CHECKLIST
  has_one :in, :project, rel_class: :ProjectStage
  delegate :title, to: :project

  def summary
    stamp_change
    persisted_marker
    checklists.map(&:item_total)
  end

  def self.search_recent
    recent.where(name: 'x')
    tracked_fields
  end

  def label_for_report
    title.upcase
  end
end
