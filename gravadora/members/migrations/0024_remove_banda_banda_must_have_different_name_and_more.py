# Generated by Django 4.1.7 on 2023-05-31 02:01

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0023_remove_produtor_produtor_must_have_different_namo_and_more'),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name='banda',
            name='banda_must_have_different_name',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='instrumento',
            name='instrumento_must_have_different_name',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='musico',
            name='musico_must_have_different_name_and_telefone',
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='banda',
            trigger=pgtrigger.compiler.Trigger(name='banda_must_have_different_name', sql=pgtrigger.compiler.UpsertTriggerSql(func='\n\t\t\t\t\tIF ((SELECT COUNT(*) FROM members_banda WHERE NOME = NEW.nome) < 1) THEN\n\t\t\t\t\t\tRETURN NEW;\n\t\t\t\t\tEND IF;\n\t\t\t\t', hash='65bdff35396cdbe2d960a880cc1929957e3e51b1', operation='UPDATE OR INSERT', pgid='pgtrigger_banda_must_have_different_name_e7880', table='members_banda', when='BEFORE')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='instrumento',
            trigger=pgtrigger.compiler.Trigger(name='instrumento_must_have_different_name', sql=pgtrigger.compiler.UpsertTriggerSql(func='\n\t\t\t\t\tIF ((SELECT COUNT(*) FROM members_instrumento WHERE NOME = NEW.nome) < 1) THEN\n\t\t\t\t\t\tRETURN NEW;\n\t\t\t\t\tEND IF;\n\t\t\t\t', hash='d755d3e3f249ca550c5123042f86deb8726b1fb6', operation='UPDATE OR INSERT', pgid='pgtrigger_instrumento_must_have_different_name_18cb6', table='members_instrumento', when='BEFORE')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='musico',
            trigger=pgtrigger.compiler.Trigger(name='musico_must_have_different_name_and_telefone', sql=pgtrigger.compiler.UpsertTriggerSql(func='\n\t\t\t\t\tIF ((SELECT COUNT(*) FROM members_musico WHERE NOME = NEW.nome AND TELEFONE =  NEW.telefone) < 1) THEN\n\t\t\t\t\t\tRETURN NEW;\n\t\t\t\t\tEND IF;\n\t\t\t\t', hash='177a155891685796033f08db7e833d89426c17e2', operation='UPDATE OR INSERT', pgid='pgtrigger_musico_must_have_different_name_and_telefone_326d4', table='members_musico', when='BEFORE')),
        ),
    ]
