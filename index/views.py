from django.shortcuts import render
from datetime import datetime

def index(request):
    now = datetime.now()
    data = { 'now': now }
    return render(request, 'index.html', data)