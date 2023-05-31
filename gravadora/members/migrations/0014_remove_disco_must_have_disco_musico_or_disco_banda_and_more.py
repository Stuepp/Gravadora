# Generated by Django 4.1.7 on 2023-05-31 00:32

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_disco_must_have_disco_musico_or_disco_banda'),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name='disco',
            name='must_have_disco_musico_or_disco_banda',
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='disco',
            trigger=pgtrigger.compiler.Trigger(name='must_have_disco_musico_or_disco_banda', sql=pgtrigger.compiler.UpsertTriggerSql(func='\n\t\t\t\t\tIF (NEW.disco_musico != NULL OR NEW.disco_banda) THEN\n\t\t\t\t\t\tRETURN NEW;\n\t\t\t\t\tEND IF;\n\t\t\t\t', hash='44786a20ae76eda48c825f22e415a3588dbf2119', operation='UPDATE OR INSERT', pgid='pgtrigger_must_have_disco_musico_or_disco_banda_19906', table='members_disco', when='BEFORE')),
        ),
    ]
