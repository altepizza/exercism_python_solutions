import re

BOLD_RE = re.compile(r'__(.*)__', re.M)
LIST_RE = re.compile(r'\* (.*)')
H1_RE = re.compile(r'^# (.*)', re.M)
H2_RE = re.compile(r'^## (.*)', re.M)
H6_RE = re.compile(r'^###### (.*)', re.M)
ITALIC_RE = re.compile(r'_(.*)_', re.M)


def parse(markdown):
    markdown = BOLD_RE.sub(r'<strong>\1</strong>', markdown)
    markdown = ITALIC_RE.sub(r'<em>\1</em>', markdown)
    markdown = H1_RE.sub(r'<h1>\1</h1>', markdown)
    markdown = H2_RE.sub(r'<h2>\1</h2>', markdown)
    markdown = H6_RE.sub(r'<h6>\1</h6>', markdown)

    lines = markdown.split('\n')
    result = ''
    in_list = False
    in_list_append = False
    for line in lines:
        emphasis = LIST_RE.match(line)
        if emphasis:
            if not in_list:
                in_list = True
                current_text = emphasis.group(1)
                line = '<ul><li>' + current_text + '</li>'
            else:
                current_text = emphasis.group(1)
                line = create_lineitem(current_text)
        else:
            if in_list:
                in_list_append = True
                in_list = False

        emphasis = re.match('<h|<ul|<p|<li', line)
        if not emphasis:
            line = '<p>' + line + '</p>'
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        result += line
    if in_list:
        result += '</ul>'
    return result


def create_lineitem(text):
    return '<li>' + text + '</li>'
