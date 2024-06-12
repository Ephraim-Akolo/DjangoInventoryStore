from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Inventory
from suppliers.models import Supplier

class InventoryCreateTests(APITestCase):

    def setUp(self) -> None:
        self.supplier = Supplier.objects.create(
            email="test_client100@gmail.com",
            mobile_number="0801000000",
            name = "Test Client"
        )

    def test_create_inventory_item(self):
        """
        Ensure we can create a new inventory item.
        """
        url = reverse('list-create-inventory')
        data = {
            'name': 'Test Client Item',
            'description': 'Testing Client create inventory item',
            'price': '1000.00',
            'supplier_ids': [self.supplier.id.hex]
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Inventory.objects.count(), 1)
        self.assertTrue('id' in response.data)
        self.assertDictContainsSubset({k:v for k, v in data.items() if k != 'supplier_ids'}, response.data)
        self.assertEqual(response.data['name'], data['name'])


class InventoryListTests(APITestCase):

    def setUp(self) -> None:
        self.supplier = Supplier.objects.create(
            email="test_client100@gmail.com",
            mobile_number="0801000000",
            name = "Test Client"
        )
        self.item = Inventory.objects.create(
            name = 'Test Client Item',
            description = 'Testing Client list inventory item',
            price = '1000.00'
        )
        self.item.suppliers.set([self.supplier])


    def test_list_inventory_items(self):
        """
        Ensure we can query all inventory items.
        """
        url = reverse('list-create-inventory')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)
        self.assertTrue(isinstance(response.data['results'], list))
        self.assertEqual(Inventory.objects.count(), len(response.data['results']))


class InventoryUpdateRetrieveTests(APITestCase):

    def setUp(self) -> None:
        self.supplier = Supplier.objects.create(
            email="test_client100@gmail.com",
            mobile_number="0801000000",
            name = "Test Client"
        )
        self.supplier2 = Supplier.objects.create(
            email="test_client200@gmail.com",
            mobile_number="+234802000000",
            name = "Test Client 2"
        )
        self.item = Inventory.objects.create(
            name = 'Test Client Item',
            description = 'Testing Client list inventory item',
            price = '1000.00'
        )
        self.item.suppliers.set([self.supplier])


    def test_put_inventory_item(self):
        """
        Ensure we can PUT update an inventory item.
        """
        url = reverse('retrieve-update-inventory', kwargs={'pk': self.item.id})
        data = {
            'name': 'Tested Item 1',
            'description': 'Testing Client create inventory item',
            'price': '2000.00',
            'supplier_ids': [self.supplier.id.hex, self.supplier2.id.hex]
            }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Inventory.objects.count(), 1)
        self.assertEqual(len(response.data['suppliers']), 2)
        self.assertDictContainsSubset({k:v for k, v in data.items() if k != 'supplier_ids'}, response.data)

    def test_patch_inventory_item(self):
        """
        Ensure we can PATCH update an inventory item.
        """
        url = reverse('retrieve-update-inventory', kwargs={'pk': self.item.id})
        data = {
            'price': '2000.00',
            'supplier_ids': [self.supplier.id.hex, self.supplier2.id.hex]
            }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Inventory.objects.count(), 1)
        self.assertEqual(len(response.data['suppliers']), 2)
        self.assertEqual(response.data['price'], data['price'])
        self.assertEqual(response.data['name'], self.item.name)


class InventoryDeleteTests(APITestCase):

    def setUp(self) -> None:
        self.supplier = Supplier.objects.create(
            email="test_client100@gmail.com",
            mobile_number="0801000000",
            name = "Test Client"
        )
        self.item = Inventory.objects.create(
            name = 'Test Client Item',
            description = 'Testing Client list inventory item',
            price = '1000.00'
        )
        self.item.suppliers.set([self.supplier])


    def test_delete_inventory_item(self):
        """
        Ensure we can delete an inventory item.
        """
        url = reverse('retrieve-update-inventory', kwargs={'pk': self.item.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Inventory.objects.count(), 0)