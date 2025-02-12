from django.shortcuts import render
from .models import Customer,Orders
from rest_framework import generics,status
from .serializers import CreateCustomerSerializer,CreateOrdersSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import datetime



class CreateCustomerApiView(generics.CreateAPIView):
    serializer_class=CreateCustomerSerializer 
    queryset=Customer.objects.all()
    

class CreateCustomerOrdersApiView(generics.CreateAPIView):
    serializer_class = CreateOrdersSerializer
    queryset = Orders.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            customer_id = request.data.get("customer")
            customer = get_object_or_404(Customer, id=customer_id)

            # Create the order
            order = serializer.save()

            return Response(
                {
                    "message": f"Order for customer {customer.name} created successfully at {datetime.datetime.now()}",
                    "order": CreateOrdersSerializer(order).data,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {
                    "message":str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )



class CustomerOrdersApiView(generics.ListAPIView):
    serializer_class = CreateOrdersSerializer

    def get_queryset(self):
        customer_id = self.kwargs.get("customer_id")
        customer = get_object_or_404(Customer, id=customer_id)
        return Orders.objects.filter(customer=customer)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        
        if not queryset.exists():
            return Response(
                {"message": "No orders found for this customer"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)