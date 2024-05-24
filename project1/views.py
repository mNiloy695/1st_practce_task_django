from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
def main_page(request):

    d={"naim":'vai',"val":"","file_formate":12328939293,"time":datetime.now(),"age":30,"lst":["naim","is","best","and","hotest"],"details":[{
        "name":"naim",
        "age":26,
        "weight":60
    },{
        "name":"salah uddin",
        "age":20,
        "weight":45
    },
    {
        "name":"Nirob",
        "age":16,
        "weight":49
    }]}
    return render(request,"main_page.html",d)