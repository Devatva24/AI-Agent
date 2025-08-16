import requests
import os

# Load API key securely
GROQ_API_KEY = os.getenv("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")  # Store your key as an environment variable

# Define the function to interact with Groq API
def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {"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"}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "mixtral-8x7b-32768",  # Ensure the model is available in your plan
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        return f"Error: {response.json().get('error', 'Unknown error')}"

    response_data = response.json()

    # ✅ Extract AI response safely
    return response_data["choices"][0]["message"]["content"]

# Main function for user interaction
def ai_agent():
    print("🤖 AI Agent Started. Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break
        
        response = ask_groq(user_input)
        print("AI:", response)

# Run the agent
if __name__ == "__main__":
    ai_agent()
