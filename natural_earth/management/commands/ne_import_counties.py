import sys
import os
from natural_earth.models import County
from django.core.management.base import LabelCommand
from django.template import loader, Context
from haystack.constants import DEFAULT_OPERATOR
from django.contrib.gis.gdal import *
from django.contrib.gis.utils import LayerMapping


county_mapping = {
    'name' : 'NAME_0',
    'name_1': 'NAME_1',
    'varname_1' : 'VARNAME_1',
    'nl_name_1' : 'NL_NAME_1',
    'vertex_cou' : 'VertexCou',
    'hasc_1': 'HASC_1',
    'type_1':'TYPE_1',
    'engtype_1': 'ENGTYPE_1',
    'validfr_1': 'VALIDFR_1',
    'validto_1': 'VALIDTO_1',
    'remarks_1':'REMARKS_1',
    'region': 'Region',
    'region_var':'RegionVar',
    'region_cod': 'Region_Cod',
    'region_c_1': 'Region_C_1',
    'region_c_2': 'Region_C_2',
    'region_c_3': 'Region_C_3',
    'country_pr': 'Country_Pr',
    'scale_rank': 'ScaleRank',
    'check_me': 'CheckMe',
    'gadm_level': 'gadm_level',
    'fips_1': 'FIPS_1',
    'first_fips': 'FIRST_FIPS',
    'first_hasc': 'FIRST_HASC',
    'nev_countr': 'NEV_Countr',
    'prov_number': 'ProvNumber',
    'shape_leng': 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'mpoly' : 'MULTIPOLYGON',
}

class Command(LabelCommand):
    help = "Imports County vector Files into natural_earth.County"
    args = 'Path to the .shp file'
    label = 'shp_path'
    
    def handle_label(self, label, **options):
        world_shp = os.path.abspath(label)
        ds = DataSource(world_shp)
        print "Datasource has %s layers"%len(ds)
        layer = ds[0]
        print "Importing Layer %s of type %s, size: %s"\
                                            %(layer,layer.geom_type,len(layer))
        

        lm = LayerMapping(County, world_shp, county_mapping,
                      transform=False, encoding='iso-8859-1')

        lm.save(strict=True, verbose=True)
        print "Successfully stored Counties"
        


        

