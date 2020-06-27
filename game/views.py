from django.shortcuts import render

# Create your views here.
def mine(request):
    return render(request, 'games/mine.html')