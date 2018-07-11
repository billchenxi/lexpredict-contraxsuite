"""
    Copyright (C) 2017, ContraxSuite, LLC

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    You can also be released from the requirements of the license by purchasing
    a commercial license from ContraxSuite, LLC. Buying such a license is
    mandatory as soon as you develop commercial activities involving ContraxSuite
    software without disclosing the source code of your own applications.  These
    activities include: offering paid services to customers as an ASP or "cloud"
    provider, processing documents on the fly in a web application,
    or shipping ContraxSuite within a closed source product.
"""
from django.core.management import BaseCommand

from allauth.account.models import EmailAddress
from apps.users.models import User

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2018, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-contraxsuite/blob/1.1.1b/LICENSE"
__version__ = "1.1.1b"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class Command(BaseCommand):
    help = "Create superuser --username USER --password PWD --email it@email.com"

    def add_arguments(self, parser):
        parser.add_argument('--username',
                            help='Username')

        parser.add_argument('--password',
                            help='Password')

        parser.add_argument('--email',
                            help='Email')

    def handle(self, *args, **options):
        user, created = User.objects.update_or_create(
            username=options['username'],
            is_superuser=True,
            is_staff=True,
            defaults=dict(
                email=options['email'],
                role_id=1,
                is_active=True))
        user.set_password(options['password'])
        user.save()

        if created:
            EmailAddress.objects.create(
                user=user,
                email=user.email,
                verified=True,
                primary=True)
