# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Blacklist(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=600)
    hit = models.IntegerField()
    status = models.IntegerField()
    class Meta:
        db_table = u'blacklist'

class FilterComment(models.Model):
    comment_id = models.IntegerField()
    original_message = models.TextField()
    parse_message = models.TextField()
    channel_id = models.IntegerField()
    date_created = models.DateTimeField()
    status = models.IntegerField()
    class Meta:
        db_table = u'filter_comment'

class KdXmlrpcNews(models.Model):
    news_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=765, blank=True)
    short_desc = models.TextField(blank=True)
    full_desc = models.TextField(blank=True)
    author = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField()
    class Meta:
        db_table = u'kd_xmlrpc_news'

class OtAbuse(models.Model):
    id = models.IntegerField(primary_key=True)
    channel_id = models.IntegerField()
    content_id = models.IntegerField()
    comment_id = models.IntegerField()
    note = models.TextField()
    status = models.IntegerField()
    user_id = models.IntegerField()
    ip = models.CharField(max_length=150)
    class Meta:
        db_table = u'ot_abuse'

class OtComment0(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_0'

class OtComment1(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_1'

class OtComment10001(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_10001'

class OtComment11(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_11'

class OtComment12(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_12'

class OtComment13(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_13'

class OtComment137(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_137'

class OtComment138(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_138'

class OtComment14(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_14'

class OtComment144(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_144'

class OtComment15(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_15'

class OtComment16(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_16'

class OtComment160(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_160'

class OtComment168(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_168'

class OtComment169(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_169'

class OtComment17(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_17'

class OtComment170(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_170'

class OtComment171(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_171'

class OtComment172(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_172'

class OtComment173(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_173'

class OtComment174(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_174'

class OtComment175(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_175'

class OtComment176(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_176'

class OtComment177(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_177'

class OtComment178(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_178'

class OtComment179(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_179'

class OtComment18(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_18'

class OtComment180(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_180'

class OtComment181(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_181'

class OtComment182(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_182'

class OtComment183(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_183'

class OtComment184(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_184'

class OtComment185(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_185'

class OtComment186(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_186'

class OtComment187(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_187'

class OtComment188(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_188'

class OtComment189(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_189'

class OtComment2(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_2'

class OtComment205(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_205'

class OtComment216(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_216'

class OtComment222(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_222'

class OtComment224(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_224'

class OtComment228(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_228'

class OtComment241(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_241'

class OtComment261(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_261'

class OtComment266(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_266'

class OtComment283(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_283'

class OtComment290(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_290'

class OtComment298(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_298'

class OtComment3(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_3'

class OtComment348(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_348'

class OtComment349(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_349'

class OtComment350(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_350'

class OtComment355(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_355'

class OtComment392(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_392'

class OtComment400(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_400'

class OtComment406(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_406'

class OtComment415(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_415'

class OtComment434(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_434'

class OtComment45(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_45'

class OtComment500(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    title_content = models.CharField(max_length=768)
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_500'

class OtComment58(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_58'

class OtComment59(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_59'

class OtComment60(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_60'

class OtComment61(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_61'

class OtComment62(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_62'

class OtComment63(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_63'

class OtComment64(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_64'

class OtComment65(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    parent_id = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_65'

class OtComment67(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_67'

class OtComment68(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_68'

class OtComment69(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    source = models.IntegerField(null=True, blank=True)
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_69'

class OtCommentProperty(models.Model):
    id_comment_property = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=768)
    label = models.CharField(max_length=768)
    datecreate = models.DateTimeField()
    active = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_property'

class OtCommentVideo13(models.Model):
    id_comment_video = models.IntegerField(primary_key=True)
    id_content = models.IntegerField()
    name = models.CharField(max_length=768)
    email = models.CharField(max_length=768)
    url = models.CharField(max_length=768, blank=True)
    detail = models.TextField()
    laik = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_comment_video_13'

class OtCommentVideoProperty(models.Model):
    id_comment_video_property = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=768)
    label = models.CharField(max_length=768)
    datecreate = models.DateTimeField()
    active = models.IntegerField()
    class Meta:
        db_table = u'ot_comment_video_property'

class OtContentOkezone(models.Model):
    content_id = models.IntegerField(unique=True)
    channel_id = models.IntegerField()
    title = models.CharField(max_length=765)
    date_created = models.DateTimeField()
    class Meta:
        db_table = u'ot_content_okezone'

class OtGroup(models.Model):
    id_group = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=384, blank=True)
    group_description = models.CharField(max_length=768, blank=True)
    datecreate = models.DateTimeField()
    active = models.IntegerField()
    class Meta:
        db_table = u'ot_group'

class OtGroupUseApp(models.Model):
    id_group_use_app = models.IntegerField(primary_key=True)
    id_group = models.IntegerField()
    id_otizen_app = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_group_use_app'

class OtGroupUseComment(models.Model):
    id_group_use_comment = models.IntegerField(primary_key=True)
    id_group = models.IntegerField()
    id_comment_property = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_group_use_comment'

class OtGroupUseCommentVideo(models.Model):
    id_group_use_comment_video = models.IntegerField(primary_key=True)
    id_group = models.IntegerField()
    id_comment_video_property = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_group_use_comment_video'

class OtGroupUseMenu(models.Model):
    id_group_use_menu = models.IntegerField(primary_key=True)
    id_group = models.IntegerField()
    id_menu = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_group_use_menu'

class OtGroupUsePolling(models.Model):
    id_group_use_polling = models.IntegerField(primary_key=True)
    id_group = models.IntegerField()
    id_polling_property = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_group_use_polling'

class OtGroupUseShout(models.Model):
    id_group_use_shout = models.IntegerField(primary_key=True)
    id_group = models.IntegerField()
    id_shout_property = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_group_use_shout'

class OtGroupUseShoutthematic(models.Model):
    id_group_use_shoutthematic = models.IntegerField(primary_key=True)
    id_group = models.IntegerField()
    id_shoutthematic_property = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_group_use_shoutthematic'

class OtMenu(models.Model):
    id_menu = models.IntegerField(primary_key=True)
    caption = models.CharField(max_length=384)
    description = models.CharField(max_length=1536)
    datecreate = models.DateTimeField()
    path = models.CharField(max_length=384)
    active = models.IntegerField()
    id_user = models.IntegerField()
    class Meta:
        db_table = u'ot_menu'

class OtOrganization(models.Model):
    id_organization = models.IntegerField(primary_key=True)
    organization_name = models.CharField(max_length=768, blank=True)
    address = models.CharField(max_length=1536, blank=True)
    url = models.CharField(max_length=192, blank=True)
    sector = models.CharField(max_length=192, blank=True)
    datecreate = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'ot_organization'

class OtOtizenApp(models.Model):
    id_otizen_app = models.IntegerField(primary_key=True)
    caption = models.CharField(max_length=135, blank=True)
    description = models.CharField(max_length=1536)
    datecreate = models.DateTimeField(null=True, blank=True)
    active = models.IntegerField()
    class Meta:
        db_table = u'ot_otizen_app'

class OtPollingA(models.Model):
    id_polling_a = models.IntegerField(primary_key=True)
    answer = models.CharField(max_length=384)
    hit = models.IntegerField()
    id_polling_q = models.IntegerField()
    class Meta:
        db_table = u'ot_polling_a'

class OtPollingProperty(models.Model):
    id_polling_property = models.IntegerField()
    polling_name = models.CharField(max_length=384)
    datecreate = models.DateTimeField()
    active = models.IntegerField()
    class Meta:
        db_table = u'ot_polling_property'

class OtPollingQ(models.Model):
    id_polling_q = models.IntegerField()
    topic = models.CharField(max_length=768)
    question = models.TextField()
    datecreate = models.DateTimeField()
    active = models.IntegerField()
    id_polling_property = models.IntegerField()
    class Meta:
        db_table = u'ot_polling_q'

class OtRatingVideo(models.Model):
    id_rating_video = models.BigIntegerField(primary_key=True)
    video_id = models.BigIntegerField()
    hit = models.BigIntegerField()
    class Meta:
        db_table = u'ot_rating_video'

class OtRatingVideoAgent(models.Model):
    rating_video_agent_id = models.BigIntegerField(primary_key=True)
    id_rating_video = models.BigIntegerField()
    ip = models.CharField(max_length=156)
    a_hit = models.IntegerField()
    agent = models.CharField(max_length=384)
    datehit = models.DateTimeField()
    class Meta:
        db_table = u'ot_rating_video_agent'

class OtRelationalContags(models.Model):
    id_relational_contags = models.IntegerField(primary_key=True)
    datecreate = models.DateTimeField(null=True, blank=True)
    id_user = models.IntegerField(null=True, blank=True)
    id_content = models.IntegerField(null=True, blank=True)
    id_content_tags = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ot_relational_contags'

class OtShout(models.Model):
    id_shout = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1536, blank=True)
    address = models.CharField(max_length=768, blank=True)
    email = models.CharField(max_length=384, blank=True)
    url = models.CharField(max_length=3072, blank=True)
    shout = models.TextField(blank=True)
    datecreate = models.DateTimeField(null=True, blank=True)
    avatar = models.CharField(max_length=3072, blank=True)
    laik = models.IntegerField(null=True, blank=True)
    id_shout_property = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ot_shout'

class OtShoutProperty(models.Model):
    id_shout_property = models.IntegerField(primary_key=True)
    shout_name = models.CharField(max_length=768)
    install_mode = models.CharField(max_length=384)
    need_moderation = models.IntegerField()
    email_to_admin = models.IntegerField()
    datecreate = models.DateTimeField()
    active = models.IntegerField()
    class Meta:
        db_table = u'ot_shout_property'

class OtShoutthematicProperty(models.Model):
    id_shoutthematic_property = models.IntegerField(primary_key=True)
    shoutthematic_name = models.CharField(max_length=768)
    install_mode = models.CharField(max_length=384)
    need_moderation = models.IntegerField()
    email_to_admin = models.IntegerField()
    datecreate = models.DateTimeField()
    active = models.IntegerField()
    class Meta:
        db_table = u'ot_shoutthematic_property'

class OtShoutthematicQuestion(models.Model):
    id_shoutthematic_question = models.IntegerField(primary_key=True)
    topic = models.TextField()
    question = models.CharField(max_length=3072)
    laik = models.IntegerField()
    id_shoutthematic_property = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_shoutthematic_question'

class OtShoutthematicReply(models.Model):
    id_shoutthematic_reply = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1536, blank=True)
    address = models.CharField(max_length=768, blank=True)
    email = models.CharField(max_length=384, blank=True)
    url = models.CharField(max_length=3072, blank=True)
    shout = models.TextField(blank=True)
    datecreate = models.DateTimeField(null=True, blank=True)
    avatar = models.CharField(max_length=3072, blank=True)
    laik = models.IntegerField(null=True, blank=True)
    id_shoutthematic_topic = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ot_shoutthematic_reply'

class OtShoutthematicTopic(models.Model):
    id_shoutthematic_topic = models.IntegerField(primary_key=True)
    topic = models.TextField()
    question = models.CharField(max_length=3072)
    laik = models.IntegerField()
    id_shoutthematic_property = models.IntegerField()
    datecreate = models.DateTimeField()
    class Meta:
        db_table = u'ot_shoutthematic_topic'

class OtUser(models.Model):
    id_user = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=1536)
    email = models.CharField(max_length=384)
    active = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=384)
    datesignup = models.DateTimeField(null=True, blank=True)
    dateactived = models.DateTimeField(null=True, blank=True)
    activecode = models.CharField(max_length=1536, blank=True)
    id_organization = models.IntegerField(null=True, blank=True)
    id_group = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ot_user'

class OtUserSessions(models.Model):
    session_id = models.CharField(max_length=120, primary_key=True)
    id_user = models.IntegerField()
    user_agent = models.CharField(max_length=1536, blank=True)
    user_ip = models.CharField(max_length=96, blank=True)
    last_activity = models.IntegerField()
    class Meta:
        db_table = u'ot_user_sessions'

class OtUserlog(models.Model):
    id_userlog = models.IntegerField(primary_key=True)
    date_login = models.DateTimeField(null=True, blank=True)
    date_logout = models.DateTimeField(null=True, blank=True)
    session_id = models.CharField(max_length=384, blank=True)
    ip = models.CharField(max_length=96, blank=True)
    id_user = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'ot_userlog'

class OtVideosOkezone(models.Model):
    video_id = models.IntegerField()
    channel_id = models.IntegerField()
    title = models.CharField(max_length=765)
    date_created = models.DateTimeField()
    class Meta:
        db_table = u'ot_videos_okezone'

class OtWisdom(models.Model):
    wisdom_id = models.IntegerField(primary_key=True)
    wisdom_quote = models.TextField()
    wisdom_source = models.CharField(max_length=1536)
    class Meta:
        db_table = u'ot_wisdom'

