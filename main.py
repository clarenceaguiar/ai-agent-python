import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function
import json
import sys


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key == "" or api_key is None:
    raise Exception("api_key not found or invalid")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": str(args.user_prompt)}
]

def main():
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            #temperature=0,
            tools=available_functions
        )
        if response.usage is None:
            raise RuntimeError("Failed API request")
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls != None and message.tool_calls != []:
            for tool_call in message.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                result_message: dict[str] = call_function(tool_call, function_args)
                if result_message["content"] == "":
                    raise Exception("Content message is empty...")
                if args.verbose:
                    print(f"-> {result_message['content']}")
                messages.append(result_message)
        else:
            print(f"Response:\n{response.choices[0].message.content}")
            break
    else:
        sys.exit("The limit of iteration finished...")
if __name__ == "__main__":
    main()
