from django.contrib.gis.db import models

class Country(models.Model):
    name = models.CharField(max_length=150)
    featurecla = models.CharField(max_length=32)
    soviso = models.CharField(max_length=100)
    scalerank = models.IntegerField()
    sovereignt = models.CharField(max_length=200)
    sov_a3 = models.CharField(max_length=200)
    level = models.FloatField()
    type = models.CharField(max_length=200)
    sortname = models.CharField(max_length=200)
    adm0_a3 = models.CharField(max_length=200)
    name_sm = models.CharField(max_length=200)
    name_lng = models.CharField(max_length=200)
    terr = models.CharField(max_length=200)
    parentheti = models.CharField(max_length=200)
    name_alt = models.CharField(max_length=200)
    local_lng = models.CharField(max_length=200)
    local_sm = models.CharField(max_length=200)
    former = models.CharField(max_length=200)
    abbrev = models.CharField(max_length=200)
    fips_10 = models.CharField(max_length=200)
    iso_a2 = models.CharField(max_length=200)
    iso_a3 = models.CharField(max_length=200)
    iso_n3 = models.FloatField()
    map_color = models.FloatField()
    people = models.FloatField()
    gdp_usdm = models.FloatField()
    itu = models.CharField(max_length=200)
    ioc = models.CharField(max_length=200)
    fifa = models.CharField(max_length=200)
    ds = models.CharField(max_length=200)
    wmo = models.CharField(max_length=200)
    
    gaul = models.FloatField()
    marc = models.CharField(max_length=200)
    stanag1059 = models.CharField(max_length=200)
    gw_id = models.FloatField()
    dial = models.FloatField()
    internet = models.CharField(max_length=3)
    cog = models.CharField(max_length=5)
    actual = models.CharField(max_length=1)
    capay = models.CharField(max_length=5)
    crpay = models.CharField(max_length=5)
    ani = models.CharField(max_length=4)
    libenr = models.CharField(max_length=50)
    ancnom = models.CharField(max_length=20)
    pays_r_gio = models.CharField(max_length=50)
    comment = models.CharField(max_length=260)
    
    
    # Multipolygon since Polygon fields in Shapefiles can be Multipolygons
    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

    # So the model is pluralized correctly in the admin.
    class Meta:
        verbose_name_plural = "Countries"

    # Returns the string representation of the model.
    def __unicode__(self):
        return self.name
    
    
    
    
    
    
    
    
    
    
    
    
class County(models.Model):
    vertex_cou = models.FloatField()
    name = models.CharField(max_length=175)
    name_1 = models.CharField(max_length=175)
    varname_1 = models.CharField(max_length=175)
    nl_name_1 = models.CharField(max_length=175)
    hasc_1 = models.CharField(max_length=15)
    type_1 = models.CharField(max_length=50)
    engtype_1 = models.CharField(max_length=50)
    validfr_1 = models.CharField(max_length=25)
    validto_1 = models.CharField(max_length=15)
    remarks_1 = models.CharField(max_length=125)
    region = models.CharField(max_length=100)
    region_var = models.CharField(max_length=254)
    region_cod = models.CharField(max_length=50)
    region_c_1 = models.CharField(max_length=50)
    region_c_2 = models.CharField(max_length=50)
    region_c_3 = models.CharField(max_length=50)
    
    country_pr = models.CharField(max_length=128)
    
    scale_rank = models.IntegerField()
    check_me = models.IntegerField()
    gadm_level = models.FloatField()
    fips_1 = models.CharField(max_length=254)
    first_fips = models.CharField(max_length=254)
    first_hasc = models.CharField(max_length=254)
    nev_countr = models.CharField(max_length=100)
    prov_number = models.IntegerField()
    
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    
    mpoly = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.name
    

