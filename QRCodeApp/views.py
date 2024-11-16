from django.shortcuts import render,redirect

def home(request):
    query = request.GET.get('query')
    results = "https://quickchart.io/qr?text="
    display = None
    if query:
        display =  f'{results}{query}'
    return render(request,'QRCodeApp/index.html',{'query':query,'results':display})

