class ProjectStage
  include ActiveGraph::Relationship
  from_class :Project
  to_class :Stage
  type 'HAS_STAGE'
end
