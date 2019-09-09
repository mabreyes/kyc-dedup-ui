from django.shortcuts import render

# Create your views here.
def view_ui(request):
    return render(request, 'sample.html')

def view_list(request):
    return render(request, 'view_list.html')