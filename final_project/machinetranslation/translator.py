"""
watson translator
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# instance Step 9

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')

translation = language_translator.translate(
    test='Hello, how are you today?',
    model_id='en-fr').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

# Step 10

def english_to_french(englishtext):
    """ translate english to french"""
    if len(englishtext) == 0:
        return 'Error: No text provided for translation'
    response = language_translator.translate(text=englishtext, model_id='en-fr').get_result()
    french_text = response["translations"][0]["translation"]
    return french_text

# Step 11

def french_to_english(frenchtext):
    """ translate french to english"""
    if len(frenchtext) == 0:
        return 'Error: No text provided for translation'
    response = language_translator.translate(text=frenchtext, model_id='en-fr').get_result()
    english_text = response["translations"][0]["translation"]
    return english_text
