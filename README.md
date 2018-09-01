dowload zip and unpack webapp (mkdir)

Hybrid wiki : <a href="https://gitcafe.com/leewind/leewind-experiment/wiki/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%9E%84%E5%BB%BA-Hybrid%E5%A4%A7%E7%89%88%E6%9C%AC%E6%89%93%E5%8C%85%E5%B7%A5%E5%85%B7">wiki</a>

## python webservice 注意事项

SOAP 可以使用suds模块，python3可以下载另外一个版本<a href="https://pypi.python.org/pypi/suds-jurko/0.4.1.jurko.3">suds-jurko</a>

SEND DATA，需要注意一点，格式化发送参数，一定不能出现特殊字符，比如\n\t\r这类。具体传参，根据WSDL返回的参数而定。

 suds模块的，调试级别，可以根据参数调整，一般情况下，可以把suds.client这个开出来。使用sys  logging模块。
 
 
 ```python 
 
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
      
 ```
