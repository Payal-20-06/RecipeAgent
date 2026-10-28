from dotenv import load_dotenv
from langchain.agents import create_agent
from .prompt import SYSTEM_CHEF_PROMPT, CHEF_PROMPT
from langchain.messages import HumanMessage
from .tools import web_search
from .photo_decoder import choose_image_file, build_image_message
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

load_dotenv()


logging.info("creating our agent...")
agent = create_agent(
    model="google_genai:gemini-3.8-flash",
    tools=[web_search],
    system_prompt=SYSTEM_CHEF_PROMPT,
)

logging.info("choosing our image...")
path = choose_image_file()
message = build_image_message(path, CHEF_PROMPT)


logging.info("invoking our agent...")
response = agent.invoke(
    {"messages": [message]}
)


from recipeagent.photo_decoder import image_to_data_url

data_url = image_to_data_url(path)
print(data_url[:50])
final_message = response["messages"][-1]
content = final_message.content

if isinstance(content, str):
    print(content)
else:
    for block in content:
        if isinstance(block, dict) and block.get("type") == "text":
            print(block.get("text", ""), end="")