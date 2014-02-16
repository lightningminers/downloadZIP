__author__ = 'xiangwenwen'

import urllib.request
import tkinter
import json

#test url http://www.wanyan.com/vote/vote-star!getVoteByRecommendBefore.dhtml?pointNumber=4
#处理请求
def hanlderURL(val_url):
    # val_url = str(input())
    try:
        rq = urllib.request.urlopen(val_url)
        headers = rq.info()
        print('HEADER')
        print(headers)
        code = rq.getcode()
        print('STATUS')
        print(code)
        data = rq.read()
        return data.decode('utf-8')
    except ValueError:
        raise  ValueError('error：it\'s not')
    pass

#序列化json
def hanlderJSON(rq_data):
    jsonData = json.loads(rq_data,'\n')
    return  jsonData
    pass
#窗口
def tkwindow():
    root = tkinter.Tk()
    root.geometry('{0}x{1}'.format(450,100))
    root.title('查看请求信息')
    def butEvent(event):
        val_url = myinput.get()
        rq_data = hanlderURL(val_url)
        json_data = hanlderJSON(rq_data)
        print('\n\n\n')
        print('DATA')
        print(json_data)
        button.option_clear()
        # print(type([]))
        pass
    myinput = tkinter.Entry(root,width=450)
    myinput.pack(padx=5,pady=5)
    button = tkinter.Button(root,text='request',width=10,height=1)
    button.bind('<Button-1>',butEvent)
    button.pack(padx=5,pady=5,anchor='w')
    root.resizable()
    root.mainloop()
    pass
tkwindow()