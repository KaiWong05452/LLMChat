from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import template

"""
Please refer to COSTAR Prompt structure CONTEXT, OBJECTIVE, STYLE, TONE, AUDIENCE, RESPONSE FORMAT
"""

# Transcript correction

role = """
As a Speech Transcript Corrector, you need to analyze the provided speech transcript, 
identify potential pronunciation errors, and make necessary corrections. 
Please utilize the subject/assignment context provided to infer the original words that were intended in the speech.
"""

objective = """
To return a corrected transcript that is free of pronunciation errors. 
In addition, you need to provide a word pair for each correction made, 
which includes the original word from the transcript and the corrected word. 
This allows for a clear understanding of the changes made to the transcript.
"""

assignment_context = """
Here is the subject/assignment context, which provide a general summary and relevant information of a the course.
{assignment_context}
"""


class OutputFormat(BaseModel):
    Corrected_transcript: str = Field(description="The corrected transcript without pronunciation errors")
    Word_pair: str = Field(description="word pair of original word and corrected word. "
                                       "e.g. original word 1, corrected word 1; original word 2, corrected word 2.")


parser = JsonOutputParser(pydantic_object=OutputFormat)

system_message = (template.create_system_message
                  (role=role, objective=objective,
                   assignment_context=assignment_context))

system_prompt = PromptTemplate(
    template=system_message+"\n{output_format}",
    input_variables=["assignment_context"],
    partial_variables={"output_format": "{output_format}"}
)

user_message = """
Here is the user input:
{transcript}
"""

user_prompt = PromptTemplate(
    template=user_message,
    input_variables=["transcript"]
)
