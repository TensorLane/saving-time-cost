import boto3
import os
import time

# AWS S3 setup
BUCKET_NAME = "your-s3-bucket-name"
FOLDER_PATH = "/home/ec2-user/generated_data"
UPLOADED_FILES_TRACKER = set()

# Initialize S3 client
s3_client = boto3.client('s3')

def upload_new_files():
    global UPLOADED_FILES_TRACKER

    for file_name in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file_name)

        # Skip directories and already uploaded files
        if not os.path.isfile(file_path) or file_name in UPLOADED_FILES_TRACKER:
            continue

        try:
            # Upload file to S3
            s3_client.upload_file(file_path, BUCKET_NAME, f"data/{file_name}")
            print(f"Uploaded: {file_name}")
            UPLOADED_FILES_TRACKER.add(file_name)
        except Exception as e:
            print(f"Failed to upload {file_name}: {e}")

def main():
    while True:
        upload_new_files()
        time.sleep(30)

if __name__ == "__main__":
    main()
