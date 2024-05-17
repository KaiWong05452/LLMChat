from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import template

"""
Please refer to COSTAR Prompt structure CONTEXT, OBJECTIVE, STYLE, TONE, AUDIENCE, RESPONSE FORMAT
"""

# summary

role = """
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.
Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content.
Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense,
or is not factually coherent, explain why instead of answering something not correct.
If you don't know the answer to a question, please don't share false information.
"""

objective = """
Please read the content of the assignment carefully, 
and provide a reflection with focus on what the author is trying to convey, 
sentiment(positive/neutral/negative), and key points of the assignment.
"""

assignment_context = """
Here is the subject context, which provide a general summary and relevant information of a the course.
{assignment_context}
"""

system_message = (template.create_system_message
                  (role=role, objective=objective,
                   assignment_context=assignment_context))


class OutputFormat(BaseModel):
    Key_Points: str = Field(description="a list of the main points in the assignment.")
    Summary: str = Field(description="a concise summary of the assignment.")
    Sentiment: str = Field(description="capture the overall sentiment of the assignment")


parser = JsonOutputParser(pydantic_object=OutputFormat)

system_prompt = PromptTemplate(
    template=system_message+"\n{output_format}",
    input_variables=["assignment_context"],
    partial_variables={"output_format": "{output_format}"}
)

user_message = """
Here is the user input:
{assignment}
"""

user_prompt = PromptTemplate(
    template=user_message,
    input_variables=["assignment"]
)
