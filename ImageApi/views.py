from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
import json
import PIL.Image as Image


class PostImage(APIView):

    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        image = request.data['Image']
        with open('sample.jpg', 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        return Response(json.dumps({'success': True}))
