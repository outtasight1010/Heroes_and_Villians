from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
# api_view = This will assign certain permissions to this function
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from super_types.models import SuperType
from .serializers import SuperSerializer
from super_types.serializers import SuperTypeSerializer

@api_view(["GET", "POST"])
def super_list(request):
    if request.method == "GET":

        supers_kind = request.query_params.get("super type")
        print(supers_kind)

        queryset = queryset.filter(supers_kind__name =supers_kind)

        serializer = SuperSerializer(queryset, many =True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
@api_view(["GET","PUT","DELETE"])
def super_detail(request,pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == "GET":
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SuperSerializer(super,data= request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        super.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    



    



        
        



# Create your views here.
