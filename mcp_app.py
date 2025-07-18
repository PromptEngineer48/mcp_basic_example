import os
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
from langchain_ollama import OllamaLLM

import streamlit as st


BRD_API_KEY = os.environ.get("BRD_API_KEY")

mcp = MultiServerMCPClient(
{
    "Bright Data": {
      "command": "node",
      "args": ["../.npm/_npx/a50edfa03303c0a4/node_modules/@brightdata/mcp/server.js"],
      "transport": "stdio",
      "env": {
        "API_TOKEN": BRD_API_KEY,
        "WEB_UNLOCKER_ZONE": "web_unlocker1",
      }
    }
})

async def mcp_tools():
    tools = await mcp.get_tools()
    
    for idx, tool in enumerate(tools):
        print(idx, tool.name)
        print(tool.args)
        print("***************")
    
    return tools



async def handle_prompt(tools, url, user_prompt):
    if url.startswith("https://reddit.com/"):
        scraper = tools[45]
    elif url.startswith("https://www.linkedin.com/feed/"):
        scraper = tools[17]
    else:
        scraper = tools[1]
    result = await scraper.ainvoke({
        "url": url
    })

    full_prompt = (
        "Context (scraped data):\n\n"
        + result.strip()
        + "\n\nQuestion:\n\n"
        + user_prompt
    )
    
    llm = OllamaLLM(model="gemma3n:latest")
    llm_response = llm.invoke(
        full_prompt
    )
    print(llm_response)
    return llm_response
    

tools = asyncio.run(mcp_tools())
# asyncio.run(handle_prompt(tools))


st.title("🕸️LLM Web Search")
url = st.text_input("Enter URL:")
user_prompt = st.text_area("Enter Question:")
submit = st.button("Submit")

if submit:
    with st.spinner("Processing..."):
        #handle_prompt function
        llm_response = asyncio.run(handle_prompt(
            tools,
            url,
            user_prompt
            ))
        
        st.write(llm_response)
        