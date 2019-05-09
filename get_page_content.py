#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException

# 推荐用requests替代urllib


def get_page_by_requests(url):
    try:
        response = requests.get(url, timeout=1)
        print(response.status_code)
        print(response.content)
        exit() if not response.status_code == 200 else print('Success! fjp')
    except ReadTimeout:
        print('Timeout')
    except HTTPError:
        print('Http,error')
    except RequestException:
        print('error')


def main():
    print('starting...')
    url = 'http://www.baidu.com'
    get_page_by_requests(url)


if __name__ == "__main__":
    main()
