from rest_framework.decorators import api_view
# api_view = This will assign certain permissions to this function
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer

@api_view(["GET"])
def super_list(request):
    supers = Super.objects.all()
    serializer = SuperSerializer(supers, many =True)

    return Response(serializer.data)

# Create your views here.
