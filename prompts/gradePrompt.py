from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import template

"""
Please refer to COSTAR Prompt structure CONTEXT, OBJECTIVE, STYLE, TONE, AUDIENCE, RESPONSE FORMAT
"""


# grade
role = """
You are a rigorous and exceptional university professor.
For each criterion provided, you must strictly score a user-submitted assignment entry at the university level.
Your response should be strictly in JSON format and should include separate grading for each criterion.
For each separate grading, you should summarize the criterion as one word and use it as the key of that JSON.
You should focus on identifying all flaws in the assignment, even minor ones, 
and your grading should reflect these findings.
"""

chain_of_thought = """
Start by carefully reading the assignment, understand their argument, evidence, and overall logic.
Noticed that, the assignment should rigorously follow the academic, descriptive, and formal style.
If not, the following criteria scores should be considered to deduct.
Based on the criteria provided, assess whether the assignment accurately addressed the topic, 
used correct information, and followed the specified format.
The criteria demonstrates the requirement of grade range A.
For grade range, it consists of A,B,C,D,F.
If the assignment can outperforms the criteria, consider giving an A grade.
If the assignment is meeting the most of criteria, consider giving an B grade.
If one mismatch is found, consider giving a C grade.
More mismatches and errors could result in D to F grade.
Based on the overall performance towards a criteria, decide whether to assign a sub grade to main grade.
The sub grade consists of (+,unchanged,-).
If the assignment show more features towards the criteria, give a "+".
If the features are matched, leave the main grade unchanged.
For several mismatches, consider a "-".
Then, the main grade of the criteria becomes grade range + sub grade. For examples, "C","B-","A+".
Meanwhile, the grade range D and F do not have sub grade.

Ensure that your grading is consistent for all assignments. Avoid personal biases or deviations from the standard.

Please think step by step.
"""

assignment_context = """
Here is the subject/assignment context, which provide a general summary and relevant information of a the course.
{assignment_context}
"""

rubrics = """
Please provide a separate grading assessment for the following criterion.
{criteria}
"""

output_format_hint = """
Please output the JSON in the following format:
"somthing" should be an array, where each element is an object containing the keys "key1", "key2", and "key3", 
each with their respective values.

Do not output the JSON in the following format:
"somthing" should not be an object containing multiple keys, where each key corresponds to an object that contains 
the keys "key1", "key2", and "key3".
"""


class OutputFormat(BaseModel):
    Criterion: str = Field(description="Summarize the criterion as one word")
    Main_Grade: str = Field(description="the grade result according to the previous chain of thought and reasoning.")
    Reason_of_Main_Grading: (
        str) = Field(description="the grade result according to the previous chain of thought and reasoning,"
                                 "please clearly state and explain why you give the main grade of the grade range "
                                 "and a corresponding sub grade, and find out all the flaws with summarized example "
                                 "of the assignment. Your strict scoring can push students to do better in the future")


parser = JsonOutputParser(pydantic_object=OutputFormat)

system_message = template.create_system_message(role=role,
                                                chain_of_thought=chain_of_thought,
                                                assignment_context=assignment_context,
                                                grading_rubrics=rubrics,
                                                output_format_hint=output_format_hint,)

system_prompt = PromptTemplate(
    template=system_message+"\n{output_format}",
    input_variables=["assignment_context", "criteria"],
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
