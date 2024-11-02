from config import GOOGLE_API_KEY
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

model = ChatVertexAI(model="gemini-1.5-flash")
parser = StrOutputParser()


system_message = """You are common vulnerabilities sequence labeling bot. You will assign labels to token, which will be used by information extraction tools downstream. 
This is the BIO scheme to do sequence labeling in
B-Attack: Beginning of an attack type or description
I-Attack: Inside of an attack type or description
B-Vector: Beginning of pathway or method used by attackers
I-Vector: Inside of pathway or method used by attackers
B-Prerequisite: Beginning of a prerequisite input
I-Prerequisite: Inside a prerequisite input
B-Output: Beginning of a potential output
I-Output: Inside a potential output
O: Outside any relevant category
"""

messages = [
    SystemMessage(content=system_message),
    HumanMessage(content="What are you and what is your function?"),
]

result = model | parser
print(result)
