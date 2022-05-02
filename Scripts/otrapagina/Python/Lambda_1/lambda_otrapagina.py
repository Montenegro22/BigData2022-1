
import json
import boto3
import urllib.request
def app(event, context):
        contents = urllib.request.urlopen("https://www.eltiempo.com/").read()
        print(contents)
        s3 = boto3.resource('s3')
        s3object = s3.Object('bcc2','headlines/raw/Periodico=bbc/year=bbc/month=bbc/day=bbc/otra.html')
        s3object.put(Body=contents)
        return  contents


