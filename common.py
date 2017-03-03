# This is free and unencumbered software released into the public
# domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a
# compiled binary, for any purpose, commercial or non-commercial, and
# by any means.

# In jurisdictions that recognize copyright laws, the author or
# authors of this software dedicate any and all copyright interest in
# the software to the public domain. We make this dedication for the
# benefit of the public at large and to the detriment of our heirs
# and successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to
# this software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <http://unlicense.org>

"""Things that other scripts import and use.

The markdown files use / as a path separator. That's why they need the
posixpath module for processing paths, but they use functions in this
file when actually opening files.
"""

import contextlib
import itertools
import os
import posixpath
import re
import shutil
import string


_LINK_REGEX = r'!?\[(.*?)\]\((.*?)\)'


def find_links(file):
    """Find all markdown links in a file object.

    Yield (lineno, regexmatch) tuples.
    """
    # don't yield same link twice
    seen = set()

    # we need to loop over the file two lines at a time to support
    # multi-line (actually two-line) links, so this is kind of a mess
    firsts, seconds = itertools.tee(file)
    next(seconds)  # first line is never second line

    # we want 1-based indexing instead of 0-based and one-line links get
    # caught from linepair[1], so we need to start at two
    for lineno, linepair in enumerate(zip(firsts, seconds), start=2):
        lines = linepair[0] + linepair[1]
        for match in re.finditer(_LINK_REGEX, lines, flags=re.DOTALL):
            if match.group(0) not in seen:
                seen.add(match.group(0))
                yield match, lineno


def get_markdown_files():
    """Yield the names of all markdown files in this tutorial.

    The yielded paths use / as the path separator.
    """
    for root, dirs, files in os.walk('.'):
        for file in files:
            if not file.endswith('.md'):
                continue
            path = os.path.normpath(os.path.join(root, file))
            yield path.replace(os.sep, '/')


def header_link(title):
    """Return a github-style link target for a title.

    >>> header_link('Hello there!')
    'hello-there'
    """
    # This doesn't do the-title-1, the-title-2 etc. with multiple titles
    # with same text, but usually this doesn't matter.
    result = ''
    for character in title:
        if character in string.whitespace:
            result += '-'
        elif character in string.punctuation:
            pass
        else:
            result += character.lower()
    return result


def askyesno(question, default=True):
    """Ask a yes/no question and return True or False.

    The default answer is yes if default is True and no if default is
    False.
    """
    if default:
        # yes by default
        question += ' [Y/n] '
    else:
        # no by default
        question += ' [y/N] '

    while True:
        result = input(question).upper().strip()
        if result == 'Y':
            return True
        if result == 'N':
            return False
        if not result:
            return default
        print("Please type y, n or nothing at all.")


def slashfix(path):
    """Replace / with os.sep."""
    return path.replace('/', os.sep)


def slashfix_open(file, mode):
    """An easy way to use slashfix() and open() together."""
    return open(slashfix(file), mode)


@contextlib.contextmanager
def backup(filename):
    """A context manager that backs up a file."""
    shutil.copy(filename, filename + '.backup')
    try:
        yield
    except Exception:
        # It failed, we need to restore from the backup.
        shutil.copy(filename + '.backup', filename)
    else:
        # Everything's fine, we can safely get rid of the backup.
        os.remove(filename + '.backup')


def header_link(title):
    """Return a github-style link target for a title.

    >>> header_link('Hello there!')
    'hello-there'
    """
    # This doesn't handle multiple titles with the same text in the
    # same file, but usually that's not a problem. GitHub makes
    # links like the-title, the-title-1, the-title-2 etc.
    result = ''
    for character in title:
        if character in string.whitespace:
            result += '-'
        elif character in string.punctuation:
            pass
        else:
            result += character.lower()
    return result
