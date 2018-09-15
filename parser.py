# https://python-markdown.github.io/reference/

import re
file = "tests.chs"

# Open document
with open(file) as fileObj:
    doc = fileObj.read()

def parse_as_single_line_code(s):
    """ Given a single line of text it tries to parse as a single line
        code-description block eg:
            myfunc()  #### my description
    Returns: (None or dict)
        If it matches the pattern, then returns a dict with the keys:
        - code
        - desc
        Else it returns `None`
    """
    pattern = r"(?P<code>.+) #### (?P<desc>.+)"
    match = re.search(pattern, s)
    if match:
        x = match.groupdict()
        x["code"] = x["code"].strip()
        x["desc"] = x["desc"].strip()
        return x
    else:
        return None

