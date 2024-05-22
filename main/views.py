import qrcode
from io import BytesIO
from django.http import HttpResponse
from .models import QRCodeData

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")


def view_qr_code(request, data_id):
    qr_data = QRCodeData.objects.get(id=data_id)
    context = {
        'qr_data': qr_data,
    }
    return render(request, 'view_qr_code.html', context)


def generate_qr_code(request, data):
    qr_data = QRCodeData.objects.create(data=data)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data.data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer)
    qr_data.save()
    return HttpResponse(buffer.getvalue(), content_type='image/png')



