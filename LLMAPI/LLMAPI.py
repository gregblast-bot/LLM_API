import openai
import os

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_chatgpt_response(prompt, model="gpt-3.5-turbo"):
    """
    Sends a prompt to the ChatGPT API and returns the response.

    Args:
        prompt (str): The prompt to send to the API.
        model (str): The model to use for the API call.

    Returns:
        str: The response from the API.
    """
    try:
        completion = openai.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break
        response = get_chatgpt_response(user_input)
        if response:
            print("ChatGPT:", response)
