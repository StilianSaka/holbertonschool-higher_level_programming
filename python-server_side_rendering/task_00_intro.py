import re

def generate_invitations(template, attendees):
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    if not isinstance(template, str):
        print("Template should be a string.")
        return
    
    if not all(isinstance(value, dict) for value in attendees):
        print("Attendees should be a list of dictionaries.")
        return

    # Find all unique placeholders in the template
    placeholders = re.findall(r'{(.*?)}', template)

    for i, attendee in enumerate(attendees):
        personal_template = template
        for placeholder in placeholders:
            # Replace with attendee value or "N/A" if missing
            value = attendee.get(placeholder, "N/A")
            personal_template = personal_template.replace('{' + placeholder + '}', value)

        with open(f'output_{i + 1}.txt', 'w', encoding="utf-8") as f:
            f.write(personal_template)
