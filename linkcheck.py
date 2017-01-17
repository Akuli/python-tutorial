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

"""Check for broken links.

This finds links like this...

    [click here](some-file.md)
    [or here](../some/path/another-file.md)
    ![here's an image](../images/some-cool-image.png)

...but not like this:

    [some website](http://github.com/)
    [another website](https://github.com/)
    [local header](#some-header)
"""

# The markdown files use posix-style paths, so we need posixpath for
# processing them. See help('posixpath').
import collections
import os
import posixpath
import re

import common


class Link:

    def __init__(self, regexmatch, filepath, lineno):
        # The .group(0) is not perfect, but it's good enough.
        self.markdown = regexmatch.group(0)
        self.text = regexmatch.group(1)
        self.target = regexmatch.group(2)
        self.filepath = filepath
        self.lineno = lineno
        self.status = None

    def _get_status(self):
        if self.target.startswith(('http://', 'https://')):
            # Checking for http(s) links can be added later, but 
            # currently it's not needed.
            return "ok"

        target = self.target
        if '#' in target:
            where = target.index('#')
            if where == 0:
                # It's a link to a title in the same file, we need to 
                # skip it.
                return "ok"
            target = target[:where]

        path = posixpath.join(posixpath.dirname(self.filepath), target)
        realpath = path.replace('/', os.sep)

        if not os.path.exists(realpath):
            return "doesn't exist"
        if target.endswith('/'):
            # A directory.
            if os.path.isdir(directory):
                return "ok"
            return "not a directory"
        else:
            # A file.
            if os.path.isfile(realpath):
                return "ok"
            return "not a file"

    def check(self):
        """Check if the link's target is like it should be.

        Return an error message string or "ok". The return value is also 
        assigned to the status attribute.
        """
        self.status = self._get_status()
        return self.status

    def print_status(self):
        print("  file {0.filepath}, line {0.lineno}: {0.status}".format(self))
        print("    " + self.markdown)
        print()


def main():
    print("Searching links...")
    links = []
    for path in common.get_markdown_files():
        with open(path.replace('/', os.sep), 'r') as f:
            for match, lineno in common.find_links(f):
                links.append(Link(match, path, lineno))
    print("  found", len(links), "links")

    print("Checking for broken links...")
    brokens = 0
    for link in links:
        if link.check() != "ok":
            link.print_status()
            brokens += 1

    if brokens == 0:
        print("All links seem to be OK.")
    elif brokens == 1:
        print("1 link is broken!")
    else:
        print(brokens, "links are broken!")


if __name__ == '__main__':
    main()
