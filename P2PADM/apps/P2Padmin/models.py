from django.db import models

# Create your models here.
class P2PServerInfo(models.Model):
    project = models.CharField(max_length=50)
    col_date = models.DateTimeField()
    p2p_onlinenum = models.CharField(max_length=50)
    rel_onlinenum = models.CharField(max_length=50)
    relay_accnum = models.CharField(max_length=50)
    p2p_accnum = models.CharField(max_length=50)
    def __unicode__(self):
        return self.headline
