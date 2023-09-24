from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        serializer.save(album_id=self.kwargs.get("pk"))
      
    @extend_schema(operation_id="song_list", summary="Listagem de músicas", description="Rota para listar todas as músicas da aplicação.", tags=["Song"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @extend_schema(operation_id="song_create", summary="Criação de músicas", description="Rota de criação de músicas da aplicação.", tags=["Song"])
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)