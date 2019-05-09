#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from requests.exceptions import ReadTimeout, HTTPError, RequestException


class Spider:
    def __init__(self, url):
        self.url = url

    def get_page(self):
        try:
            response = requests.get(self.url, timeout=1)
            print(response.status_code)
            if not response.status_code == 200:
                print("status_code error")
            else:
                return response.content
        except ReadTimeout:
            print("timeout")
        except HTTPError:
            print("http error")
        except RequestException:
            print("error")


def main():
    print('starting...')
    url = 'http://www.baidu.com'
    spider = Spider(url)
    content = spider.get_page()
    print(content)


if __name__ == "__main__":
    main()
