import requests
import json

# Function to get a list of hook IDs for the repository
def get_hook_ids():
    url = f"https://api.github.com/repos/Fiserv/developer-studio-support/hooks"
    headers = {
        "Authorization": f"Bearer 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",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    hooks = response.json()
    hook_ids = [hook["id"] for hook in hooks]
    return hook_ids


if __name__ == "__main__":
    hook_ids = get_hook_ids()
    print("Hook IDs:", hook_ids)
