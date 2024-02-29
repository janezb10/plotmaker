import io

from django.shortcuts import render
from django.http import HttpResponse
from matplotlib import pyplot as plt
from pydantic import ValidationError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.schemas.Scatter import Scatter

from api.serializers import ScatterSerializer

def validate_request_data(data_dict: dict,tip):
    try:
        data = tip(**data_dict)
        return True, data
    except ValidationError as e:
        return False, e


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")


@api_view(['POST'])
def scatter(request, format=None):
    if request.method == 'POST':
        valid, data = validate_request_data(request.data, Scatter)
        if not valid:
            return Response(data.errors(), status=status.HTTP_400_BAD_REQUEST)

        fig = plt.figure()
        svg_file = io.BytesIO()
        plt.scatter(**request.data)
        plt.savefig(svg_file, format='svg')
        svg_string = svg_file.getvalue().decode('utf-8').replace('\n', '').replace('\"', "'")
        return Response({"svg_image": svg_string}, status=status.HTTP_200_OK)

    return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)