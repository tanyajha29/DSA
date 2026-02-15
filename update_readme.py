from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---------- CONFIG ----------
# Root folder where topic READMEs live.
# Set to "." to keep topic folders at the repo root.
DSA_FOLDER = "."

# Auto-generated section markers inside each topic README.
AUTO_START = "<!-- AUTO-GENERATED START -->"
AUTO_END = "<!-- AUTO-GENERATED END -->"

# Ordered topic rules (first match wins). Adjust keywords to improve detection.
TOPIC_RULES = [
    {"topic": "Trie", "keywords": ["trie", "prefix tree", "prefix-tree"], "pattern": "Trie"},
    {"topic": "Graph", "keywords": ["graph", "bfs", "dfs", "dijkstra", "topological", "union find", "union-find", "disjoint", "mst"], "pattern": "Graph"},
    {"topic": "Trees", "keywords": ["tree", "bst", "binary tree", "binary-tree", "binary search tree", "binary-search-tree"], "pattern": "Tree"},
    {"topic": "Recursion_Backtracking", "keywords": ["recursion", "backtracking", "permutation", "combination", "subset", "n-queens"], "pattern": "Backtracking"},
    {"topic": "Sliding_Window", "keywords": ["sliding window", "sliding-window", "window", "substring", "subarray"], "pattern": "Sliding Window"},
    {"topic": "Two_Pointers", "keywords": ["two pointers", "two-pointers", "3sum", "4sum", "container with most water", "fast", "slow"], "pattern": "Two Pointers"},
    {"topic": "Stack", "keywords": ["stack", "parentheses", "histogram", "monotonic"], "pattern": "Stack"},
    {"topic": "Queue", "keywords": ["queue", "deque", "priority queue", "priority-queue", "heap"], "pattern": "Queue / Heap"},
    {"topic": "LinkedList", "keywords": ["linked list", "linked-list", "listnode"], "pattern": "Linked List"},
    {"topic": "Hashing", "keywords": ["hash", "anagram", "map", "dictionary", "two sum"], "pattern": "Hashing"},
    {"topic": "Arrays", "keywords": ["array", "matrix", "rotate", "prefix", "suffix", "product", "stock"], "pattern": "Arrays"},
]

# Fallback category when no topic matches.
DEFAULT_TOPIC = "Others"
DEFAULT_PATTERN = "General"
DEFAULT_TIME_COMPLEXITY = "TBD"
DEFAULT_SPACE_COMPLEXITY = "TBD"

# Optional per-problem overrides (keyed by problem number as string).
# Use this to set a better topic, pattern, or complexity when needed.
PROBLEM_OVERRIDES: Dict[str, Dict[str, str]] = {
    "1": {"topic": "Hashing", "pattern": "Hashing", "time": "O(n)", "space": "O(n)"},
    "2": {"topic": "LinkedList", "pattern": "Linked List", "time": "O(m+n)", "space": "O(1)"},
    "3": {"topic": "Sliding_Window", "pattern": "Sliding Window", "time": "O(n)", "space": "O(1)"},
    "11": {"topic": "Two_Pointers", "pattern": "Two Pointers", "time": "O(n)", "space": "O(1)"},
    "15": {"topic": "Two_Pointers", "pattern": "Sorting + Two Pointers", "time": "O(n^2)", "space": "O(1)"},
    "19": {"topic": "LinkedList", "pattern": "Two Pointers", "time": "O(n)", "space": "O(1)"},
    "20": {"topic": "Stack", "pattern": "Stack", "time": "O(n)", "space": "O(n)"},
    "21": {"topic": "LinkedList", "pattern": "Linked List", "time": "O(m+n)", "space": "O(1)"},
    "49": {"topic": "Hashing", "pattern": "Sorting / Hashing", "time": "O(n * k log k)", "space": "O(nk)"},
    "84": {"topic": "Stack", "pattern": "Monotonic Stack", "time": "O(n)", "space": "O(n)"},
    "121": {"topic": "Arrays", "pattern": "Greedy / One Pass", "time": "O(n)", "space": "O(1)"},
    "143": {"topic": "LinkedList", "pattern": "Reverse + Merge", "time": "O(n)", "space": "O(1)"},
    "238": {"topic": "Arrays", "pattern": "Prefix / Suffix", "time": "O(n)", "space": "O(1)"},
}

# Preferred solution file extensions (first match is used).
SOLUTION_EXT_PREFERENCE = [".cpp", ".java", ".py"]
# ---------------------------

REPO_ROOT = Path(__file__).resolve().parent
DSA_DIR = REPO_ROOT / DSA_FOLDER
LEETSYNC_DIR_RE = re.compile(r"^(\d+)-(.+)$")


@dataclass
class ProblemEntry:
    number: str
    title: str
    folder_name: str
    difficulty: str
    topic: str
    pattern: str
    time: str
    space: str
    code: Optional[str]
    code_lang: Optional[str]


def slug_to_title(slug: str) -> str:
    return " ".join(word.capitalize() for word in slug.replace("-", " ").split())


def parse_difficulty(folder: Path) -> str:
    readme = folder / "README.md"
    if not readme.exists():
        return "Unknown"
    text = readme.read_text(encoding="utf-8", errors="ignore")
    match = re.search(r"Difficulty-([A-Za-z]+)", text)
    if match:
        return match.group(1)
    match = re.search(r"Difficulty:\s*([A-Za-z]+)", text)
    if match:
        return match.group(1)
    return "Unknown"


def detect_topic(title: str, slug: str) -> Tuple[str, str]:
    haystack = f"{title} {slug}".lower()
    for rule in TOPIC_RULES:
        if any(keyword in haystack for keyword in rule["keywords"]):
            return rule["topic"], rule.get("pattern", DEFAULT_PATTERN)
    return DEFAULT_TOPIC, DEFAULT_PATTERN


def find_solution_file(folder: Path) -> Tuple[Optional[str], Optional[str]]:
    for ext in SOLUTION_EXT_PREFERENCE:
        matches = sorted(folder.glob(f"*{ext}"))
        if matches:
            code = matches[0].read_text(encoding="utf-8", errors="ignore").rstrip()
            lang = {
                ".cpp": "cpp",
                ".java": "java",
                ".py": "python",
            }[ext]
            return code, lang
    return None, None


def parse_existing_metadata(readme_text: str) -> Dict[str, Dict[str, str]]:
    metadata: Dict[str, Dict[str, str]] = {}
    headers = list(re.finditer(r"^###\s+(\d+)\.\s+.+?\s+\(([^)]+)\)\s*$", readme_text, re.MULTILINE))
    for i, match in enumerate(headers):
        number = match.group(1)
        difficulty = match.group(2).strip()
        start = match.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(readme_text)
        block = readme_text[start:end]
        pattern = re.search(r"\*\*Pattern(?:/Category)?:\*\*\s*(.+)", block)
        time = re.search(r"\*\*Time Complexity\*\*:\s*(.+)", block)
        space = re.search(r"\*\*Space Complexity\*\*:\s*(.+)", block)
        metadata[number] = {
            "difficulty": difficulty,
            "pattern": pattern.group(1).strip() if pattern else "",
            "time": time.group(1).strip() if time else "",
            "space": space.group(1).strip() if space else "",
        }
    return metadata


def extract_auto_block(content: str) -> str:
    start = content.find(AUTO_START)
    end = content.find(AUTO_END)
    if start == -1 or end == -1 or end < start:
        return ""
    inner = content[start + len(AUTO_START) : end]
    return inner.strip("\n")


def render_entry(problem: ProblemEntry, topic_readme: Path) -> str:
    relative_link = Path(os.path.relpath(REPO_ROOT / problem.folder_name, topic_readme.parent)).as_posix()
    lines: List[str] = [
        f"### {problem.number}. {problem.title} ({problem.difficulty})",
        "",
        f"🔗 LeetCode Folder: [`{problem.folder_name}`]({relative_link})",
        "",
        f"- **Pattern:** {problem.pattern}",
        f"- **Time Complexity:** {problem.time}",
        f"- **Space Complexity:** {problem.space}",
        "",
    ]

    if problem.code and problem.code_lang:
        lines.extend([
            f"```{problem.code_lang}",
            problem.code,
            "```",
            "",
        ])
    else:
        lines.extend(["_No solution file found in the LeetSync folder._", ""])

    return "\n".join(lines)


def build_topic_readme(topic: str, entries: List[ProblemEntry]) -> str:
    header = [
        f"# {topic}",
        "",
        f"Placement-focused revision notes for {topic}.",
        "",
        "## Problems",
        "",
        AUTO_START,
        "",
    ]

    if not entries:
        body = ["_No problems added yet._", ""]
    else:
        body = []
        for entry in entries:
            body.append(render_entry(entry, DSA_DIR / topic / "README.md"))

    footer = [AUTO_END, ""]
    return "\n".join(header + body + footer)


def update_topic_file(topic: str, content: str) -> None:
    topic_dir = DSA_DIR / topic
    topic_dir.mkdir(parents=True, exist_ok=True)
    readme_path = topic_dir / "README.md"

    if readme_path.exists():
        existing = readme_path.read_text(encoding="utf-8", errors="ignore")
        if AUTO_START in existing and AUTO_END in existing:
            before, _, rest = existing.partition(AUTO_START)
            _, _, after = rest.partition(AUTO_END)
            auto_block = extract_auto_block(content)
            new_content = (
                before.rstrip()
                + "\n\n"
                + AUTO_START
                + "\n\n"
                + auto_block
                + "\n\n"
                + AUTO_END
                + "\n"
                + after.lstrip()
            )
        else:
            new_content = content
    else:
        new_content = content

    if not readme_path.exists() or readme_path.read_text(encoding="utf-8", errors="ignore") != new_content:
        readme_path.write_text(new_content, encoding="utf-8")


def main() -> None:
    DSA_DIR.mkdir(parents=True, exist_ok=True)

    # Gather existing metadata to preserve manual edits (pattern/time/space).
    existing_meta: Dict[str, Dict[str, str]] = {}
    if DSA_DIR.exists():
        for topic_dir in DSA_DIR.iterdir():
            readme = topic_dir / "README.md"
            if not readme.exists():
                continue
            text = readme.read_text(encoding="utf-8", errors="ignore")
            # Only parse metadata from our auto-generated topic READMEs.
            if AUTO_START in text and AUTO_END in text:
                existing_meta.update(parse_existing_metadata(text))

    # Build problem entries from LeetSync folders.
    problems_by_topic: Dict[str, Dict[str, ProblemEntry]] = {}

    for item in REPO_ROOT.iterdir():
        if not item.is_dir():
            continue
        match = LEETSYNC_DIR_RE.match(item.name)
        if not match:
            continue

        number, slug = match.group(1), match.group(2)
        title = slug_to_title(slug)

        override = PROBLEM_OVERRIDES.get(number, {})
        topic, detected_pattern = detect_topic(title, slug)
        topic = override.get("topic", topic)

        difficulty = parse_difficulty(item)
        if difficulty == "Unknown" and number in existing_meta:
            difficulty = existing_meta[number].get("difficulty", "Unknown")

        pattern = override.get("pattern") or existing_meta.get(number, {}).get("pattern") or detected_pattern
        time = override.get("time") or existing_meta.get(number, {}).get("time") or DEFAULT_TIME_COMPLEXITY
        space = override.get("space") or existing_meta.get(number, {}).get("space") or DEFAULT_SPACE_COMPLEXITY

        code, lang = find_solution_file(item)

        entry = ProblemEntry(
            number=number,
            title=title,
            folder_name=item.name,
            difficulty=difficulty or "Unknown",
            topic=topic,
            pattern=pattern,
            time=time,
            space=space,
            code=code,
            code_lang=lang,
        )

        problems_by_topic.setdefault(topic, {})[number] = entry

    # Always ensure fallback topic exists.
    problems_by_topic.setdefault(DEFAULT_TOPIC, {})

    # Write/update each topic README.
    for topic, entries_map in sorted(problems_by_topic.items()):
        entries = list(entries_map.values())
        entries.sort(key=lambda e: int(e.number))
        content = build_topic_readme(topic, entries)
        update_topic_file(topic, content)


if __name__ == "__main__":
    main()

