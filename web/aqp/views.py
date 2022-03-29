from django.shortcuts import render, Http404
from .models import Data,pol
import urllib
import time
from bs4 import BeautifulSoup
import re
import urllib.request
import os
from django.conf import settings
import csv
from django.views.decorators.csrf import csrf_exempt
import time

#static_template = os.path.join(settings.STATIC_ROOT, 'templates/aqp')
#print(static_template)

file_path = os.path.join(settings.STATIC_ROOT, 'data.csv')

import json
from django.http import JsonResponse
from django.urls import reverse
# from django.core.urlresolvers import reverse_lazy
from django.utils.encoding import force_text
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.views import generic
from .forms import Form1,Form2
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart,ColumnChart,GaugeChart
from graphos.renderers import gchart,highcharts


def stat(request):

  return render(request, 'aqp/stats.html')


# JUST FOR TESTING
def homie(request):
    form1 = Form1(request.GET or None)
    form2 = Form2(request.GET or None)
    #template = 'template.html'
    datas = Data.objects.all()
    context = {"products": products}
    if request.GET.get('featured'):
        featured_filter1 = request.GET.get('From')
        featured_filter2 = request.GET.get('To')

        datas = Data.objects.filter(Year__range=[featured_filter1,featured_filter2])

    else:
        datas = Data.objects.all()

    return render(request, "home.html", {'form1': form1,'form2': form2,"products": datas})



@csrf_exempt
def data(request):
     Am = " "
     CO = " "
     NO = " "
     OZ = " "
     SO2 = " "
     AT = " "
     PM10 = " "
     BE = " "
     NO2 = " "
     ON = " "
     pxy = " "
     TO = " "
     BP = " "
     PM2_5 = " "
     SR = " "
     Station_Name = " "


     if request.method == 'POST':
         if 'rowd' in request.POST:
           rowd = request.POST['rowd']

           
           station_code = {"av":"QW5hbmRWaWhhcg==","mm":"TWFuZGlybWFyZw==",
           "pb":"UHVuamFiaUJhZ2g=","rkPuram":"UktQdXJhbQ==","airpo":"SUdJ",
           "civilLines":"Q2l2aWxsaW5lcw==","dw":"RHdhcmthU2VjdHJvOA=="}
           result = None
           #while result:
           sc = {"av":1,"mm":2,
           "pb":3,"rkPuram":4,"airpo":5,
           "civilLines":6,"dw":7}

           station_names = {"av":"Anand Vihar","mm":"Mandir Marg",
           "pb":"Punjabi Bagh","rkPuram":"R.K. Puram","airpo":"IGI Airport",
           "civilLines":"Civil Lines","dw":"Dwarka"}

           while(result is None):
                     print("station",station_names[rowd])
                     Station_Name = " in " + station_names[rowd]
                     url = "http://www.dpccairdata.com/dpccairdata/display/AallStationView5MinData.php?stName={}".format(station_code[rowd])

                     html = urllib.request.urlopen(url).read()
                     soup = BeautifulSoup(html)
                     regex = re.compile('tdcolor.*')
                     td1 = soup.find_all("tr", {"class" : regex})
                     #td2 = soup.find_all("tr", {"class" : "tdcolor2"})
                     param = ["Ammonia","Carbon Monoxide","Nitrogen Oxide","Ozone","Sulphur Dioxide","Ambient Temperature"," Particulate Matter < 10 µg","Benzene","Nitrogen Dioxide","Oxides of Nitrogen","p-Xylene","Toluene","Barometric Pressure"," Particulate Matter < 2.5 µg","Solar Radiation"]

                     for i in td1:
                         td_list = i.find_all("td")
                         if td_list[0].text in param:

                             val = td_list[3].text.split(" ")[0]
                             if(val==''):
                                val = "-"
                             if param.index(td_list[0].text) == 0:
                                 Ammonia = val                            
                                 print("AMMONIA:",val)
                                 Am = val
                             elif param.index(td_list[0].text) == 1:
                                 Carbon_Monoxide = val
                                 print("CO:",val)
                                 CO = val
                             elif param.index(td_list[0].text) == 2:
                                 Nitrogen_Oxide = val
                                 print("NO:",val)
                                 NO = val
                             elif param.index(td_list[0].text) == 3:
                                 Ozone = val
                                 print("OZONE:",val)
                                 OZ = val
                             elif param.index(td_list[0].text) == 4:
                                 Sulphur_Dioxide = val
                                 print("SO2:",val)
                                 SO2 = val
                             elif param.index(td_list[0].text) == 5:
                                 Ambient_Temperature = val
                                 print("AMBIENT TEMP:",val)
                                 AT = val
                             elif param.index(td_list[0].text) == 6:
                                 Particulate_Matter_10 = val
                                 print("PPP10:",val)
                                 PM10 = val
                             elif param.index(td_list[0].text) == 7:
                                 Benzene = val
                                 print("BENZENE:",val)
                                 BE = val
                             elif param.index(td_list[0].text) == 8:
                                 Nitrogen_Dioxide = val
                                 print("NO2:",val)
                                 NO2 = val
                             elif param.index(td_list[0].text) == 9:
                                 Oxides_of_Nitrogen = val
                                 print("ON:",val)
                                 ON = val
                             elif param.index(td_list[0].text) == 10:
                                 p_Xylene = val
                                 print("P_XYLENE:",val)
                                 pxy = val
                             elif param.index(td_list[0].text) == 11:
                                 Toluene = val
                                 print("TOLUENE:",val)
                                 TO = val
                             elif param.index(td_list[0].text) == 12:
                                 Barometric_Pressure = val
                                 print("BAROMETRIC:",val)
                                 BP = val
                             elif param.index(td_list[0].text) == 13:
                                 Particulate_Matter_2 = val
                                 print("PPO2:",val)
                                 PM2_5 = val
                             elif param.index(td_list[0].text) == 14:
                                 Solar_Radiation = val
                                 print("Solar_rad:",val)
                                 SR = val
                     
                     #time.sleep(1000)
                     global context
                     result = 1
                     '''obj = pol(str(sc[rowd]))
                     print(Ammonia,Carbon_Monoxide,Nitrogen_Oxide,Ozone,Sulphur_Dioxide,Ambient_Temperature,Particulate_Matter_10
                     ,Benzene,Nitrogen_Dioxide,Oxides_of_Nitrogen,p_Xylene,Toluene,Barometric_Pressure,Particulate_Matter_2,Solar_Radiation)
                     obj.Ammonia = Ammonia
                     obj.Carbon_Monoxide = Carbon_Monoxide
                     obj.Nitrogen_Oxide = Nitrogen_Oxide
                     obj.Ozone = Ozone
                     obj.Sulphur_Dioxide = Sulphur_Dioxide
                     obj.Ambient_Temperature = Ambient_Temperature
                     obj.Particulate_Matter_10 = Particulate_Matter_10
                     obj.Benzene = Benzene
                     obj.Nitrogen_Dioxide = Nitrogen_Dioxide
                     obj.Oxides_of_Nitrogen = Oxides_of_Nitrogen
                     obj.p_Xylene = p_Xylene
                     obj.Toluene = Toluene
                     obj.Barometric_Pressure = Barometric_Pressure
                     obj.Particulate_Matter_2 = Particulate_Matter_2
                     obj.Solar_Radiation = Solar_Radiation
                     obj.save()'''
     
     context = {"Ammonia":Am,"Carbon_Monoxide":CO,"Nitrogen_Oxide":NO,"Ozone":OZ,
"Sulphur_Dioxide":SO2,"Ambient_Temperature":AT,"Particulate_Matter_10":PM10
          ,"Benzene":BE,"Nitrogen_Dioxide":NO2,"Oxides_of_Nitrogen":ON,"p_Xylene":pxy,
"Toluene":TO,"Barometric_Pressure":BP,"Particulate_Matter_2":PM2_5,"Solar_Radiation":SR,"StationName":Station_Name}
     print(context)
     #print(type(context) is dict)
     return render(request,"aqp/template.html",context)                 



def home(request):
    template = 'aqp/home.html'

    form1 = Form1(request.GET or None)
    form2 = Form2(request.GET or None)
    #template = 'template.html'
    filterdata = Data.objects.all()

    '''for i in products:
        print((Data.RPD_deaths)[1])'''
    featured_filter1 = 2001
    featured_filter2 = 2015
    if request.GET.get('featured'):
        featured_filter1 = request.GET.get('From')
        featured_filter2 = request.GET.get('To')
        #print("dsds",Data.RPD_deaths)
        filterdata = Data.objects.filter(Year__range=[featured_filter1,featured_filter2])

    else:
        filterdata = Data.objects.all()
    #print(products)
    
    data = [['Year','Four_wheelers','Two_wheelers','Auto_rickshaw','Buses','Taxis',
'e.Good_vehicles','Total_vehicles']]

    for e in filterdata:
        data.append([str(e.Year),e.Four_wheelers,e.Two_wheelers,e.Auto_rickshaw,e.Buses,e.Taxis,e.Good_vehicles,e.Total_vehicles])

    # DataSource object
    data_source = SimpleDataSource(data=data)

    chart = gchart.LineChart(data_source)


    data_deaths = [['Year',"RPD_deaths","Total_deaths"]]
    for e in filterdata:
        data_deaths.append([str(e.Year),e.RPD_deaths,e.Total_deaths])



    # DataSource object
    data_source2 = SimpleDataSource(data=data_deaths)
    chart2  =  highcharts.DonutChart(data_source2,height=450, width=1200,options={'title':"Deaths caused by Air Pollution"})
    #chart3 = gchart.AreaChart(data_source2,height=400, width=1100,options={'title':"Deaths caused by Air Pollution"})

    fw,tw,ar,bs,tx,gv ="None","None","None","None","None","None"
    fws,tws,ars,bss,txs,gvs ="None","None","None","None","None","None"
    if featured_filter1 <= featured_filter2:
        ob1 = filterdata[0]
        ob2 = filterdata[len(filterdata)-1]
        #print(ob1,ob2)
        fw = ob2.Four_wheelers-ob1.Four_wheelers

        tw = ob2.Two_wheelers-ob1.Two_wheelers

        ar = ob2.Auto_rickshaw-ob1.Auto_rickshaw

        bs = ob2.Buses-ob1.Buses

        tx = ob2.Taxis-ob1.Taxis

        gv = ob2.Good_vehicles-ob1.Good_vehicles
   
        fws,tws,ars,bss,txs,gvs =0,0,0,0,0,0
        if fws < 0:
            fws = 1
        if tw <0:
            tws = 1
        if ar <0:
            ars = 1
        if bs < 0:
            bss = 1
        if tx < 0:
            txs = 1
        if gv < 0:
            gvs = 1

        fw = "{:,}".format(fw)

        tw = "{:,}".format(tw)

        ar = "{:,}".format(ar)

        bs = "{:,}".format(bs)

        tx = "{:,}".format(tx)

        gv = "{:,}".format(gv)
    

    return render(request, "aqp/home.html",{"form1":form1,"form2":form2,"filterdata":filterdata,"chart":chart,"chart2":chart2,"data":data,
"fws":fws,"tws":tws,"ars":ars,"bss":bss,"txs":txs,"gvs":gvs,"fw":fw,"gv":gv,"tw":tw,"ar":ar,"bs":bs,"tx":tx})




def about(request):

	template = 'aqp/about.html'
	context = {
				}
	return render(request, template, context)


def contact(request):
	form_class = ContactForm
	return render(request,'aqp/contact.html', {
	    'form':form_class ,
	})


def import_data():
    with open(file_path) as f:
           reader = csv.reader(f)
           #form = DataForms(None)
           #obj = form.save()

           for row in reader:
              row = str(row[0]).split(' ')


              if row[0]!='YEAR':
                  #print(row)
                  obj = Data(str(row[0]))
                  #y = str(row[0])
                  obj.Year = row[0]
                  obj.RPD_deaths = row[1]
                  obj.Total_deaths = row[2]
                  obj.Four_wheelers =  row[3]
                  obj.Two_wheelers =  row[4]
                  obj.Auto_rickshaw =  row[5]
                  obj.Buses =  row[6]
                  obj.Taxis =  row[7]
                  obj.Good_vehicles =  row[8]
                  obj.Total_vehicles =  row[9]
                  obj.Population =  row[10]
                  obj.save()



import_data()

'''

                  obj, created = Data.objects.get_or_create(
    year = row[0],
    RPS = row[1] ,
    Tdeath = row[2],
    fw =  row[3],
    tw =  row[4],
    ar =  row[5],
    bs =  row[6],
    tx =  row[7],
    gv =  row[8],
    tv =  row[9],
    pop =  row[10],

                  )
                  obj.save()
'''

'''
with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Data.objects.get_or_create(
                first_name=row[0],
                last_name=row[1],
                middle_name=row[2],
                )
'''
