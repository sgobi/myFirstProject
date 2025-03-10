from django.shortcuts import render

# Create your views here.
def show_my_first(request):
    return render(request,'hello.html')