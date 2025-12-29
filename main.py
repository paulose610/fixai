import os
from dotenv import load_dotenv
import pprint
import argparse

from google import genai
from google.genai import types


def main():

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No Gemini api key set in .env")

    client = genai.Client(api_key=api_key)

    user_prompt = args.user_prompt

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    ai_res = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = messages
    )

    if ai_res.usage_metadata is None:
        raise RuntimeError('No response from the Agent')
    
    if args.verbose:
        ai_res = {
            'User Prompt': user_prompt,
            'Prompt Tokens': ai_res.usage_metadata.prompt_token_count,
            'Response Tokens': ai_res.usage_metadata.candidates_token_count,
            'Response': ai_res.text
        }
    else:
        ai_res = ai_res.text

    pprint.pprint(ai_res,sort_dicts=False)

if __name__ == "__main__":
    main()
