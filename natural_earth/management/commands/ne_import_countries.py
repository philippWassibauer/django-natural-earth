import sys
import os
from natural_earth.models import Country
from django.core.management.base import LabelCommand
from django.template import loader, Context
from haystack.constants import DEFAULT_OPERATOR
from django.contrib.gis.gdal import *
from django.contrib.gis.utils import LayerMapping


country_mapping = {
    'name' : 'COUNTRY',
    'featurecla' : 'FEATURECLA',
    'sov' : 'SOV',
    'shape_leng' : 'SHAPE_LENG',
    'shape_area' : 'SHAPE_AREA',
    'mpoly' : 'MULTIPOLYGON',
}


class Command(LabelCommand):
    help = "Imports Country vector Files into natural_earth.Country"
    args = 'Path to the .shp file'
    label = 'shp_path'
    
    def handle_label(self, label, **options):
        world_shp = os.path.abspath(label)
        ds = DataSource(world_shp)
        print "Datasource has %s layers"%len(ds)
        layer = ds[0]
        print "Importing Layer %s of type %s, size: %s"\
                                            %(layer,layer.geom_type,len(layer))
        
        lm = LayerMapping(Country, world_shp, country_mapping,
                      transform=False, encoding='iso-8859-1')

        lm.save(strict=True, verbose=True)
        print "Successfully stored Countries"

        

