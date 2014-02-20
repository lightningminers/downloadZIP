__author__ = 'wwxiang'
import sys
import logging
import suds.client
import http.client
import urllib.parse
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

bodyNotXML = '<?xml version="1.0"?><Request><Header UserID="CtripTest" SessionID="0d21swty1o22qatzzrke4vip" RequestID="1c34b903-e1f5-4c6d-bbb4-d1bcd0a664e3" RequestType="Operation.HybridPublishService.HybridPackageQueryRQ" ClientIP="172.16.150.76" AsyncRequest="false" Timeout="0" MessagePriority="3" AssemblyVersion="1.0.2.5" RequestBodySize="0" SerializeMode="Xml" RouteStep="1" /><HybridPackageQueryRQ><EnvCode>1</EnvCode><ClientVersion>5.3</ClientVersion></HybridPackageQueryRQ></Request>'


#<?xml version="1.0"?><Request><Header UserID="CtripTest"SessionID="0d21swty1o22qatzzrke4vip"RequestID="1c34b903-e1f5-4c6d-bbb4-d1bcd0a664e3"RequestType="Operation.HybridPublishService.HybridPackageQueryRQ"ClientIP="172.16.150.76"AsyncRequest="false"Timeout="0"MessagePriority="3"AssemblyVersion="1.0.2.5"RequestBodySize="0"SerializeMode="Xml"RouteStep="1"/><HybridPackageQueryRQ><EnvCode>1</EnvCode><ClientVersion>5.3</ClientVersion></HybridPackageQueryRQ></Request>
#sending:


bodyXML = '''
  <?xml version="1.0"?>
  <Request>
    <Header UserID="CtripTest" SessionID="0d21swty1o22qatzzrke4vip" RequestID="1c34b903-e1f5-4c6d-bbb4-d1bcd0a664e3" RequestType="Operation.HybridPublishService.HybridPackageQueryRQ" ClientIP="172.16.150.76" AsyncRequest="false" Timeout="0" MessagePriority="3" AssemblyVersion="1.0.2.5" RequestBodySize="0" SerializeMode="Xml" RouteStep="1" />
    <HybridPackageQueryRQ>
      <EnvCode>1</EnvCode>
      <ClientVersion>5.3</ClientVersion>
    </HybridPackageQueryRQ>
  </Request>'''


bodyXML = ' '.join(bodyXML.split())
print(bodyXML)

# print(bodyXML)
#第一种连接方式

#http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx

# webservice = http.client.HTTPConnection('wb.mobile.sh.ctripcorp.com')
# webservice.set_debuglevel(4)
# webservice.putrequest('POST','/hybridpublish/service.asmx?wsdl')
# webservice.putheader('Host','wb.mobile.sh.ctripcorp.com')
# webservice.putheader('Content-Type','text/xml; charset=utf-8')
# webservice.putheader('Content-Length','%d'%len(bodyXML))
# webservice.putheader('SOAPAction','http://wb.mobile.sh.ctripcorp.com')
# webservice.endheaders()
# webRes = webservice.getresponse()
# print(webRes.headers)
# print(webRes.read())

#bodyXML  XML一定要进行处理，\r\n这样的特殊字符。另外根据wsdl定义的参数，是string所以不需要转字节码
webSuds = suds.client.Client('http://wb.mobile.sh.ctripcorp.com/hybridpublish/service.asmx?wsdl')
print(webSuds)
res = webSuds.service.Request(bodyXML)
print(res)