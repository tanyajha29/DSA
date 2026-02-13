import os
import re

# ---------- CONFIG ----------
LEETSYNC_FOLDER_PREFIX = ""
DSA_FOLDER = "DSA"

# Simple topic mapping (edit this according to your need)
TOPIC_MAPPING = {
    "array": "Arrays",
    "linked": "LinkedList",
    "list": "LinkedList",
    "stack": "Stack",
    "queue": "Queue",
    "tree": "Trees",
    "graph": "Graph",
    "two": "Two_Pointers",
    "window": "Sliding_Window",
    "subarray": "Sliding_Window",
    "hash": "Hashing",
    "sum": "Arrays",
}

# ----------------------------

def detect_topic(folder_name):
    name = folder_name.lower()
    for keyword, topic in TOPIC_MAPPING.items():
        if keyword in name:
            return topic
    return "Others"

def format_problem(folder_name):
    parts = folder_name.split("-", 1)
    if len(parts) < 2:
        return None

    number = parts[0]
    title = parts[1].replace("-", " ").title()

    return f"""
### {number}. {title}

🔗 LeetCode Folder: `{folder_name}`

- Time Complexity: _To be added_
- Space Complexity: _To be added_

---
"""

def update_readme(topic, content):
    topic_path = os.path.join(DSA_FOLDER, topic)

    os.makedirs(topic_path, exist_ok=True)

    readme_path = os.path.join(topic_path, "README.md")

    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {topic}\n\n")

    with open(readme_path, "a") as f:
        f.write(content)

def main():
    for item in os.listdir():
        if re.match(r"^\d+-", item) and os.path.isdir(item):
            topic = detect_topic(item)
            formatted = format_problem(item)
            if formatted:
                update_readme(topic, formatted)

if __name__ == "__main__":
    main()