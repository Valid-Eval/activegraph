module Trackable
  extend ActiveSupport::Concern

  included do
    before_save :stamp_change
    scope :recent, -> { where(recent: true) }
  end

  class_methods do
    def tracked_fields
      [:name]
    end
  end

  def stamp_change
    write_change_log
  end

  private

  def write_change_log
    true
  end
end
