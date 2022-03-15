from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User


from postulant.serializer import UserCustomSerializer, AuthCustomTokenSerializer


class CustomAuthToken(APIView):
    serializer_class = AuthCustomTokenSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })



class UserView(APIView):

    def get(self, request, pk):
        user = User.objects.filter(pk=pk, is_active=True).first()
        serializer = UserCustomSerializer(user)
        return  Response(serializer.data)
