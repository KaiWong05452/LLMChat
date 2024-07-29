import setup
import os
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.runnables import RunnablePassthrough

class Interaction:
    def __init__(self, api_key, endpoint, openai_api_version, deployment_name, temperature=0, model_version=None):
        os.environ["AZURE_OPENAI_API_KEY"] = api_key
        os.environ["AZURE_OPENAI_ENDPOINT"] = endpoint

        self.output_parser = StrOutputParser()

        self.model = AzureChatOpenAI(
            openai_api_version=openai_api_version,
            deployment_name=deployment_name,
            temperature=temperature,
            model_version=model_version
        )

    def invoke(self, system_message, user_message, output_format='str'):

        user_template = """
        {user_input}
        """
        system_prompt = SystemMessagePromptTemplate.from_template(system_message)
        user_prompt = HumanMessagePromptTemplate.from_template(user_template)
        chat_prompt = ChatPromptTemplate.from_messages([system_prompt, user_prompt])

        if output_format == 'str':
            self.output_parser = StrOutputParser()

            chain = ({"user_input": RunnablePassthrough()} | chat_prompt | self.model | self.output_parser)
            result = chain.invoke(user_message)
        else:
            # Self-define case
            self.output_parser = output_format

            chain = ({"user_input": RunnablePassthrough(),
                      "output_format": RunnablePassthrough()} | chat_prompt | self.model | self.output_parser)
            result = chain.invoke({"user_input": user_message,
                                   "output_format": self.output_parser.get_format_instructions()})

        return result
