from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Customer, Orders
from decimal import Decimal

class CustomerOrdersAPITest(TestCase):
    def setUp(self):
        """Set up test client and sample data."""
        self.client = APIClient()

        # Create a test customer instance
        self.customer = Customer.objects.create(
            name="Akal Erupe",
            email="akal@example.com"
        )

        # Order data payload
        self.order_data = {
            "customer": self.customer.id,
            "product_name": "Test Product",
            "amount": "50.75"
        }

    def test_create_customer(self):
        """Test creating a new customer."""
        response = self.client.post(
            "/customers/",
            {"name": "Jane Doe", "email": "janedoe@example.com"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)

    def test_create_order(self):
        """Test creating an order for a valid customer."""
        response = self.client.post("/customers/orders/", self.order_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Orders.objects.count(), 1)
        self.assertEqual(Orders.objects.first().amount, Decimal("50.75"))

    def test_get_orders_for_customer(self):
        """Test retrieving orders for a customer."""
        Orders.objects.create(customer=self.customer, product_name="Test Product", amount=Decimal("50.75"))

        response = self.client.get(f"/customers/{self.customer.id}/orders/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["product_name"], "Test Product")

    def test_get_orders_for_customer_no_orders(self):
        """Test retrieving orders for a customer with no orders."""
        response = self.client.get(f"/customers/{self.customer.id}/orders/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["message"], "No orders found for this customer")

    def test_create_order_invalid_customer(self):
        """Test creating an order with a non-existent customer."""
        invalid_order_data = {
            "customer": 9999,  # Invalid customer ID sample
            "product_name": "Invalid Order",
            "amount": "30.00"
        }
        response = self.client.post("/customers/orders/", invalid_order_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_customer_deletion_cascade(self):
        """Test that deleting a customer deletes their orders (CASCADE)."""
        order = Orders.objects.create(customer=self.customer, product_name="Product A", amount=Decimal("20.00"))
        self.customer.delete()
        
        self.assertEqual(Orders.objects.count(), 0)  # Orders should be deleted
