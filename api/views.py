from rest_framework.response import Response
from rest_framework.decorators import api_view
from lawyer.models import Lawyer
from .serializers import LawyerSerializer,PrendreRendezVousSerializer
from .models import PrendreRendezVous
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404




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

@api_view(['GET'])
def get_appointments_by_lawyer(request, lawyer_id):
    try:
        lawyer = get_object_or_404(Lawyer, lawyer_id=lawyer_id)
        appointments = PrendreRendezVous.objects.filter(laywer_id_id=lawyer)
        serializer = PrendreRendezVousSerializer(appointments, many=True)
        return Response(serializer.data)
    except Lawyer.DoesNotExist:
        return Response({'error': 'Lawyer not found'})




from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PrendreRendezVous
from .serializers import PrendreRendezVousSerializer

@api_view(['POST']) 
@authentication_classes([])
@permission_classes([AllowAny])
def schedule_appointment(request, lawyer_id):
    token_key = request.data.get('token', None)
    time = request.data.get('startTime', None)
    description = request.data.get('description', '')
    
    if token_key:
        user = Token.objects.filter(key=token_key).first()
        if not user:
            return Response({"success": False, "message": "Access denied. Invalid token."})
    else:
        return Response({"success": False, "message": "Access denied. Token not provided."})
    
    # Assuming you have a ForeignKey relationship between User and PrendreRendezVous
    prende_rendez_vous = PrendreRendezVous.objects.create(
        lawyer_id=lawyer_id,
        id=user,
        rdate=time,
        situation=description
    )

    return Response({"success": True, "message": "Appointment scheduled successfully."})

