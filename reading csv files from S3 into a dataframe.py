#importing relevant libraries
import boto3
import pandas as pd
from io import StringIO

#block of code to read structured data from a file
if __name__ == "__main__":
        
    # Set up AWS credentials and specify the region as you have done in your code
    session = boto3.Session(
        aws_access_key_id='enter your access key id here',
        aws_secret_access_key='enter your secret access key here',
        region_name='eu-north-1'  # Replace with your desired region
    )

    # Create an S3 client
    s3 = session.client('s3')
    bucket_name = 'firstemrbucket'
    object_key = 'sales_data.csv'  # Replace with the correct object key

    # Download the CSV file from S3
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    csv_data = response['Body'].read().decode('utf-8')

    # Load CSV data into a Pandas DataFrame
    df = pd.read_csv(StringIO(csv_data))

    #printing out the first few rows of our dataframe
    df.head()