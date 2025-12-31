import random

def generate_script(owner_name, company_name):
    templates = [
        f"Hi {owner_name}, saw {company_name} has great reviews in the area. Are you guys equipped to handle an extra 5-10 service calls a week right now? We're looking for one HVAC partner in your city.",
        f"Hey {owner_name}, I'm with Gruntworks. We specialize in HVAC growth. We're looking to help a local pro in your area hit their revenue goals this quarter. Got 5 mins to chat?",
    ]
    return random.choice(templates)

if __name__ == "__main__":
    print(generate_script("John", "Elite Air HVAC"))
