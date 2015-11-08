from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

class UploadMedia(generics.GenericAPIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        f = request.data['file']

        return Response(None)
