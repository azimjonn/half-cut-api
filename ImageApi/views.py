from django.http import HttpResponse
from wsgiref.util import FileWrapper
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
import json
import PIL.Image as Image
from .custom_renderers import PNGRenderer
from .models import DataSample

class PostImage(APIView):

    parser_classes = [MultiPartParser, FormParser]
    renderer_classes = [PNGRenderer]
    def post(self, request):
        image = request.data['Image']
        image_path = 'data/' + image.name
        with open(image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        output_path = 'out/temp.png'
        res = open(output_path, 'rb')
        response = HttpResponse(FileWrapper(res))
        return response

class PostData(APIView):
    def post(self, request):
        file_name = request.GET['name']
        left_p = request.GET['left']
        right_p = request.GET['right']

        new_data = DataSample(image_name=file_name, left=left_p, right=right_p)
        new_data.save()
        print(new_data)

        return HttpResponse(json.dumps({"success" : True}))