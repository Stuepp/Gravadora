from django.db import models

class Banda(models.Model):
	nome = models.CharField(max_length=75)

	def __str__(self):
		return '%s' % (self.nome)

class Instrumento(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.nome)

class Musico(models.Model):
	endereco = models.CharField(max_length=200)
	telefone = models.CharField(max_length=25)
	nome = models.CharField(max_length=50)
	esta = models.ManyToManyField(Banda)
	toca = models.ManyToManyField(Instrumento)

	def __str__(self):
		return '%s' % (self.nome)

class Produtor(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.nome)

class Disco(models.Model):
	titulo = models.CharField(max_length=75)
	formato = models.CharField(max_length=75)
	data = models.DateField() # see better
	disco_musico = models.ManyToManyField(Musico)
	disco_banda = models.ManyToManyField(Banda)
	#produzido = models.ForeignKey(Produtor, on_delete=models.SET_NULL, default='') # Check how ManyToOneRel works

	def __str__(self):
		return '%s' % (self.titulo)

class Musica(models.Model):
	titulo = models.CharField(max_length=50)
	autores = models.CharField(max_length=150)
	file = models.FileField(upload_to='songs/') # see better
	image = models.FileField(upload_to='images/') # see better
	participa_Musico = models.ManyToManyField(Musico)
	participa_Banda = models.ManyToManyField(Banda)
	aparece = models.ManyToManyField(Disco)