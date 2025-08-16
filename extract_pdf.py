# Manually entered employee directory data
employees = [
    {"ID": "SSS-AT-101", "Name": "Dr. Alistair Crowley", "Cabin": "A12", "Expertise": "Dark Magic", "Phone": "+1-555-789-1011", "Email": "a.crowley@special.edu"},
    {"ID": "SSS-AT-205", "Name": "Prof. Nikola Tesla", "Cabin": "B07", "Expertise": "Free Energy", "Phone": "+1-555-234-5678", "Email": "n.tesla@special.edu"},
    {"ID": "SSS-AT-312", "Name": "Dr. Helena Blavatsky", "Cabin": "C19", "Expertise": "Tantra", "Phone": "+1-555-345-6789", "Email": "h.blavatsky@special.edu"},
    {"ID": "SSS-AT-278", "Name": "Prof. Grigori Rasputin", "Cabin": "B23", "Expertise": "Tantra", "Phone": "+1-555-567-8901", "Email": "g.rasputin@special.edu"},
    {"ID": "SSS-AT-409", "Name": "Dr. Marie Curie", "Cabin": "D14", "Expertise": "Free Energy", "Phone": "+1-555-678-9012", "Email": "m.curie@special.edu"},
    {"ID": "SSS-AT-223", "Name": "Dr. Michael Faraday", "Cabin": "B09", "Expertise": "Free Energy", "Phone": "+1-555-987-6543", "Email": "m.faraday@special.edu"},
]

# Function to summarize data
def summarize_data():
    print("Summary of Employee Directory:")
    for emp in employees[:3]:  # Print first 3 records as summary
        print(f"{emp['ID']} - {emp['Name']} ({emp['Expertise']})")

# Function to find employees with expertise in Free Energy
def find_free_energy_experts():
    experts = [emp for emp in employees if emp["Expertise"] == "Free Energy"]
    return experts

# Function to find Rasputin's details
def find_rasputin():
    for emp in employees:
        if "Rasputin" in emp["Name"]:
            return emp
    return "No faculty with name Rasputin found."

# Function to find the user of a specific cabin
def find_cabin_user(cabin):
    for emp in employees:
        if emp["Cabin"] == cabin:
            return emp
    return f"No user found for cabin {cabin}."

# Run functions and display results
summarize_data()
print("\nFree Energy Experts:", find_free_energy_experts())
print("\nFaculty with Rasputin:", find_rasputin())
print("\nCabin A12 User:", find_cabin_user("A12"))