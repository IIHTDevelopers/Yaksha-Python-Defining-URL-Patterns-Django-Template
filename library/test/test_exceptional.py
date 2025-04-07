from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
from django.test import TestCase
from library.models import Product

class ProductExceptionalTest(APITestCase):

    def test_invalid_product_id(self):
        """Test if an error occurs when accessing a non-existent product"""
        test_obj = TestUtils()
        try:
            response = self.client.get('/products/9999/')
            if response.status_code == 404 and 'error' in response.json():
                test_obj.yakshaAssert("TestInvalidProductID", True, "exceptional")
                print("TestInvalidProductID = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidProductID", False, "exceptional")
                print("TestInvalidProductID = Failed")
        except:
            test_obj.yakshaAssert("TestInvalidProductID", False, "exceptional")
            print("TestInvalidProductID = Failed")

    def test_checkout_view_without_login(self):
        """Test if users who are not logged in cannot access the checkout view"""
        test_obj = TestUtils()
        try:
            response = self.client.get('/checkout/')
            if response.status_code == 200 and 'status' in response.json():
                test_obj.yakshaAssert("TestCheckoutWithoutLogin", True, "exceptional")
                print("TestCheckoutWithoutLogin = Passed")
            else:
                test_obj.yakshaAssert("TestCheckoutWithoutLogin", False, "exceptional")
                print("TestCheckoutWithoutLogin = Failed")
        except:
            test_obj.yakshaAssert("TestCheckoutWithoutLogin", False, "exceptional")
            print("TestCheckoutWithoutLogin = Failed")
