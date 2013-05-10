from django.http import HttpResponse
import pandas
import numpy

from pandas.io.data import DataReader
from datetime import datetime

from django import forms

from django.shortcuts import render

def search_form(request):
    return render(request, 'search_form.html')

# Create your views here.
def fullfil(request):
    
    stockticker =request.GET['q'].encode('ascii','ignore')
    stockticker1 =request.GET['z'].encode('ascii','ignore')
    stock = DataReader(stockticker,  "yahoo", datetime(2005,1,1), datetime(2012,1,1))
    stock1 = DataReader(stockticker1,  "yahoo", datetime(2005,1,1), datetime(2012,1,1))
    corell = stock["Adj Close"].corr(stock1["Adj Close"])
    return HttpResponse(corell)


