module Taggable
  def normalize_tag(tag)
    tag.to_s.downcase
  end
end
