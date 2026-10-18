import re

with open("input.txt", "r") as f:
    text = f.read()

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = sorted(set(re.findall(pattern, text)))

with open("emails.txt", "w") as f:
    f.write("\n".join(emails))

print(f"Found {len(emails)} emails. Saved to emails.txt")