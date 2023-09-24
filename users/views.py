from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(operation_id="user_list", summary="Listagem de usuário", description="Rota para listar todos os usuários da aplicação.", tags=["User"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @extend_schema(operation_id="user_create", summary="Criação de usuário", description="Rota de criação dos usuários da aplicação.", tags=["User"])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(operation_id="user_list_id", summary="Lista um usuário pelo id", description="Rota para listar um usuários pelo id da aplicação.", tags=["User"])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(operation_id="user_update", summary="Atualiza um usuário pelo id", description="Rota para atualizção de usuário da aplicação.", tags=["User"])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    @extend_schema(operation_id="user_delete", summary="Deleta um usuário pelo id", description="Rota para deleção de usuário da aplicação.", tags=["User"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @extend_schema(operation_id="user_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
