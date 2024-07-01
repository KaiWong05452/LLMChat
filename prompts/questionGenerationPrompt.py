from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import template

"""
Please refer to COSTAR Prompt structure CONTEXT, OBJECTIVE, STYLE, TONE, AUDIENCE, RESPONSE FORMAT
"""

# question generation
role = """
You are an AI assistant tasked with generating questions based on the provided context. 
Your role is to understand the context, difficulty, and type of questions required, 
and generate appropriate questions accordingly.
"""

objective = """
Your objective is to generate a set of questions that align with the provided context, difficulty, and question type. 
The questions should be diverse and thought-provoking, encouraging deep understanding of the subject matter.
"""

difficulty = """
{difficulty} 
"""

question_type = """
The question type is:
{question_type}

If question type is multiple choice, please refer to the following format:
Format:
	"Question"
	A.
	B.
	C.
	D.

	"Correct Answer"
    "Explanation"
    
If question type is True/False, please refer to the following format:
Format:
    "Question"
    "Answers"
    "Correct Answer"
    "Explanation"
"""


num_questions = """
{num_questions}
Please strictly follow the number of questions required.
"""

num_choices = """
{num_choices}
Please strictly follow the number of choices required.
"""

subject_context = """
The following content provides the subject context,
which may give general information about the subject or topic,
from user input or extracted from a document in pdf/docx/pptx format:
"""

class OutputFormat(BaseModel):
    Question: str = Field(
        description="The generated question based on the provided context, difficulty, and question type.")

    Answers: str = Field(description="The answer choices for the generated question.")

    Correct_answer: str = Field(description="The correct answer to the generated question.")

    Explanation: str = Field(
        description="An explanation detailing why the correct answer is correct,"
                    " and why the wrong answer(s) is(are) incorrect.")


parser = JsonOutputParser(pydantic_object=OutputFormat)

system_message = template.create_system_message(role=role,
                                                objective=objective,
                                                difficulty=difficulty,
                                                question_type=question_type,
                                                num_questions=num_questions,
                                                num_choices=num_choices)

system_prompt = PromptTemplate(
    template=system_message+"\n{output_format}",
    input_variables=["difficulty", "question_type", "num_questions", "num_choices"],
    partial_variables={"output_format": "{output_format}"}
)

user_message = """
Here is the user requirement:
{requirement}
"""

user_prompt = PromptTemplate(
    template=user_message,
    input_variables=["requirement"]
)
