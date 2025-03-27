from google.oauth2 import credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import os

# Replace with your folder ID and desired download path
FOLDER_ID = '19J6wpAUaxkvlUzZbS6xigD7kzMuya9ie'
DOWNLOAD_PATH = 'downloads'
NUM_FILES_TO_DOWNLOAD = 10  # Download only the latest 10 files

def download_latest_gdrive_docx_as_txt(folder_id, download_path, num_files):
    """Downloads the latest num_files docx files from a Google Drive folder as TXT, skipping already downloaded files."""

    creds = None
    if os.path.exists('token.json'):
        creds = credentials.Credentials.from_authorized_user_file('token.json', ['https://www.googleapis.com/auth/drive'])
    if not creds or not creds.valid:
        from google_auth_oauthlib.flow import InstalledAppFlow
        flow = InstalledAppFlow.from_client_secrets_file(
            'scripts\side-stories-processor\credentials.json', ['https://www.googleapis.com/auth/drive'])
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        query = f"'{folder_id}' in parents and mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document'" #changed to docx mimetype
        results = service.files().list(q=query, fields="files(id, name, createdTime)", orderBy="createdTime desc").execute()
        items = results.get('files', [])

        if not items:
            print('No docx files found.')
            return

        files_to_download = items[:num_files]  # Slice list to only include latest files.

        downloaded_files = os.listdir(download_path)  # list files already downloaded.

        for item in files_to_download:
            file_id = item['id']
            file_name = item['name'] + ".txt"

            if file_name in downloaded_files:
                print(f"Skipping: {file_name} (already downloaded)")
                continue  # Skip to the next file
            try:
                request = service.files().export_media(fileId=file_id, mimeType='text/plain')
                fh = io.BytesIO()
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print(f"Download {int(status.progress() * 100)}%.")

                file_path = os.path.join(download_path, file_name)
                with open(file_path, 'wb') as f:
                    fh.seek(0)
                    f.write(fh.read())
                print(f"Downloaded: {file_name}")

            except Exception as export_error:
                print(f'An error occurred exporting {item["name"]}: {export_error}')

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    if not os.path.exists(DOWNLOAD_PATH):
        os.makedirs(DOWNLOAD_PATH)
    download_latest_gdrive_docx_as_txt(FOLDER_ID, DOWNLOAD_PATH, NUM_FILES_TO_DOWNLOAD)