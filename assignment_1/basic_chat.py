import os
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel, Field
from typing import Optional
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
#LANGCHAIN TRACKING AND TRACING
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT'] = "AgenticAILearningAssignment1"
os.environ['LANGCHAIN_TRACING_v2'] = "true"

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
llm = ChatGroq(model='deepseek-r1-distill-llama-70b',temperature=0.5)
#llm = ChatOpenAI(model="gpt-4o")

class Product(BaseModel):
    ProductName : str
    ProductDetails : str
    TentativePrice : int =Field(description="The price must be provided in USD")

from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser(pydantic_object=Product)
parser

prompt = ChatPromptTemplate.from_template("Tell me about the Product {query}\n{format_instructions}").partial(format_instructions=parser.get_format_instructions())
prompt

chain = prompt | llm | parser

chain.invoke({"query":"Sony TV"})
