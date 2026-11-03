class Project
  include ActiveGraph::Node
  has_many :out, :stages, rel_class: :ProjectStage

  def title
    'project'
  end
end
