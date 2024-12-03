from django.shortcuts import render

# Create your views here.
def dqsalman(request):
    d={'name':'Lucky Baskar','rating':9}
    return render(request,'jinja_operation.html',context=d)
