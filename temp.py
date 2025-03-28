import requests
import json
import os

def get_file_ids_from_shared_folder_http(folder_id, access_token):
    """
    Retrieves file IDs from a shared Google Drive folder using the HTTP API.

    Args:
        folder_id: The ID of the shared folder.
        access_token: The OAuth 2.0 access token.

    Returns:
        A list of file IDs, or None if an error occurs.
    """
    url = f"https://www.googleapis.com/drive/v3/files?q='{folder_id}' in parents and trashed=false&fields=files(id)"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        data = response.json()
        files = data.get('files', [])
        file_ids = [file['id'] for file in files]
        return file_ids

    except requests.exceptions.RequestException as e:
        print(f"An HTTP request error occurred: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        return None
    except KeyError as e:
        print(f"Key error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage:
# Replace 'YOUR_FOLDER_ID' and 'YOUR_ACCESS_TOKEN' with actual values.
folder_id = '19J6wpAUaxkvlUzZbS6xigD7kzMuya9ie'
access_token = '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'

file_ids = get_file_ids_from_shared_folder_http(folder_id, access_token)

if file_ids:
    print("File IDs in the folder:")
    for file_id in file_ids:
        print(file_id)
else:
    print("Failed to retrieve file IDs.")