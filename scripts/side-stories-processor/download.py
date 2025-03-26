import os
import json
import requests
from urllib.parse import urljoin

def download_files_from_shared_folder(shared_folder_url, local_download_path, index_file_path="index-files.json"):
    """
    Downloads all files from a shared folder URL, checks against an index file,
    and updates the index with new files.

    Args:
        shared_folder_url (str): The URL of the shared folder.
        local_download_path (str): The local path to save downloaded files.
        index_file_path (str): The path to the index JSON file.
    """

    if not os.path.exists(local_download_path):
        os.makedirs(local_download_path)

    try:
        response = requests.get(shared_folder_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        # Assuming the shared folder provides a listing of files as HTML or JSON.
        # This part is highly dependent on how the shared folder is structured.
        # In this example, we'll assume it's a simple HTML listing.
        # Adapt this part to the actual structure of your shared folder listing.

        # Example: Simple HTML parsing (adapt to the actual structure)
        # This example assumes that the HTML contains <a> tags with href attributes
        # pointing to the files.
        # You will need to adapt this part based on the actual HTML structure.

        # Example using a very basic and fragile parsing.
        # For real-world scenarios, consider using a proper HTML parsing library like BeautifulSoup.

        html_content = response.text
        file_urls = []
        for line in html_content.splitlines():
            if '<a href="' in line:
                start = line.find('<a href="') + len('<a href="')
                end = line.find('"', start)
                file_url = line[start:end]
                # If the file_url is relative, make it absolute
                if not file_url.startswith('http'):
                    file_url = urljoin(shared_folder_url, file_url)
                file_urls.append(file_url)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching file list: {e}")
        return

    # Load existing index or create a new one
    try:
        with open(index_file_path, "r") as f:
            downloaded_files = json.load(f)
    except FileNotFoundError:
        downloaded_files = []

    new_downloads = []

    for file_url in file_urls:
        filename = os.path.basename(file_url)
        local_file_path = os.path.join(local_download_path, filename)

        if filename not in [os.path.basename(f) for f in downloaded_files]:
            try:
                file_response = requests.get(file_url, stream=True)
                file_response.raise_for_status()

                with open(local_file_path, "wb") as f:
                    for chunk in file_response.iter_content(chunk_size=8192):
                        f.write(chunk)

                print(f"Downloaded: {filename}")
                new_downloads.append(filename)

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {filename}: {e}")

    # Update and save the index
    downloaded_files.extend(new_downloads)
    with open(index_file_path, "w") as f:
        json.dump(downloaded_files, f, indent=4)

    print("Index updated.")

# Example usage:
shared_folder_url = "https://drive.google.com/drive/u/0/folders/19J6wpAUaxkvlUzZbS6xigD7kzMuya9ie" # Replace with your shared folder's URL.
local_download_path = "downloads"
download_files_from_shared_folder(shared_folder_url, local_download_path)