var express = require('express');
var  app = express()
app.get('/zip',function(request,respones){
      var xml = '<?xml version="1.0" encoding="utf-8"?> <zip>https://github.com/xiangwenwen/downloadZIP/archive/master.zip</zip>';
      respones.type('xml');
      respones.send(xml) 
});
app.listen(9898)  
console.log('server start 127.0.0.1L:9898 for xml Data');