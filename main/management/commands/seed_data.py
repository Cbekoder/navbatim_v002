from django.core.management.base import BaseCommand
from main.models import Category, Service


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **options):
        # Create categories
        categories = [
            {'name': 'BEAUTY', 'icon': '💄'},
            {'name': 'RESTAURANTS', 'icon': '🍴'},
            {'name': 'SERVICES', 'icon': '💼'},
            {'name': 'EDUCATION', 'icon': '🎓'},
            {'name': 'STYLE', 'icon': '💬'},
            {'name': 'RENT', 'icon': '🏠'},
            {'name': 'MORE', 'icon': '•••'},
        ]

        for cat_data in categories:
            Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'icon': cat_data['icon']}
            )

        beauty_category = Category.objects.get(name='BEAUTY')

        # Create services
        services = [
            {
                'name': 'Barbanera',
                'address': 'Массив Кашгар 30',
                'rating': 5.0,
                'reviews_count': 22,
                'category': beauty_category,
            },
            {
                'name': 'Женское Царство',
                'address': 'Фаргона Йули 222/7',
                'rating': 5.0,
                'reviews_count': 333,
                'is_award_winner': True,
                'award_year': '24',
                'category': beauty_category,
            },
            {
                'name': 'Наташа',
                'address': 'Боттепа 13, 2 этаж',
                'rating': 5.0,
                'reviews_count': 1,
                'is_company': False,
                'category': beauty_category,
            },
            {
                'name': 'EYEDEPTH',
                'address': 'Ниёзбек Йули, 7',
                'rating': 5.0,
                'reviews_count': 1,
                'category': beauty_category,
            },
            {
                'name': 'Beauty Dolce Salon',
                'address': 'проспект Мирзо Улугбека 52',
                'category': beauty_category,
            },
            {
                'name': 'The Stories',
                'address': 'Фаргана Йули 222/12',
                'category': beauty_category,
            },
        ]

        for service_data in services:
            Service.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))