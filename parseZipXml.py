__author__ = 'xiangwenwen'

import tkinter
import tkinter.messagebox
import tkinter.filedialog
import os
import urllib.request
import xml.etree.ElementTree
import shutil
import sys
import zipfile

class ClientApp:
    def __init__(self,width=420,height=100):
        self.root = tkinter.Tk()
        self.root.geometry('{0}x{1}'.format(width,height))
        self.root.title('downloadZIP')
        label = tkinter.Label(self.root,text='download zip the current directory mkdir webapp and download')
        label.pack(padx=5,pady=5,anchor='w')
        pass
    def handler(self):
        workpath = os.getcwd()
        #处理请求，并解析xml
        def handlerURL(event):
            # val = url_input.get()
            # try:
            #     fq = urllib.request.urlopen(val)
            #     headrs = fq.info()
            #     code = fq.getcode()
            #     dataxml = fq.read()
            #     if code == 200 :
            #         downloadParseXml(dataxml)
            #     else:
            #         tkinter.messagebox.showerror('error information','the request code is ' + repr(code))
            #     #关闭请求
            #     fq.close()
            # except ValueError:
            #     tkinter.messagebox.showerror('error information','Error:'+repr(ValueError))
            #     pass
            pass
        #打包webpp
        def unpackwebapp():

            pass
        #检校md5
        def calibrationMD5():

            pass
        #下载zip文件并解压缩至webapp
        def zipDecompression(dowbloadall):
            #生成目录
            workmkdir = ['download']
            for wkdir in workmkdir:
                lastwkdir = workpath + os.path.sep + wkdir
                print('mkdir:'+ lastwkdir)
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
                    openSearchXml.option_clear()
                print('download '+rURL+'：%.2f%%'%per)
                pass
            downmkdir = workpath+os.path.sep+'download'
            webappmkdir = downmkdir + os.path.sep + 'webapp'
            #下载远程资源到本地
            zip_all = []
            for rURL in dowbloadall:
                findUrl = rURL.rfind('/')
                _rurl = rURL[findUrl+1:len(rURL)]
                zip_all.append(downmkdir+os.path.sep+_rurl)
                urllib.request.urlretrieve(rURL,downmkdir+os.path.sep+_rurl,reporthook=callback)

            #解压zip包到webpp目录
            os.mkdir(webappmkdir)
            print('mkdir:'+ webappmkdir)
            # print(zip_all)
            for zip_app in zip_all:
                zip_file = zipfile.ZipFile(zip_app,'r')
                zip_name_list = zip_file.namelist()
                zip_info_list = zip_file.infolist()
                for zip_c_file in zip_name_list:

                    if zip_c_file[-1] is zip_name_list[0][-1]:
                        os.mkdir(webappmkdir+os.path.sep+zip_c_file)
                        print('mkdir:'+ webappmkdir+os.path.sep+zip_c_file)
                    else:
                        f_zip = open(webappmkdir+os.path.sep+zip_c_file,'w')
                        print('open:'+ webappmkdir+os.path.sep+zip_c_file)
                        zip_red = zip_file.read(zip_c_file)
                        f_zip.write(zip_red.decode('utf-8'))
                        f_zip.close()
                    pass
                zip_file.close()
                pass
            pass
        #解析xml
        def handlerparseXML(event):
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
            print('path:' + filename)
            #根元素
            elemtroot = xmlContent.getroot()
            print('start：load xml success and parse xml')
            #查找元素节点
            dowbloadall = []
            for elemtChild in elemtroot:
                for elemtzip in elemtChild:
                    dowbloadall.append(elemtzip.text)
            # print(elemtroot)
            zipDecompression(dowbloadall)
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