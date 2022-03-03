from django.shortcuts import render

# Create your views here.

# the first view: FBV (function based view)
def homePageView(request):
    return HttpResponse("Hello World")