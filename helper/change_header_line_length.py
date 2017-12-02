#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib_mate import Path
from dataIO import textfile

header_char = "=-~+*"

def fix_rst_header_char_lenght(abspath):
    lines = list(textfile.readlines(abspath))
    for ind, line in enumerate(lines):
        for char in header_char:
            line = line.strip()
            if len(line):
                if line == (char * len(line)):
                    line = char * 78
                    lines[ind] = line
                    break
    content = "\n".join(lines)
    textfile.write(content, abspath)

if __name__ == "__main__":
    source_dir = Path("/Users/sanhehu/Documents/GitHub/mm6doc-project/docs/source")

    for p in source_dir.select_by_pattern_in_fname("_content"):
        fix_rst_header_char_lenght(p.abspath)

