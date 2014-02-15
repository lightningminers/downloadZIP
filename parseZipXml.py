__author__ = 'xiangwenwen'

import tkinter
import tkinter.messagebox
import tkinter.filedialog
import os
import urllib.request
import xml.etree.ElementTree
import shutil
import sys

class ClientApp:
    def __init__(self,width=420,height=100):
        self.root = tkinter.Tk()
        self.root.geometry('{0}x{1}'.format(width,height))
        self.root.title('downloadZIP')
        label = tkinter.Label(self.root,text='download zip the current directory mkdir webapp and download')
        label.pack(padx=5,pady=5,anchor='w')
        pass
    def handler(self):
        #解析xml
        def handlerparseXML(event):
            workpath = os.getcwd()
            #打开一个xml文件
            filename = tkinter.filedialog.askopenfilename(initialdir=workpath)
            if len(filename) == 0 :
                return False
            xmlTypes = filename.split('.')[1]
            if not xmlTypes == 'xml':
                tkinter.messagebox.showerror('error','is not xml')
                return False
            #解析xml
            xmlContent = xml.etree.ElementTree.parse(filename)
            # messagePrint.insert('end','\n')
            # messagePrint.insert('end','path:' + filename +' \n\n')
            #根元素
            elemtroot = xmlContent.getroot()
            # messagePrint.insert('end','start：load xml success and parse xml \n\n')
            #查找元素节点
            zipall = []
            for elemtChild in elemtroot:
                for elemtzip in elemtChild:
                    zipall.append(elemtzip.text)
            # print(elemtroot)
            # print(zipall)
            #生成目录
            workmkdir = ['download','webapp','log']
            for wkdir in workmkdir:
                lastwkdir = workpath + os.path.sep + wkdir
                # messagePrint.insert('end','mkdir:'+ lastwkdir+'\n\n')
                if os.path.exists(lastwkdir):
                    shutil.rmtree(lastwkdir)
                    os.mkdir(lastwkdir)
                else:
                    os.mkdir(lastwkdir)
            #显示下载进度
            def callback(count, blockSize, totalSize):
                per = 100.0*count*blockSize/totalSize
                if per > 100:
                    per = 100
                print('end','%.2f%%'%per)
                pass
            print(zipall)
            #下载远程资源到本地
            for rURL in zipall:
                print(rURL)
                urllib.request.urlretrieve(rURL,workpath+os.path.sep+'download'+os.path.sep+'python.tgz',reporthook=callback)
            pass
        #GUI空间界面
        openSearchXml = tkinter.Button(self.root,text='open',width=10,height=1)
        openSearchXml.bind('<Button-1>',handlerparseXML)
        openSearchXml.pack(padx=5,pady=5,anchor='w')
        # messagePrint = tkinter.Text(self.root,width=600,height=450)
        # messagePrint.pack(ipadx=5,ipady=5,anchor='w')
        # messagePrint.bind('<KeyPress>', lambda e : 'break')
        # messagePrint.focus_set()
        # _scrollbar = tkinter.Scrollbar(self.root)
        # _scrollbar.pack(side='right',fill='y')
        # _scrollbar.config(command=messagePrint.yview)
        # messagePrint.config(yscrollcommand=_scrollbar.set)
        pass
    def loop(self):
        self.root.resizable(False,False)
        self.handler()
        self.root.mainloop()
        pass
    pass

app = ClientApp()
app.loop()