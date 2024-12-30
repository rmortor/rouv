from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import (
    productos_pedidosViews,
    productosViews,
    pedidosViews,
    llamadasView,
    cuentasViews,
)
from django.conf import settings
from django.conf.urls.static import static

# Registro de todas las vistas en un único router
router = routers.DefaultRouter()
router.register(r'productos_pedidos', productos_pedidosViews, 'productos_pedidos')
router.register(r'productos', productosViews, 'productos')
router.register(r'pedidos', pedidosViews, 'pedidos')
router.register(r'llamadas', llamadasView, 'llamadas')  # Cambié el nombre del endpoint
router.register(r'cuentas', cuentasViews, 'cuentas')

# Definición de las URL
urlpatterns = [
    path('api/', include(router.urls)),  # Una única raíz para todos los endpoints
    path('docs/', include_docs_urls(title='backend')),
]

# Manejo de archivos estáticos y media en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
