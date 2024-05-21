from flask import request


def extract_values(keys):
    values = {}
    for key in keys:
        values[key] = request.json.get(key, None)
    return values


def remove_special_characters(s):
    s = s.replace('\n', '\\n')
    s = s.replace('"', '\\"')
    s = s.replace('\t', '\\t')
    return s
