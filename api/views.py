import io

from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import pyplot as plt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ScatterSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


@api_view(['POST'])
def scatter(request, format=None):
    if request.method == 'POST':
        serializer = ScatterSerializer(data = request.data)
        if serializer.is_valid():
            fig = plt.figure()
            x = list(map(float, serializer.data["x"].strip("[]").split(",")))
            y = list(map(float, serializer.data["y"].strip("[]").split(",")))
            # create a bytesIO object
            svg_file = io.BytesIO()
            # scatter
            plt.scatter(x, y)
            # save the plot to the bytesIO object
            plt.savefig(svg_file, format='svg')
            svg_string = svg_file.getvalue().decode('utf-8').replace('\n', '').replace('\"', "'")

            return Response({"svg_image": svg_string}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "serializer not valid"}, status=status.HTTP_418_IM_A_TEAPOT)
    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)