from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from ..models import Published
from ..models import with_outbox

User = get_user_model()


class WithOutBoxTestCase(TestCase):

    def test_when_is_correct_queue_name(self):
        queue_name = 'queue'
        user_with_outbox = with_outbox(name=queue_name)(User)
        user_with_outbox.objects.create(username='test')
        self.assertEqual(Published.objects.get().name, f"{queue_name}.v1")

    def test_when_no_has_specified_field(self):
        date_joined = timezone.now()
        fields_expected = {
            'email': '',
            'groups': [],
            'is_staff': False,
            'password': '',
            'username': 'test',
            'is_active': True,
            'last_name': '',
            'first_name': '',
            'last_login': None,
            'date_joined': date_joined.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
            'is_superuser': False,
            'user_permissions': []
        }

        use_with_outbox = with_outbox(name='queue')(User)
        use_with_outbox.objects.create(username='test', date_joined=date_joined)
        fields = Published.objects.get().content['fields']
        self.assertEqual(fields, fields_expected)

    def test_when_has_specified_fields(self):
        fields_expected = {
            'email': 'test@test.com',
            'username': 'test',

        }
        use_with_outbox = with_outbox(name='queue', fields=['email', 'username'])(User)
        use_with_outbox.objects.create(username='test', email='test@test.com')
        fields = Published.objects.get().content['fields']
        self.assertEqual(fields, fields_expected)
