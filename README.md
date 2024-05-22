# LLM Chat
## Description
LLM Chat runs on the Flask app (back-end) for educational (teacher-side) purposes, aiming at relieving the workload of evaluating students' assignments. The currently supported functions include:

1. Comment: Provide constructive and accurate feedback on the highlights and drawbacks of the student's assignment (essay type).
2. Grade: Grade the assignment (essay type) based on the provided criteria, and course-related context
3. Mark: Mark the assignment (non-essay type) based on the question, solution, and marks of the solution.
4. Question: Provide conversation with history based on the teacher's query on the assignment (essay type).
5. Summary and Sentiment: Summarize the key points and perform sentiment analysis of the assignment (essay type)
6. Speech feedback: To provide comprehensive feedback on the student's presentation from visual and speech analysis.
7. Transcript correction: To correct transcript that are incorrectly-transcribed due to pronunciation errors based on the context. 

## Requirements
The LLM used is the GPT4 model from Azure OpenAI Service. Corresponding API key, endpoint, open_api_version, and model_version are required.

## Usage
To use the functions, run main.py. The Flask app will run on localhost:5000 by default. All functions use the HTTP POST method.
1. Comment: requires the input field of all criteria, assignment, and assignment context, returns with the comment
2. Grade: requires the input field of criteria, assignment, and assignment context, returns with the grade of criteria name, grade, and explanation of the grade.
3. Question: requires the input field of assignment, assignment context, conversation history, and question, returns with the answer of the question.
4. Summary and sentiment: requires the input field of assignment, assignment context, and returns with the summary and sentiment.
5. Mark: requires the input field of assignment, assignment context, question, sample solution, total marks, returns with the marks and explanation of the mark.
Details of implementation may refer to the main.py
6. Speech feedback: the input field of transcript, assignment context, gaze, clear view, filler words, transcript count, pronunciation_error, returns with the speech feedback.
7. Transcript correction: the input field of original transcript, assignment context, returns with the corrected transcript and corrected word pairs.

To add additional functions, please refer to the prompts package, the prompt structure is simplified to declaring your requirements, and then assembling them. To have a consistent output format, please refer to prompts of grade, mark, and summary, which includes the initialization of using Pydantic and output parser. Then, you can add the new function in main, structures are similar to other implementations.
