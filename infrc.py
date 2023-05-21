import re
import sys
import json
import time
import random
import requests

def get_page(url):
    '''伪装成点击在浏览器从CSDN博客搜索到的文章'''
    try:
        headers = {
            'Referer': 'https://blog.csdn.net',  # 伪装成从CSDN博客搜索到的文章
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }  # 伪装成浏览器
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        _ = input('Infrc002: 请求出错：请检查 '+filepath+' 中 '+url+' 中是否存在拼写错误...')
        sys.exit()

def view_page(url):
    '''获取当前博客访问量'''
    global read_num
    read_num = int(re.compile(
        '<span class="read-count">(.*?)</span>').search(get_page(url)).group(1))

def main():
    print("Infrc (Infinite Read-Count 无限阅读量) 推量工具 By 轩哥啊哈OvO")
    global filepath
    while True:
        '''填入待访问的博客下面刷取四个博客访问量'''
        try:
            with open(sys.argv[1], encoding="utf-8"): pass
            filepath = sys.argv[1]
        except IndexError:
            try:
                with open("config.json", encoding="utf-8") as configs:
                    config = json.load(configs)
                filepath = config['urls']
            except FileNotFoundError:
                filepath = 'urls.txt'
        
        try:
            with open(filepath, encoding="utf-8"): pass
        except:
            _ = input("Infrc001: 没有找到 urls.txt 或指定的文件。")
            sys.exit()
                
        with open(filepath, encoding="utf-8") as urls:
            for url in urls:
                if url == "\n" or url[0] == "#":
                    continue
                view_page(url.rstrip())
                print(url.rstrip(), read_num)
        try:
            with open("config.json", encoding="utf-8") as configs:
                config = json.load(configs)
                sleep_time_min = config['sleep_time']['min']
                sleep_time_max = config['sleep_time']['max']
            sleep_time = random.randint(sleep_time_min, sleep_time_max)
        except TypeError:
            _ = input("Infrc003: config.json 中存在填写错误。")
            sys.exit()
        except FileNotFoundError:
            sleep_time = random.randint(30, 40)
        print('等待', sleep_time, '秒')
        time.sleep(sleep_time)  # 设置访问频率，过于频繁的访问会触发反爬虫

if __name__ == '__main__':
    main()
