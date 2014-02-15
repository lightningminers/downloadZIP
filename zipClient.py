__author__ = 'wwxiang'

import tkinter
import tkinter.messagebox
import os
import urllib.request
import xml

#GUI CLASS
class ClientApp:
    def __init__(self,width=650,height=550):
        self.root = tkinter.Tk()
        self.root.geometry('{0}x{1}'.format(width,height))
        self.root.title('downloadZIP for parse build')
        label = tkinter.Label(self.root,text='download address * webapp')
        label.pack(anchor='w')
        pass
    def te_init(self):
        # webapp 压缩
        def compression():

            pass
        #zip xml 解析与下载
        def downloadParseXml(xml):
            bepath = os.getcwd()
            print(bepath)
            newDirectory = os.path.join(bepath,'\webapp')
            newDownload = os.path.join(bepath,'\download')
            print(newDirectory)
            print(newDownload)
            print(os.path.expanduser('~'))
            isExist_dir = os.path.exists(newDirectory)
            isExist_down = os.path.exists(newDownload)
            if not isExist_dir and not isExist_down:
                os.mkdir(newDirectory)
                os.mkdir(newDownload)
            pass
        #处理请求，并解析xml
        def handlerURL(event):
            val = url_input.get()
            try:
                fq = urllib.request.urlopen(val)
                headrs = fq.info()
                code = fq.getcode()
                dataxml = fq.read()
                if code == 200 :
                    downloadParseXml(dataxml)
                else:
                    tkinter.messagebox.showerror('error information','the request code is ' + repr(code))
                #关闭请求
                fq.close()
            except ValueError:
                tkinter.messagebox.showerror('error information','Error:'+repr(ValueError))
                pass
            pass

        def handlerParseXml():
            print(123)
            pass
        #控件GUI
        label = tkinter.Label(self.root,text='download url:')
        label.pack(anchor='w')
        url_input = tkinter.Entry(self.root,width=450)
        url_input.pack(anchor='w')
        parseURL = tkinter.Button(self.root,text='build')
        parseURL.bind('<Button-1>',handlerURL)
        parseURL.pack(anchor='w',pady=10,padx=10)
        pass
    def loop(self):
        self.root.resizable(False,False)
        self.te_init()
        self.root.mainloop()
        pass
    pass
app = ClientApp()
app.loop()