import requests
import os
from bs4 import *
import bs4


class CommentSpider(object):
    def __init__(self, url, uaPath,filePath):
        self.uaPath = uaPath
        self.url = url
        self.rootPath = filePath

    def getUA(self):
        with open(self.uaPath) as f:
            uas = f.readlines()
            import random
            index = random.randint(0, len(uas)-1)
            return uas[index].replace("\n", "")

    def getHeader(self, url):
        header = {
            'Referer': url,
            'User-agent': self.getUA(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accetp-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'en-US,en;q=0.8'
        }
        return header

    def getHtml(self,page):
        if page == 1:
            url2 = ".html"
        else:
            url2 = "/"+str(page)+".html"
        url = self.url+url2
        header = self.getHeader(url)
        with requests.session() as s:
            req = s.get(url,headers = header)
            #cookie = requests.utils.dict_from_cookiejar(req.cookies)
            htmlpage = req.content.decode('utf-8','ignore')
        return htmlpage
            

    def getComment(self,html):
        comments = []
        soup = BeautifulSoup(html)
        for div in soup.find_all('div'):
            if div.get('class')!=None and "review-overall" in div.get('class'):
                content = ""
                for text in div:
                    if type(text) is not bs4.element.Tag:
                        content += text.replace("\n","")
                        content = content.replace("    ","")
                comments.append(content)
        return comments
    

    def fileWriter(self,filename,path,o):
        writePath = path+filename
        with open(writePath,'a',encoding = 'utf-8') as f:
            for item in o:
                f.write(item+'\n')
        pass
    
    def run(self):
        for i in range(1,25):
            print("--------------Now page %d---------"%(i))
            htmlpage = spider.getHtml(i)
            comments = spider.getComment(htmlpage)
            print(len(comments))
            self.fileWriter("commentsTest.data",self.rootPath,comments)



if __name__ == "__main__":
    filePath = "D:/Project/Python/Spider/"
    #url = "https://www.productreview.com.au/p/holden-captiva.html"
    url = "https://www.productreview.com.au/p/holden-captiva"
    uaPath = filePath+"/newUA.txt"
    spider = CommentSpider(url, uaPath,filePath)
    spider.run()


