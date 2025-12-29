import os
import google.generativeai as g
from google.generativeai import types
from colorama import Fore, Style


client=g.configure(api_key="AIzaSyAhKCXXHgbr8f9Ld0NPzLuF0jKnfESUz2A")

def generate_response(prompt, temperature=0.3):

    try:
        contents=[types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params=types.GenerateContentConfig(temperature=temperature)
        response=client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
def bias_mitigation_activity():

    print(Fore.GREEN + "\n=== BIAS MITIGATION ACTIVITY ===\n" + Style.RESET_ALL)


    prompt=input(Fore.RED + "Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): " + Style.RESET_ALL)
    initial_response=generate_response(prompt)
    print(Fore.YELLOW + f"\nIntial AI response: {initial_response}" + Style.RESET_ALL)


    modified_prompt=input(Fore.BLUE + "Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor'): " + Style.RESET_ALL)
    modified_response=generate_response(modified_prompt)
    print(Fore.CYAN + f"\nModified AI response (Neutral): {modified_response}" + Style.RESET_ALL)

def token_limit_activity():

    print(Fore.GREEN + "\n=== TOKEN LIMIT ACTIVITY ===\n" + Style.RESET_ALL)


    long_prompt=input(Fore.RED + "Enter a long prompt (more than 300 words, e.g., a detailed story or description): " + Style.RESET_ALL)
    long_response=generate_response(long_prompt)
    print(Fore.YELLOW + f"\nResponse to Long Prompt: {long_response[:500]}..." + Style.RESET_ALL)


    short_prompt=input(Fore.BLUE + "Now, condense the prompt to be more concise: " + Style.RESET_ALL)
    short_response=generate_response(short_prompt)
    print(Fore.CYAN + f"\nResponse to Condensed Prompt: {short_response}" + Style.RESET_ALL)

def run_activity():

    print(Fore.GREEN + "\n=== AI Learning Activity ===\n" + Style.RESET_ALL)


    activity_choice=input(Fore.LIGHTBLUE_EX + "Which activity would you like to run? (1: Bias Mitigation, 2: Token Limits): " + Style.RESET_ALL)

    if activity_choice=="1":
        bias_mitigation_activity()
    elif activity_choice=="2":
        token_limit_activity()
    else:
        print(Fore.RED + "Invalid choice. Please choose either 1 or 2." + Style.RESET_ALL)

if __name__=="__main__":
    run_activity()