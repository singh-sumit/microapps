from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class NoteHomeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print("request.user: ", request)
        content = {"message": "Hello From Note Service"}
        return Response(content)