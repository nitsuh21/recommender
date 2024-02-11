from django.core.management.base import BaseCommand, CommandParser
from recommendation_ai import utils
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=10)

    
    def handle(self, *args, **options):
        count = options.get('count')
        total = options.get('total')
        profiles = utils.get_fake_profiles(count=count)
        new_users = []
        for profile in profiles:
            new_users.append(User(**profile))
        User.objects.bulk_create(new_users,ignore_conflicts=True)
        if total:
            print(f"total: {User.objects.count()}")
