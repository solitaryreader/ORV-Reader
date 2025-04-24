import json
import os
import praw

# Retrieve credentials from environment variables
client_id = os.environ.get("REDDIT_CLIENT_ID")
client_secret = os.environ.get("REDDIT_CLIENT_SECRET")
user_agent = "by u/RealNPC_"
username = "RealNPC_"
password = os.environ.get("REDDIT_PASSWORD")
subreddit_name = "test"
json_file_path = "/website/meta/cont.json"

def create_reddit_post(title, selftext):
    if not all([client_id, client_secret, user_agent, username, password, subreddit_name]):
        print("Error: One or more Reddit API credentials or the subreddit name are not set as environment variables.")
        return

    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password,
        )

        subreddit = reddit.subreddit(subreddit_name)
        submission = subreddit.submit(title, selftext=selftext)
        print(f"Successfully created post: {submission.url}")
    except praw.exceptions.RedditAPIException as e:
        print(f"Error creating post: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def extract_title_from_json(json_file_path):
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            if not data or not isinstance(data, list):
                print("Error: Invalid JSON format.")
                return None

            highest_index_entry = max(data, key=lambda item: item.get('index', -1), default=None)

            if highest_index_entry and "index" in highest_index_entry and "title" in highest_index_entry:
                chapter_number = highest_index_entry["index"]
                full_title = highest_index_entry["title"]
                parts = full_title.split(" Episode ", 1)
                if len(parts) == 2:
                    episode_part = parts[0].split()
                    episode_number_str = episode_part[-1].rstrip('.')
                    rest_of_title_from_json = parts[1]
                    # Still need to know where "Side Stories" and "Avatar (1) ‒ [Release Discussion]" come from
                    formatted_title = f"Side Stories {chapter_number} • Episode {episode_number_str} ‒ {rest_of_title_from_json}"
                    return formatted_title
                else:
                    print("Warning: Unexpected title format in JSON.")
                    return None
            else:
                print("Error: Could not find 'index' or 'title' in the JSON data.")
                return None
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {json_file_path}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading JSON: {e}")
        return None

if __name__ == "__main__":
    extracted_title = extract_title_from_json(json_file_path)
    if extracted_title:
        selftext = "This is a test post created using PRAW and a title extracted from a JSON file."
        create_reddit_post(extracted_title, selftext)
    else:
        print("Could not extract a valid title. Not creating Reddit post.")
