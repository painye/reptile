from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import requests
import time
import re

# 定义一个浏览器对象


'''browser = webdriver.Edge()
wait = WebDriverWait(browser, 5)'''


# 航班信息网站


# 加载每一页航班信息
def get_product(request):
    #                               航班号                        出发机场               到达机场   计划起飞时间   计划到达时间
    pattern = re.compile('<strong>\s(.*?)\s</strong>.*?</td>.*?<td>\s(.*?)</td>.*?<td>\s(.*?)<td>\s(.*?)<br\s/>\s(.*?)</td>', re.S)
    results = re.findall(pattern, request)
    for result in results:
        number, strating, bourn, s_time, b_time = result
        number = re.sub("\s", "", number)
        strating = re.sub("\s", "", strating)
        s_time = re.sub("\s", "", s_time)
        b_time = re.sub("\s", "", b_time)
        print(number, strating, bourn, s_time, b_time)
    '''# 判定dynamic是否加载成功
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#tab1 > table')))
    html = browser.page_source
    # pyquery解析网页源代码
    doc = pq(html)
    bg_0s = doc('.base_wrapper #layoutifx .main .tab1 #dynamic_data #bg_0').items()
    for bg_0 in bg_0s:
        print(bg_0)'''


def main():
    pages = 50
    web = 'https://flights.ctrip.com/actualtime/arrive-ctu.p'
    request = requests.get('https://flights.ctrip.com/actualtime/arrive-ctu/').text
    get_product(request)
    for i in range(2, 51):
        webs = web + str(i) + '/'
        request = requests.get(webs).text
        get_product(request)


if __name__ == '__main__':
    main()
