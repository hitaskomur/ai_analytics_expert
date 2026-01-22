from database.db_fetch import DATA
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()
from ai_utils.analyzer_prompt import prompt
import fastapi




llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)

data = DATA
prompt = prompt

app = fastapi.FastAPI()

@app.post("/analyze")
async def analyze(question: str):

    chunk = prompt | llm | JsonOutputParser()

    response = chunk.invoke({"data": data,"question": question})
    #print(response)


    return response