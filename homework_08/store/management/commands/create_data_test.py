from django.core.management.base import BaseCommand
from store.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        category = Category.objects.create(
            name='Отечественная литература',
            description='Книги',
        )

        Product.objects.create(
            name='Война и мир (в 2-х книгах) (комплект)',
            description='Русская классика',
            price=1799.00,
            category=category,
        )


