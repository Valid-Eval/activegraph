module Taggable
  def add_tag(tag)
    tags << normalize_tag(tag)
  end
end
