from django.shortcuts import render
def showIndex(request):
    return render(request,"one.html")
def Main(request):
    fname=request.POST.get("t1")
    lname=request.POST.get("t2")
    return render(request,"one.html",{"data":fname+lname})
