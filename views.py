from rest_framework.decorators import api_view
# api_view = This will assign certain permissions to this function
from rest_framework.response import Response
from .models import SuperType
from .serializers import SuperTypeSerializer

@api_view(["GET"])
def super_type_list(request):
    supertypes = SuperType.objects.all()
    serializer = SuperTypeSerializer(supertypes, many =True)

    return Response(serializer.data)



# Create your views here.
