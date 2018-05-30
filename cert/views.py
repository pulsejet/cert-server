from django.http import FileResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from cert.models import Cert
import datetime
import os

def get_cert(request, uuid):
    cert = get_object_or_404(Cert.objects.all(), uuid=uuid)
    filename = cert.file_path
    rendered = render_to_string('cert.html', {
        'cert': cert
    })
    return HttpResponse(rendered)

def file_cert(request, uuid):
    cert = get_object_or_404(Cert.objects.all(), uuid=uuid)
    filename = cert.file_path
    response = FileResponse(open('files/' + filename, 'rb'))
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'inline;filename="{0}"'.format(filename);
    return response
