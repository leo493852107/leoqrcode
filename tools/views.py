from django.http import HttpResponse
import qrcode
from cStringIO import StringIO


def generate_qrcode(request, data):
    img = qrcode.make(data)

    buf = StringIO()
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream, content_type='image/png')
    response['Last-Modified'] = 'Sat, 14 May 2016 21:11:00 GMT'
    response['Cache-Control'] = 'max-age=31536000'
    return response
