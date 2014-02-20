__author__ = 'wwxiang'

import sys
import logging
import tkinter
import tkinter.messagebox
import suds.client
import http.client
import urllib.parse
import urllib.request
import xml.etree.ElementTree
import shutil
import zipfile

#日志信息
handler = logging.StreamHandler(sys.stderr)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logger = logging.getLogger('suds.transport.http')
logger.setLevel(logging.DEBUG), handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
class OutgoingFilter(logging.Filter):
    def filter(self, record):
        return record.msg.startswith('sending:')
handler.addFilter(OutgoingFilter())

#SOAP http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx?wsdl


#SOAP SEND
bodyXML = '''
  <?xml version="1.0"?>
  <Request>
    <Header UserID="CtripTest" SessionID="0d21swty1o22qatzzrke4vip" RequestID="1c34b903-e1f5-4c6d-bbb4-d1bcd0a664e3" RequestType="Operation.HybridPublishService.HybridPackageQueryRQ" ClientIP="172.16.150.76" AsyncRequest="false" Timeout="0" MessagePriority="3" AssemblyVersion="1.0.2.5" RequestBodySize="0" SerializeMode="Xml" RouteStep="1" />
    <HybridPackageQueryRQ>
      <EnvCode>1</EnvCode>
      <ClientVersion>5.3</ClientVersion>
    </HybridPackageQueryRQ>
  </Request>'''

#主类
class ClientApp:
    def __init__(self,width=600,height=300):
        self.root = tkinter.Tk()
        self.root.geometry('{0}x{1}'.format(width,height))
        self.root.title('downloadZIP')
        label = tkinter.Label(self.root,text='download zip the current directory mkdir webapp and download')
        label.pack(padx=5,pady=5,anchor='w')
        pass
    def downloadControls(self):
        #格式化 XML
        def formatXML(SOAPXML):
            return ' '.join(SOAPXML.split())
            pass
        #解析 XML
        def handlerparseXML(xmlData):
            print(xmlData)
            elementRoot = xml.etree.ElementTree.fromstring(xmlData)
            elementHead = elementRoot.getiterator('Header')
            print(elementHead)
            help(elementHead)
            pass
        #SOAP WEBSERVICE
        def getValue(event):
            SOAPURL = getURL.get()
            print(SOAPURL)
            SOAPSENDDATA = getSendDate.get(1.0,'end')
            SOAPSENDDATA = formatXML(SOAPSENDDATA)
            print(SOAPSENDDATA)
            try:
                webservice = suds.client.Client(SOAPURL)
                SOAPRESPONSE = webservice.service.Request(SOAPSENDDATA)
                handlerparseXML(SOAPRESPONSE)
            except ValueError:
                raise  ValueError ('url bad')
            pass
        messURL = tkinter.Label(self.root,text='Request url:')
        messURL.pack(padx=5,anchor='w')
        getURL = tkinter.Entry(self.root,width=500)
        getURL.pack(padx=5,pady=5)
        parmas = tkinter.Label(self.root,text='Send Date:')
        parmas.pack(padx=5,anchor='w')
        getSendDate = tkinter.Text(self.root,width=400,height=10)
        getSendDate.pack(padx=5,pady=5,anchor='w')
        getSendDate.focus_set()
        Tscrollbar = tkinter.Scrollbar(self.root)
        Tscrollbar.pack(side='right',fill='y')
        Tscrollbar.config(command=getSendDate.yview)
        getSendDate.config(yscrollcommand=Tscrollbar.set)
        openSOAP = tkinter.Button(self.root,text='openSOAP',width=10,height=1)
        openSOAP.bind('<Button-1>',getValue)
        openSOAP.pack(padx=5,pady=5,anchor='w')
        pass
    def loop(self):
        self.root.resizable(False,False)
        self.downloadControls()
        self.root.mainloop()
        pass
    pass

app = ClientApp()
app.loop()