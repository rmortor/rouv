from rest_framework import serializers
from .models import productos, pedidos, productos_pedidos, cuentas, llamadas

class productosSerializer(serializers.ModelSerializer):
    class Meta:
        model = productos
        fields = '__all__'

class productos_pedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = productos_pedidos
        fields = '__all__'

class pedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedidos
        fields = '__all__'

class llamadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = llamadas
        fields = '__all__'

class cuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = cuentas
        fields = '__all__'