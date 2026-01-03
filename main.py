import os
from dotenv import load_dotenv
import pprint
import argparse

from google import genai
from google.genai import types

from prompts import system_prompt
from function_calls import available_functions, call_function, ai_res_dum
from config import DUMMY

def main():

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    func_results = []
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No Gemini api key set in .env")

    client = genai.Client(api_key=api_key)

    user_prompt = args.user_prompt

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )

    if DUMMY:
        ai_res = ai_res_dum
    else:
        ai_res = client.models.generate_content(
            model = 'gemini-2.5-flash',
            contents = messages,
            config = config
        )

    if ai_res.usage_metadata is None:
        raise RuntimeError('No response from the Agent')

    if args.verbose:
        return_text = {
            'User Prompt': user_prompt,
            'Prompt Tokens': ai_res.usage_metadata.prompt_token_count,
            'Response Tokens': ai_res.usage_metadata.candidates_token_count,
            'Response': ai_res.text
        }
    else:
        return_text = ai_res.text

    if ai_res.function_calls:
        for i in ai_res.function_calls:
            func_call_res = call_function(i,verbose=args.verbose)

            if not func_call_res.parts:
                raise ValueError("cannot be an empty list")
            
            if not func_call_res.parts[0].function_response:
                return ValueError("No response from function")
            
            if not func_call_res.parts[0].function_response.response:
                raise ValueError("Response is None")
            
            func_results.append(func_call_res.parts[0])

    pprint.pprint(return_text,sort_dicts=False)

if __name__ == "__main__":
    main()
