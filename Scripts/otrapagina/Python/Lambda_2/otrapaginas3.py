import boto3
import json
import pandas as pd
import html_to_json
import requests
import urllib.request
from bs4 import BeautifulSoup
from datetime import date
def app(event, context):
        today = date.today()
        year = str(today.year)
        month = str(today.month)
        day = str(today.day)
   #page = requests.get('https://www.bbc.com/')
   #soup_1 = BeautifulSoup(page.text, 'html.parser')
        directory_periodic = "/news/final/periodico=otrapagina/year="+year+"/month="+month+"/day="+day
        #directory_search_bbc = "/headlines/raw/Periodico=bbc/year="+year+"/month="+month+"/day="+day+"/bbc.html"
        s3 = boto3.resource('s3')
        obj = s3.Object('otrapagina','headlines/raw/periodicos/year/month/day/otrapagina.html')
        #j=obj.get()['Body'].read().decode('utf-8')
        #s3 = boto3.resource('s3')
        #content_object = s3.Object('bcc2', directory_search_bbc)
        file_content = obj.get()['Body'].read()
        print(file_content)
        soup = BeautifulSoup(file_content, 'html.parser')
        section_items = soup.find_all('section')
        category = []
        for i_sect in section_items:
                #category.append(i_sect.find(class_='media__tag tag tag--new'))
                alfa = str(i_sect.get_text()).strip()
		    alfa = str(i_sect.get_text()).strip()
                alf2=str(i_sect.get_text()).strip()
                alfa3=str(i_sect.get_text()).strip()
                category.append({'title':alfa})
                category.append({'categoria':alfa1})
                category.append({'enlance':alfa2})
                #category.append(str(soup.find_all('a')))
                category.append({'title':alfa})
                #category.append(str(soup.find_all('a')))
        df =  pd.DataFrame([category])
        csv = df.to_csv(index = False)
        s3Object_1 = s3.Object('otrapaginas3',directory_periodic+'/otrapagina.csv')
        s3Object_1.put(
                Body=csv
        )

