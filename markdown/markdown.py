import re


def parse(markdown):
    lines = markdown.split('\n')
    result = ''
    in_list = False
    in_list_append = False
    for line in lines:
        line = match_and_create_headline(line)
        emphasis = re.match(r'\* (.*)', line)
        if emphasis:
            if not in_list:
                in_list = True
                current_text = emphasis.group(1)
                current_text = match_and_create_bold(current_text)
                current_text = match_and_create_italic(current_text)
                line = '<ul><li>' + current_text + '</li>'
            else:
                current_text = emphasis.group(1)
                current_text = match_and_create_bold(current_text)
                current_text = match_and_create_italic(current_text)
                line = create_lineitem(current_text)
        else:
            if in_list:
                in_list_append = True
                in_list = False

        emphasis = re.match('<h|<ul|<p|<li', line)
        if not emphasis:
            line = '<p>' + line + '</p>'
        line = match_and_create_bold(line)
        line = match_and_create_italic(line)
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        result += line
    if in_list:
        result += '</ul>'
    return result


def match_and_create_bold(text):
    match = re.match('(.*)__(.*)__(.*)', text)
    if match:
        return match.group(1) + '<strong>' + match.group(2) + '</strong>' + match.group(3)
    return text


def match_and_create_italic(text):
    match = re.match('(.*)_(.*)_(.*)', text)
    if match:
        return match.group(1) + '<em>' + match.group(2) + '</em>' + match.group(3)
    return text


def match_and_create_headline(line):
    if re.match('###### (.*)', line):
        line = '<h6>' + line[7:] + '</h6>'
    elif re.match('## (.*)', line):
        line = '<h2>' + line[3:] + '</h2>'
    elif re.match('# (.*)', line):
        line = '<h1>' + line[2:] + '</h1>'
    return line


def create_lineitem(text):
    return '<li>' + text + '</li>'
