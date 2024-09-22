from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FloatData, BooleanData
from .serializers import FloatDataSerializer, BooleanDataSerializer

# Float data with parameters
@api_view(['POST'])
def add_float_data(request, value1, value2, value3, value4, value5):
    data = {'todayUsage': value1, 'monthUsage': value2, 'device1Usage': value3, 'device2Usage': value4, 'device3Usage': value5}
    serializer = FloatDataSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_float_data(request):
    try:
        data = FloatData.objects.all().last()
        serializer = FloatDataSerializer(data)
        return Response(serializer.data)
    except FloatData.DoesNotExist:
        return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

# Boolean data with parameters
@api_view(['POST'])
def add_boolean_data(request, bool1, bool2, bool3):
    data = {'device1Switch': bool1 == 'true', 'device2Switch': bool2 == 'true', 'device3Switch': bool3 == 'true'}
    serializer = BooleanDataSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_boolean_data(request):
    try:
        data = BooleanData.objects.all().last()
        serializer = BooleanDataSerializer(data)
        return Response(serializer.data)
    except BooleanData.DoesNotExist:
        return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
