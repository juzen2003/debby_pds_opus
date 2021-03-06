# opus/application/search/test_db_integrity.py

from unittest import TestCase

from django.apps import apps
from django.db import connection
from django.db.models import Count
from django.http import QueryDict

from search.views import *
from tools.db_utils import MYSQL_TABLE_NOT_EXISTS

class DBIntegrityTest(TestCase):

    #############################################
    ######### DATABASE INTEGRITY CHECKS #########
    #############################################

    def test__pds_image_wl_volume_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_pds, obs_type_image, obs_wavelength
           Test that the observation count per volume is the same in
           obs_general, obs_pds, obs_type_image, and obs_wavelength, since
           these tables should all include the exact same set of observations.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        pds = (ObsPds.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        self.assertEqual(list(obs), list(pds))
        img = (ObsTypeImage.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        self.assertEqual(list(obs), list(img))
        wl = (ObsWavelength.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        self.assertEqual(list(obs), list(wl))

    def test__cassini_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_mission_cassini
           Test that the observation count per volume is the same in
           obs_general for mission_id='CO' and obs_mission_cassini.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(mission_id='CO')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsMissionCassini.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__galileo_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_mission_galileo
           Test that the observation count per volume is the same in
           obs_general for mission_id='GO' and obs_mission_galileo.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(mission_id='GO')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsMissionGalileo.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__hubble_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_mission_hubble
           Test that the observation count per volume is the same in
           obs_general for mission_id='HST' and obs_mission_hubble.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(mission_id='HST')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsMissionHubble.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__nh_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_mission_new_horizons
           Test that the observation count per volume is the same in
           obs_general for mission_id='NH' and obs_mission_newhorizons.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(mission_id='NH')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsMissionNewHorizons.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__voyager_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_mission_voyager
           Test that the observation count per volume is the same in
           obs_general for mission_id='VG' and obs_mission_voyager.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(mission_id='VG')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsMissionVoyager.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
           self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__COCIRS_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_instrument_cocirs
           Test that the observation count per volume is the same in
           obs_general for instrument_id='COCIRS' and obs_instrument_cocirs.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(instrument_id='COCIRS')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsInstrumentCocirs.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__COISS_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_instrument_coiss
           Test that the observation count per volume is the same in
           obs_general for instrument_id='COISS' and obs_instrument_coiss.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(instrument_id='COISS')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsInstrumentCoiss.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__COUVIS_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_instrument_couvis
           Test that the observation count per volume is the same in
           obs_general for instrument_id='COUVIS' and obs_instrument_couvis.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(instrument_id='COUVIS')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsInstrumentCouvis.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__COVIMS_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_instrument_covims
           Test that the observation count per volume is the same in
           obs_general for instrument_id='COVIMS' and obs_instrument_covims.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(instrument_id='COVIMS')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsInstrumentCovims.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__GOSSI_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_instrument_gossi
           Test that the observation count per volume is the same in
           obs_general for instrument_id='GOSSI' and obs_instrument_gossi.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(instrument_id='GOSSI')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsInstrumentGossi.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__nhlorri_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_instrument_nhlorri
           Test that the observation count per volume is the same in
           obs_general for instrument_id='NHLORRI' and obs_instrument_nhlorri.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(instrument_id='NHLORRI')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsInstrumentNhlorri.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__nhmvic_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_instrument_nhmvic
           Test that the observation count per volume is the same in
           obs_general for instrument_id='NHMVIC' and obs_instrument_nhmvic.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(instrument_id='NHMVIC')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsInstrumentNhmvic.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__vgiss_counts_match_obs_general(self):
        """DB Integrity: volumes in obs_general = obs_instrument_vgiss
           Test that the observation count per volume is the same in
           obs_general for instrument_id='VGISS' and obs_instrument_vgiss.
        """
        obs = (ObsGeneral.objects.values_list('volume_id')
               .filter(instrument_id='VGISS')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        ref = (ObsInstrumentVgiss.objects.values_list('volume_id')
               .annotate(Count('volume_id'))
               .order_by('volume_id'))
        try:
            self.assertEqual(list(obs), list(ref))
        except Exception as e:
            if e.args[0] != MYSQL_TABLE_NOT_EXISTS:
                raise

    def test__mult_field_matches_id_fields_in_mult_tables(self):
        """DB Integrity: intended target name mults exist
           Check the obs_general target_name mult to make sure there are no
           references to an id in the mult table that don't have entries.
        """
        cursor = connection.cursor()
        q = """SELECT COUNT(*) FROM obs_general
               WHERE mult_obs_general_target_name NOT IN
                   (SELECT id FROM mult_obs_general_target_name)"""
        cursor.execute(q)
        result = cursor.fetchone()
        cursor.close()
        self.assertEqual(result[0], 0)

    def test__all_sfc_geo_models_should_have_same_fields_as_each_other(self):
        """DB Integrity: all surface geometry tables have same fields
           Find all surface geo models by inspecting the param_info table and
           check that they each have the same parameters defined in the
           Django models.
        """
        # Mimas sets the standard template
        expected_fields = sorted([n for n in ObsSurfaceGeometryMimas.__dict__])
        param_info = (ParamInfo.objects
                      .filter(category_name__contains='surface_geometry__'))
        all_category_names = sorted(list(set([p.category_name
                                              for p in param_info])))
        for cat_name in all_category_names:
            model_name = cat_name.title().replace('_','')
            print(f'Working on {model_name}')
            model = apps.get_model('search', model_name)
            fields = sorted([n for n in model.__dict__])
            print(f'Found {len(fields)} fields expected {len(expected_fields)}')
            self.assertEqual(expected_fields, fields)

    def test__partables_has_all_surface_geo_tables(self):
        """DB Integrity: partables table has an entry for each surface_geo table
           XXX NOTE: We exclude Callirrhoe and Elara from this comparison
           because of GitHub issue #465 "Missing surface geo for Callirrhoe
           and Elara in NHJULO_2001". This causes a surface_geo table to be
           created during the import of NHJULO_1001, and then have no actual
           contents when NHJULO_1001 is replaced by NHJULO_2001.
        """
        count_partables = (Partables.objects
                           .filter(partable__contains='surface_geometry__')
                           .exclude(partable__contains='callirrhoe')
                           .exclude(partable__contains='elara')
                           .values('partable').distinct().count())
        count_surface_geo = (ObsSurfaceGeometry.objects
                             .values('target_name').distinct().count())
        self.assertEqual(count_partables, count_surface_geo)

    def test__tablenames_has_all_surface_geo_tables(self):
        """DB Integrity: table_names table has an entry for each surface_geo table
        """
        count_partables = (Partables.objects
                           .filter(partable__contains='surface_geometry__')
                           .values('partable').distinct().count())
        count_tablenames = (TableNames.objects
                            .filter(table_name__contains='surface_geometry__')
                            .values('table_name').distinct().count())
        self.assertEqual(count_partables, count_tablenames)

    def test__planets_properly_ordered(self):
        "DB Integrity: planets are properly ordered in the planet mult table"
        the_planets = [planet['label']
                       for planet in MultObsGeneralPlanetId.objects
                                        .filter(display='Y').values('label')]
        print('SELECT label FROM mult_obs_general_planet_id WHERE display = "Y" ORDER BY disp_order;')
        expect = ['Venus','Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
                  'Neptune', 'Pluto', 'Other']
        self.assertEqual(expect, the_planets)

    def test__surface_geometry_table_label_is_correct(self):
        "DB Integrity: label of the obs_surface_geometry table in table_names"
        label = TableNames.objects.get(table_name='obs_surface_geometry').label
        self.assertEqual(label, 'Surface Geometry Constraints')
