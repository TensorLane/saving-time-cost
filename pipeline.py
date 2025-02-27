import os
import time
import boto3
from datetime import datetime

# AWS S3 configuration
S3_BUCKET_NAME = "s3-bucket-tensorlane"
S3_FOLDER = "uploaded_data"  # Optional: folder in S3 to store files
LOCAL_FOLDER = "generated_data"

# Ensure AWS credentials are correctly set up on the instance or use IAM role
s3_client = boto3.client('s3')

# Function to upload a file to S3
def upload_to_s3(file_path, s3_key):
    try:
        s3_client.upload_file(file_path, S3_BUCKET_NAME, s3_key)
        print(f"Uploaded {file_path} to S3 as {s3_key}")
        return True
    except Exception as e:
        print(f"Failed to upload {file_path}: {e}")
        return False

# Main function for the data pipeline
def main():
    already_uploaded = set()  # Track files already uploaded
    
    while True:
        try:
            # List all JSON files in the directory
            files = [f for f in os.listdir(LOCAL_FOLDER) if f.endswith('.json')]
            for file in files:
                file_path = os.path.join(LOCAL_FOLDER, file)
                
                # Skip if file already uploaded
                if file_path in already_uploaded:
                    continue

                # Define S3 key (optional: add timestamp/folder structure)
                s3_key = f"{S3_FOLDER}/{file}" if S3_FOLDER else file
                
                # Upload the file to S3
                if upload_to_s3(file_path, s3_key):
                    already_uploaded.add(file_path)  # Mark as uploaded
            
            # Wait 30 seconds before the next check
            time.sleep(30)

        except Exception as e:
            print(f"Error in pipeline: {e}")
            time.sleep(30)

if __name__ == "__main__":
    main()
