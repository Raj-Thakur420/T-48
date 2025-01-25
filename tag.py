import facebook
import os
import time
from dotenv import load_dotenv
from random import choice

# Load environment variables
load_dotenv()

# ANSI Escape Codes for colors
COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
]
RESET = "\033[0m"

# Enhanced VIP ASCII Art Logo
def print_vip_logo():
    logo = f"""
{choice(COLORS)}██████╗ ██╗██████╗ {RESET} {choice(COLORS)}██████╗ ██╗   ██╗██████╗ {RESET}
{choice(COLORS)}██╔══██╗██║██╔══██╗{RESET} {choice(COLORS)}██╔══██╗██║   ██║██╔══██╗{RESET}
{choice(COLORS)}██║  ██║██║██║  ██║{RESET} {choice(COLORS)}██║  ██║██║   ██║██████╔╝{RESET}
{choice(COLORS)}██║  ██║██║██║  ██║{RESET} {choice(COLORS)}██║  ██║██║   ██║██╔═══╝ {RESET}
{choice(COLORS)}██████╔╝██║██████╔╝{RESET} {choice(COLORS)}██████╔╝╚██████╔╝██║     {RESET}
{choice(COLORS)}╚═════╝ ╚═╝╚═════╝ {RESET} {choice(COLORS)}╚═════╝  ╚═════╝ ╚═╝     {RESET}
    """
    print(logo)

# Function to take user inputs
def get_input():
    access_token = input(f"{choice(COLORS)}Enter your Facebook Access Token: {RESET}").strip()
    message_file = input(f"{choice(COLORS)}Enter the path of the message file (e.g., message.txt): {RESET}").strip()
    profile_link = input(f"{choice(COLORS)}Enter the Facebook Profile Link to mention: {RESET}").strip()
    delay = int(input(f"{choice(COLORS)}Enter the delay between posts (in seconds): {RESET}").strip())
    return access_token, message_file, profile_link, delay

# Fetch user name from Facebook profile link
def fetch_user_name(graph, profile_link):
    try:
        # Extract profile ID or username from the link
        profile_id = profile_link.split("/")[-1]
        user_info = graph.get_object(profile_id)
        return user_info.get("name", "User")
    except Exception as e:
        print(f"{choice(COLORS)}Error fetching user name: {e}{RESET}")
        return "User"

# Post message with name mention
def post_message_with_name(access_token, message, name):
    try:
        graph = facebook.GraphAPI(access_token)
        # Create the post message with mention
        post_message = f"@[{name}] {message}"
        # Post the message
        graph.put_object(parent_object="me", connection_name="feed", message=post_message)
        print(f"{choice(COLORS)}Post successfully uploaded with mention: {name}!{RESET}")
    except Exception as e:
        print(f"{choice(COLORS)}Error: {e}{RESET}")

# Main function for unlimited posting
def post_indefinitely():
    print_vip_logo()  # Display VIP logo
    access_token, message_file, profile_link, delay = get_input()
    graph = facebook.GraphAPI(access_token)

    # Fetch the user name from the provided profile link
    user_name = fetch_user_name(graph, profile_link)

    print(f"{choice(COLORS)}Starting unlimited post process...{RESET}")

    # Read the message file line by line
    with open(message_file, "r") as file:
        messages = file.readlines()

    while True:
        for message in messages:
            message = message.strip()  # Remove extra spaces or newlines
            if message:  # Ensure the message is not empty
                print(f"{choice(COLORS)}Posting message: {message} for {user_name}{RESET}")
                post_message_with_name(access_token, message, user_name)
                print(f"{choice(COLORS)}Waiting for {delay} seconds before the next post...{RESET}")
                time.sleep(delay)

if __name__ == "__main__":
    post_indefinitely()