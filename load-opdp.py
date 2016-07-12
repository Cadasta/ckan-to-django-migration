#!/usr/bin/env python3

import argparse
import os
import sys

import django

sys.path.append('../cadasta-platform/cadasta')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")


def load_opdp():
    """Load OPDP data."""
    from organization.models import Organization, Project
    from party.models import Party, TenureRelationship, TenureRelationshipType
    from spatial.models import SpatialUnit

    org = Organization.objects.create(
        name='OPDP', slug='opdp',
        description='',
        urls=[''],
        logo='https://s3.amazonaws.com/cadasta-dev-tmp/etl-test/opdp.jpg',
        contacts=[]
    )
    proj1 = Project.objects.create(
        organization=org,
        name='Community Mapping',
        slug='community-mapping',
        description="""Community mapping of natural resources and physical features.""",
        country='KE',
        extent=("""SRID=4326;POLYGON ((33.7939453125 -5.00339434502215, 33.7939453125 5.003394345022162, 41.87988281249999 5.003394345022162, 41.87988281249999 -5.00339434502215, 33.7939453125 -5.00339434502215))""")
    )
    su1 = SpatialUnit.objects.create(
        name='',
        geometry=("""SRID=4326;POLYGON((35.5478096008301 0.0873112340607699,35.5483245849609 0.0850796386858006,35.5521011352539 0.0845646551192806,35.555362701416 0.0842213327378052,35.559139251709 0.0850796386858006,35.562744140625 0.0849079774977155,35.5660057067871 0.0852512998731224,35.5673789978027 0.086452928162811,35.5660057067871 0.0876545564144855,35.5639457702637 0.0883412011124513,35.562572479248 0.0893711681355713,35.559139251709 0.0928043913355374,35.5569076538086 0.0929760524868935,35.5543327331543 0.0924610690303317,35.5527877807617 0.0922894078764947,35.5510711669922 0.0898861516363302,35.5478096008301 0.0873112340607699))"""),
        project=proj1,
        type='PA')

    p1 = Party.objects.create(
        name="Koibatek",
        type="GR",
        project=proj1
    )

    proj2 = Project.objects.create(
        organization=org,
        name='Mapping Infrastructure Sasimwani',
        slug='mapping-infrastructure-sasimwani',
        description="""Mapping of man-made features found in the community, e.g., roads, schools, churches etc.""",
        country='KE',
        extent=('SRID=4326;'
                """POLYGON ((34.9200439453125 -1.2138984340943106, 34.9200439453125 0.05493163220967156, 36.6339111328125 0.05493163220967156, 36.6339111328125 -1.2138984340943106, 34.9200439453125 -1.2138984340943106))""")
    )

    su1 = SpatialUnit.objects.create(
        name='',
        geometry=("""SRID=4326;POINT(35.8236694335938 -0.748422319076921)"""),
        project=proj2,
        type='PA')

    su2 = SpatialUnit.objects.create(
        name='',
        geometry=("""SRID=4326;LINESTRING(35.848388671875 -0.777730899383458,35.8514785766602 -0.76914861255639,35.8531951904297 -0.759879723404385,35.8538818359375 -0.752670573635443,35.8645248413086 -0.732759527000417,35.8641815185547 -0.7221173794242,35.8617782592773 -0.712161799452128,35.859375 -0.705982463117918,35.8600616455078 -0.699803118571605,35.8624649047852 -0.695340253554815,35.8617782592773 -0.689504192940443,35.8604049682617 -0.682981528496451,35.8604049682617 -0.675085659702511,35.8600616455078 -0.667533077552432)"""),
        project=proj2,
        type='RW')

    p1 = Party.objects.create(
        name="Sasimwani",
        type="GR",
        project=proj2
    )

    proj3 = Project.objects.create(
        organization=org,
        name='Mapping Natural Resource Rights',
        slug='mapping-natural-resource-rights',
        description="""Mapping forests, water sources, stones, grazing areas, pasture, gathering areas, boundaries, landmarks.""",
        country='KE',
        extent=("""SRID=4326;POLYGON ((35.4638671875 -0.46966026762837204, 35.4638671875 0.12084951976866681, 36.1724853515625 0.12084951976866681, 36.1724853515625 -0.46966026762837204, 35.4638671875 -0.46966026762837204))""")
    )

    su1 = SpatialUnit.objects.create(
        name='',
        geometry=("""SRID=4326;POLYGON((35.8353424072266 -0.372631307105529,35.8463287353516 -0.370571413906517,35.8573150634766 -0.364391731446192,35.8628082275391 -0.36267515222965,35.877571105957 -0.357525412632875,35.8871841430664 -0.352375670147851,35.8930206298828 -0.345852658918886,35.8889007568359 -0.333836573929815,35.8858108520508 -0.324223695341298,35.8731079101562 -0.323880378078442,35.8617782592773 -0.323537060803958,35.8477020263672 -0.325253647059945,35.841178894043 -0.321820474257548,35.8329391479492 -0.317014030395739,35.8205795288086 -0.316670712891275,35.8137130737305 -0.313924172447233,35.8119964599609 -0.325596964276162,35.8353424072266 -0.372631307105529))"""),
        project=proj3,
        type='CB')

    su2 = SpatialUnit.objects.create(
        name='',
        geometry=("""SRID=4326;LINESTRING(35.8246994018555 -0.378998734327517,35.826416015625 -0.370072533450234,35.830192565918 -0.356683215360425,35.8315658569336 -0.346727043087433,35.8353424072266 -0.33265105759747,35.8370590209961 -0.326471350258376,35.8428955078125 -0.319261686901058,35.8518218994141 -0.314111924258455,35.8583450317383 -0.301752483642104,35.8607482910156 -0.291452939044748,35.8597183227539 -0.280810066403804,35.8610916137695 -0.282183340845174)"""),
        project=proj3,
        type='RW')

    p1 = Party.objects.create(
        name="Ogiek community of Ngongongeri",
        type="GR",
        project=proj3
    )
    cu = TenureRelationshipType.objects.get(id='CU')
    TenureRelationship.objects.create(
        project=proj3,
        party=p1,
        spatial_unit=su2,
        tenure_type=cu
    )


def drop_opdp():
    """Drop OPDP data."""
    from organization.models import Organization, Project
    from spatial.models import SpatialUnit
    from party.models import Party, TenureRelationship
    for org in Organization.objects.filter(name__contains='OPDP'):
        for proj in Project.objects.filter(organization=org):
            for s in SpatialUnit.objects.filter(project=proj):
                s.delete()
            for p in Party.objects.filter(project=proj):
                p.delete()
            for t in TenureRelationship.objects.filter(project=proj):
                t.delete()
            proj.delete()
        org.delete()


if __name__ == '__main__':
    django.setup()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--delete", help='delete all data for this organization',
        action="store_true")
    args = parser.parse_args()
    if args.delete:
        drop_opdp()
    else:
        drop_opdp()
        load_opdp()
