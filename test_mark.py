from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from prompts import commentPrompt,gradePrompt,markPrompt,questionPrompt,summaryPrompt
import template
import models
import os

chat = models.Interaction(os.getenv('AZURE_OPENAI_KEY'),
                          os.getenv('AZURE_OPENAI_ENDPOINT'))

# Please refer to COSTAR Prompt structure CONTEXT, OBJECTIVE, STYLE, TONE, AUDIENCE, RESPONSE FORMAT


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
Here is the subject context, which provide a general summary and relevant information of a the course.
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
    partial_variables={"output_format": parser.get_format_instructions()}
)

user_message = """
Here is the user input:
{assignment}
"""

user_prompt = PromptTemplate(
    template=user_message,
    input_variables=["assignment"]
)

assignment_context_input = """
"subject: Computer Science",
"topic: Search algorithnm",
"difficulty: Intermediate",
"type: Open-ended"
"""
question_input = """
What is the difference between breadth-first search (BFS) and depth-first search(DFS) in terms of their exploration strategy?
"""
sample_solution_input = """
BFS explores the search space level by level, visiting all neighbors of a node beforemoving on to the next level(1.5 marks).
DFS, on the other hand, explores as far as possible alongeach branch before backtracking(1.5 marks).
"""
total_marks_input = """
3
"""
student_solution_input = """
BFS use FIFS and DFS use LIFO.
"""
system_message = markPrompt.system_prompt.format(assignment_context=assignment_context_input,
                                           question=question_input,
                                           sample_solution=sample_solution_input,
                                           total_marks=total_marks_input)

user_message = markPrompt.user_prompt.format(assignment=student_solution_input)

result = chat.invoke(system_message, user_message, output_format=markPrompt.parser)

print(result)
