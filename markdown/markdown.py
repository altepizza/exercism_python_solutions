import re

BOLD_RE = re.compile(r'__(.*)__')
H1_RE = re.compile(r'^# (.*)', re.M)
H2_RE = re.compile(r'^## (.*)', re.M)
H6_RE = re.compile(r'^###### (.*)', re.M)
ITALIC_RE = re.compile(r'_(.*)_')
LIST_ITEM_RE = re.compile(r'^\* (.*)', re.M)
LIST_RE = re.compile(r'(<li>.*</li>)', re.S)
NEW_PARAGRAGRAPH_RE = re.compile(r'^(?!<[h|li|ul])(.*)', re.M)


def parse(markdown):
    markdown = BOLD_RE.sub(r'<strong>\1</strong>', markdown)
    markdown = ITALIC_RE.sub(r'<em>\1</em>', markdown)
    markdown = H1_RE.sub(r'<h1>\1</h1>', markdown)
    markdown = H2_RE.sub(r'<h2>\1</h2>', markdown)
    markdown = H6_RE.sub(r'<h6>\1</h6>', markdown)
    markdown = LIST_ITEM_RE.sub(r'<li>\1</li>', markdown)
    markdown = LIST_RE.sub(r'<ul>\1</ul>', markdown)
    markdown = NEW_PARAGRAGRAPH_RE.sub(r'<p>\1</p>', markdown)
    markdown = markdown.replace('\n', '')
    return markdown
