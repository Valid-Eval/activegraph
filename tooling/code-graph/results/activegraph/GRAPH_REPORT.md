# Graph Report

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1941 nodes · 3092 edges · 133 communities (75 shown, 58 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 156 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `51b2e983`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 18
- Community 19
- Community 20
- Community 21
- Community 22
- Community 23
- Community 24
- Community 25
- Community 26
- Community 27
- Community 28
- Community 29
- Community 30
- Community 31
- Community 32
- Community 33
- Community 34
- Community 35
- Community 36
- Community 37
- Community 38
- Community 39
- Community 40
- Community 41
- Community 42
- Community 43
- Community 44
- Community 45
- Community 46
- Community 47
- Community 48
- Community 49
- Community 50
- Community 51
- Community 52
- Community 53
- Community 54
- Community 55
- Community 56
- Community 57
- Community 58
- Community 59
- Community 60
- Community 61
- Community 62
- Community 63
- Community 64
- Community 65
- Community 66
- Community 67
- Community 68
- Community 69
- Community 70
- Community 71
- Community 72
- Community 73
- Community 74
- Community 75
- Community 76
- Community 77
- Community 78
- Community 79
- Community 80
- Community 81
- Community 82
- Community 83
- Community 84
- Community 85
- Community 86
- Community 87
- Community 88
- Community 91
- Community 92
- Community 93
- Community 94
- Community 95
- Community 96
- Community 98
- Community 99
- Community 100
- Community 101
- Community 102
- Community 103
- Community 104
- Community 105
- Community 106
- Community 107
- Community 108
- Community 109
- Community 110
- Community 111
- Community 112
- Community 113
- Community 114
- Community 115
- Community 116
- Community 117
- Community 118
- Community 119
- Community 120
- Community 121
- Community 122
- Community 123
- Community 124
- Community 125
- Community 126
- Community 127
- Community 128
- Community 129
- Community 130
- Community 131

## God Nodes (most connected - your core abstractions)
1. `ActiveGraph::Node::Query::QueryProxy` - 43 edges
2. `ActiveGraph::Base` - 41 edges
3. `ActiveGraph::Shared::Persistence` - 38 edges
4. `ActiveGraph::Node::HasN::Association` - 38 edges
5. `ActiveGraph::Node::Query::QueryProxyMethods` - 37 edges
6. `ActiveGraph::Core::Query` - 37 edges
7. `ActiveGraph::Shared::DeclaredProperties` - 31 edges
8. `ActiveGraph::Migrations::Runner` - 31 edges
9. `ActiveGraph::Shared::TypeConverters` - 31 edges
10. `ActiveGraph::Node::HasN::AssociationProxy` - 30 edges

## Surprising Connections (you probably didn't know these)
- `ActiveGraph::Node` --mixes_in--> `ActiveGraph::Node::Unpersisted`  [EXTRACTED]
  active_graph/node.rb → active_graph/node/unpersisted.rb
- `ActiveGraph::Migrations::Base` --mixes_in--> `ActiveGraph::Migrations::Helpers::IdProperty`  [EXTRACTED]
  active_graph/migrations/base.rb → active_graph/migrations/helpers/id_property.rb
- `ActiveGraph::Node::Query::QueryProxy` --mixes_in--> `ActiveGraph::Node::Dependent::QueryProxyMethods`  [EXTRACTED]
  active_graph/node/query/query_proxy.rb → active_graph/node/dependent/query_proxy_methods.rb
- `ActiveGraph::Node::Query::QueryProxy` --mixes_in--> `ActiveGraph::Node::Query::QueryProxyEnumerable`  [EXTRACTED]
  active_graph/node/query/query_proxy.rb → active_graph/node/query/query_proxy_enumerable.rb
- `ActiveGraph::Node::Query::QueryProxy` --mixes_in--> `ActiveGraph::Node::Query::QueryProxyFindInBatches`  [EXTRACTED]
  active_graph/node/query/query_proxy.rb → active_graph/node/query/query_proxy_find_in_batches.rb

## Import Cycles
- None detected.

## Communities (133 total, 58 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (9): ActiveGraph::Node, ActiveGraph::Node::HasN, ActiveGraph::Node::HasN::AssociationProxy, ActiveGraph::Node::HasN::ClassMethods, ActiveGraph::Node::HasN::HasOneConstraintError, ActiveGraph::Node::HasN::NonPersistedNodeError, ActiveGraph, ActiveGraph::Node (+1 more)

### Community 1 - "Community 1"
Cohesion: 0.05
Nodes (10): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::Element, ActiveGraph, ActiveGraph::Migration, ActiveGraph::Migration::AddIdProperty, ActiveGraph, ActiveGraph::Migrations (+2 more)

### Community 2 - "Community 2"
Cohesion: 0.06
Nodes (14): ActiveGraph, ActiveGraph::Migrations, ActiveGraph, ActiveGraph::Migrations, ActiveGraph::Migrations::CheckPending, ActiveGraph, ActiveGraph::Migrations, ActiveGraph::Migrations::MigrationFile (+6 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (13): ActiveGraph::Node::HasN::Association, ActiveGraph::Node::HasN::Association::RelWrapper, ActiveGraph::Relationship, ActiveGraph::Relationship::Persistence, ActiveGraph::Relationship::Persistence::ClassMethods, ActiveGraph::Relationship::Persistence::ModelClassInvalidError, ActiveGraph::Relationship::Persistence::RelCreateFailedError, ActiveGraph::Relationship::Persistence::RelInvalidError (+5 more)

### Community 4 - "Community 4"
Cohesion: 0.05
Nodes (15): ActiveGraph, ActiveGraph::Config, ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::Instrumentable, subscribe_to_query(), ActiveGraph, ActiveGraph::Core (+7 more)

### Community 5 - "Community 5"
Cohesion: 0.07
Nodes (11): ActiveGraph, ActiveGraph::Migrations, ActiveGraph::Migrations::Base, ActiveGraph, ActiveGraph::Migrations, ActiveGraph::Migrations::Helpers, ActiveGraph::Migrations::Helpers::ClassMethods, ActiveGraph (+3 more)

### Community 6 - "Community 6"
Cohesion: 0.06
Nodes (12): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::Label, ActiveGraph, ActiveGraph::Migrations, ActiveGraph::Migrations::Helpers, ActiveGraph::Migrations::Helpers::Schema, ActiveGraph (+4 more)

### Community 7 - "Community 7"
Cohesion: 0.07
Nodes (12): ActiveGraph::Node, ActiveGraph::Node::Enum, ActiveGraph::Node::Enum::ClassMethods, ActiveGraph::Node, ActiveGraph::Node::Scope, ActiveGraph::Node::Scope::ClassMethods, ActiveGraph::Node::Scope::ScopeEvalContext, ActiveGraph::Shared (+4 more)

### Community 8 - "Community 8"
Cohesion: 0.07
Nodes (8): ActiveGraph::Node::HasN, ActiveGraph::Node::HasN::Association, ActiveGraph::Node::HasN::Association::RelFactory, ActiveGraph::Shared, ActiveGraph::Shared::FilteredHash, ActiveGraph::Shared::FilteredHash::InvalidHashFilterType, ActiveGraph::Shared, ActiveGraph::Shared::RelQueryFactory

### Community 9 - "Community 9"
Cohesion: 0.08
Nodes (17): query(), query_run(), setup_query!(), ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::QueryBuilder, ActiveGraph::Core::QueryBuilder::Query, ActiveGraph (+9 more)

### Community 11 - "Community 11"
Cohesion: 0.09
Nodes (7): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::QueryMethods, ActiveGraph::Relationship, ActiveGraph::Relationship::Query, ActiveGraph::Relationship::Query::ClassMethods, ActiveGraph::Relationship::Query::RecordNotFound

### Community 13 - "Community 13"
Cohesion: 0.10
Nodes (6): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Query, ActiveGraph::Node::Query::QueryProxy, ActiveGraph::Node::Query::QueryProxy::Link, try_id()

### Community 14 - "Community 14"
Cohesion: 0.09
Nodes (6): ActiveGraph::Relationship::Persistence, ActiveGraph::Relationship::Persistence::QueryFactory, ActiveGraph::Shared, ActiveGraph::Shared::NodeQueryFactory, ActiveGraph::Shared, ActiveGraph::Shared::QueryFactory

### Community 17 - "Community 17"
Cohesion: 0.11
Nodes (6): ActiveGraph::Shared, ActiveGraph::Shared::DeclaredProperty, ActiveGraph::Shared::DeclaredProperty::IllegalPropertyError, ActiveGraph::Shared, ActiveGraph::Shared::DeclaredProperty, ActiveGraph::Shared::DeclaredProperty::Index

### Community 18 - "Community 18"
Cohesion: 0.10
Nodes (4): ActiveGraph::Node, ActiveGraph::Node::Persistence, ActiveGraph::Node::Persistence::ClassMethods, ActiveGraph::Node::Persistence::RecordInvalidError

### Community 20 - "Community 20"
Cohesion: 0.10
Nodes (9): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::Type, ActiveGraph, ActiveGraph::Relationship, ActiveGraph::Relationship::Types, ActiveGraph::Relationship::Types::ClassMethods, ActiveGraph::Shared (+1 more)

### Community 21 - "Community 21"
Cohesion: 0.10
Nodes (6): ActiveGraph, ActiveGraph::Base, ActiveGraph, ActiveGraph::Shared, ActiveGraph::Shared::Callbacks, ActiveGraph::Shared::Callbacks::ClassMethods

### Community 22 - "Community 22"
Cohesion: 0.12
Nodes (14): ActiveGraph, ActiveGraph::DangerousAttributeError, ActiveGraph::DeprecatedSchemaDefinitionError, ActiveGraph::Error, ActiveGraph::InvalidParameterError, ActiveGraph::InvalidPropertyOptionsError, ActiveGraph::IrreversibleMigration, ActiveGraph::MigrationError (+6 more)

### Community 23 - "Community 23"
Cohesion: 0.09
Nodes (11): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::QueryClauses, ActiveGraph::Core::QueryClauses::ArgError, ActiveGraph::Core::QueryClauses::CreateUniqueClause, ActiveGraph::Core::QueryClauses::DetachDeleteClause, ActiveGraph::Core::QueryClauses::MergeClause, ActiveGraph::Core::QueryClauses::OnCreateSetClause (+3 more)

### Community 26 - "Community 26"
Cohesion: 0.12
Nodes (7): ActiveGraph::Shared, ActiveGraph::Shared::Boolean, ActiveGraph::Shared::TypeConverters, ActiveGraph::Shared::TypeConverters::BaseConverter, ActiveGraph::Shared::TypeConverters::Boolean, ActiveGraph, ActiveGraph::TypeConverters

### Community 27 - "Community 27"
Cohesion: 0.15
Nodes (5): ActiveGraph::Node::Initialize, ActiveGraph::Relationship, ActiveGraph::Relationship::Initialize, ActiveGraph::Shared, ActiveGraph::Shared::Initialize

### Community 28 - "Community 28"
Cohesion: 0.16
Nodes (3): ActiveGraph::Shared, ActiveGraph::Shared::Attributes, ActiveGraph::Shared::Attributes::ClassMethods

### Community 30 - "Community 30"
Cohesion: 0.18
Nodes (5): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Query, ActiveGraph::Node::Query::QueryProxyEagerLoading, ActiveGraph::Node::Query::QueryProxyEagerLoading::AssociationTree

### Community 31 - "Community 31"
Cohesion: 0.18
Nodes (3): ActiveGraph::Relationship, ActiveGraph::Relationship::RelatedNode, ActiveGraph::Relationship::RelatedNode::UnsetRelatedNodeError

### Community 32 - "Community 32"
Cohesion: 0.18
Nodes (4): ActiveGraph::Shared, ActiveGraph::Shared::Property, ActiveGraph::Shared::Property::MultiparameterAssignmentError, ActiveGraph::Shared::Property::UndefinedPropertyError

### Community 34 - "Community 34"
Cohesion: 0.16
Nodes (5): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::Result, ActiveGraph::Node, ActiveGraph::Node::NodeListFormatter

### Community 35 - "Community 35"
Cohesion: 0.16
Nodes (4): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::OrmAdapter, ActiveGraph::Node::OrmAdapter::ClassMethods

### Community 36 - "Community 36"
Cohesion: 0.22
Nodes (4): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Query, ActiveGraph::Node::Query::QueryProxyEnumerable

### Community 37 - "Community 37"
Cohesion: 0.20
Nodes (4): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Query, ActiveGraph::Node::Query::QueryProxyMethodsOfMassUpdating

### Community 38 - "Community 38"
Cohesion: 0.13
Nodes (4): ActiveGraph::Node, ActiveGraph::Node::Reflection, ActiveGraph::Node::Reflection::AssociationReflection, ActiveGraph::Node::Reflection::ClassMethods

### Community 39 - "Community 39"
Cohesion: 0.12
Nodes (4): ActiveGraph::Shared::TypeConverters::DateConverter, ActiveGraph::Shared::TypeConverters::DateTimeConverter, ActiveGraph::Shared::TypeConverters::FloatConverter, ActiveGraph::Shared::TypeConverters::ObjectConverter

### Community 40 - "Community 40"
Cohesion: 0.13
Nodes (6): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::Entity, ActiveGraph, ActiveGraph::Shared, ActiveGraph::Shared::Identity

### Community 41 - "Community 41"
Cohesion: 0.13
Nodes (4): ActiveGraph::Core::QueryClauses::CallClause, ActiveGraph::Core::QueryClauses::RemoveClause, ActiveGraph::Core::QueryClauses::UnwindClause, ActiveGraph::Core::QueryClauses::UsingClause

### Community 43 - "Community 43"
Cohesion: 0.20
Nodes (3): ActiveGraph::Node::IdProperty, ActiveGraph::Node::IdProperty::Accessor, ActiveGraph::Node::IdProperty::Accessor::ClassMethods

### Community 48 - "Community 48"
Cohesion: 0.17
Nodes (6): ActiveGraph, inherited(), ActiveGraph, ActiveGraph::Shared, ActiveGraph::Shared::ClassMethods, inherited()

### Community 49 - "Community 49"
Cohesion: 0.18
Nodes (6): ActiveGraph, ActiveGraph::Relationship, ActiveGraph::Relationship::Validations, ActiveGraph, ActiveGraph::Shared, ActiveGraph::Shared::Validations

### Community 50 - "Community 50"
Cohesion: 0.17
Nodes (3): ActiveGraph::Node::Labels, ActiveGraph::Node::Labels::Index, ActiveGraph::Node::Labels::Index::ClassMethods

### Community 51 - "Community 51"
Cohesion: 0.24
Nodes (3): ActiveGraph, ActiveGraph::Migrations, ActiveGraph::Migrations::Schema

### Community 52 - "Community 52"
Cohesion: 0.21
Nodes (4): ActiveGraph::Node, ActiveGraph::Node::ClassMethods, ActiveGraph::Shared, ActiveGraph::Shared::PermittedAttributes

### Community 53 - "Community 53"
Cohesion: 0.18
Nodes (4): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Dependent, ActiveGraph::Node::Dependent::AssociationMethods

### Community 54 - "Community 54"
Cohesion: 0.21
Nodes (4): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Labels, ActiveGraph::Node::Labels::RecordNotFound

### Community 55 - "Community 55"
Cohesion: 0.20
Nodes (4): ActiveGraph::Relationship, ActiveGraph::Relationship::FrozenRelError, ActiveGraph, ActiveGraph::Transactions

### Community 57 - "Community 57"
Cohesion: 0.27
Nodes (3): ActiveGraph::Shared, ActiveGraph::Shared::TypecastedAttributes, ActiveGraph::Shared::TypecastedAttributes::ClassMethods

### Community 63 - "Community 63"
Cohesion: 0.18
Nodes (8): ActiveGraph, ActiveGraph::Timestamps, ActiveGraph, ActiveGraph::Timestamps, ActiveGraph::Timestamps::Created, ActiveGraph, ActiveGraph::Timestamps, ActiveGraph::Timestamps::Updated

### Community 65 - "Community 65"
Cohesion: 0.36
Nodes (3): ActiveGraph::Node, ActiveGraph::Node::IdProperty, ActiveGraph::Node::IdProperty::TypeMethods

### Community 66 - "Community 66"
Cohesion: 0.27
Nodes (3): ActiveGraph::Node, ActiveGraph::Node::Property, ActiveGraph::Node::Property::ClassMethods

### Community 67 - "Community 67"
Cohesion: 0.27
Nodes (4): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Query, ActiveGraph::Node::Query::ClassMethods

### Community 68 - "Community 68"
Cohesion: 0.20
Nodes (4): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Validations, ActiveGraph::Node::Validations::ClassMethods

### Community 69 - "Community 69"
Cohesion: 0.20
Nodes (5): ActiveGraph, ActiveGraph::Generators, ActiveGraph::Generators::MigrationGenerator, ActiveGraph::Generators::SourcePathHelper, ActiveGraph::Generators::SourcePathHelper::ClassMethods

### Community 71 - "Community 71"
Cohesion: 0.33
Nodes (3): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::Record

### Community 72 - "Community 72"
Cohesion: 0.22
Nodes (3): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::DependentCallbacks

### Community 73 - "Community 73"
Cohesion: 0.22
Nodes (3): ActiveGraph, ActiveGraph::Shared, ActiveGraph::Shared::Typecaster

### Community 76 - "Community 76"
Cohesion: 0.29
Nodes (3): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::CypherError

### Community 79 - "Community 79"
Cohesion: 0.36
Nodes (3): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::QueryFindInBatches

### Community 80 - "Community 80"
Cohesion: 0.32
Nodes (6): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::SchemaErrors, ActiveGraph::Core::SchemaErrors::ConstraintAlreadyExistsError, ActiveGraph::Core::SchemaErrors::ConstraintValidationFailedError, ActiveGraph::Core::SchemaErrors::IndexAlreadyExistsError

### Community 81 - "Community 81"
Cohesion: 0.29
Nodes (4): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::Wrappable, wrap()

### Community 82 - "Community 82"
Cohesion: 0.29
Nodes (4): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Dependent, ActiveGraph::Node::Dependent::QueryProxyMethods

### Community 83 - "Community 83"
Cohesion: 0.32
Nodes (3): ActiveGraph::Shared, ActiveGraph::Shared::SerializedProperties, ActiveGraph::Shared::SerializedProperties::ClassMethods

### Community 87 - "Community 87"
Cohesion: 0.32
Nodes (3): ActiveGraph, ActiveGraph::Generators, ActiveGraph::Generators::UpgradeV8Generator

### Community 91 - "Community 91"
Cohesion: 0.29
Nodes (4): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Query, ActiveGraph::Node::Query::QueryProxyFindInBatches

### Community 94 - "Community 94"
Cohesion: 0.29
Nodes (3): ActiveGraph, ActiveGraph::Shared, ActiveGraph::Shared::Marshal

### Community 96 - "Community 96"
Cohesion: 0.40
Nodes (3): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::QueryExt

### Community 98 - "Community 98"
Cohesion: 0.33
Nodes (3): ActiveGraph::Node::Labels, ActiveGraph::Node::Labels::Reloading, ActiveGraph::Node::Labels::Reloading::ClassMethods

### Community 99 - "Community 99"
Cohesion: 0.33
Nodes (3): ActiveGraph, ActiveGraph::Relationship, ActiveGraph::Relationship::Callbacks

### Community 100 - "Community 100"
Cohesion: 0.40
Nodes (3): ActiveGraph, ActiveGraph::Relationship, ActiveGraph::Relationship::Wrapping

### Community 103 - "Community 103"
Cohesion: 0.40
Nodes (3): ActiveGraph, ActiveGraph::Core, ActiveGraph::Core::Node

### Community 110 - "Community 110"
Cohesion: 0.50
Nodes (3): ActiveGraph, inherit_id_property(), inherited()

### Community 111 - "Community 111"
Cohesion: 0.40
Nodes (3): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Dependent

### Community 118 - "Community 118"
Cohesion: 0.40
Nodes (3): ActiveGraph, ActiveGraph::Generators, ActiveGraph::Generators::GeneratedAttribute

### Community 119 - "Community 119"
Cohesion: 0.50
Nodes (3): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Callbacks

### Community 120 - "Community 120"
Cohesion: 0.50
Nodes (3): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::HasN

### Community 121 - "Community 121"
Cohesion: 0.50
Nodes (3): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::HasN

### Community 122 - "Community 122"
Cohesion: 0.50
Nodes (3): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Query

### Community 123 - "Community 123"
Cohesion: 0.50
Nodes (3): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Query

### Community 124 - "Community 124"
Cohesion: 0.50
Nodes (3): ActiveGraph, ActiveGraph::Node, ActiveGraph::Node::Query

## Knowledge Gaps
- **58 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ActiveGraph::Base` connect `Community 21` to `Community 0`, `Community 1`, `Community 4`, `Community 5`, `Community 6`, `Community 37`, `Community 9`, `Community 42`, `Community 11`, `Community 10`, `Community 12`, `Community 16`, `Community 49`, `Community 50`, `Community 51`, `Community 18`, `Community 55`, `Community 61`?**
  _High betweenness centrality (0.347) - this node is a cross-community bridge._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.05154320987654321 - nodes in this community are weakly interconnected._
- **Why does `ActiveGraph::Core::Query` connect `Community 29` to `Community 96`, `Community 130`, `Community 11`, `Community 79`, `Community 23`, `Community 89`, `Community 59`, `Community 60`, `Community 61`?**
  _High betweenness centrality (0.161) - this node is a cross-community bridge._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.05370101596516691 - nodes in this community are weakly interconnected._
- **Why does `ActiveGraph::Core::QueryClauses` connect `Community 23` to `Community 64`, `Community 104`, `Community 41`, `Community 105`, `Community 106`, `Community 107`, `Community 45`, `Community 78`, `Community 108`, `Community 77`, `Community 109`, `Community 24`, `Community 29`, `Community 62`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.06095791001451379 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.053061224489795916 - nodes in this community are weakly interconnected._