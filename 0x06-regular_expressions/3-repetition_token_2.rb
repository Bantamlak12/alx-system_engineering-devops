#!/usr/bin/env ruby
# A a Ruby script that accepts one argument and pass it to a
# regular expression matching method.


puts ARGV[0].scan(/hbt{1,4}n/).join