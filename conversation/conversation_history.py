# Convert the conversation history which is a json list format into string output
def extract_conversation_history(data):
    output = ""
    for i, item in enumerate(data, start=1):
        output += f"question {i}: {item['question']},\n"
        output += f"answer {i}: {item['answer']},\n"
    return output
