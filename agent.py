from tool import tools
import os
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent


api_key=os.getenv('GROQ_API_KEY')  

llm=ChatGroq(  
    model='llama-3.3-70b-versatile',   
    api_key=api_key 
)

graph=create_react_agent(llm,tools)
example_query = "Draft an email to hamza5993795@gmail.com thanking them for coffee."
 
events = graph.stream(
    {"messages": [("user", example_query)]},
    stream_mode="values",
)
for event in events:
    event["messages"][-1].pretty_print() 