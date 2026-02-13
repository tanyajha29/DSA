# DSA for Campus Placements

LeetSync auto-generates problem folders at the repo root. Topic-wise revision notes live in `DSA/` and are updated by `update_readme.py`.

## Structure
- LeetSync problem folders: `123-problem-name/`
- Topic folders: `DSA/Arrays/`, `DSA/LinkedList/`, `DSA/Stack/`, `DSA/Queue/`, `DSA/Two_Pointers/`, `DSA/Sliding_Window/`, `DSA/Hashing/`, `DSA/Recursion_Backtracking/`, `DSA/Trees/`, `DSA/Graph/`, `DSA/Trie/`
- Automation: `update_readme.py`, `.github/workflows/auto-update.yml`

## Topic Index
- [Arrays](DSA/Arrays/README.md)
- [LinkedList](DSA/LinkedList/README.md)
- [Stack](DSA/Stack/README.md)
- [Queue](DSA/Queue/README.md)
- [Two_Pointers](DSA/Two_Pointers/README.md)
- [Sliding_Window](DSA/Sliding_Window/README.md)
- [Hashing](DSA/Hashing/README.md)
- [Recursion_Backtracking](DSA/Recursion_Backtracking/README.md)
- [Trees](DSA/Trees/README.md)
- [Graph](DSA/Graph/README.md)
- [Trie](DSA/Trie/README.md)
- [Others](DSA/Others/README.md)

## Workflow
- Solve on LeetCode (LeetSync auto-saves).
- Run `python update_readme.py` locally or let GitHub Actions update on push.
- Keep each entry focused: pattern, time/space, and the final solution code.

## Notes
- LeetSync folders are ignored via `.gitignore` and should not be modified.
