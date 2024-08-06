import os
import json

def main():
    # Load the GitHub event payload
    event_path = os.getenv("GITHUB_EVENT_PATH")
    with open(event_path, 'r') as f:
        event = json.load(f)
    
    # Get the comment body
    comment_body = event.get("comment", {}).get("body", "")
    
    # Check if the comment contains ".deploy"
    if ".deploy" in comment_body:
        print("Deployment comment detected.")
        # Set an environment variable or return a specific code to signal detection
        with open(os.getenv("GITHUB_ENV"), "a") as env_file:
            env_file.write("DEPLOYMENT_COMMENT_DETECTED=true\n")
    else:
        print("No deployment comment detected.")
        with open(os.getenv("GITHUB_ENV"), "a") as env_file:
            env_file.write("DEPLOYMENT_COMMENT_DETECTED=false\n")

if __name__ == "__main__":
    main()
