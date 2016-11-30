"""Update ends of markdown files."""

import collections
import glob
import re


BASIC_END = """
***

You may use this tutorial freely at your own risk. See
[LICENSE](LICENSE).

[Back to the list of contents](README.md#list-of-contents)
"""

CHAPTER_END = """
***

You may use this tutorial freely at your own risk. See
[LICENSE](LICENSE).

[Previous]({prev}) | [Next]({next}) |
[Back to the list of contents](README.md#list-of-contents)
"""


MARKDOWN_LINK_REGEX = r'\[.*\]\((.*\.md)\)'
CHAPTER_LINK_REGEX = '^\d+\. ' + MARKDOWN_LINK_REGEX + '$'


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
        all_files = re.findall(MARKDOWN_LINK_REGEX, f.read())
    others = set(all_files) - set(chapters)

    return chapters, others


def has_end(filename, template):
    linecount = template.count('\n')
    with open(filename, 'r') as f:
        # get the last linecount lines
        filelines = collections.deque(f, maxlen=linecount)
    templatelines = template.rstrip('\n').split('\n')

    for templateline, fileline in zip(templatelines, filelines):
        if '{' not in templateline:
            # It doesn't contain formatting, we can do something with it.
            if templateline.strip() != fileline.strip():
                # It's different than what using the template would result in.
                return False

    # All lines matched if we get here.
    return True


def main():
    chapter_files, other_files = get_filenames()

    # make previous of first file and next of last file to just bring
    # back to README
    prevs = ['README.md'] + chapter_files[:-1]
    nexts = chapter_files[1:] + ['README.md']

    print("Chapter files")
    for filename, prev, next in zip(chapter_files, prevs, nexts):
        if has_end(filename, CHAPTER_END):
            print("  Has end:", filename)
        else:
            print("  Adding end:", filename)
            with open(filename, 'a') as f:
                f.write(CHAPTER_END.format(prev=prev, next=next))

    print()

    print("Other files")
    for filename in other_files:
        if has_end(filename, BASIC_END):
            print("  Has end:", filename)
        else:
            print("  Adding end:", filename)
            with open(filename, 'a') as f:
                f.write(BASIC_END)


if __name__ == '__main__':
    main()
