from django.shortcuts import render, Http404
from .models import Data
import urllib
import time
import re
import urllib.request
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

#static_template = os.path.join(settings.STATIC_ROOT, 'templates/aqp')
#print(static_template)

# file_path = os.path.join(settings.STATIC_ROOT, 'data.csv')

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


