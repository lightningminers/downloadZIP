__author__ = 'xiangwenwen'

import suds.client
import httplib2
import logging

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
# _client = suds.client.Client('http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx?wsdl')
# print(_client.service.test(__inject={'msg':header}))
# print(_client)

#快速测试suds 运行情况
def testSuds():
    url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
    client = suds.client.Client(url)
    # print(client)
    result = client.service.getMobileCodeInfo(15989012552)
    print(result)
    _client = suds.client.Client('http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl')
    print(_client.service.qqCheckOnline(1368843198))
    pass
testSuds()