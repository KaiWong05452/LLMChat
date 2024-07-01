from flask import request


def extract_values(keys):
    values = {}
    for key in keys:
        values[key] = request.json.get(key, None)
    return values


def extract_form_data(document_key, value_keys):
    file = request.files.get(document_key, None)

    values = {}

    for key in value_keys:
        values[key] = request.form.get(key, None)

    return file, values


def remove_special_characters(s):
    s = s.replace('\n', '\\n')
    s = s.replace('"', '\\"')
    s = s.replace('\t', '\\t')
    return s
