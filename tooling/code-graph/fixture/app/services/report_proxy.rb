class ReportProxy
  def initialize(target)
    @target = target
  end

  def method_missing(name, *args)
    @target.public_send(name, *args)
  end

  def respond_to_missing?(name, include_private = false)
    @target.respond_to?(name, include_private) || super
  end
end
