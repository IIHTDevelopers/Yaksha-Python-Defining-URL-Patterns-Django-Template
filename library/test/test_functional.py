from django.test import TestCase
from django.urls import reverse
from library.test.TestUtils import TestUtils
from library.models import Product
from rest_framework.test import APITestCase


class ProductFunctionalTest(APITestCase):

    def test_product_list_view(self):
        """Test if the product list view returns a 200 status code"""
        test_obj = TestUtils()
        try:
            response = self.client.get('/products/')
            if response.status_code == 200 and 'products' in response.json():
                test_obj.yakshaAssert("TestProductListView", True, "functional")
                print("TestProductListView = Passed")
            else:
                test_obj.yakshaAssert("TestProductListView", False, "functional")
                print("TestProductListView = Failed")
        except:
            test_obj.yakshaAssert("TestProductListView", False, "functional")
            print("TestProductListView = Failed")

    def test_product_detail_view(self):
        """Test if the product detail view works correctly"""
        test_obj = TestUtils()
        Product.objects.create(
            name="prd1",
            price=10.9
        )
        try:
            response = self.client.get('/products/1/')
            if response.status_code == 200 and 'product' in response.json():
                test_obj.yakshaAssert("TestProductDetailView", True, "functional")
                print("TestProductDetailView = Passed")
            else:
                test_obj.yakshaAssert("TestProductDetailView", False, "functional")
                print("TestProductDetailView = Failed")
        except:
            test_obj.yakshaAssert("TestProductDetailView", False, "functional")
            print("TestProductDetailView = Failed")

    def test_checkout_view(self):
        """Test if the checkout view is accessible"""
        test_obj = TestUtils()
        try:
            response = self.client.get('/checkout/')
            if response.status_code == 200 and 'message' in response.json():
                test_obj.yakshaAssert("TestCheckoutView", True, "functional")
                print("TestCheckoutView = Passed")
            else:
                test_obj.yakshaAssert("TestCheckoutView", False, "functional")
                print("TestCheckoutView = Failed")
        except:
            test_obj.yakshaAssert("TestCheckoutView", False, "functional")
            print("TestCheckoutView = Failed")
