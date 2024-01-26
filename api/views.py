from rest_framework.response import Response
from rest_framework.decorators import api_view
from lawyer.models import Lawyer
from .serializers import LawyerSerializer
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def lawyer_profile_search(request):
    query = request.GET.get('query', '')
    categories = request.GET.getlist('categories')
    rating = request.GET.get('rating', '')

    search_results = Lawyer.objects.all()

    if query:
        name_filter = (
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )
        address_filter = (
            Q(address__icontains=query)
        )

        search_results = search_results.filter(name_filter | address_filter)

    if categories != ['']:
        category_filter = Q()
        for category in categories:
            category_filter |= Q(specialization__iexact=category)
        search_results = search_results.filter(category_filter)

    if rating:
        search_results = search_results.filter(rating__gte=rating)

    paginated_results = search_results.order_by('-rating').distinct()

    # You may need to create a serializer for the Lawyer model
    serialized_results = LawyerSerializer(paginated_results, many=True).data

    return Response({'search_results': serialized_results})




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


