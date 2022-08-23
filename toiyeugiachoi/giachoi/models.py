from django.db import models
class giachoi(models.Model):
        tencachchuabenh = models.CharField(max_length=300)
        cachchoi = models.CharField(max_length=500)
        loaibenhdechua = models.CharField(max_length=400)
def __str__(self):
        return self.gh