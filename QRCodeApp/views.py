from django.shortcuts import render

def home(request):
    query = request.GET.get('query')
    results = None
    if query:
        display =  {'query':query,'results':f'Result:{query}'}
        
    return render(request,'QRCodeApp/index.html',{'query':query,'results':results})