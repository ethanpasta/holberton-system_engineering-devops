#!/usr/bin/env ruby
L_FORMAT = /^*from:(.*?)\] \[to:(.+?)\] *\[flags:(.+?)\]/
ma = ARGV[0].match(L_FORMAT)
if ma
  puts "#{ma[1]},#{ma[2]},#{ma[3]}"
end
