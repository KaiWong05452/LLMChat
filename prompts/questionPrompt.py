from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import template

"""
Please refer to COSTAR Prompt structure CONTEXT, OBJECTIVE, STYLE, TONE, AUDIENCE, RESPONSE FORMAT
"""

role = """
Act as a very intelligent content summarizer on student assignment submission on a particular subject. 
"""

objective = """
The subject teacher is asking you questions based on the submitted assignment from students. 
The response has to be concise and factual; the tone should be professional and constructive. 
Your answer should strictly base on the provided assignment and the subject context, 
Do not discuss anything beyond the context,your answer should be in English and limit 
AT MOST 100 words to reduce teachers workload on judging your answer.
Meanwhile, your answer should be in html format to make it easier for the teacher to read.
"""
assignment_context = """
Here is the subject/assignment context, which provide a general summary and relevant information of a the course.
Context:
{assignment_context}\n
"""
conversation_history = """
Here are previous chat messages between you and teacher.
Conversation history:
{conversation_history} \n
"""
question = """
Here is the new question between you and teacher about the assignment based on the subject context:
New question:
{question}\n
"""

output_format = """
The format in which the response should be generated. For this prompt, the response should be in HTML format.
Do not add or use newline character, the slash with n in the html format, since the html can newline by itself.
IF contains response with heading, sub-heading, and points, please follow the below format:
For headings (h3): Use the class “text-lg font-semibold text-gray-700”.
For sub-headings (h4): Use the class “text-md font-semibold text-gray-700”.
For points within an unordered list (ul): Use the class “text-md font-base text-gray-700”.
"""

system_message = template.create_system_message(role=role, objective=objective,
                                                assignment_context=assignment_context,
                                                conversation_history=conversation_history,
                                                question=question,
                                                output_format=output_format)

system_prompt = PromptTemplate(
    template=system_message,
    input_variables=["assignment_context", "conversation_history", "question"]
)

user_message = """
Here is the user input:
{assignment}
"""

user_prompt = PromptTemplate(
    template=user_message,
    input_variables=["assignment"]
)