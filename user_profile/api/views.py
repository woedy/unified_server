from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.response import Response


@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def get_user_profile(request):

    payload = {}
    data = {}
    errors = {}

    if request.method == 'GET':
        user_id = request.query_params.get("user_id", None)

        print(user_id)

    return Response(payload)