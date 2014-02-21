__author__ = 'wwxiang'

import sys
import logging
import os
import tkinter
import tkinter.messagebox
import suds.client
import urllib.parse
import urllib.request
import xml.etree.ElementTree
import xml.dom.minidom
import shutil
import zipfile
import time


#日志信息
# handler = logging.StreamHandler(sys.stderr)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)
# logger = logging.getLogger('suds.transport.http')
# logger.setLevel(logging.DEBUG), handler.setLevel(logging.DEBUG)
# logger.addHandler(handler)
# class OutgoingFilter(logging.Filter):
#     def filter(self, record):
#         return record.msg.startswith('sending:')
# handler.addFilter(OutgoingFilter())

#全局信息
G_LOG = []

#工作目录
workPath = os.getcwd()
downloadPath = workPath + os.path.sep + 'download'
webappmkdir = downloadPath + os.path.sep + 'webapp'
webLog = downloadPath + os.path.sep + 'webLog'
if os.path.isdir(downloadPath):
    shutil.rmtree(downloadPath)
os.mkdir(downloadPath)
os.mkdir(webappmkdir)
os.mkdir(webLog)
G_LOG.append('mkdir:'+downloadPath + '\n')
G_LOG.append('mkdir:'+webappmkdir + '\n')
G_LOG.append('mkdir:'+webLog + '\n')

#获取当前系统时间
theTime = time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
G_LOG.append('当前系统时间：'+theTime + '\n')

#SOAP 源
#SOAP http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx?wsdl
#SOAP SEND
bodyXML = '''
  <?xml version="1.0"?>
  <Request>
    <Header UserID="CtripTest" SessionID="0d21swty1o22qatzzrke4vip" RequestID="1c34b903-e1f5-4c6d-bbb4-d1bcd0a664e3" RequestType="Operation.HybridPublishService.HybridPackageQueryRQ" ClientIP="172.16.150.76" AsyncRequest="false" Timeout="0" MessagePriority="3" AssemblyVersion="1.0.2.5" RequestBodySize="0" SerializeMode="Xml" RouteStep="1" />
    <HybridPackageQueryRQ>
      <EnvCode>1</EnvCode>
      <ClientVersion>{0}</ClientVersion>
    </HybridPackageQueryRQ>
  </Request>'''

#格式化 XML
def formatXML(SOAPXML):
    return ' '.join(SOAPXML.split())
    pass
# 获取TEXT 节点
def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)
# 解压
def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir)
    zfobj = zipfile.ZipFile(zipfilename,'r')
    for name in zfobj.namelist():
        name = name.replace('\\','/')
        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else:
            ext_filename = os.path.join(unziptodir, name)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir) : os.mkdir(ext_dir)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()
    pass

#主类
class ClientApp:
    def __init__(self,width=600,height=150):
        self.root = tkinter.Tk()
        self.root.geometry('{0}x{1}'.format(width,height))
        self.root.title('downloadZIP')
        label = tkinter.Label(self.root,text='download zip the current directory mkdir webapp and download')
        label.pack(padx=5,pady=5,anchor='w')
        pass
    def downloadControls(self):
        #打包webpp
        def unpackwebapp(webappmkdir):
            print('unpack webapp path :'+ webappmkdir)
            G_LOG.append('unpack webapp path :'+ webappmkdir+'\n')
            unpack_zip = zipfile.ZipFile('webapp.zip','w')
            for dirpath, dirnames, filenames in os.walk(webappmkdir):
                for filename in filenames:
                    unpack_zip_path = os.path.join('webapp'+os.path.sep+ dirpath.split('webapp')[1],filename)
                    print('wait :' + filename)
                    unpack_zip.write(os.path.join(dirpath,filename),unpack_zip_path)
                    print('success :' + filename)
                    G_LOG.append('SUCCESS ' + unpack_zip_path + '\n')
            print('done')
            unpack_zip.close()
            webLogFile = open(webLog+os.path.sep+'web-log-'+theTime+'.txt','w',encoding='utf-8')
            webLogFile.write(' '.join(G_LOG))
            webLogFile.close()
            tkinter.messagebox.showinfo('SUCCESS MESSAGE','DONE')
            pass
        #检校md5
        def calibrationMD5():

            pass
        #下载zip文件并解压缩至webapp
        def zipDecompression(downloadStart):
            #显示下载进度
            def downSize(count, blockSize, totalSize):
                if not count:
                    print('connection opened')
                if totalSize <0:
                    print('远程主机，返回的下载总量为负数')
                    print('read %d blocks' % count)
                else:
                    print ('download '+zip_down[1]+' %d KB, totalsize: %d KB' % (count*blockSize/1024.0,totalSize/1024.0))
                pass
            zip_all = []
            for zip_down in downloadStart:
                #远程主机，返回的头信息是否与此匹配，来判断是否是zip文件 application/x-zip-compressed
                remoteHostTest = urllib.request.urlopen(zip_down[1])
                if not remoteHostTest.headers['Content-Type'] == 'application/x-zip-compressed':
                    continue
                print('request '+ zip_down[1] +' wait ....')
                G_LOG.append('DOWNLOAD '+ zip_down[1] +'\n')
                try:
                    zip_add = downloadPath+os.path.sep+zip_down[0]+'.zip'
                    zip_all.append(zip_add)
                    urllib.request.urlretrieve(zip_down[1],zip_add,reporthook=downSize)
                except ValueError:
                    print(zip_down[1])
                    raise ValueError('Error: download url bad'+zip_down[1])
                    G_LOG.append('Error: download url bad'+zip_down[1]+'\n')

            print('download is success')
            for zip_app in zip_all:
                zip_file = zipfile.ZipFile(zip_app,'r')
                zip_name_file = zip_file.namelist()
                zip_info_file = zip_file.infolist()
                for name in zip_name_file:
                    G_LOG.append('UN ZIP '+name + '\n')
                zip_file.extractall(path = webappmkdir)
                zip_file.close()
                pass
            unpackwebapp(webappmkdir)
            pass
        #解析 XML
        def handlerparseXML(xmlData):
            SOAP_ZIP_XML_PATH = downloadPath + os.path.sep +'SOAP_zip.xml'
            with open(SOAP_ZIP_XML_PATH,'w',encoding='utf-8') as xml_f:
                xml_f.write(xmlData)
                xml_f.close()
            SOAP_DIC = {}
            SOAP_XML_DOM = xml.dom.minidom.parseString(xmlData)
            SOAP_XMl_HEAD = SOAP_XML_DOM.getElementsByTagName('Header')
            SOAP_DIC['ServerIP'] = SOAP_XMl_HEAD[0].getAttribute('ServerIP')
            SOAP_DIC['ResultCode'] = SOAP_XMl_HEAD[0].getAttribute('ResultCode')
            SOAP_DIC['ResultMsg'] = SOAP_XMl_HEAD[0].getAttribute('ResultMsg')
            SOAP_DIC['ResultNo'] = SOAP_XMl_HEAD[0].getAttribute('ResultNo')
            if not len(SOAP_DIC['ServerIP']):
                print('ERROR: SOAP REQUEST BAD')
                print(SOAP_DIC['ResultNo'])
                print(SOAP_DIC['ResultMsg'])
                G_LOG.append('ERROR: SOAP REQUEST BAD \n')
                G_LOG.append('THE ERRPR MESSAGE '+SOAP_DIC['ResultMsg']+'\n')
                return
            SOAP_XML_Result = SOAP_XML_DOM.getElementsByTagName('Result')
            # print(getText(SOAP_XML_Result[0].childNodes))
            # SOAP_XML_Result_Text = SOAP_XML_Result[0].data()
            # print(SOAP_XML_Result_Text)
            SOAP_XML_HybridPackage = SOAP_XML_DOM.getElementsByTagName('HybridPackage')
            downloadALL = []
            count = -1
            for node in SOAP_XML_HybridPackage:
                downloadALL.append([])
                count += 1
                for node_value in node.childNodes:
                    node_text = getText(node_value.childNodes)
                    if len(node_text):
                        downloadALL[count].append(node_text)
            zipDecompression(downloadALL)
            pass
        #SOAP WEBSERVICE
        def getValue(event):
            SOAPURL = 'http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx?wsdl'
            SOAPSENDDATA = getVersion.get()
            SOAPSENDDATA = bodyXML.format(SOAPSENDDATA)
            SOAPSENDDATA = formatXML(SOAPSENDDATA)
            try:
                webservice = suds.client.Client(SOAPURL)
                SOAPRESPONSE = webservice.service.Request(SOAPSENDDATA)
                print('SOAP SUCCESS:'+SOAPURL)
                G_LOG.append('SOAP URL :' +SOAPURL + '\n')
                G_LOG.append('SOAP SEND DATA :' +SOAPSENDDATA + '\n' )
            except ValueError:
                raise  ValueError ('url bad')
            handlerparseXML(SOAPRESPONSE)
            pass
        messURL = tkinter.Label(self.root,text='SOAP URL: http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx?wsdl')
        messURL.pack(padx=5,anchor='w')
        parmas = tkinter.Label(self.root,text='Send VERSION:')
        parmas.pack(padx=5,anchor='w')
        getVersion = tkinter.Entry(self.root,width=500)
        getVersion.pack(padx=5,pady=5)
        # getSendDate = tkinter.Text(self.root,width=400,height=10)
        # getSendDate.pack(padx=5,pady=5,anchor='w')
        # getSendDate.focus_set()
        # Tscrollbar = tkinter.Scrollbar(self.root)
        # Tscrollbar.pack(side='right',fill='y')
        # Tscrollbar.config(command=getSendDate.yview)
        # getSendDate.config(yscrollcommand=Tscrollbar.set)
        openSOAP = tkinter.Button(self.root,text='openSOAP and unpackWebapp',width=30,height=1)
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