from rest_framework.response import Response
from rest_framework.decorators import api_view
from lawyer.models import Lawyer
from .serializers import LawyerSerializer
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def search_lawyers(request):
    # Get query parameters
    name = request.GET.get('name', '')
    location = request.GET.get('location', '')
    specialization = request.GET.get('specialization', '')

    # Build the queryset based on the provided parameters
    queryset = Lawyer.objects.filter(
        Q(first_name__icontains=name) | Q(last_name__icontains=name),
        Q(address__icontains=location),
        Q(specialization__icontains=specialization)
    )

    # Serialize the queryset
    serializer = LawyerSerializer(queryset, many=True)

    return Response(serializer.data)





@api_view(['GET'])
def get_all_lawyers(request):
    queryset = Lawyer.objects.all()
    serializer = LawyerSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_lawyer_by_id(request, lawyer_id):
    try:
        lawyer = Lawyer.objects.get(lawyer_id=lawyer_id)
        serializer = LawyerSerializer(lawyer)
        return Response(serializer.data)
    except Lawyer.DoesNotExist:
        return Response({'error': 'Lawyer not found'})



