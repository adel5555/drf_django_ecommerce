import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModels:

    def test_str_method(self, category_factory):
        # Arrange

        # Act
        category = category_factory()

        # Assert
        assert category.__str__() == "test_category"

        pass


class TestBrandModels:
    def test_str_method(self, brand_factory):
        # Act
        brand = brand_factory()

        # Assert
        assert brand.__str__() == "test_brand"


class TestProductModels:
    def test_str_method(self, product_factory):
        # Act
        product = product_factory()

        # Assert
        assert product.__str__() == "test_product"

        pass
