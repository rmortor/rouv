from rest_framework import viewsets
from .serializer import productos_pedidosSerializer, productosSerializer,pedidosSerializer,llamadasSerializer,cuentasSerializer
from .models import productos_pedidos,productos, pedidos, cuentas, llamadas

# Create your views here.
class productos_pedidosViews(viewsets.ModelViewSet):
    serializer_class = productos_pedidosSerializer
    queryset = productos_pedidos.objects.all()

class productosViews(viewsets.ModelViewSet):
    serializer_class = productosSerializer
    queryset = productos.objects.all()

class pedidosViews(viewsets.ModelViewSet):
    serializer_class = pedidosSerializer
    queryset = pedidos.objects.all()

class llamadasView(viewsets.ModelViewSet):
    serializer_class = llamadasSerializer
    queryset = llamadas.objects.all()

class cuentasViews(viewsets.ModelViewSet):
    serializer_class = cuentasSerializer
    queryset = cuentas.objects.all()