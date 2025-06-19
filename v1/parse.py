# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Set your Gemini API key
# genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# template = (
#     "You are tasked with extracting specific information from the following text content: {dom_content}. "
#     "Please follow these instructions carefully: \n\n"
#     "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
#     "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
#     "3. **Empty Response:** If no information matches the description, return an empty string ('')."
#     "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
# )

# def parse_with_gemini(dom_content, parse_description):
#     model = genai.GenerativeModel("gemini-2.5-flash")
#     parsed_result = []
#     for i, chunk in enumerate(dom_content, start=1):
#         prompt = template.format(dom_content=chunk, parse_description=parse_description)
#         try:
#             response = model.generate_content(prompt)
#             # Safely extract the text, or use empty string if nothing returned
#             text = ""
#             if response.candidates and response.candidates[0].content.parts:
#                 text = response.candidates[0].content.parts[0].text.strip()
#             else:
#                 print(f"Parsed batch {i} of {len(dom_content)}: EMPTY RESPONSE")
#             parsed_result.append(text)
#         except ValueError as e:
#             print(f"Parsed batch {i} of {len(dom_content)}: ValueError occurred - {e}")
#             parsed_result.append("")
#     return "\n".join(parsed_result)

import google.generativeai as genai
from dotenv import load_dotenv
import os
import json # Import the json module

load_dotenv()

# Set your Gemini API key
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **Output Format:** You MUST return the extracted information as a JSON array of objects. "
    "   Each object in the array should represent a distinct item or record, with keys corresponding to the attributes you are extracting. "
    "   For example, if you are asked for 'product names and prices', the output should look like: "
    "   `[{{\"product_name\": \"Product A\", \"price\": \"$10.00\"}}, {{\"product_name\": \"Product B\", \"price\": \"$25.50\"}}]`\n"
    "   If you are extracting a single piece of information, return an array with one object: `[{{\"extracted_data\": \"The extracted text\"}}]`\n"
    "3. **No Extra Content:** Do not include any additional text, comments, or explanations outside the JSON array. "
    "4. **Empty Response:** If no information matches the description, return an empty JSON array `[]`."
)

def parse_with_gemini(dom_content, parse_description):
    model = genai.GenerativeModel("gemini-2.5-flash")
    all_parsed_data = [] # This will store all dictionaries

    for i, chunk in enumerate(dom_content, start=1):
        prompt = template.format(dom_content=chunk, parse_description=parse_description)
        try:
            response = model.generate_content(prompt)
            text = ""
            if response.candidates and response.candidates[0].content.parts:
                text = response.candidates[0].content.parts[0].text.strip()

                # --- START: New logic to remove markdown code block fences ---
                if text.startswith('```json'):
                    text = text[len('```json'):] # Remove ```json from the beginning
                if text.endswith('```'):
                    text = text[:-len('```')] # Remove ``` from the end
                text = text.strip() # Strip any remaining whitespace
                # --- END: New logic ---

            if text:
                try:
                    # Attempt to parse the JSON string
                    json_data = json.loads(text)
                    if isinstance(json_data, list):
                        all_parsed_data.extend(json_data)
                    elif isinstance(json_data, dict): # If Gemini returns a single object instead of array
                        all_parsed_data.append(json_data)
                    else:
                        print(f"Warning: Gemini returned non-JSON array/object for batch {i}: {text}")
                except json.JSONDecodeError as e:
                    print(f"JSON parsing error for batch {i}: {e}. Raw text: {text}")
            else:
                print(f"Parsed batch {i} of {len(dom_content)}: EMPTY RESPONSE from Gemini.")

        except ValueError as e: # Gemini API specific errors (e.g., if content is blocked)
            print(f"Parsed batch {i} of {len(dom_content)}: ValueError occurred - {e}")
            # Optionally append an empty dictionary or mark as error if you want to track it
            # all_parsed_data.append({"error": f"API Error: {e}"})
        except Exception as e: # Catch other potential errors
            print(f"An unexpected error occurred for batch {i}: {e}")
            # Optionally append an empty dictionary or mark as error
            # all_parsed_data.append({"error": f"Unexpected Error: {e}"})

    return all_parsed_data # Return a list of dictionaries
