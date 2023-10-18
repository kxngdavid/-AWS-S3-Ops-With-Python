#importing relevant libraries
import boto3

#defining what goes into our main construct
if __name__== "__main__":

    # specif the name of your SQL bucket
    bucket_name = 'enter the name of your s3 bucket here'
   
    # The path and name you want for the object in the bucket
    object_key = 's3bucketname/name_of_file_to_upload'  
    
    # Path to the file you want to upload. Ideally, this should be in the ssme directory you're in
    local_file_path = ''  

    # Create an S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id = 'enter your access key id here',
        aws_secret_access_key = 'enter your secret key here'
        )

    #A try and except block to upload the file to the S3 bucket
    try:
        s3.upload_file(local_file_path, bucket_name, object_key)
        print(f'File {local_file_path} uploaded to S3 bucket {bucket_name} as {object_key}')
    except Exception as e:
        print(f"An error occurred during the S3 upload: {str(e)}")
    
