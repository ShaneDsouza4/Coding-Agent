from dotenv import load_dotenv
from openai import OpenAI
import json
from tools.command_execution_tools import *
from tools.File_IO_tools import *
from tools.navigation_tools import *
from tools.utilities import *
from prompts.coding_assistant_prompt import AGENT_SYSTEM_PROMPT
import time

load_dotenv()


available_tools = {
    "run_command": run_command,
    "run_command_stream_output": run_command_stream_output,
    "run_background_process": run_background_process,
    "check_command_exists": check_command_exists,
    "install_angular_cli": install_angular_cli,
    "create_angular_project": create_angular_project,
    "create_react_project": create_react_project,
    "generate_angular_entity": generate_angular_entity,
    "read_file": read_file,
    "write_file": write_file,
    "update_file":update_file,
    "search_in_file":search_in_file,
    "append_to_file": append_to_file,
    "get_current_directory": get_current_directory,
    "change_directory": change_directory,
    "delete_file": delete_file,
    "create_folder": create_folder,
    "delete_folder": delete_folder,
    "get_weather": get_weather
}   

SYSTEM_PROMPT = AGENT_SYSTEM_PROMPT

client = OpenAI()

messages = [
    { "role":"system", "content": SYSTEM_PROMPT },
]

print("Welcome! I'm your terminal coding agent. 🚀")
print("Tell me what to build, I'll take care of it.\n")
print()

while True:
    query = input("> ")
    messages.append({"role":"user", "content": query})

    # Internal Agent Loop
    while True:
        response = client.chat.completions.create(
            model="gpt-4.1",
            response_format={"type":"json_object"},
            messages=messages
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        parsed_response = json.loads(reply)

        step = parsed_response.get("step")

        if step == "analyse":
            print("🔍 Analyse:", parsed_response.get("content"))
            print() 

        elif step == "plan":
            print("🧠 Plan:", parsed_response.get("content"))
            print() 

        elif step == "user-interaction":
            question = parsed_response.get("content")
            print("🤔 Question:", question)
            user_reply = input("> ")
            messages.append({"role": "user", "content": user_reply})
            print() 

        elif step == "user-response":
            print("📥 Processing...")
            print() 

        elif step == "think-on-user":
            print("🧠 Adjusted Plan:", parsed_response.get("content"))
            print() 

        elif step == "generate":
            tool_name = parsed_response.get("function")
            tool_input = parsed_response.get("input")
            
            print(f"🛠️ Generating with {tool_name}: {tool_input}")
            print() 
            
            if available_tools.get(tool_name) != False:
                output = available_tools[tool_name](tool_input)
                messages.append({
                    "role": "user",
                    "content": json.dumps({"step": "observe", "output": output})
                })
            
        elif step == "output":
            print("🤖:", parsed_response.get("content"))
            print() 
            break  
