from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from char_count.models import CharCount


class CharCount(APIView):
    """
    Print the character count of the text submitted by the user
    """

    def handle_char_count(self, serializer):
        try:
            return Response({"count": len(serializer.data)})
        except Exception as e:
            return Response({"count": None}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer = CharCount(data=request.query_params.get("text"))
        return self.handle_char_count(serializer=serializer)

    def post(self, request):
        serializer = CharCount(data=request.data.get("text", ""))
        return self.handle_char_count(serializer=serializer)
