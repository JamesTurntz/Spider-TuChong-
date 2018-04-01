# !/usr/bin/env
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os
import time


class Spider:
    def __init__(self, url='', interval=0.5):
        self.siteURL = url
        self.interval = interval

    # 设置链接地址
    def setUrl(self, url):
        self.siteURL = url

    # 设置时间间隔
    def setInterval(self, interval):
        self.interval = interval

    # 获取图像id
    def getImageId(self, page):
        pattern = re.compile('imageId":"(.*?)","width"', re.S)
        images = re.findall(pattern, page)
        return images

    # 获取页面内容
    def getPage(self, encoder):
        request = urllib2.Request(self.siteURL)
        response = urllib2.urlopen(request)
        return response.read().decode(encoder)

    # 保存单张图片
    def saveImg(self, imageURL, fileName):
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print u'保存图片', fileName
        f.close()

    # 创建目录
    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            print u'创建', path, u'文件夹'
            return True
        else:
            print u'已创建', path, u'文件夹'
            return False

    # 图片保存操作
    def saveTuchong(self, url, dir):
        self.setUrl(url)
        self.mkdir(dir)
        imageIds = self.getImageId(self.getPage('utf-8'))
        for imageId in imageIds:
            url = 'http://p3a.pstatp.com/weili/l/' + imageId + '.jpg'
            name = dir + '/' + imageId + '.jpg'
            self.saveImg(url, name)
            time.sleep(0.5)


# 测试:
if __name__ == "__main__":
    s = Spider()
    s.saveTuchong('https://stock.tuchong.com/search?category=149,2004', 'travel')
    s.setInterval(0.3)
    s.saveTuchong('https://stock.tuchong.com/free', 'free')
