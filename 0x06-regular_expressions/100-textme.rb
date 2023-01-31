#!/usr/bin/env ruby
# A script that output [SENDER] phone number or name
# [RECEIVER] phone number or name,and [FLAGS] that were used.

puts ARGV[0].scan(/from:(\w+|\+\d{1,15})|to:(\w+|\+\d{1,15})|flags:([-\d:]+)/).flatten.compact.join(",")
