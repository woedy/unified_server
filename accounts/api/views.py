from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.response import Response


@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def register_user(request):

    payload = {}
    data = {}
    errors = {}

    if request.method == 'POST':
        email = request.data.get('email', "").lower()

        print(email)

    return Response(payload)



