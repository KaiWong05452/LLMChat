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
Respond using Markdown.
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