# llm/review_prompt.py
"""
Holds the prompt template you send to GPT (you can edit/tune it later)
"""

def generate_review_prompt(diff: str) -> str:
    return f"""
You are reviewing the following GitHub pull request diff.

Analyze the code for:
- Violations of SOLID principles
- Poor design decisions or patterns
- Any suggestions for refactoring or clean code improvements

Provide your reasoning and suggest before/after code snippets if possible.

Diff:
{diff}
"""