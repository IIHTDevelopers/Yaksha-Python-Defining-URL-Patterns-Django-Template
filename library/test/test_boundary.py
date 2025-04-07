from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from django.urls import reverse
from django.test import TestCase


class ProductBoundaryTest(APITestCase):

    def test_boundary_product_listing(self):
        """Test if the product listing is paginated correctly"""
        test_obj = TestUtils()
        try:
            response = self.client.get('/products/?page=1')
            if response.status_code == 200 and 'products' in response.json():
                test_obj.yakshaAssert("TestBoundaryProductListing", True, "boundary")
                print("TestBoundaryProductListing = Passed")
            else:
                test_obj.yakshaAssert("TestBoundaryProductListing", False, "boundary")
                print("TestBoundaryProductListing = Failed")
        except:
            test_obj.yakshaAssert("TestBoundaryProductListing", False, "boundary")
            print("TestBoundaryProductListing = Failed")
