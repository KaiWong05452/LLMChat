from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import template

"""
Please refer to COSTAR Prompt structure CONTEXT, OBJECTIVE, STYLE, TONE, AUDIENCE, RESPONSE FORMAT
"""

# marking
role = """
You are a rigorous and exceptional university instructor.
"""
task_description = """
Please think step by step,
You need to evaluate and mark the student's solution based on the question and sample solution.
The sample solution is correct in terms of content. It would receive full marks.
"""
assignment_context = """
Here is the subject/assignment context, which provide a general summary and relevant information of a the course.
{assignment_context}
"""
question = """
Here is the question:
{question}
"""
sample_solution = """
Here is the sample solution:
{sample_solution}
"""
total_marks = """
Here is the total marks:
{total_marks}
"""


class OutputFormat(BaseModel):
    marking: str = Field(description="Mark of the solution.")
    explanation: str = Field(description="Explanation to the marks.")


parser = JsonOutputParser(pydantic_object=OutputFormat)

system_message = (template.create_system_message
                  (role=role, task_description=task_description,
                   assignment_context=assignment_context,
                   question=question,
                   sample_solution=sample_solution,
                   total_marks=total_marks))

system_prompt = PromptTemplate(
    template=system_message+"\n{output_format}",
    input_variables=["assignment_context", "question"
                     "sample_solution", "total_marks"],
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
