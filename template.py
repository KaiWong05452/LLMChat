rules = {
    "QA": {"Context": "You are a helpful question answering assistant.",
           "Objective": "You task is to answer questions"}
}


def create_default_system_message(rule_name):
    rule = rules.get(rule_name)
    if not rule:
        return None

    system_message = ""
    for key, value in rule.items():
        system_message += f'"{key}": {value} \n'
    return system_message


def create_system_message(**kwargs):
    system_message = ""
    for key, value in kwargs.items():
        system_message += f'"{key}": {value} \n'
    return system_message
