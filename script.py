import random
import string
import time
import subprocess
import os
from datetime import datetime, timedelta

def generate_random_content():
    content_types = [
        lambda: f"# Random Heading {random.randint(1, 10)}\n",
        lambda: f"- Bullet Point {random.randint(1, 100)}\n",
        lambda: f"{random.randint(1, 100)}. Numbered Item\n",
        lambda: f"```\nprint('Hello, World {random.randint(1, 1000)}!')\n```\n",
        lambda: f"Random paragraph with some text: {' '.join([random.choice(['lorem', 'ipsum', 'dolor', 'sit', 'amet']) for _ in range(10)])}.\n",
        lambda: f"**Bold Text {random.randint(1, 100)}**\n",
        lambda: f"![Random Image](https://via.placeholder.com/{random.randint(100, 500)})\n",
    ]
    return random.choice(content_types)()

def generate_random_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def generate_random_date():
    today = datetime.now()
    random_days_ago = random.randint(0, 30)
    random_time = timedelta(days=random_days_ago, hours=random.randint(0, 23), minutes=random.randint(0, 59))
    random_date = today - random_time
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

def edit_markdown(file_path):
    try:
        with open(file_path, "a") as file:
            random_content = generate_random_content()
            file.write(random_content)
        print(f"Updated {file_path} with:\n{random_content}")
    except Exception as e:
        print(f"Error editing Markdown file: {e}")

def push_to_github():
    random_key = generate_random_key()
    commit_message = f"Automated update with ID: {random_key}"
    random_date = generate_random_date()
    
    try:
        subprocess.run(["git", "add", "."], check=True)

        # Set the commit date
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = random_date
        env["GIT_COMMITTER_DATE"] = random_date

        subprocess.run(["git", "commit", "-m", commit_message], check=True, env=env)

        subprocess.run(["git", "push"], check=True)
        print(f"Changes pushed to GitHub with commit message: '{commit_message}' on date: {random_date}")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")

def main():
    markdown_file = "example.md" 
    interval = 3  # seconds

    if not os.path.exists(markdown_file):
        with open(markdown_file, "w") as file:
            file.write("# Example Markdown\n")

    while True:
        edit_markdown(markdown_file)
        push_to_github()
        time.sleep(interval)

if __name__ == "__main__":
    main()
