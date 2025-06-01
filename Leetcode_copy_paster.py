import re
import pyperclip

def transform_leetcode_title(raw):
    raw = re.sub(r"^(\d+)\.\s*", r"\1_", raw)
    raw = raw.replace(" ", "_")
    return raw.lower() + ".py"

def process_clipboard():
    original = pyperclip.paste()
    modified = transform_leetcode_title(original)
    pyperclip.copy(modified)
    print(f"Modified clipboard:\n{modified}")

if __name__ == "__main__":
    process_clipboard()