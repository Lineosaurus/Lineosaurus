import os

from mykit.kit.time import TimeFmt

from src.constants import __version__


class Vars:

    _DATE_ = TimeFmt.date()
    _OWNER_ = os.environ['GITHUB_ACTOR']

    ## Total lines of code across all repositories, regardless only-type and ignore-type.
    _LINES_ = ''
    _LINESFMT_ = ''
    _LINESROUND_ = ''
    _LINESAPPROX_ = ''

    ## Total characters across all repositories, regardless only-type and ignore-type.
    _CHARS_ = ''
    _CHARSFMT_ = ''
    _CHARSROUND_ = ''
    _CHARSAPPROX_ = ''

    ## Total lines of code across all repositories, following only-type and ignore-type.
    _LINE_ = ''
    _LINEFMT_ = ''
    _LINEROUND_ = ''
    _LINEAPPROX_ = ''

    ## Total commits across all repositories
    _CMIT_ = ''
    _CMITFMT_ = ''
    _CMITROUND_ = ''
    _CMITAPPROX_ = ''

    _VER_ = __version__


def replace_vars(text):
    for var, value in Vars.__dict__.items():
        if var.startswith('__'): continue  # `Vars` magic attributes (Vars internal)
        text = text.replace(var, str(value))
    return text