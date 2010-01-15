require 'fileutils'

task :default => [:clean]

desc "Remove temporary files"
task :clean do
  puts "Removing temporary files"
  `rm -fr dist build`
  `rm -fr *.egg-info`
  `rm *.pyc`
end

desc "Upversion files"
task :upversion do
  puts "Upversioning"

  Dir.glob("*.py").each do |filename|
    f = File.new(filename, File::RDWR)
    contents = f.read()

    contents.gsub!(/__version__ = ".+?"/){|m|
      cur_version = m.scan(/\d+\.\d+/)[0].to_f
      new_version = cur_version + 0.1

      puts "Current version: #{cur_version}"
      puts "New version: #{new_version}"

      new_line = "__version__ = \"#{new_version}\""

      puts "Old line: #{m}"
      puts "New line: #{new_line}"

      m = new_line
    }

    puts contents[0]

    f.truncate(0) # empty the existing file
    f.seek(0)
    f.write(contents.to_s) # write modified file
    f.close()
  end
end

desc "Upload current version to PyPi"
task :topypi do
  cur_file = File.open("iencode.py").read()
  tvdb_api_version = cur_file.scan(/__version__ = "(.*)"/)
  tvdb_api_version = tvdb_api_version[0][0].to_f

  puts "Build sdist and send project v#{tvdb_api_version} to PyPi?"
  if $stdin.gets.chomp == "y"
    puts "Sending source-dist (sdist) to PyPi"

    if system("python setup.py sdist register upload")
      print "tvdb_api uploaded!"
    end

  else
    puts "Cancelled"
  end
end

