from django.contrib.gis.db import models

class Country(models.Model):
    name = models.CharField(max_length=150)
    featurecla = models.CharField(max_length=32)
    sov = models.CharField(max_length=100)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    
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
    

