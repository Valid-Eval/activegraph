# Graph Report

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 1650 nodes · 2096 edges · 151 communities (136 shown, 15 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 39 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `91986227`
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
- Community 89
- Community 90
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
- Community 132
- Community 133
- Community 134
- Community 135
- Community 136
- Community 137
- Community 138
- Community 139
- Community 140
- Community 141
- Community 142
- Community 143
- Community 144
- Community 145
- Community 146
- Community 147
- Community 148

## God Nodes (most connected - your core abstractions)
1. `Neo4j::Driver::Bolt::Connection` - 54 edges
2. `Neo4j::Driver::Routing::LoadBalancer` - 40 edges
3. `Neo4j::Driver::PackStream::Packer` - 26 edges
4. `Neo4j::Driver::Session` - 25 edges
5. `Neo4j::Driver::Result` - 24 edges
6. `Neo4j::Driver::Bolt::Pool` - 22 edges
7. `Neo4j::Driver::Bolt::Protocol::Base` - 22 edges
8. `Neo4j::Driver::Summary::ResultSummary` - 22 edges
9. `Neo4j::Driver::Bolt::Wire` - 20 edges
10. `Neo4j::Driver::PackStream::Structure` - 20 edges

## Surprising Connections (you probably didn't know these)
- `Neo4j::Driver::Ext::ConfigConverter` --mixes_in--> `Neo4j::Driver::Internal::DurationNormalizer`  [EXTRACTED]
  jruby/neo4j/driver/ext/config_converter.rb → shared/neo4j/driver/internal/duration_normalizer.rb
- `Neo4j::Driver::Ext::InternalSession` --mixes_in--> `Neo4j::Driver::AutoCloseable`  [EXTRACTED]
  jruby/neo4j/driver/ext/internal_session.rb → shared/neo4j/driver/auto_closeable.rb
- `Neo4j::Driver::Ext::InternalDriver` --mixes_in--> `Neo4j::Driver::AutoCloseable`  [EXTRACTED]
  jruby/neo4j/driver/ext/internal_driver.rb → shared/neo4j/driver/auto_closeable.rb
- `Neo4j::Driver::Session` --mixes_in--> `Neo4j::Driver::Internal::DurationNormalizer`  [EXTRACTED]
  mri/neo4j/driver/session.rb → shared/neo4j/driver/internal/duration_normalizer.rb
- `Neo4j::Driver::Ext::GraphDatabase` --mixes_in--> `Neo4j::Driver::AutoCloseable`  [EXTRACTED]
  jruby/neo4j/driver/ext/graph_database.rb → shared/neo4j/driver/auto_closeable.rb

## Import Cycles
- None detected.

## Communities (151 total, 15 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (12): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Logger, Neo4j, Neo4j::Driver, Neo4j::Driver::Types, Neo4j::Driver::Types::LocalTime (+4 more)

### Community 1 - "Community 1"
Cohesion: 0.08
Nodes (13): Neo4j, Neo4j::Driver, Neo4j::Driver::Bookmark, Neo4j, Neo4j::Driver, Neo4j::Driver::Session, Neo4j, Neo4j::Driver (+5 more)

### Community 2 - "Community 2"
Cohesion: 0.06
Nodes (13): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::Base, Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions (+5 more)

### Community 3 - "Community 3"
Cohesion: 0.06
Nodes (13): Neo4j, Neo4j::Driver, Neo4j::Driver::Direct, Neo4j::Driver::Direct::ConnectionProvider, Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::Metrics (+5 more)

### Community 4 - "Community 4"
Cohesion: 0.08
Nodes (13): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Message, Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol (+5 more)

### Community 5 - "Community 5"
Cohesion: 0.11
Nodes (8): Neo4j, Neo4j::Driver, Neo4j::Driver::PackStream, Neo4j::Driver::PackStream::Packer, Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::ZoneIdentifier

### Community 6 - "Community 6"
Cohesion: 0.10
Nodes (12): Neo4j, Neo4j::Driver, Neo4j::Driver::PackStream, Neo4j::Driver::PackStream::Markers, Neo4j, Neo4j::Driver, Neo4j::Driver::PackStream, Neo4j::Driver::PackStream::Unpacker (+4 more)

### Community 7 - "Community 7"
Cohesion: 0.11
Nodes (7): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::StreamHandler, Neo4j, Neo4j::Driver, Neo4j::Driver::UnmanagedTransaction

### Community 8 - "Community 8"
Cohesion: 0.11
Nodes (10): Neo4j, Neo4j::Driver, Neo4j::Driver::AuthTokenManager, Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::ExceptionMapper, Neo4j (+2 more)

### Community 9 - "Community 9"
Cohesion: 0.10
Nodes (10): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Message, Neo4j::Driver::Bolt::Message::Failure, Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt (+2 more)

### Community 10 - "Community 10"
Cohesion: 0.14
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::Result

### Community 11 - "Community 11"
Cohesion: 0.17
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Pool

### Community 14 - "Community 14"
Cohesion: 0.10
Nodes (6): Neo4j, Neo4j::Driver, Neo4j::Driver::Driver, Neo4j, Neo4j::Driver, Neo4j::Driver::EagerResult

### Community 15 - "Community 15"
Cohesion: 0.12
Nodes (8): Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::Clock, Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::DriverFactory

### Community 16 - "Community 16"
Cohesion: 0.11
Nodes (12): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::CloseOverride, Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::ExceptionCheckable (+4 more)

### Community 17 - "Community 17"
Cohesion: 0.12
Nodes (9): Neo4j, Neo4j::Driver, Neo4j::Driver::Summary, Neo4j::Driver::Summary::GqlNotification, Neo4j, Neo4j::Driver, Neo4j::Driver::Summary, Neo4j::Driver::Summary::Notification (+1 more)

### Community 18 - "Community 18"
Cohesion: 0.12
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::RecordBuffer

### Community 19 - "Community 19"
Cohesion: 0.11
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Types, Neo4j::Driver::Types::LocalDateTime

### Community 20 - "Community 20"
Cohesion: 0.12
Nodes (11): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::Cluster, Neo4j::Driver::Ext::Internal::Cluster::RoutingTableRegistryImpl, Neo4j, Neo4j::Driver (+3 more)

### Community 22 - "Community 22"
Cohesion: 0.22
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Handshake

### Community 23 - "Community 23"
Cohesion: 0.21
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::TlsConfig

### Community 24 - "Community 24"
Cohesion: 0.13
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Routing, Neo4j::Driver::Routing::RoutingTable

### Community 25 - "Community 25"
Cohesion: 0.18
Nodes (6): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::Summary, Neo4j::Driver::Ext::Internal::Summary::InternalQueryProfile

### Community 28 - "Community 28"
Cohesion: 0.18
Nodes (8): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::AuthTokens, Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::NeoConverter

### Community 29 - "Community 29"
Cohesion: 0.23
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::BookmarkManagers, Neo4j::Driver::Ext::ConfigConverter

### Community 30 - "Community 30"
Cohesion: 0.15
Nodes (9): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::AbstractQueryRunner, Neo4j, Neo4j::Driver, Neo4j::Driver::Ext (+1 more)

### Community 31 - "Community 31"
Cohesion: 0.14
Nodes (9): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V6, Neo4j, Neo4j::Driver, Neo4j::Driver::Types (+1 more)

### Community 32 - "Community 32"
Cohesion: 0.18
Nodes (7): Neo4j, Neo4j::Driver, Neo4j::Driver::BookmarkManagers, Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::DefaultBookmarkManager

### Community 33 - "Community 33"
Cohesion: 0.19
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::InternalDriver

### Community 34 - "Community 34"
Cohesion: 0.17
Nodes (7): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::GraphDatabase, Neo4j, Neo4j::Driver, Neo4j::Driver::AutoCloseable

### Community 35 - "Community 35"
Cohesion: 0.15
Nodes (8): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::InternalKeys, Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::InternalResult

### Community 36 - "Community 36"
Cohesion: 0.15
Nodes (8): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::ConnectionReadTimeoutException, Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::ServiceUnavailableException

### Community 37 - "Community 37"
Cohesion: 0.15
Nodes (8): Neo4j, Neo4j::Driver, Neo4j::Driver::GraphDatabase, Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::Security, Neo4j::Driver::Internal::Security::StaticAuthTokenManager

### Community 38 - "Community 38"
Cohesion: 0.15
Nodes (8): Neo4j, Neo4j::Driver, Neo4j::Driver::Routing, Neo4j::Driver::Routing::RoutedConnection, Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::SessionExpiredException

### Community 39 - "Community 39"
Cohesion: 0.17
Nodes (6): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::Summary, Neo4j::Driver::Ext::Internal::Summary::InternalGqlNotification

### Community 40 - "Community 40"
Cohesion: 0.22
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::Validator

### Community 41 - "Community 41"
Cohesion: 0.18
Nodes (6): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::Summary, Neo4j::Driver::Ext::Internal::Summary::InternalNotification

### Community 42 - "Community 42"
Cohesion: 0.18
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Connection::ResponseCollector

### Community 44 - "Community 44"
Cohesion: 0.18
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::HomeDbCache

### Community 45 - "Community 45"
Cohesion: 0.18
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Summary, Neo4j::Driver::Summary::SummaryCounters

### Community 46 - "Community 46"
Cohesion: 0.20
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::ClockAdapter

### Community 48 - "Community 48"
Cohesion: 0.20
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Message, Neo4j::Driver::Bolt::Message::Ignored

### Community 49 - "Community 49"
Cohesion: 0.20
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Message, Neo4j::Driver::Bolt::Message::Record

### Community 50 - "Community 50"
Cohesion: 0.20
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Message, Neo4j::Driver::Bolt::Message::Success

### Community 51 - "Community 51"
Cohesion: 0.20
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V51

### Community 52 - "Community 52"
Cohesion: 0.20
Nodes (6): Neo4j, Neo4j::Driver, Neo4j::Driver::ClientCertificate, Neo4j, Neo4j::Driver, Neo4j::Driver::ClientCertificates

### Community 53 - "Community 53"
Cohesion: 0.20
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::NoSuchRecordException

### Community 54 - "Community 54"
Cohesion: 0.20
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Types, Neo4j::Driver::Types::Point

### Community 55 - "Community 55"
Cohesion: 0.22
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::DriverFactory

### Community 56 - "Community 56"
Cohesion: 0.22
Nodes (6): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::Summary, Neo4j::Driver::Ext::Internal::Summary::InternalPlan

### Community 57 - "Community 57"
Cohesion: 0.22
Nodes (6): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::Summary, Neo4j::Driver::Ext::Internal::Summary::InternalResultSummary

### Community 58 - "Community 58"
Cohesion: 0.22
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::BoltVersion

### Community 59 - "Community 59"
Cohesion: 0.22
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V4

### Community 60 - "Community 60"
Cohesion: 0.25
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V43

### Community 61 - "Community 61"
Cohesion: 0.22
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V44

### Community 62 - "Community 62"
Cohesion: 0.22
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V5

### Community 63 - "Community 63"
Cohesion: 0.22
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V52

### Community 64 - "Community 64"
Cohesion: 0.25
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V53

### Community 65 - "Community 65"
Cohesion: 0.22
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V61

### Community 66 - "Community 66"
Cohesion: 0.22
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Summary, Neo4j::Driver::Summary::Profile

### Community 67 - "Community 67"
Cohesion: 0.28
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Types, Neo4j::Driver::Types::TemporalValue

### Community 68 - "Community 68"
Cohesion: 0.25
Nodes (7): Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::Security, Neo4j::Driver::Net, Neo4j::Driver::Summary, Neo4j::Driver::Types

### Community 69 - "Community 69"
Cohesion: 0.25
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::InternalEntity, Neo4j::Driver::Ext::MapConverter

### Community 70 - "Community 70"
Cohesion: 0.25
Nodes (6): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::Metrics, Neo4j::Driver::Ext::Internal::Metrics::InternalConnectionPoolMetrics

### Community 71 - "Community 71"
Cohesion: 0.25
Nodes (6): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::Summary, Neo4j::Driver::Ext::Internal::Summary::InternalGqlStatusObject

### Community 72 - "Community 72"
Cohesion: 0.32
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::RubyConverter

### Community 73 - "Community 73"
Cohesion: 0.25
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::AuthTokens

### Community 74 - "Community 74"
Cohesion: 0.29
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::ProtocolVersionHandler

### Community 75 - "Community 75"
Cohesion: 0.25
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::SecurityRetryableException

### Community 76 - "Community 76"
Cohesion: 0.25
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V54

### Community 77 - "Community 77"
Cohesion: 0.21
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt

### Community 78 - "Community 78"
Cohesion: 0.25
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::ClockAdapter

### Community 79 - "Community 79"
Cohesion: 0.29
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::Record

### Community 80 - "Community 80"
Cohesion: 0.25
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Summary, Neo4j::Driver::Summary::DatabaseInfo

### Community 81 - "Community 81"
Cohesion: 0.25
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Summary, Neo4j::Driver::Summary::ServerInfo

### Community 82 - "Community 82"
Cohesion: 0.25
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Types, Neo4j::Driver::Types::Entity

### Community 83 - "Community 83"
Cohesion: 0.25
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Types, Neo4j::Driver::Types::Relationship

### Community 84 - "Community 84"
Cohesion: 0.25
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::Neo4jException

### Community 85 - "Community 85"
Cohesion: 0.25
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::Value, Neo4j::Driver::Exceptions::Value::LossyCoercion

### Community 86 - "Community 86"
Cohesion: 0.25
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::Value, Neo4j::Driver::Exceptions::Value::Uncoercible

### Community 87 - "Community 87"
Cohesion: 0.25
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::InternalAuthTokenManager

### Community 89 - "Community 89"
Cohesion: 0.29
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::EagerResultValue

### Community 90 - "Community 90"
Cohesion: 0.29
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::InternalRecord

### Community 91 - "Community 91"
Cohesion: 0.29
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::InternalTransaction

### Community 92 - "Community 92"
Cohesion: 0.29
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::StartEndNaming

### Community 93 - "Community 93"
Cohesion: 0.29
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V55

### Community 94 - "Community 94"
Cohesion: 0.29
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V56

### Community 95 - "Community 95"
Cohesion: 0.29
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Bolt, Neo4j::Driver::Bolt::Protocol, Neo4j::Driver::Bolt::Protocol::V58

### Community 96 - "Community 96"
Cohesion: 0.29
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Net, Neo4j::Driver::Net::ServerAddress

### Community 98 - "Community 98"
Cohesion: 0.29
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Summary, Neo4j::Driver::Summary::GqlStatusObject

### Community 99 - "Community 99"
Cohesion: 0.29
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Summary, Neo4j::Driver::Summary::Plan

### Community 100 - "Community 100"
Cohesion: 0.29
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Types, Neo4j::Driver::Types::Node

### Community 101 - "Community 101"
Cohesion: 0.29
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Types, Neo4j::Driver::Types::UnboundRelationship

### Community 102 - "Community 102"
Cohesion: 0.29
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::Value, Neo4j::Driver::Exceptions::Value::NotMultiValued

### Community 103 - "Community 103"
Cohesion: 0.29
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::Value, Neo4j::Driver::Exceptions::Value::Unsizable

### Community 104 - "Community 104"
Cohesion: 0.29
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::Value, Neo4j::Driver::Exceptions::Value::ValueException

### Community 105 - "Community 105"
Cohesion: 0.29
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::Deprecator

### Community 106 - "Community 106"
Cohesion: 0.29
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::Loader

### Community 107 - "Community 107"
Cohesion: 0.33
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::ClientCertificateManager

### Community 108 - "Community 108"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::AuthToken

### Community 109 - "Community 109"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::ClientCertificates

### Community 110 - "Community 110"
Cohesion: 0.33
Nodes (5): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Internal, Neo4j::Driver::Ext::Internal::InternalNotificationSeverity

### Community 111 - "Community 111"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::InternalNode

### Community 112 - "Community 112"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::InternalRelationship

### Community 113 - "Community 113"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::PlainMapConverter

### Community 114 - "Community 114"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::Query

### Community 115 - "Community 115"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext, Neo4j::Driver::Ext::UnsupportedType

### Community 116 - "Community 116"
Cohesion: 0.33
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::ClientCertificateManager

### Community 117 - "Community 117"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Routing, Neo4j::Driver::Routing::LoadBalancer::Handler

### Community 119 - "Community 119"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Summary, Neo4j::Driver::Summary::Query

### Community 120 - "Community 120"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::AuthenticationException

### Community 121 - "Community 121"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::AuthorizationExpiredException

### Community 122 - "Community 122"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::DatabaseException

### Community 123 - "Community 123"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::DiscoveryException

### Community 124 - "Community 124"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::FatalDiscoveryException

### Community 125 - "Community 125"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::IllegalStateException

### Community 126 - "Community 126"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::ProtocolException

### Community 127 - "Community 127"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::ResultConsumedException

### Community 128 - "Community 128"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::SecurityException

### Community 129 - "Community 129"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::TokenExpiredException

### Community 130 - "Community 130"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::TransactionNestingException

### Community 131 - "Community 131"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::TransactionTerminatedException

### Community 132 - "Community 132"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::TransientException

### Community 133 - "Community 133"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::UnsupportedFeatureException

### Community 134 - "Community 134"
Cohesion: 0.33
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::UntrustedServerException

### Community 135 - "Community 135"
Cohesion: 0.40
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::ClientCertificateManagers

### Community 136 - "Community 136"
Cohesion: 0.40
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Internal, Neo4j::Driver::Internal::Extras

### Community 137 - "Community 137"
Cohesion: 0.40
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Exceptions, Neo4j::Driver::Exceptions::CertificateException

### Community 138 - "Community 138"
Cohesion: 0.40
Nodes (4): Neo4j, Neo4j::Driver, Neo4j::Driver::Summary, Neo4j::Driver::Summary::QueryType

### Community 139 - "Community 139"
Cohesion: 0.50
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext

### Community 140 - "Community 140"
Cohesion: 0.50
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::Ext

### Community 141 - "Community 141"
Cohesion: 0.50
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::AccessMode

### Community 142 - "Community 142"
Cohesion: 0.50
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::AutoCommitRetriesMode

### Community 143 - "Community 143"
Cohesion: 0.50
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::Summary

### Community 144 - "Community 144"
Cohesion: 0.50
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::Types

### Community 145 - "Community 145"
Cohesion: 0.50
Nodes (3): Neo4j, Neo4j::Driver, Neo4j::Driver::Types

## Knowledge Gaps
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Neo4j::Driver::Bolt::Wire` connect `Community 21` to `Community 74`, `Community 43`, `Community 77`?**
  _High betweenness centrality (0.171) - this node is a cross-community bridge._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.057624113475177305 - nodes in this community are weakly interconnected._
- **Why does `Neo4j::Driver::Bolt::Connection` connect `Community 13` to `Community 3`, `Community 36`, `Community 42`, `Community 75`, `Community 74`, `Community 12`, `Community 47`, `Community 26`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.08194905869324474 - nodes in this community are weakly interconnected._
- **Why does `Neo4j::Driver::PackStream::Packer` connect `Community 5` to `Community 21`, `Community 6`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.06039488966318235 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.06282051282051282 - nodes in this community are weakly interconnected._