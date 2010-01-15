`iencode-ng` is the evolution of iencode , a set of scripts to ease encoding of movies and series for iPhone/iPod Touch.

This software require [HandbrakeCLI 0.9.4][handbrakecli] in your PATH

## To install

You can easily install `iencode-ng` via `easy_install`

    easy_install iencode-ng

You may need to use sudo, depending on your setup:

    sudo easy_install iencode-ng

If you wish to install the latest (non-stable) development version from source, download the latest version of the code, either from <http://github.com/tuxtof/iencode-ng/tarball/master> or by running:

	git clone git://github.com/tuxtof/iencode-ng.git

..then `cd` into the directory, and run:

	sudo rake install

## Basic usage

Usage: iencode [options] <path to moviefile>
iencode -h for full list of options

Options:
  -h, --help            show this help message and exit
  -d, --debug           Shows all debugging info
  -v, --verbose         Will provide some feedback [default]
  -q, --quiet           For ninja-like processing
  -f, --force           Overwrite existing target movie file
  -t, --tvtags          Tag file.mp4 after conversion with tvtags
  -m, --movietags       Tag file.mp4 after conversion with movietags
  -n, --renaming       Enable cleaning name for tvtags & movietags
  -s <subtitle file>, --sub=<subtitle file>
                        Use this subtitle file instead of video file.srt
  -T, --test            Test mode, only encode 30 first seconds
  --version             Show  version information for iencode


[handbrakecli]: http://handbrake.fr/downloads.php