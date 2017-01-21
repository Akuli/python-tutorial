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

"""Strip trailing whitespace from markdown files."""

import common


def needs_stripping(file):
    with common.slashfix_open(file, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            if line != line.rstrip():
                # contains trailing whitespace other than '\n'
                return True
    return False


def strip(file):
    lines = []
    with common.slashfix_open(file, 'r') as f:
        for line in f:
            lines.append(line.rstrip())
    with common.slashfix_open(file, 'w') as f:
        for line in lines:
            print(line, file=f)


def main():
    for file in common.get_markdown_files():
        if needs_stripping(file):
            print("Stripping", file)
            strip(file)
        else:
            print("No trailing whitespace in", file)


if __name__ == '__main__':
    main()
