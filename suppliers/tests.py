from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Supplier

class SupplierCreateTests(APITestCase):

    def test_create_supplier(self):
        """
        Ensure we can create a supplier.
        """
        url = reverse('list-create-suppliers')
        data = {
            "email": "test_client100@gmail.com",
            "mobile_number": "0801000000",
            "name":  "Test Client",
            "address": "",
            "other_contact_info": ""
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertTrue('id' in response.data)
        self.assertDictContainsSubset(data, response.data)
        
    def test_mobile_number_fail_create_inventory_item(self):
        """
        Ensure we can validate a supplier's mobile number.
        """
        url = reverse('list-create-suppliers')
        data = {
            "email": "test_client100@gmail.com",
            "mobile_number": "+2348",
            "name":  "Test Client",
            "address": "",
            "other_contact_info": ""
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Supplier.objects.count(), 0)
        self.assertTrue('mobile_number' in response.data)
  

class SupplierListTests(APITestCase):

    def setUp(self) -> None:
        self.supplier = Supplier.objects.create(
            email="test_client100@gmail.com",
            mobile_number="0801000000",
            name = "Test Client"
        )

    def test_list_inventory_items(self):
        """
        Ensure we can query all suppliers.
        """
        url = reverse('list-create-suppliers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)
        self.assertTrue(isinstance(response.data['results'], list))
        self.assertEqual(Supplier.objects.count(), len(response.data['results']))


class SupplierUpdateRetrieveTests(APITestCase):

    def setUp(self) -> None:
        self.supplier = Supplier.objects.create(
            email="test_client100@gmail.com",
            mobile_number="0801000000",
            name = "Test Client"
        )


    def test_put_supplier_details(self):
        """
        Ensure we can PUT update a supplier details.
        """
        url = reverse('retrieve-update-suppliers', kwargs={'pk': self.supplier.id})
        data = {
            "email": "test_client100@gmail.com",
            "mobile_number": "+2348087899098",
            "name":  "Test Client",
            "address": "24 Example Update Street",
            "other_contact_info": ""
            }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertDictContainsSubset(data, response.data)

    def test_patch_supplier_details(self):
        """
        Ensure we can PATCH update a supplier details.
        """
        url = reverse('retrieve-update-suppliers', kwargs={'pk': self.supplier.id})
        data = {
            "address": "24 Example Whatever Street",
            }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertEqual(data['address'], response.data['address'])

