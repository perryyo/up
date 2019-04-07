from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import image_slicer
from uploads.core.models import Document
from uploads.core.forms import DocumentForm
import os
import zipstream

from django.http import StreamingHttpResponse



def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.path(filename)
        tiles = image_slicer.slice(uploaded_file_url, 9, save=False)
        image_slicer.save_tiles(tiles, directory='media/',prefix='slice', format='png')
        os.remove(uploaded_file_url)
        z = zipstream.ZipFile(mode='w', compression=zipstream.ZIP_DEFLATED)
        z.write('media/slice_01_01.png','slice_01_01.png')
        z.write('media/slice_01_02.png','slice_01_02.png')
        z.write('media/slice_01_03.png','slice_01_03.png')
        z.write('media/slice_02_01.png','slice_02_01.png')
        z.write('media/slice_02_02.png','slice_02_02.png')
        z.write('media/slice_02_03.png','slice_02_03.png')
        z.write('media/slice_03_01.png','slice_03_01.png')
        z.write('media/slice_03_02.png','slice_03_02.png')
        z.write('media/slice_03_03.png','slice_03_03.png')
        response = StreamingHttpResponse(z, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename={}'.format('files.zip')
        return response


    return render(request, 'core/simple_upload.html')

