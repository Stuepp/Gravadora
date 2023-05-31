from django.db import models
import pgtrigger

class Banda(models.Model):
	nome = models.CharField(max_length=75)

	def __str__(self):
		return '%s' % (self.nome)
	
	class Meta: # SELECT COUNT(*) FROM members_banda / I believe is not the ideal but it works
		triggers = [
			pgtrigger.Trigger(
				name = 'banda_must_have_different_name',
				operation = pgtrigger.Update | pgtrigger.Insert,
				when = pgtrigger.Before,
				func = f"""
					IF ((SELECT COUNT(*) FROM members_banda WHERE NOME = NEW.nome) < 1) THEN
						RETURN NEW;
					END IF;
				""",
			)
		]

class Instrumento(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.nome)
	
	class Meta: # SELECT COUNT(*) FROM members_instrumento / I believe is not the ideal but it works
		triggers = [
			pgtrigger.Trigger(
				name = 'instrumento_must_have_different_name',
				operation = pgtrigger.Update | pgtrigger.Insert,
				when = pgtrigger.Before,
				func = f"""
					IF ((SELECT COUNT(*) FROM members_instrumento WHERE NOME = NEW.nome) < 1) THEN
						RETURN NEW;
					END IF;
				""",
			)
		]

class Musico(models.Model):
	endereco = models.CharField(max_length=200)
	telefone = models.CharField(max_length=25)
	nome = models.CharField(max_length=50)
	esta = models.ManyToManyField(Banda)
	toca = models.ManyToManyField(Instrumento)

	def __str__(self):
		return '%s' % (self.nome)
	
	class Meta: # SELECT COUNT(*) FROM members_musico / I believe is not the ideal but it works
		triggers = [
			pgtrigger.Trigger(
				name = 'musico_must_have_different_name_and_telefone',
				operation = pgtrigger.Update | pgtrigger.Insert,
				when = pgtrigger.Before,
				func = f"""
					IF ((SELECT COUNT(*) FROM members_musico WHERE NOME = NEW.nome OR TELEFONE =  NEW.telefone) < 1) THEN
						RETURN NEW;
					END IF;
				""",
			)
		]

class Produtor(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % (self.nome)
	
	class Meta: # SELECT COUNT(*) FROM members_produtor / I believe is not the ideal but it works
		triggers = [
			pgtrigger.Trigger(
				name = 'produtor_must_have_different_name',
				operation = pgtrigger.Update | pgtrigger.Insert,
				when = pgtrigger.Before, #(SELECT COUNT(*) FROM members_produtor WHERE NOME = NEW.nome) == 0::bigint
				func = f"""
					IF ((SELECT COUNT(*) FROM members_produtor WHERE NOME = NEW.nome) < 1) THEN
						RETURN NEW;
					END IF;
				""",
			)
		]

class Disco(models.Model):
	titulo = models.CharField(max_length=75)
	formato = models.CharField(max_length=75)
	data = models.DateField() # see better
	disco_musico = models.ManyToManyField(Musico)
	disco_banda = models.ManyToManyField(Banda)
	produzido = models.ForeignKey(Produtor, on_delete=models.SET_NULL, default='', null=True)

	def __str__(self):
		return '%s' % (self.titulo)
	#class Meta:
	#	triggers = [
	#		pgtrigger.Trigger( # registro "new" não tem campo "disco_musico", pois é outra tabela??????
	#			name = 'must_have_disco_musico_or_disco_banda',
	#			operation = pgtrigger.Update | pgtrigger.Insert, #  
	#			when = pgtrigger.Before,
	#			func = f"""
	#				IF (NEW.disco_musico != NULL OR NEW.disco_banda) THEN
	#					RETURN NEW;
	#				END IF;
	#			""",
	#		)
	#	]

class Musica(models.Model):
	titulo = models.CharField(max_length=50)
	autores = models.CharField(max_length=150) # pode remover pois particpa_Musico já faz isso -> como remover agora que já tem?
	file = models.FileField(upload_to='songs/') # see better
	image = models.FileField(upload_to='images/') # see better
	participa_Musico = models.ManyToManyField(Musico)
	participa_Banda = models.ManyToManyField(Banda)
	aparece = models.ManyToManyField(Disco)

	#class Meta:
	#	triggers = [
	#		pgtrigger.Trigger(
	#			name = 'teste', #must_have_particpa_Musico_or_participa_Banda
	#			operation = pgtrigger.Update | pgtrigger.Insert, #  OR NEW.participa_Banda != NULL
	#			when = pgtrigger.Before,
	#			func = f"""
	#				IF (NEW.participa_Musico != NULL) THEN
	#					RETURN NEW;
	#				END IF;
	#			""",
	#		)
	#	]