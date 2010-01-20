#!/usr/bin/env python
#encoding:utf-8
#author:tuxtof
#project:iencode-ng
#repository:http://github.com/tuxtof/iencode-ng
#license:Creative Commons GNU GPL v2
# (http://creativecommons.org/licenses/GPL/2.0/)

__author__ = "tuxtof"
__version__ = "0.6"

import os
import sys
from subprocess import *
import glob
from optparse import OptionParser

def whichBin(execName):
	for path in os.environ["PATH"].split(":"):
		if os.path.exists(os.path.join(path,execName)):
			return 1

def processFile(opts, fullFileName):
	
	
	(path, fileName) = os.path.split(fullFileName)
	if len(path) == 0:
		path = "./"
	(name,ext) = os.path.splitext(fileName)
	
	outputFileName = os.path.join(path, name + ".m4v")
	
	if os.path.exists(outputFileName)  and not opts.force:
		print "File %s already exist" %(name + ".m4v")
		sys.exit(1)
		
	if opts.test:
		addTest = " --stop-at duration:30"
		print "Encoding 30s of file %s" % fullFileName
	else:
		addTest = ""
		print "Encoding file %s" % fullFileName
	
	if os.path.isfile(path + name + ".srt"):
		addSub = " --srt-default --srt-lang fra --srt-file \"%s\"" % (path + name + ".srt")
	else:
		addSub = ""
		
	
	encodeCmd = "HandBrakeCLI -Z \"iPhone & iPod Touch\" -i \"%s\" -o \"%s\" --mixdown stereo %s %s" % (fullFileName, outputFileName, addTest, addSub)
	
	if opts.verbose > 1:
		print encodeCmd
	
	execCmd = Popen(encodeCmd,shell=True, stderr=PIPE)
	execCmd.wait()
	print ""
	
	if opts.tvtags:
		exectvtags(opts,outputFileName)
	
	if opts.movietags:
		execmovietags(opts,outputFileName)
	
	print "Processing is done"

def exectvtags(opts,file):
	print "Processing tvtags"
	tvtags.tvtags(opts,file)
	

def execmovietags(opts,file):
	print "Processing movietags"
	movietags.movietags(opts,file)


	
def main():
	parser = OptionParser(usage="%prog [options] <path to moviefile>\n%prog -h for full list of options")
	    
	parser.add_option(  "-d", "--debug", action="store_const", const=2, dest="verbose", help="Shows all debugging info")
	parser.add_option(  "-v", "--verbose", action="store_const", const=1, dest="verbose", help="Will provide some feedback [default]")
	parser.add_option(  "-q", "--quiet", action="store_const", const=0, dest="verbose", help="For ninja-like processing")
	parser.add_option(  "-f", "--force", action="store_true", dest="force", help="Overwrite existing target movie file")
	try:
		import tvtags
	except:
		__tvtags__ = False
	else:
		parser.add_option(  "-t", "--tvtags", action="store_true", dest="tvtags", help="Tag file.mp4 after conversion with tvtags")
	try:
		import movietags
	except:
		__movietags__ = False
	else:
		parser.add_option(  "-m", "--movietags", action="store_true", dest="movietags", help="Tag file.mp4 after conversion with movietags")
	parser.add_option(  "-n", "--renaming", action="store_true", dest="rename", help="Enable cleaning name for tvtags & movietags")
	parser.add_option(  "-T", "--test", action="store_true", dest="test", help="Test mode, only encode 30 first seconds")
	parser.add_option(	"--version", action="store_true", dest="version", help="Show  version information for iencode")
	parser.set_defaults( removetags=False, interactive=False, verbose=1, tvtags=False, movietags=False, test=False, force=False, rename=False, version=False )

	opts, args = parser.parse_args()
	
	if opts.version:
		print "iencode %s" % __version__
		sys.exit(0)
	
	if len(args) == 0:
		parser.error("You must provide at least one file to encode")
		
	if not whichBin("HandbrakeCLI"):
		print "HandBrakeCLI tools not found\nPlease go to http://handbrake.fr/downloads.php to install it"
		sys.exit(0)
	
	for file in args:
		if not os.path.isfile(file):
			print "No such movie file : %s" %file
			sys.exit(1)
		processFile(opts, file)
		
		

if __name__ == "__main__": 
	sys.exit(main())
