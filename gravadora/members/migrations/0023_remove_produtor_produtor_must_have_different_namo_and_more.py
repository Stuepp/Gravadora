# Generated by Django 4.1.7 on 2023-05-31 01:59

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0022_remove_produtor_produtor_must_have_different_name_and_more'),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name='produtor',
            name='produtor_must_have_different_namo',
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='produtor',
            trigger=pgtrigger.compiler.Trigger(name='produtor_must_have_different_name', sql=pgtrigger.compiler.UpsertTriggerSql(func='\n\t\t\t\t\tIF ((SELECT COUNT(*) FROM members_produtor WHERE NOME = NEW.nome) < 1) THEN\n\t\t\t\t\t\tRETURN NEW;\n\t\t\t\t\tEND IF;\n\t\t\t\t', hash='eee5f4a4e0749d4c0f2b2efbc2b515e9231b8761', operation='UPDATE OR INSERT', pgid='pgtrigger_produtor_must_have_different_name_4c1d7', table='members_produtor', when='BEFORE')),
        ),
    ]
