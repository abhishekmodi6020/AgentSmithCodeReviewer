import os
import sys
from dotenv import load_dotenv
from llm.review_prompt import generate_review_prompt
from llm.openai_client import OpenAIClient
from github_utils import fetch_pr_diff

def parse_pr_url(pr_url):
    parts = pr_url.rstrip("/").split("/")
    return parts[-4], parts[-3], parts[-1]

def main():
    load_dotenv()

    if len(sys.argv) < 2:
        print("❌ Please pass a GitHub PR URL as a command-line argument.")
        return

    pr_url = sys.argv[1]
    owner, repo, pr_number = parse_pr_url(pr_url)

    print(f"📦 Fetching diff from PR #{pr_number} in {owner}/{repo}...\n")
    diff = fetch_pr_diff(owner, repo, pr_number)

    if not diff:
        print("❌ Could not fetch diff.")
        return

    llm = OpenAIClient()
    prompt = generate_review_prompt(diff)
    review = llm.ask(prompt)

    print("\n💡 Code Review Suggestion:\n")
    print(review)

if __name__ == "__main__":
    main()