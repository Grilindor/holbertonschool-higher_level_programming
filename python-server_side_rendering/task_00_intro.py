#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Iterate over each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Create a copy of the template
        invitation = template[:]

        # Replace placeholders with values from the attendee dictionary
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{placeholder}}}", value)

        # Define the output file name
        output_filename = f"output_{idx}.txt"

        # Write the invitation to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)

    print(f"{len(attendees)} invitation files generated.")
