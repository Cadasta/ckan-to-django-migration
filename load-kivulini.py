#!/usr/bin/env python3

import argparse
import os
import sys
from datetime import datetime, timezone

import django

sys.path.append('../cadasta')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")


def load_kivulini():
    """Load Kivulini data."""
    from organization.models import Organization, OrganizationRole, Project
    from party.models import Party, TenureRelationship, TenureRelationshipType
    from spatial.models import SpatialUnit
    from accounts.models import User

    user = User.objects.create(
        username='kivuliniadmin',
        email='info@kivulini.domain',
        full_name='Kivulini Admin',
        email_verified=True,
        last_login=datetime.now(tz=timezone.utc))

    user.set_password('password')
    user.save()

    org = Organization.objects.create(
        name='Kivulini Trust', slug='kivulini-trust',
        description="""Kivulini Trust is registered under the Trustees Act, Laws of Kenya as a non-profit, non-political institution that exists to reconnect pastoralist and other minority groups of Northern Kenya.""",
        urls=['http://www.kivulinitrust.org'],
        logo='https://s3.amazonaws.com/cadasta-dev-tmp/etl-test/kivulini-trust.jpg',
        contacts=[{'email': 'info@kivulinitrust.org'}]
    )

    OrganizationRole.objects.create(
        organization=org, user=user, admin=True
    )

    proj = Project.objects.create(
        organization=org,
        name='Kivulini Trust Training',
        slug='kivulini-trust-training',
        description='Test project for Kivulini Trust',
        country='KE',
        extent=('SRID=4326;'
                """POLYGON ((35.66162109375 4.7406753847783865, 35.74951171875 2.986927393334876, 36.1669921875 2.218683588558448, 35.57373046875 -0.39550467153200675, 35.859375 -1.537901237431487, 38.43017578124999 -2.2406396093827206, 39.61669921875 -1.4061088354351468, 40.27587890625 1.0765967983064109, 40.27587890625 2.855262784366583, 40.10009765625 4.105369348495178, 38.935546875 3.8642546157214213, 37.77099609375 4.12728532324537, 37.0458984375 4.58737615344969, 36.27685546875 4.762572524280281, 35.66162109375 4.7406753847783865))""")
    )
    su1 = SpatialUnit.objects.create(
        geometry=('SRID=4326;POINT(38.4686279296875 0.576343353297523)'),
        project=proj,
        type='BU')
    su2 = SpatialUnit.objects.create(
        geometry=('SRID=4326;POINT(38.265380859375 0.658736021228777)'),
        project=proj,
        type='PA')
    su3 = SpatialUnit.objects.create(
        geometry=('SRID=4326;POINT(38.0374145507812 0.650422428328886)'),
        project=proj,
        type='PA')

    p1 = Party.objects.create(
        name="El dera community",
        type="GR",
        project=proj
    )
    gr = TenureRelationshipType.objects.get(id='GR')
    cu = TenureRelationshipType.objects.get(id='CU')
    tr1 = TenureRelationship.objects.create(
        project=proj,
        party=p1,
        spatial_unit=su3,
        tenure_type=gr
    )
    tr2 = TenureRelationship.objects.create(
        project=proj,
        party=p1,
        spatial_unit=su2,
        tenure_type=cu
    )


def drop_kivulini():
    from organization.models import Organization
    from accounts.models import User
    try:
        Organization.objects.get(slug='kivulini-trust').delete()
    except:
        pass
    try:
        User.objects.get(username='kivuliniadmin').delete()
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
        drop_kivulini()
    else:
        drop_kivulini()
        load_kivulini()
