#!/usr/bin/env python3

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

"""Check for broken links."""

# The markdown files use posix-style paths, so we need posixpath for
# processing them. See help('posixpath').
import collections
import os
import posixpath
import re

import common


Link = collections.namedtuple('Link', 'text target markdown lineno file')


def check_link(link):
    """Check if the link's target exists.

    Return an error message string or "ok".
    """
    if link.target.startswith(('http://', 'https://')):
        # Checking for http(s) links can be added later, but currently 
        # it's not needed.
        return "ok"
    path = posixpath.join(posixpath.dirname(link.file), link.target)
    realpath = path.replace('/', os.sep)
    if not os.path.exists(realpath):
        return "doesn't exist"
    if path.endswith('/'):
        # A directory.
        if os.path.isdir(realpath):
            return "ok"
        return "not a directory"
    else:
        # A file.
        if os.path.isfile(realpath):
            return "ok"
        return "not a file"


def main():
    print("Searching links...")
    links = []
    for path in common.get_markdown_files():
        with open(path.replace('/', os.sep), 'r') as f:
            for match, lineno in common.find_links(f):
                target = match.group(2)
                if '#' in target:
                    where = target.index('#')
                    target = target[:where]
                link = Link(
                    text=match.group(1),
                    target=target,
                    markdown=match.group(0),
                    lineno=lineno,
                    file=path)
                links.append(link)

    print("Checking for broken links...")
    broken = []     # [(Link, check result), ...]
    for link in links:
        result = check_link(link)
        if result != "ok":
            broken.append((link, result))

    if broken:
        print("\n*** %d/%d links seem to be broken! ***\n"
              % (len(broken), len(links)))
        for link, error in broken:
            print("  file {0.file}, line {0.lineno}: {1}"
                  .format(link, error))
            print("   ", link.markdown.replace('\n', ' '))
            print()
    else:
        print("All", len(links), "links seem to be OK.")


if __name__ == '__main__':
    main()
