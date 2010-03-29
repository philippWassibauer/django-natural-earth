import sys
import os
from natural_earth.models import Country
from django.core.management.base import LabelCommand
from django.template import loader, Context
from django.contrib.gis.gdal import *
from django.contrib.gis.utils import LayerMapping

country_mapping = {
    'mpoly' : 'Geometry',
    'scalerank':'ScaleRank',
    'featurecla':'FeatureCla',
    'sovereignt':'SOVEREIGNT',
    'soviso':'SOVISO',
    'sov_a3':'SOV_A3',
    'level':'LEVEL',
    'type':'TYPE',
    'name':'NAME',
    'sortname':'SORTNAME',
    'adm0_a3':'ADM0_A3',
    'name_sm':'NAME_SM',
    'name_lng':'NAME_LNG',
    'terr':'TERR_',
    'parentheti':'PARENTHETI',
    'name_alt':'NAME_ALT',
    'local_lng':'LOCAL_LNG',
    'local_sm':'LOCAL_SM',
    'former':'FORMER',
    'abbrev':'ABBREV_',
    'map_color':'MAP_COLOR',
    'people':'PEOPLE',
    'gdp_usdm':'GDP_USDM',
    'fips_10':'FIPS_10',
    'iso_a2':'ISO_A2',
    'iso_a3':'ISO_A3',
    'iso_n3':'ISO_N3',
    'itu':'ITU',
    'ioc':'IOC',
    'fifa':'FIFA',
    'ds':'DS',
    'wmo':'WMO',
    'gaul':'GAUL',
    'marc':'MARC',
    'stanag1059':'STANAG1059',
    'gw_id':'GW_ID',
    'dial':'DIAL',
    'internet':'INTERNET_',
    'cog':'COG',
    'actual':'ACTUAL',
    'capay':'CAPAY',
    'crpay':'CRPAY',
    'ani':'ANI',
    'libenr':'LIBENR',
    'ancnom':'ANCNOM',
    'pays_r_gio':'PAYS_R_GIO',
    'comment':'COMMENT',
}

    
    
class Command(LabelCommand):
    help = "Imports Country vector Files into natural_earth.Country"
    args = 'Path to the .shp file'
    label = 'shp_path'
    
    def handle_label(self, label, **options):
        world_shp = os.path.abspath(label)
        ds = DataSource(world_shp)
        layer = ds[0]
        
        print "Datasource has %s layers"%len(ds)
        print "Layers have Fields: "
        print ""
        print "country_mapping = {"
        count = 0
        for field in layer.fields:
            print "    '"+str(field).lower() + "':'"+field+""
        
        print "}"
        
        print "Importing Layer %s of type %s, size: %s"\
                                            %(layer,layer.geom_type,len(layer))
        
        lm = LayerMapping(Country, world_shp, country_mapping,
                      transform=False, encoding='iso-8859-1')

        lm.save(strict=True, verbose=True)
        print "Successfully stored Countries"

        

