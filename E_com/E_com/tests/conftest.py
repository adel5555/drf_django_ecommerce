from factories import BrandFactory, CategoryFactory, ProductFactory
from pytest_factoryboy import register

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)
