from rest_framework import serializers, viewsets
from pursuit.models.sales import SalesOrder, SalesOrderDetail, Customer

class SalesOrderListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ('id', 'remarks', 'customer_name')
        
class SalesOrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(queryset=SalesOrder.objects.all(),source='main.id')

    class Meta:
        model = SalesOrderDetail
        fields = ('id', 'unit_price', 'parent_id')
        
class SalesOrderSerializer(serializers.HyperlinkedModelSerializer):
    details = SalesOrderDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = SalesOrder
        fields = ('id', 'remarks', 'details')
        
class SalesOrderListViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderListSerializer
    
class SalesOrderViewSet(viewsets.ModelViewSet):
    serializer_class = SalesOrderSerializer
    
    def get_queryset(self):
        id = self.kwargs['id']
        return SalesOrder.objects.filter(id = id)

class CustomerListSerializer(serializers.ModelSerializer):
    #label = serializers.CharField(source='phone')
    label = serializers.SerializerMethodField('get_label2')
    value = serializers.CharField(source='phone')
    
    def get_label2(self, obj):
        return '{} - {}'.format(obj.phone, obj.name)

    class Meta:
        model = Customer
        fields = ('label', 'value')

class CustomerListViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-phone')
    serializer_class = CustomerListSerializer