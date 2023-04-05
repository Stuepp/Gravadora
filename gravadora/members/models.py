from django.db import models

# Create your models here.
class Own(models.Model):
	id = models.BigAutoField(primary_key=True)
	# fk_musico = models.ForeignKey(Musico, blank=True, null=True, on_delete=models.CASCADE)
	# fk_banda = models.ForeignKey(Banda, blank=True, null=True, on_delete=models.CASCADE)

class Musico(models.Model):
	id = models.OneToOneField(Own, primary_key=True, on_delete=models.CASCADE)
	endereco = models.CharField(max_length=200)
	telefone = models.CharField(max_length=25)
	nome = models.CharField(max_length=50)
	
class Instrumento(models.Model):
	nome = models.CharField(max_length=50)

class Produtor(models.Model):
	nome = models.CharField(max_length=50)
	
class Musica(models.Model):
	titulo = models.CharField(max_length=50)
	autores = models.CharField(max_length=150)
	file = models.FileField(upload_to='songs/') # see better
	image = models.FileField(upload_to='images/') # see better

class Banda(models.Model):
	id = models.OneToOneField(Own, primary_key=True, on_delete=models.CASCADE)
	nome = models.CharField(max_length=75)

class Disco(models.Model):
	titulo = models.CharField(max_length=75)
	formato = models.CharField(max_length=75)
	data = models.DateField() # see better
	image = models.FileField(upload_to='images/') # see better
	fk_musico = models.ForeignKey(Musico, blank=True, null=True, on_delete=models.CASCADE)
	fk_banda = models.ForeignKey(Banda, blank=True, null=True, on_delete=models.CASCADE)

class Toca(models.Model):
	fk_musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
	fk_instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)

class Produz(models.Model):
	fk_disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
	fk_produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)

class Aparece(models.Model): # Música aparece em X Discos ou X músicas aparecem em um disco, etc..
	fk_musica = models.ForeignKey(Musica, on_delete=models.CASCADE)
	fk_disco = models.ForeignKey(Disco, on_delete=models.CASCADE)

class Esta(models.Model): # músico está dentro da banda
	fk_musico = models.ForeignKey(Musico, on_delete=models.CASCADE)
	fk_banda = models.ForeignKey(Banda, on_delete=models.CASCADE)

class Participa(models.Model):
	fk_own = models.ForeignKey(Own, on_delete=models.CASCADE)
	fk_musica = models.ForeignKey(Musica, on_delete=models.CASCADE)