from django.db import models

# Create your models here.
class P2PServerInfo(models.Model):
    project = models.CharField(max_length=50)
    body_text = models.TextField()
    col_date = models.DateTimeField()
    relay_accnum = models.IntegerField()
    p2p_accnum = models.IntegerField()
    def __unicode__(self):
        return self.headline
