from rest_framework import serializers, viewsets
from pursuit.models.sales import SalesOrder, SalesOrderDetail, Customer

class SalesOrderListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ('id', 'remarks', 'customer_name')
        
class SalesOrderListViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderListSerializer

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
        
    
class SalesOrderViewSet(viewsets.ModelViewSet):
    serializer_class = SalesOrderSerializer
    
    def get_queryset(self):
        id = self.kwargs['id']
        return SalesOrder.objects.filter(id = id)

class CustomerListSerializer(serializers.ModelSerializer):
    #label = serializers.CharField(source='phone')
    # id = serializers.Field()
    label = serializers.SerializerMethodField('get_label2')
    value = serializers.CharField(source='phone')

    # def quer_id():
    #     id = self.kwargs['id']
    #     return 

    def get_label2(self, obj):
        return '{} - {}'.format(obj.phone, obj.name)


    class Meta:
        model = Customer
        fields = ('id','label', 'value','name','phone','occupation','dob','refer_by','email','office_address','delivery_address')

class CustomerListViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerListSerializer

# class CustomerPostFormSerilization(serializers.ModelSerializer):
#     name = serializers.CharField(source = "name")
#     phone = serializers.CharField(source = "phone")
#     occupation = serializers.CharField(source = "occupation")
#     dob = serializers.DateField(source = "dob")
#     refer_by = serializers.CharField(source = "refer_by")
#     email = serializers.EmailField(source = "email")
#     office_address = serializers.CharField(source = "office_address")
#     delivery_address = serializers.CharField(source = "delivery_address")


#     class Meta:
#         model = Customer
#         fields = ('id','label', 'value','name','phone','occupation','dob','refer_by','email','office_address','delivery_address')    

# class CustomerSerilizeListViewSet(viewsets.ModelViewSet):
#     queryset = Customer.object.all.order_by('-id')
#     serializer_class = CustomerPostFormSerilization
   

class CustomerListEditSerializer(serializers.HyperlinkedModelSerializer):
    
    # name = serializers.CharField()
    # phone = serializers.CharField()
    # occupation = serializers.CharField()
    # dob = serializers.DateField()
    # refer_by = serializers.CharField()
    # email = serializers.EmailField()
    # office_address = serializers.CharField()
    # delivery_address = serializers.CharField()


    # def quer_id():
    #     id = self.kwargs['id']
    #     return 

    


    class Meta:
        model = Customer
        fields = ('name','phone','occupation','dob','refer_by','email','office_address','delivery_address')

class CustomerListEditViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('-id')
    serializer_class = CustomerListEditSerializer