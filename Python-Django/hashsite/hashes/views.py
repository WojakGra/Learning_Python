from django.shortcuts import render
from django.http import JsonResponse
from .models import HexText
import hashlib


# Create your views here.
def hashing(request):
    HexTexts = HexText.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        Text = request.POST.get('Text')
        Hex = request.POST.get('Hex')

        response_data['Text'] = Text
        response_data['Hex'] = Hex

        HexText.objects.create(
            Text=Text,
            Hex=hashlib.sha1(bytearray(Hex, 'UTF-8')).hexdigest(),
        )
        return JsonResponse(response_data)

    stuff_for_frontend = {
        'HexTexts': HexTexts
    }

    return render(request, 'home.html', stuff_for_frontend)
