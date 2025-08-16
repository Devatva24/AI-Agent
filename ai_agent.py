import openai

# OpenAI API Key (Replace with your actual key)
OPENAI_API_KEY = "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"

# Manually entered employee directory data
employees = [
    {"ID": "SSS-AT-101", "Name": "Dr. Alistair Crowley", "Cabin": "A12", "Expertise": "Dark Magic", "Phone": "+1-555-789-1011", "Email": "a.crowley@special.edu"},
    {"ID": "SSS-AT-205", "Name": "Prof. Nikola Tesla", "Cabin": "B07", "Expertise": "Free Energy", "Phone": "+1-555-234-5678", "Email": "n.tesla@special.edu"},
    {"ID": "SSS-AT-278", "Name": "Prof. Grigori Rasputin", "Cabin": "B23", "Expertise": "Tantra", "Phone": "+1-555-567-8901", "Email": "g.rasputin@special.edu"},
    {"ID": "SSS-AT-409", "Name": "Dr. Marie Curie", "Cabin": "D14", "Expertise": "Free Energy", "Phone": "+1-555-678-9012", "Email": "m.curie@special.edu"},
    {"ID": "SSS-AT-223", "Name": "Dr. Michael Faraday", "Cabin": "B09", "Expertise": "Free Energy", "Phone": "+1-555-987-6543", "Email": "m.faraday@special.edu"},
]

# Function to process queries
def ai_agent(prompt):
    # Generate relevant response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an AI assistant answering queries about employee data."},
                  {"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Function to get user input and process queries
def process_query(query):
    if "free energy" in query.lower():
        experts = [emp for emp in employees if emp["Expertise"] == "Free Energy"]
        return f"Free Energy Experts: {[emp['Name'] for emp in experts]}"
    
    elif "rasputin" in query.lower():
        for emp in employees:
            if "Rasputin" in emp["Name"]:
                return f"Name: {emp['Name']}, Phone: {emp['Phone']}, Email: {emp['Email']}"
        return "No faculty with name Rasputin found."
    
    elif "cabin" in query.lower():
        cabin = query.split()[-1]  # Extract last word as cabin number
        for emp in employees:
            if emp["Cabin"] == cabin:
                return f"Cabin {cabin} is occupied by {emp['Name']}"
        return f"No user found for cabin {cabin}."
    
    else:
        return ai_agent(query)

# Run chatbot in a loop
print("AI Agent is running. Type 'exit' to stop.")
while True:
    user_query = input("Ask a question: ")
    if user_query.lower() == "exit":
        break
    response = process_query(user_query)
    print("AI Agent:", response)