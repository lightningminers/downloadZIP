////@ 此函数没有处理节假日问题
var parseDate = function(startD,endD,workSD,workED){
      ///@第一步判断，sD eD的时间区间，是否在一日之后，或?      
      var sGet = startD.getTime(),
            eGet = endD.getTime(),
            wsHours = workSD.getHours(),
            weHours = workED.getHours(),
            wsMin = workSD.getMinutes(),
            weMin = workSD.getMinutes(),
            sMonth = startD.getMonth()+1,
            eMonth = endD.getMonth()+1,
            sDay = startD.getDate(),
            eDay = endD.getDate(),
            sYear = startD.getFullYear(),
            eYear = endD.getFullYear(),
            date = [];
      var  wkStart = new Date(sYear + '-' + sMonth + '-'+sDay + ' '+ wsHours +':'+wsMin),
             wkEnd = new Date(sYear + '-' + sMonth + '-'+sDay + ' '+ weHours +':'+weMin),
             wsGet = wkStart.getTime(),
             weGet = wkEnd.getTime();
      if (sMonth == eMonth && sDay == eDay && sYear == eYear){
            // console.log(wkStart);
            ///@ method date 1
            if(sGet < wsGet && eGet > weGet){
                   date.push(wkStart,wkEnd);
                   return  date;
            }
            
            ///@ method date 2
            if((sGet >wsGet && sGet < weGet) && eGet > weGet){
                  date.push(startD,wkEnd);
                  return date;
            }
            
            ///@ method date 3
            if((sGet > wsGet && sGet < weGet) && eGet < weGet ){
                date.push(startD,endD);
                return date;
            }
            
            ///@ method date 5
            if(sGet < wsGet && (eGet < weGet && eGet > wsGet)){
                date.push(workSD,endD);
                return date;
            }
            
            ///@ method date 4 
            if((sGet > weGet && eGet > weGet)||(sGet < wsGet && sGet < wsGet)||(sGet<wsGet&&eGet < wsGet)){
                 return date;
            }
            
      }else{
          var differ = new Date(eYear+'-'+eMonth+'-'+eDay+' 0:00').getTime() - new Date(sYear+'-'+sMonth+'-'+sDay+' 0:00').getTime();
          var days = Math.floor(differ/(24*3600*1000)) + 1;
          var i = 0,pull = [];
          for(;i<days;i++){
            var _wks = wkStart.getTime()+(1000*60*60*24*i);
            var _wke = wkEnd.getTime()+(1000*60*60*24*i);
            pull.push([new Date(_wks),new Date(_wke)])
          }
          
          // console.log(date);
          var F_SGet = pull[0][0].getTime();
          var F_EGet = pull[0][1].getTime();
          var E_SGet = pull[pull.length -1][0].getTime();
          var E_EGet = pull[pull.length -1][1].getTime();
         if(sGet > F_EGet && eGet < E_SGet){
            return [];
         }
         
         date = pull.slice();
         
          if(sGet > F_EGet){
              date.splice(0,1);
              return date;
          }
          
          if(eGet < E_SGet){
              date.splice(date.length -1,1)
              return date;
          }
          
          ///@ method 5 childDate 1
          if(sGet < F_SGet && eGet < E_EGet){
                date[date.length - 1][1] = endD;
                return date;
          }
          
          ///@method 5 childDate 2
          if(sGet > F_SGet && eGet > E_EGet){
              date[0][0] = startD;
              return date;
          }
          
          ///@method 5 childDate 3 
          if(sGet > F_SGet && eGet < E_EGet){
              date[0][0] = startD;
              date[date.length - 1][1] = endD;
              return date;
          }
          
          if(sGet < F_SGet && eGet > E_EGet){
              return date;
          }
      }
}

///@ 工作开始时间

var wkSDF = new Date('2012-5-21 8:00')

///@ 工作结束时间

var wkEDF = new Date('2012-5-21 18:00')

///@订单时间
var sF1 = new Date('2013-5-21 10:59')

///@ 飞起时间
var eF1 = new Date('2013-5-22 16:23')

///@处理结果
var parseResultMethod1 = parseDate(sF1,eF1,wkSDF,wkEDF)

console.log(parseResultMethod1);


//// method date1@第一种情况startD在workSD之外， endD在 workED之外，区间为一日 print workSD -workED  print data Type [DateObject,DateObject]

/// method date2@第二种情况sD在wSD 之内，endD在wED之外,区间为一日 print startD - workED

/// mentho date3 @第三种情况sD在wSD之内，endD在wED之内，区间为一日 print startD - endD

/// mentho date4 @第四种情况 sD在wED之外，endD在wED之外, || sD 在 wSD 之外，endD在wSD之外 ，区间为一日 print False [False bool]

/// method date 5 @第五种情况 sD 在 wSD之外，endD在wED之内 区间为一日，print workSD - endD

/// method date6 @第六种情况sD与endD区间，为几日。

      /// method date5 - childDate1 @ 第一种情况sD 在wED之外，endD在wED(n)之内print workSD(1) - workED(1) --- n end: endD] [[workSD1,workED1],[workSD(n),endD]]
      
      /// metho date5 - childDate2  @ 第二种情况sD 在wED之内，endD 在wED(n)之外 print sD(1) - workED(1) ---n end : workED(n)
      
      /// method date5 - childDate3 @ 第三种情况sD  在wED之内，endD在wED(n)之内 print sD(1) - workED(1) ---n end: endD [[sD1,workED],[workSD1-endD]]
      
      ///method date5 - childDate4 @ 第四种情况 sD 在wSD之外，endD在wED之外 print workSD(1) - workED(1)
