from django.contrib.auth import get_user_model

from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializer, ChangePasswordSerializer, \
    ForgotPasswordSerializer, ForgotPasswordCompleteSerializer

User = get_user_model()


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистрировались. \n Вам отправлено письмо с активацией', status=201)




class ChengePasswordApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно изменен')


class ActivationApiViewA(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Успешно'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'Неверный код!'}, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправленно письмо для восстанавление пароля')


class ForgotPasswordCompleteAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно обновлен')