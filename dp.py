import dropbox

# Initialize Dropbox client
ACCESS_TOKEN = "sl.CBHxujy_TSOw2EhQdPECoZiD1MTCogG42nPSjjIAi4FXM9C36WDwequfZTN9e6-Vaq1R3TWbqsHLqxF6ZBNTiXGq3QXAhtebwxfDKlsIuKYF5BagS2yEWkwp1rxWkRFpPPEjziVqVdJoXoHCa3toy0g"  # Get the access token from the user
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Function to upload a file to Dropbox
def upload_to_dropbox():
    local_file_path = input("Enter the local file path to upload: ")
    dropbox_path = input("Enter the Dropbox path to save the file (e.g., /folder/file.txt): ")
    try:
        with open(local_file_path, "rb") as file:
            dbx.files_upload(file.read(), dropbox_path, mode=dropbox.files.WriteMode("overwrite"))
            print(f"File uploaded to {dropbox_path}")
    except FileNotFoundError:
        print("Local file not found. Please check the file path.")
    except dropbox.exceptions.ApiError as e:
        print(f"Error uploading file: {e}")

# Function to download a file from Dropbox
def download_from_dropbox():
    dropbox_path = input("Enter the Dropbox file path to download (e.g., /folder/file.txt): ")
    local_file_path = input("Enter the local file path to save the downloaded file: ")
    try:
        metadata, response = dbx.files_download(dropbox_path)
        with open(local_file_path, "wb") as file:
            file.write(response.content)
        print(f"File downloaded to {local_file_path}")
    except dropbox.exceptions.ApiError as e:
        print(f"Error downloading file: {e}")

# Function to list files in a Dropbox folder
def list_dropbox_folder():
    folder_path = input("Enter the Dropbox folder path to list files (leave blank for root): ")
    try:
        result = dbx.files_list_folder(folder_path)
        print(f"Files in folder {folder_path or 'root'}:")
        for entry in result.entries:
            print(f"- {entry.name}")
    except dropbox.exceptions.ApiError as e:
        print(f"Error listing folder: {e}")

# Menu-driven program
if __name__ == "__main__":
    while True:
        print("\nDropbox File Operations")
        print("1. Upload a file")
        print("2. Download a file")
        print("3. List files in a folder")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            upload_to_dropbox()
        elif choice == "2":
            download_from_dropbox()
        elif choice == "3":
            list_dropbox_folder()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
