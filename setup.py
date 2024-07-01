import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def install_chatgpt_packages():
    install('langchain')
    install('langchain-openai')
    install('flask')
    install('python-dotenv')
    install('pypdf')
    install('python-pptx')
    install('python-docx')
