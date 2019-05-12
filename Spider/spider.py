#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException
import time
import json
from mysql import DB


db = DB()
    

class Spider:
    def __init__(self, url):
        self.url = url

    def get_page(self):
        try:
            response = requests.get(self.url, timeout=1)
            if not response.status_code == 200:
                print("status_code error")
            else:
                return response.json()
        except ReadTimeout:
            print("timeout")
        except HTTPError:
            print("http error")
        except RequestException:
            print("error")

    def get_page_index(self,method='GET',data=None):
        try:
            if method=='GET':
                response = requests.get(self.url, timeout=1, params=data)
            elif method == 'POST':
                response = requests.post(self.url, data=data)
            if not response.status_code == 200:
                print("status_code error")
            else:
                return response.json()
        except ReadTimeout:
            print("timeout")
        except HTTPError:
            print("http error")
        except RequestException:
            print("error")

    def write_to_file(content):
        with open("result.txt",'a',encoding='utf-8') as f:
            f.write(json.dumps(content,ensure_ascii=False)+"\n")
            f.close


def parse_page(response):
    returnValue = response['returnValue']
    totalPage = returnValue['totalPage']
    datas_list = returnValue['datas']
    now = time.time()
    for data in datas_list:
        isOpen = data['isOpen']
        isNew = data['isNew']
        effectiveDate = int(data['effectiveDate']/1000)
        uneffectualDate = int(data['uneffectualDate']/1000)
        degree = data['degree']
        workExperience = data['workExperience']
        id = data['id']
        name = data['name']
        departmentName = data['departmentName']
        requirement = data['requirement'].replace('<br/>','\n').lower()
        recruitNumber = data['recruitNumber']
        description = data['description'].replace('<br/>','\n')
        workLocation = data['workLocation']
        # (id, name, degree, workLocation, workExperience, 
        # departmentName,effectiveDate, uneffectualDate,requirement, description,recruitNumber)
        if (isOpen == 'Y') and (isNew == 'Y') and (uneffectualDate > now) and (degree != "博士"):
            if workExperience[:1] in "四五六七八九":
                print("filter %s %s" % (id,workExperience))
                continue
            if "c++" not in requirement:
                print("filter %s requirement" % id)
                continue
                 
            if "java方向" in requirement:
                print("filter %s requirement" % id)
                continue

            effectiveDate = time.gmtime(effectiveDate)
            uneffectualDate = time.gmtime(uneffectualDate)
            params = [id,name,degree,workLocation,workExperience,departmentName,\
                      effectiveDate,uneffectualDate,requirement, description,recruitNumber\
                     ]
            print("add id %s" % id)

            db.add_item(params)

def doRequestAndParseData(spider,index=1):
    #while True:
    payload = {
        'first': '技术类',
        'location': '北京',
        'pageIndex': index,
        'pageSize': '10'
    }
    content = spider.get_page_index("POST",payload)
    totalPage = parse_page(content)
        #index +=1
        #if index >6: break
        #if index >totalPage: break

    
def main():
    url = 'https://job.alibaba.com/zhaopin/socialPositionList/doList.json'
    spider = Spider(url)
    for i in range(6):
        doRequestAndParseData(spider,i+1)
    #doRequestAndParseData(spider,1)

 #   db.show_items()

if __name__ == "__main__":
    main()
