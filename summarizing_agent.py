from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.exa import ExaTools
from textwrap import dedent
from dotenv import load_dotenv
import os

load_dotenv()

EXA_API_KEY = os.getenv("EXA_API_KEY")
if not EXA_API_KEY:
    raise ValueError("EXA_API_KEY is not set. Please set it in the .env file or as an environment variable.")

summarizing_agent = Agent(
    model=Gemini(),
    tools=[ExaTools(api_key=EXA_API_KEY)],  # Pass the API key to ExaTools
    description=dedent("""\
        You are an expert summarizing agent capable of analyzing and extracting information from structured data like employee directories. 
        Your skills include:
        - Summarizing documents and extracting key information.
        - Finding specific details based on user queries.
        - Answering questions about the data provided.
    """)
)

# Employee directory data
employee_directory = [
    {"ID": "SSS-AT-101", "Name": "Dr. Alistair Crowley", "Cabin": "A12", "Campus": "1", "Expertise": "Dark Magic", "Phone": "+1-555-789-1011", "Email": "a.crowley@special.edu"},
    {"ID": "SSS-AT-205", "Name": "Prof. Nikola Tesla", "Cabin": "B07", "Campus": "2", "Expertise": "Free Energy", "Phone": "+1-555-234-5678", "Email": "n.tesla@special.edu"},
    {"ID": "SSS-AT-312", "Name": "Dr. Helena Blavatsky", "Cabin": "C19", "Campus": "3", "Expertise": "Tantra", "Phone": "+1-555-345-6789", "Email": "h.blavatsky@special.edu"},
    {"ID": "SSS-AT-156", "Name": "Dr. Carl Jung", "Cabin": "A05", "Campus": "1", "Expertise": "Cosmic Science", "Phone": "+1-555-456-7890", "Email": "c.jung@special.edu"},
    {"ID": "SSS-AT-278", "Name": "Prof. Grigori Rasputin", "Cabin": "B23", "Campus": "2", "Expertise": "Tantra", "Phone": "+1-555-567-8901", "Email": "g.rasputin@special.edu"},
    {"ID": "SSS-AT-409", "Name": "Dr. Marie Curie", "Cabin": "D14", "Campus": "3", "Expertise": "Free Energy", "Phone": "+1-555-678-9012", "Email": "m.curie@special.edu"},
    {"ID": "SSS-AT-187", "Name": "Prof. Aleister Crowley", "Cabin": "A18", "Campus": "1", "Expertise": "Dark Magic", "Phone": "+1-555-789-0123", "Email": "a.crowley2@special.edu"},
    {"ID": "SSS-AT-321", "Name": "Dr. Wilhelm Reich", "Cabin": "B11", "Campus": "2", "Expertise": "Cosmic Science", "Phone": "+1-555-890-1234", "Email": "w.reich@special.edu"},
    {"ID": "SSS-AT-245", "Name": "Prof. Paracelsus", "Cabin": "C03", "Campus": "3", "Expertise": "Tantra", "Phone": "+1-555-901-2345", "Email": "paracelsus@special.edu"},
    {"ID": "SSS-AT-132", "Name": "Dr. John Dee", "Cabin": "A09", "Campus": "1", "Expertise": "Dark Magic", "Phone": "+1-555-012-3456", "Email": "j.dee@special.edu"},
    {"ID": "SSS-AT-298", "Name": "Prof. Giordano Bruno", "Cabin": "B15", "Campus": "2", "Expertise": "Cosmic Science", "Phone": "+1-555-123-4567", "Email": "g.bruno@special.edu"},
    {"ID": "SSS-AT-376", "Name": "Dr. Pythagoras", "Cabin": "D22", "Campus": "3", "Expertise": "Free Energy", "Phone": "+1-555-234-5678", "Email": "pythagoras@special.edu"},
    {"ID": "SSS-AT-411", "Name": "Prof. Hermes Trismegistus", "Cabin": "A27", "Campus": "1", "Expertise": "Tantra", "Phone": "+1-555-345-6789", "Email": "hermes@special.edu"},
    {"ID": "SSS-AT-223", "Name": "Dr. Michael Faraday", "Cabin": "B09", "Campus": "2", "Expertise": "Free Energy", "Phone": "+1-555-456-7890", "Email": "m.faraday@special.edu"},
    {"ID": "SSS-AT-354", "Name": "Prof. Hypatia of Alexandria", "Cabin": "C08", "Campus": "3", "Expertise": "Cosmic Science", "Phone": "+1-555-567-8901", "Email": "hypatia@special.edu"},  
]

# Functions for summarizing and querying the directory
def summarize_directory():
    return f"The directory contains {len(employee_directory)} employees with expertise in various fields such as Dark Magic, Free Energy, Tantra, and Cosmic Science."

def find_free_energy_experts():
    experts = [emp for emp in employee_directory if emp["Expertise"] == "Free Energy"]
    return experts

def find_faculty_by_name(name):
    for emp in employee_directory:
        if name.lower() in emp["Name"].lower():
            return emp
    return None

def find_faculty_by_cabin(cabin):
    for emp in employee_directory:
        if emp["Cabin"] == cabin:
            return emp
    return None

# Example usage
if __name__ == "__main__":
    print("Summary of the directory:")
    print(summarize_directory())

    print("\nFaculties with expertise in Free Energy:")
    free_energy_experts = find_free_energy_experts()
    for expert in free_energy_experts:
        print(f"{expert['Name']} - {expert['Phone']} - {expert['Email']}")

    print("\nSearching for faculty with the name 'Rasputin':")
    rasputin = find_faculty_by_name("Rasputin")
    if rasputin:
        print(f"Found: {rasputin['Name']} - {rasputin['Phone']} - {rasputin['Email']}")
    else:
        print("No faculty with the name 'Rasputin' found.")

    print("\nFinding who is using cabin A12:")
    cabin_user = find_faculty_by_cabin("A12")
    if cabin_user:
        print(f"Cabin A12 is used by {cabin_user['Name']}.")