import os
import logging_config
import models
import IO_handler
from prompts import (commentPrompt, gradePrompt, markPrompt,
                     questionPrompt, summaryPrompt,
                     speech_feedbackPrompt, transcript_correctionPrompt)

from flask import Flask, jsonify
from dotenv import load_dotenv
from logging_config import configure_logger
from arg_parser import parse_args

load_dotenv()

logger = configure_logger()
args = parse_args()

app = Flask(__name__)

chat = models.Interaction(os.getenv('AZURE_OPENAI_KEY'),
                          os.getenv('AZURE_OPENAI_ENDPOINT'))


@app.route('/comment', methods=['POST'])
def comment():
    try:
        inputs = IO_handler.extract_values(['all_criteria', 'journal', 'assignment context'])

        system_message = commentPrompt.system_prompt.format(criteria=inputs['all_criteria'],
                                                            assignment_context=inputs['assignment context'])

        user_message = commentPrompt.user_prompt.format(assignment=inputs['journal'])

        response = chat.invoke(system_message, user_message, output_format="str")

        return jsonify({'comment': response})

    except Exception as e:
        logging_config.error_logger(Exception, e)


@app.route('/grade', methods=['POST'])
def grade():
    try:
        inputs = IO_handler.extract_values(['criteria', 'journal', 'assignment context'])

        system_message = gradePrompt.system_prompt.format(criteria=inputs['criteria'],
                                                          assignment_context=inputs['assignment context'])

        user_message = gradePrompt.user_prompt.format(assignment=inputs['journal'])

        response = chat.invoke(system_message, user_message, output_format=gradePrompt.parser)

        return jsonify({'grade': response})

    except Exception as e:
        logging_config.error_logger(Exception, e)


@app.route('/question', methods=['POST'])
def question():
    try:
        inputs = IO_handler.extract_values(['journal', 'service_context',
                                           'history', 'question'])

        system_message = questionPrompt.system_prompt.format(conversation_history=inputs['history'],
                                                             assignment_context=inputs['service_context'],
                                                             question=inputs['question'])

        user_message = questionPrompt.user_prompt.format(assignment=inputs['journal'])

        response = chat.invoke(system_message, user_message, output_format="str")

        return jsonify({'answer': response})

    except Exception as e:
        logging_config.error_logger(Exception, e)


@app.route('/summaryNsentiment', methods=['POST'])
def summaryNsentiment():
    try:
        inputs = IO_handler.extract_values(['text', 'assignment context'])

        system_message = summaryPrompt.system_prompt.format(assignment_context=inputs['assignment context'])

        user_message = summaryPrompt.user_prompt.format(assignment=inputs['text'])

        response = chat.invoke(system_message, user_message, output_format=summaryPrompt.parser)

        return jsonify(response)

    except Exception as e:
        logging_config.error_logger(Exception, e)


@app.route('/marking', methods=['POST'])
def marking():
    try:
        inputs = IO_handler.extract_values(['assignment context', 'question',
                                           'sample solution', 'total marks',
                                            'student solution'])

        system_message = markPrompt.system_prompt.format(assignment_context=inputs['assignment context'],
                                                         question=inputs['question'],
                                                         sample_solution=inputs['sample solution'],
                                                         total_marks=inputs['total marks'])

        user_message = markPrompt.user_prompt.format(assignment=inputs['student solution'])

        response = chat.invoke(system_message, user_message, output_format=markPrompt.parser)

        return jsonify([response])

    except Exception as e:
        logging_config.error_logger(Exception, e)


@app.route('/speech_feedback', methods=['POST'])
def speech_feedback():
    try:
        inputs = IO_handler.extract_values(['assignment context', 'gaze',
                                           'clear_view', 'filler_word',
                                            'pronunciation_error',
                                            'transcript_count',  'transcript'])

        system_message = speech_feedbackPrompt.system_prompt.format(
            assignment_context=inputs['assignment context'],
            gaze=inputs['gaze'],
            clear_view=inputs['clear_view'],
            filler_word=inputs['filler_word'],
            pronunciation_error=inputs['pronunciation_error'],
            transcript_count=inputs['transcript_count']
        )
        user_message = speech_feedbackPrompt.user_prompt.format(transcript=inputs['transcript'])

        response = chat.invoke(system_message, user_message, output_format='str')

        return jsonify({'speech feedback': response})

    except Exception as e:
        logging_config.error_logger(Exception, e)


@app.route('/transcript_correction', methods=['POST'])
def transcript_correction():
    try:
        inputs = IO_handler.extract_values(['assignment context', 'transcript'])

        system_message = (transcript_correctionPrompt.system_prompt.
                          format(assignment_context=inputs['assignment context']))

        user_message = transcript_correctionPrompt.user_prompt.format(transcript=inputs['transcript'])

        response = chat.invoke(system_message, user_message, output_format=transcript_correctionPrompt.parser)

        return jsonify([response])

    except Exception as e:
        logging_config.error_logger(Exception, e)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
