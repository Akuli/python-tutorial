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
    [local link](#some-title)
"""

import os
import posixpath

import common


def check(this_file, target, title, titledict):
    """Check if a link's target is like it should be.

    Return an error message string or "ok".
    """
    if target.startswith(('http://', 'https://')):
        # We don't need this currently, but checking these links could
        # be added later.
        return "ok"

    path = posixpath.join(posixpath.dirname(this_file), target)
    path = posixpath.normpath(path)
    real_path = common.slashfix(path)

    if not os.path.exists(real_path):
        return "doesn't exist"

    if target.endswith('/'):
        # A directory.
        if not os.path.isdir(real_path):
            return "not a directory"
    else:
        # A file.
        if not os.path.isfile(real_path):
            return "not a file"

    if title is not None and title not in titledict[path]:
        return "no title named %s" % title
    return "ok"


def find_titles(filename):
    """Read titles of a markdown file and return a list of them."""
    result = []

    with common.slashfix_open(filename, 'r') as f:
        for line in f:
            if line.startswith('```'):
                # it's a code block, let's skip to the end of it to
                # avoid detecting comments as titles
                while f.readline().rstrip() != '```':
                    pass
            if line.startswith('#'):
                # found a title
                result.append(common.header_link(line.lstrip('#').strip()))

    return result


def find_links(this_file):
    """Read links of a markdown file.

    Return a list of (target, title, lineno) pairs where title can be None.
    """
    result = []

    with common.slashfix_open(this_file, 'r') as f:
        for match, lineno in common.find_links(f):
            target = match.group(2)
            if '#' in target:
                file, title = target.split('#', 1)
                if not file:
                    # link to this file, [blabla](#hi)
                    file = posixpath.basename(this_file)
            else:
                file = target
                title = None

            result.append((file, title, lineno))

    return result


def get_line(filename, lineno):
    """Return the lineno'th line of a file."""
    with common.slashfix_open(filename, 'r') as f:
        for lineno2, line in enumerate(f, start=1):
            if lineno == lineno2:
                return line
    raise ValueError("%s is less than %d lines long" % (filename, lineno))


def main():
    print("Searching for titles and links...")
    titledict = {}      # {filename: [title1, title2, ...]}
    linkdict = {}       # {filename: [(file, title, lineno), ...])
    for path in common.get_markdown_files():
        titledict[path] = find_titles(path)
        linkdict[path] = find_links(path)

    print("Checking the links...")
    total = 0
    broken = 0

    for filename, linklist in linkdict.items():
        for target, title, lineno in linklist:
            status = check(filename, target, title, titledict)
            if status != "ok":
                print("  file %s, line %d: %s" % (filename, lineno, status))
                print("    %s" % get_line(filename, lineno))
                broken += 1
            total += 1

    print("%d/%d links seem to be broken." % (broken, total))


if __name__ == '__main__':
    main()
