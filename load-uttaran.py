#!/usr/bin/env python3

import argparse
import os
import sys
from datetime import datetime, timezone

import django

sys.path.append('../cadasta')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")


def load_uttaran():
    """Load Uttaran data."""
    from organization.models import Organization, Project
    from party.models import Party, TenureRelationship, TenureRelationshipType
    from spatial.models import SpatialUnit

    org = Organization.objects.create(
        name='Uttaran', slug='uttaran',
        description="""We are Uttaran (Transition), a people centred NGO using a rights based approach to empower poor communities and reduce poverty. We work across the coastal region of southwest Bangladesh. We are gradually expanding our activities to other parts of the country. Our work is focused on human rights, land rights and agrarian reform, sustainable water management, community based river basin management, adaptation to climate change, sustainable agriculture and food security.""",
        urls=['http://www.uttaran.net/'],
        logo='https://s3.amazonaws.com/cadasta-dev-tmp/etl-test/uttaran.jpg',
        contacts=[]
    )

    proj = Project.objects.create(
        organization=org,
        name='Uttaran Testing',
        slug='uttaran-testing',
        description='Testing the Cadasta Platform',
        country='BD',
        extent=("""SRID=4326;POLYGON ((87.73681640625 20.220965779522313, 87.73681640625 26.725986812271756, 92.96630859375 26.725986812271756, 92.96630859375 20.220965779522313, 87.73681640625 20.220965779522313))""")
    )
    su1 = SpatialUnit.objects.create(
        geometry=('SRID=4326;POLYGON((89.874941 24.821238,89.874938 24.821246,89.874938 24.821254,89.874933 24.821278,89.874949 24.821401,89.87502 24.821403,89.875168 24.821378,89.875213 24.821256,89.875248 24.821136,89.875248 24.821125,89.875156 24.82105,89.874996 24.821021,89.874941 24.821238))'),
        project=proj,
        type='PA')
    su2 = SpatialUnit.objects.create(
        geometry=('SRID=4326;POINT(89.875126 24.820293)'),
        project=proj,
        type='PA')

    p1 = Party.objects.create(
        name="Akbar Mia",
        type="IN",
        project=proj
    )
    p2 = Party.objects.create(
        name="Abdul Satter",
        type="IN",
        project=proj
    )
    oc = TenureRelationshipType.objects.get(id='OC')
    tn = TenureRelationshipType.objects.get(id='TN')
    tr1 = TenureRelationship.objects.create(
        project=proj,
        party=p1,
        spatial_unit=su2,
        tenure_type=tn
    )
    tr2 = TenureRelationship.objects.create(
        project=proj,
        party=p2,
        spatial_unit=su1,
        tenure_type=oc
    )


def load_users():
    from organization.models import Organization, OrganizationRole
    from accounts.models import User

    users = [{'username': 'uttaranadmin',
              'full_name': 'Uttaran Admin', 'admin': True},
             {'username': 'mamun_rashid', 'full_name':
              'Mamun Ur Rashid', 'admin': True},
             {'username': 'sampa_bala', 'full_name':
              'Sampa Rani Bala', 'admin': False},
             {'username': 'jahidul_ahsan', 'full_name':
              'Jahidul Ahsan', 'admin': True},
             {'username': 'salim_swapan', 'full_name':
              'Shaikh Salim Akhter', 'admin': False},
             {'username': 'zaghani', 'full_name':
              'Zannat Ara Ghani', 'admin': True}]

    org = Organization.objects.get(slug='uttaran')

    for user in users:
        u = User.objects.create(
            username=user['username'],
            email='',
            full_name=user['full_name'],
            email_verified=True,
            last_login=datetime.now(tz=timezone.utc)
        )
        u.set_password('password')
        u.save()
        OrganizationRole.objects.create(
            organization=org, user=u, admin=user['admin']
        )


def drop_users():
    from organization.models import OrganizationRole
    from accounts.models import User
    users = ['uttaranadmin', 'mamun_rashid', 'sampa_bala',
             'jahidul_ahsan', 'salim_swapan', 'zaghani']
    for user in users:
        try:
            u = User.objects.get(username=user)
            o = OrganizationRole.objects.get(user=u)
            o.delete()
            u.delete()
        except:
            pass


def drop_uttaran():
    """Drop Uttaran data."""
    from organization.models import Organization
    drop_users()
    try:
        Organization.objects.get(slug='uttaran').delete()
    except:
        pass


if __name__ == '__main__':
    django.setup()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--delete", help='delete all data for this organization',
        action="store_true")
    args = parser.parse_args()
    if args.delete:
        drop_uttaran()
    else:
        drop_uttaran()
        load_uttaran()
        load_users()
