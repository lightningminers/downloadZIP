__author__ = 'xiangwenwen'

import suds.client
import logging
import sys
import httplib2
import xml.dom.minidom
import http.client
import urllib.parse

# client http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx


header = '''
    <?xml version="1.0"?>
    <Request>
      <Header UserID="CtripTest" SessionID="0d21swty1o22qatzzrke4vip" RequestID="1c34b903-e1f5-4c6d-bbb4-d1bcd0a664e3" RequestType="Operation.HybridPublishService.HybridPackageQueryRQ" ClientIP="172.16.150.76" AsyncRequest="false" Timeout="0" MessagePriority="3" AssemblyVersion="1.0.2.5" RequestBodySize="0" SerializeMode="Xml" RouteStep="1" />
      <HybridPackageQueryRQ>
        <EnvCode>1</EnvCode>
        <ClientVersion>5.3</ClientVersion>
      </HybridPackageQueryRQ>
    </Request>
'''


#日志信息
handler = logging.StreamHandler(sys.stderr)
logger = logging.getLogger('suds.transport.http')
logger.setLevel(logging.DEBUG), handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
class OutgoingFilter(logging.Filter):
    def filter(self, record):
        return record.msg.startswith('sending:')
handler.addFilter(OutgoingFilter())

#快速测试suds 运行情况
def testSuds():
    url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
    client = suds.client.Client(url)
    print(client)
    result = client.service.getMobileCodeInfo(15989012552)
    print(result)
    pass
# testSuds()

#创建一个提交xml

impl = xml.dom.minidom.getDOMImplementation()
dom = impl.createDocument(None, None, None)
root = dom.createElement('Request')
Header = dom.createElement('Header')
Header.setAttribute('UserID','CtripTest')
Header.setAttribute('SessionID','0d21swty1o22qatzzrke4vip')
Header.setAttribute('RequestID','1c34b903-e1f5-4c6d-bbb4-d1bcd0a664e3')
Header.setAttribute('RequestType','Operation.HybridPublishService.HybridPackageQueryRQ')
Header.setAttribute('ClientIP','172.16.150.76')
Header.setAttribute('AsyncRequest','false')
Header.setAttribute('Timeout','0')
Header.setAttribute('MessagePriority','3')
Header.setAttribute('AssemblyVersion','1.0.2.5')
Header.setAttribute('RequestBodySize','0')
Header.setAttribute('SerializeMode','xml')
Header.setAttribute('RouteStep','1')
root.appendChild(Header)
HybridPackageQueryRQ = dom.createElement('HybridPackageQueryRQ')
EnvCode = dom.createElement('EnvCode')
EnvCodeText = dom.createTextNode('1')
EnvCode.appendChild(EnvCodeText)
HybridPackageQueryRQ.appendChild(EnvCode)
ClientVersion = dom.createElement('ClientVersion')
ClientVersionText = dom.createTextNode('5.3')
ClientVersion.appendChild(ClientVersionText)
HybridPackageQueryRQ.appendChild(ClientVersion)
root.appendChild(HybridPackageQueryRQ)
dom.appendChild(root)

#测试 xml 生成情况
# f = open('d:\\Users\\wwxiang\\Desktop\\zip.xml','w')
# dom.writexml(f,'',' ','\n','utf-8')
# f.close()
#http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx

#http://www.wanyan.com/vote/vote-star!getTopVoteStarByMonth.dhtml
#POST是成功的
web = http.client.HTTPConnection('www.wanyan.com')
webDate = str({'rownum':'3'})
webHead = {
    'Host':'www.wanyan.com',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Content-Length':'%d' % len(webDate),
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Python Post'
}
web.request('POST','/vote/vote-star!getTopVoteStarByMonth.dhtml',body=webDate,headers=webHead)
res = web.getresponse()
print(res.read())

# webservice = http.client.HTTPConnection('wb.mobile.sh.ctripcorp.com')
# print(res)



# mo_ctrip =  suds.client.Client('http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx?wsdl')
#
# print(mo_ctrip)
# print(mo_ctrip.service.CommRequest())

#运行测试真实地址
# _client = suds.client.Client('http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx?wsdl')
# print(_client)
# print(_client.service.Request(header))


#测试soap webservice
#http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl

codeWS = http.client.HTTPConnection('webservice.webxml.com.cn')
codeWSHead = {
    'Host':'webservice.webxml.com.cn',
    'Content-Type':'text/xml; charset=utf-8',
    'Content-Length':'%d' % len(webDate),
    'SOAPAction':'/',
    'User-Agent':'Python Post'
}
codeWS.request('GET','/WebServices/MobileCodeWS.asmx?wsdl',headers=codeWSHead)

codeRES = codeWS.getresponse()
print(codeRES.read().getMobileCodeInfo(15989012552))

# urllib.parse.urlencode()