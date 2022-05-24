def _stencil(args):
    """ Copy pre-formatted exploit code to current directory """
    import os.path
    if len(args) == 1:
        filename = os.path.join($STENCILS_DIR, args[0] + ".py")
        if os.path.isfile(filename):
            cp @(filename) ./exploit.py
        else:
            print(f"No such stencil: {os.path.basename(filename)}")
    if len(args) == 2:
        filename = os.path.join($STENCILS_DIR, ".".join([args[1], args[0]]))
        if os.path.isfile(filename):
            cp @(filename) .
        else:
            print(f"No such stencil: {os.path.basename(filename)}")
aliases["stencil"] = _stencil

# Completion functions
from xonsh.completers.tools import *

@contextual_command_completer_for("stencil")
def _complete_stencil(command):
    """ Complete stencil command with valid filenames """
    if command.arg_index == 1:
        from os import listdir
        return set([x.rstrip(".py") for x in listdir($STENCILS_DIR)])
__xonsh__.completers["stencil"] = _complete_stencil
__xonsh__.completers.move_to_end("stencil", last=False)