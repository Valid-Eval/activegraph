require_relative 'report_format'
module ReportLoader
  autoload :LazyPart, 'lazy_part'
  def self.build
    ReportFormat.render
    LazyPart.new
  end
end
