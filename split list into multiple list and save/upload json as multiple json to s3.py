import json

# un comment if you want to upload to s3
# import boto3
# s3Client = boto3.resource('s3')
# bucketName = 'BUCKET_NAME'
# s3Folder = 'data_{}.json'

with open('data.json','r') as file:
    data = json.loads(file.read())

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]
n = 2000
data_list = list(divide_chunks(data['data'],n))

fileCount = 1
for item in data_list:
    temp = {
        "data" : item
    }
    # use below code if you want to upload to S3
    # s3Client.Object(bucketName, s3Folder.format(fileCount)).put(Body = json.dumps(temp,indent=4))
    with open(f'data{fileCount}.json','w+') as temp_file:
        temp_file.write(json.dumps(temp))
    fileCount += 1