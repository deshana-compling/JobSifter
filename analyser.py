import os
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT, USER_PROMPT
from google import genai 

load_dotenv(override=True)
geminikey = os.getenv('GEMINI_KEY')

if not geminikey:
    raise ValueError('API Key not found! Please check your .env file')

client = genai.Client(api_key=geminikey)

def cvanalyser(cv_text, job_description):
    response = client.models.generate_content(
        model='gemini-3.7-flash',
        contents=USER_PROMPT.format(
            cv=cv_text,
            job_description=job_description
        ),
        config={
            'system_instruction': SYSTEM_PROMPT
        }
    )
    return response.text

if __name__ == '__main__':

    with open('demo/demo_cv.txt', 'r', encoding='utf-8') as file:
        test_cv = file.read()

    with open('demo/demo_job.txt', 'r', encoding='utf-8') as file:
        test_job = file.read()

    result = cvanalyser(test_cv, test_job)

    print(result)