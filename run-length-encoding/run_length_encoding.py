import re

re_decode_instructions = re.compile(r'[0-9]*.{1}')
re_get_count = re.compile(r'[0-9]+')


def _partial_decode(decode_instruction):
    if len(decode_instruction) >= 2:
        count = re_get_count.search(decode_instruction)[0]
        char = decode_instruction.replace(count, '')
        return char * int(count)
    return decode_instruction


def decode(string):
    instructions = re_decode_instructions.findall(string)
    return ''.join([_partial_decode(i) for i in instructions])


def _partial_encode(string):
    for count, char in enumerate(string):
        if count + 1 < len(string):
            if string[count] != string[count + 1]:
                return count, char
        else:
            return count, char


def encode(string):
    tmp_encodes = []
    while (string):
        count, char = _partial_encode(string)
        if count > 0:
            tmp_encodes.append(f'{count+1}{char}')
        else:
            tmp_encodes.append(char)
        string = string[count + 1:]
    return ''.join(tmp_encodes)
