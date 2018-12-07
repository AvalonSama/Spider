

class Tag(object):
    def __init__(self,filePath,rootPath):
        self.filePath = filePath
        self.rootPath = rootPath
    #属性 情感词 情感极性
    def tagging(self):
        path = self.rootPath+self.filePath
        with open(path,"r",encoding = 'utf-8') as f:
            for line in f.readlines():
                result = []
                while True:
                    print(line)
                    aspect = input("请标注属性")
                    if aspect =="ss":
                        break
                    emotion_word = input("请标注情感词")
                    polarity = input("请标注情感极性")
                    after_tag = line+"||"+aspect+"||"+emotion_word+"||"+polarity+"\n"
                    result.append(after_tag)
                self.fileWriter("taggedComments.data",result)
        print("标注完成！")
        pass
    
    def fileWriter(self,filename,o):
        path = self.rootPath+filename
        with open(path,"a",encoding = 'utf-8') as f:
            f.writelines(o)
        pass
    
    def run(self):
        self.tagging()
        print("大完成~")

if __name__ == "__main__":
    rootPath = "D:/Project/Python/Spider/"
    filename = "commentsTest.data"
    tag = Tag(filename,rootPath)
    tag.run()
