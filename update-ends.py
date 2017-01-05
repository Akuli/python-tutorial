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

"""Update ends of markdown files."""

import re


BASIC_END = """\
You may use this tutorial freely at your own risk. See
[LICENSE](LICENSE).

[List of contents](README.md#list-of-contents)
"""

CHAPTER_END = """\
You may use this tutorial freely at your own risk. See
[LICENSE](LICENSE).

[Previous]({prev}) | [Next]({next}) |
[List of contents](README.md#list-of-contents)
"""


LINK_REGEX = r'\[.*\]\((.*\.md)\)'
CHAPTER_LINK_REGEX = r'^\d+\. ' + LINK_REGEX + r'$'


def get_filenames():
    """Get chapter files and other files from README.

    Return a two-tuple of chapter files and other files.
    """
    chapters = []
    with open('README.md', 'r') as f:
        # move to where the content list starts
        while f.readline().strip() != "## List of contents":
            pass

        # now let's read the content list
        for line in f:
            line = line.strip()
            if line:
                # not empty line
                match = re.search(CHAPTER_LINK_REGEX, line)
                if match is None:
                    # end of content list
                    break
                chapters.append(match.group(1))

    # now let's find other links to markdown files
    with open('README.md', 'r') as f:
        all_files = re.findall(LINK_REGEX, f.read())
    others = set(all_files) - set(chapters)

    return chapters, others


def update_end(filename, end):
    """Add *** and end to a file if it doesn't contain them already."""
    end = '\n***\n\n' + end
    with open(filename, 'r') as f:
        content = f.read()
    if content.endswith(end):
        # No need to do anything.
        print("  Has end:", filename)
        return

    if '\n***\n' in content:
        # We need to remove the old ending first.
        print("  Removing old end:", filename)
        where = content.index('\n***\n')
        with open(filename, 'w') as f:
            f.write(content[:where])

    print("  Adding end:", filename)
    with open(filename, 'a') as f:
        f.write(end)


def main():
    chapter_files, other_files = get_filenames()

    # make previous of first file and next of last file to just bring
    # back to README
    prevs = ['README.md'] + chapter_files[:-1]
    nexts = chapter_files[1:] + ['README.md']

    print("Chapter files:")
    for filename, prev, next in zip(chapter_files, prevs, nexts):
        end = CHAPTER_END.format(prev=prev, next=next)
        update_end(filename, end)

    print()

    print("Other files:")
    for filename in other_files:
        update_end(filename, BASIC_END)


if __name__ == '__main__':
    main()
