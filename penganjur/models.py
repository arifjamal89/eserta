from django.db import models

# Create your models here.
class Aktiviti(models.Model):
	tajuk = models.CharField('Tajuk',blank=False,null=False,max_length=300)
	tempat = models.CharField('Tempat',blank=False,null=True,max_length=300)
	penceramah = models.CharField('Penceramah',blank=False,null=True,max_length=300)
	hadpeserta = models.IntegerField('Had Peserta',blank=True,null=True)

	def __str__(self):
		return str(self.pk)
