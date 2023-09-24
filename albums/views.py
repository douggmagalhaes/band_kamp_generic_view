from .models import Album
from .serializers import AlbumSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema


class AlbumView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @extend_schema(operation_id="album_list", summary="Listagem de álbuns", description="Rota para listar todos os álbuns da aplicação.", tags=["Álbum"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @extend_schema(operation_id="album_create", summary="Criação de álbuns", description="Rota de criação de álbuns da aplicação.", tags=["Álbum"])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


