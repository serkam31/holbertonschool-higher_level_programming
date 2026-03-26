def generate_invitations(template, attendees):
    if not isinstance(attendees, list) or not isinstance(template, str):
        print("bad format")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, 1):
        result = template.replace("{name}", str(attendee.get("name") or "N/A"))
        result = result.replace("{event_title}", str(attendee.get("event_title") or "N/A"))
        result = result.replace("{event_date}", str(attendee.get("event_date") or "N/A"))
        result = result.replace("{event_location}", str(attendee.get("event_location") or "N/A"))
        with open(f"output_{index}.txt", "w") as f:
            f.write(result)
