import re

file = "test"
with open(file) as fileObj:
    text = fileObj.read()


SECTION_PATTERN = "\n#{10,}\n\s*(.*)\n#{10,}\n"
SECTION_REPLACEMENT = "\n<h2>{0}</h2>\n"


count = 0
match = re.search(SECTION_PATTERN, text)
if match:
    while match:
        count += 1
        print count
        substitution = SECTION_REPLACEMENT.format(*match.groups())
        text_before = text[:match.start()]
        text_after = text[match.end():]
        text = text_before + substitution + text_after
        match = re.search(SECTION_PATTERN, text)


print text

