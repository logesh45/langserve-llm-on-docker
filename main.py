from fastapi import FastAPI
from langserve import add_routes
from langchain_community.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import re

# Create a FastAPI app
app = FastAPI(title="Llama Server")

# Define the Llama model
llm = LlamaCpp(
    model_path="your model name",
    temperature=0.75,
    max_tokens=2000,
    top_p=1
)

# Define the prompt template
prompt = PromptTemplate(
    input_variables=["system_message", "user_message"],
    template="""<s>[INST] <<SYS>>
    {system_message}
    <</SYS>>
    {user_message} [/INST]"""
)

chain = LLMChain(llm=llm, prompt=prompt)

# Add routes to the FastAPI app
add_routes(
    app,
    chain,
    path="/llama"
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000)
