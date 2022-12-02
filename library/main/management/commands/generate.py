import random
from faker import Faker
from django.core.management.base import BaseCommand, CommandError
from main.models import Book


class Command(BaseCommand):
    help = 'Create fake books'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Qty books for add')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            fake = Faker()
            a = fake.name()
            ttl = fake.sentences(1)[0]
            txt = ' '.join(fake .sentences(3))
            pub = fake.year()
            c = random.randint(1, 20)
            try:
                print (ttl)
                Book.objects.create(
                    title=ttl,
                    author=a,
                    text=txt,
                    published='2022-01-01 00:00:00',
                    count=c
                )
            except Exception as err :
                raise CommandError(f'Error of creating: {err}')
            else:
                print(f'{i+1} books added')