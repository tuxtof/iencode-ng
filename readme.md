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

From the command line, simply run:

	iencode the.file.mkv
	
For example:

	$ iencode Chuck.3x03.mkv
	Encoding file Chuck.3x03.mkv
	Encoding: task 1 of 1, 0.58 %
	Muxing: this may take awhile...
	Processing is done

## Command line arguments

There are various flags you can use with `iencode`, run..

    iencode --help

..to see them, and a short description of each.



`-h, --help` show help message and exit

`-d, --debug` show all debugging info

`-v, --verbose` will provide some feedback [default]

`-q, --quiet` for ninja-like processing

`-f, --force` overwrite existing target movie file

`-t, --tvtags` tag file.mp4 after conversion with `tvtags` [(required)][tvtags]

`-m, --movietags` tag file.mp4 after conversion with `movietags` [(required)][movietags]

`-n, --renaming` enable cleaning name for tvtags & movietags

`-i, --itunes` Automatically add to iTunes
	
`-T, --test` test mode, only encode 30 first seconds

`--version` show  version information for iencode


[handbrakecli]: http://handbrake.fr/downloads.php
[tvtags]: http://github.com/tuxtof/tvtags
[movietags]: http://github.com/tuxtof/movietags