import random
import time
import subprocess
import os

# Function to make random edits to a Markdown file
def edit_markdown(file_path):
    try:
        with open(file_path, "a") as file:
            # Add a random line
            random_line = f"\nRandom edit: {random.randint(1, 1000)}"
            file.write(random_line)
        print(f"Updated {file_path} with: {random_line}")
    except Exception as e:
        print(f"Error editing Markdown file: {e}")

# Function to commit and push changes to GitHub
def push_to_github(commit_message="Random update"):
    try:
        # Git add
        subprocess.run(["git", "add", "."], check=True)
        # Git commit
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        # Git push
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")

# Main loop
def main():
    markdown_file = "example.md"  # Change this to your Markdown file
    interval = 60  # Time interval in seconds

    # Ensure the Markdown file exists
    if not os.path.exists(markdown_file):
        with open(markdown_file, "w") as file:
            file.write("# Example Markdown\n")

    while True:
        edit_markdown(markdown_file)
        push_to_github(commit_message="Automated random update")
        time.sleep(interval)

if __name__ == "__main__":
    main()
