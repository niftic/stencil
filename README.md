# stencil
Binary exploitation templates with xonsh autocompletion

## Why
I was getting tired of writing the same base scripts for binary exploitation using `pwntools` and running `chmod` every time, so I created this tool to save some time during CTF competitions.

## How to use
Simply use the command `stencil` with the name of your stencil to copy it to your current directory.

For example, this will copy the file `remote.py` from your stencil directory to your current one.
~~~
stencil remote
~~~
The file will also be renamed to `exploit.py`, since it's what I usually use.

To use the autocompletion feature, simply press TAB after typing `stencil` on the command line.

Some example stencil scripts are provided in this repository as well.

## Install
To use the tool, you will need to set the `STENCILS_DIR` environment variable, for instance by adding this line in your `.xonshrc` file.
~~~python
$STENCILS_DIR = "/path/to/stencil/dir"
# you can also use python functions
import os.path
$STENCILS_DIR = os.path.expanduser("~/.stencils/")
~~~

Then, simply copy the contents of `stencil.py` at the end of your `.xonshrc` file.
