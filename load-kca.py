#!/usr/bin/env python3

import argparse
import os
import sys
from datetime import datetime, timezone

import django

sys.path.append('../cadasta')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")


def load_kca():
    """Load Kivulini data."""
    from organization.models import Organization, OrganizationRole, Project
    from party.models import Party, TenureRelationship, TenureRelationshipType
    from party.models import TenureRelationshipType
    from spatial.models import SpatialUnit
    from accounts.models import User

    user = User.objects.create(
        username='kcaadmin',
        email='info@kca.domain',
        full_name='KCA Admin',
        email_verified=True,
        last_login=datetime.now(tz=timezone.utc))

    user.set_password('password')
    user.save()

    org = Organization.objects.create(
        name='KCA', slug='kca',
        description='',
        urls=[''],
        logo='https://s3.amazonaws.com/cadasta-dev-tmp/etl-test/kca.png',
        contacts=[]
    )

    OrganizationRole.objects.create(
        organization=org, user=user, admin=True
    )

    proj = Project.objects.create(
        organization=org,
        name='KCA Pilot Training',
        slug='kca-pilot-training',
        description="""As part of the World Bank Real Estate and Cadastre Project, the KCA is testing various approaches for documenting property rights in Krusha e Madhe. This includes using drone imagery, mobile devices for data collection in the field, and the use of tools such as FieldPapers. This project for the KCA will be for testing the data collection devices.""",
        country='KV',
        extent=('SRID=4326;'
                """POLYGON ((19.973144531249996 41.832735062152615, 19.973144531249996 43.265206318396025, 21.8902587890625 43.265206318396025, 21.8902587890625 41.832735062152615, 19.973144531249996 41.832735062152615))""")
    )
    su1 = SpatialUnit.objects.create(
        geometry=('SRID=4326;POINT(20.631539 42.32537)'),
        project=proj,
        type='BU')
    su2 = SpatialUnit.objects.create(
        geometry=('SRID=4326;POINT(20.636637 42.320297)'),
        project=proj,
        type='PA')
    su3 = SpatialUnit.objects.create(
        geometry=('SRID=4326;POINT(20.636772 42.320147)'),
        project=proj,
        type='PA')
    su4 = SpatialUnit.objects.create(
        geometry=('SRID=4326;POINT(21.16524 42.661555)'),
        project=proj,
        type='PA')

    p1 = Party.objects.create(
        name="Rexhep Dellova",
        type="IN",
        project=proj
    )
    p2 = Party.objects.create(
        name="Nexhmedin Dellova",
        type="IN",
        project=proj
    )
    p3 = Party.objects.create(
        name="Shtepia muze e Ukshin Hotit",
        type="IN",
        project=proj
    )
    jt = TenureRelationshipType.objects.get(id='JT')
    tc = TenureRelationshipType.objects.get(id='TC')
    es = TenureRelationshipType.objects.get(id='ES')
    tr1 = TenureRelationship.objects.create(
        project=proj,
        party=p1,
        spatial_unit=su3,
        tenure_type=tc
    )
    tr2 = TenureRelationship.objects.create(
        project=proj,
        party=p2,
        spatial_unit=su2,
        tenure_type=tc
    )
    tr3 = TenureRelationship.objects.create(
        project=proj,
        party=p3,
        spatial_unit=su1,
        tenure_type=jt
    )


def drop_kca():
    from organization.models import Organization
    from accounts.models import User
    try:
        Organization.objects.get(slug='kca').delete()
    except:
        pass
    try:
        User.objects.get(username='kcaadmin').delete()
    except:
        pass


if __name__ == '__main__':
    django.setup()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--delete", help='Delete all data for this organization', action="store_true")
    args = parser.parse_args()
    if args.delete:
        drop_kca()
    else:
        drop_kca()
        load_kca()
