# Local development only.
#
# The site is published by GitHub Pages, which builds with its own pinned gem set
# and does not install from this file. It exists so `bundle exec jekyll serve`
# gives a local preview instead of having to push to see a change.
#
# GitHub Pages currently tracks Jekyll 3.9.x. This pins the same major line so
# local output stays close to what actually ships; if you ever move the build
# into a GitHub Actions workflow, you can move to Jekyll 4 here and in the
# workflow together.

source 'https://rubygems.org'

gem 'github-pages', group: :jekyll_plugins

group :jekyll_plugins do
  gem 'jekyll-sitemap'
end

# Windows and JRuby do not include zoneinfo files; tzinfo-data supplies them.
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]

# Performance booster for watching directories on Windows.
gem 'wdm', '~> 0.1', platforms: [:mingw, :mswin, :x64_mingw]
