from django.shortcuts import render

# Create your views here.

def someone(request) -> render:
    succesful = 'succesful'
    return render(
    request, 'base.html', context={succesful:succesful}
    )