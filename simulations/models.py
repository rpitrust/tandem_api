from __future__ import unicode_literals
from collections import OrderedDict

from django.db import models
from jsonfield import JSONField

from querysets import SimresultsQuerySet, SimresultsSingleQuerySet


class Simresults(models.Model):
    caseid = models.AutoField(primary_key=True)
    graphtype = models.CharField(max_length=100, blank=True)
    radius = models.FloatField(blank=True, null=True)
    numagents = models.IntegerField(blank=True, null=True)
    numtrials = models.IntegerField(blank=True, null=True)
    agent_per_fact = models.IntegerField(blank=True, null=True)
    fact = models.IntegerField(blank=True, null=True)
    noise = models.IntegerField(blank=True, null=True)
    competence = models.FloatField(blank=True, null=True)
    willingness = models.FloatField(blank=True, null=True)
    spammer = models.FloatField(blank=True, null=True)
    selfish = models.FloatField(blank=True, null=True)
    trust_used = models.NullBooleanField()
    trust_filter_on = models.NullBooleanField()
    inbox_trust_sorted = models.NullBooleanField()
    ratio = models.FloatField(blank=True, null=True)
    behavtype = models.CharField(max_length=15, blank=True)
    behavvalue = models.FloatField(blank=True, null=True)
    sa = models.FloatField(blank=True, null=True)
    comm = models.FloatField(blank=True, null=True)
    steps = models.FloatField(blank=True, null=True)
    maxsa = models.FloatField(blank=True, null=True)
    comm_maxsa = models.FloatField(blank=True, null=True)
    steps_maxsa = models.FloatField(blank=True, null=True)
    sa0 = models.FloatField(blank=True, null=True)
    steps0 = models.FloatField(blank=True, null=True)
    commtotal0 = models.FloatField(blank=True, null=True)
    comm0 = models.FloatField(blank=True, null=True)
    all_comm = models.FloatField(blank=True, null=True)
    objects = SimresultsQuerySet.as_manager()

    class Meta:
        managed = False
        db_table = 'simresults'


class SimresultsSingle(models.Model):
    caseid = models.AutoField(primary_key=True)
    simulationmodel = models.CharField(max_length=20, blank=True)
    gname = models.CharField(max_length=100, blank=True)
    graphtype = models.CharField(max_length=100, blank=True)
    connection_probability = models.FloatField(blank=True, null=True)
    num_nodes_to_attach = models.IntegerField(blank=True, null=True)
    numagents = models.IntegerField(blank=True, null=True)
    numtrials = models.IntegerField(blank=True, null=True)
    agent_per_fact = models.IntegerField(blank=True, null=True)
    fact = models.IntegerField(blank=True, null=True)
    noise = models.IntegerField(blank=True, null=True)
    competence = models.FloatField(blank=True, null=True)
    willingness = models.FloatField(blank=True, null=True)
    spammer = models.FloatField(blank=True, null=True)
    selfish = models.FloatField(blank=True, null=True)
    trust_used = models.NullBooleanField()
    trust_filter_on = models.NullBooleanField()
    inbox_trust_sorted = models.NullBooleanField()
    ratio = models.FloatField(blank=True, null=True)
    behavtype = models.CharField(max_length=15, blank=True)
    behavvalue = models.FloatField(blank=True, null=True)
    sa = models.FloatField(blank=True, null=True)
    comm = models.FloatField(blank=True, null=True)
    steps = models.FloatField(blank=True, null=True)
    maxsa = models.FloatField(blank=True, null=True)
    comm_maxsa = models.FloatField(blank=True, null=True)
    steps_maxsa = models.FloatField(blank=True, null=True)
    sa0 = models.FloatField(blank=True, null=True)
    steps0 = models.FloatField(blank=True, null=True)
    commtotal0 = models.FloatField(blank=True, null=True)
    comm0 = models.FloatField(blank=True, null=True)
    all_comm = models.FloatField(blank=True, null=True)
    id_of_null_graph = models.ForeignKey('self', db_column='id_of_null_graph',
                                         blank=True, null=True)
    sa_increment = models.IntegerField(blank=True, null=True)
    statistic_taking_frequency = models.IntegerField(blank=True, null=True)
    num_cc = models.IntegerField(blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    cc = models.FloatField(blank=True, null=True)
    bc = models.FloatField(blank=True, null=True)
    deg = models.FloatField(blank=True, null=True)
    objects = SimresultsSingleQuerySet.as_manager()

    class Meta:
        managed = False
        db_table = 'simresults_single'


class Graph(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    data = JSONField()

    class Meta:
        db_table = 'graphs'


class SimAll(models.Model):
    caseid = models.ForeignKey('Simresults', db_column='caseid', blank=True, null=True)
    sa = models.FloatField(blank=True, null=True)
    comm = models.FloatField(blank=True, null=True)
    steps = models.FloatField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'sim_all'


class SimAllRaw(models.Model):
    caseid = models.ForeignKey('Simresults', db_column='caseid', blank=True, null=True)
    sa = models.FloatField(blank=True, null=True)
    comm = models.FloatField(blank=True, null=True)
    steps = models.FloatField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'sim_all_raw'


class SimAllRawSingle(models.Model):
    caseid = models.ForeignKey('SimresultsSingle', db_column='caseid', blank=True, null=True)
    sa = models.FloatField(blank=True, null=True)
    comm = models.FloatField(blank=True, null=True)
    steps = models.FloatField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'sim_all_raw_single'


class SimOne(models.Model):
    caseid = models.ForeignKey('Simresults', db_column='caseid', blank=True, null=True)
    sa0 = models.FloatField(blank=True, null=True)
    comm0 = models.FloatField(blank=True, null=True)
    commtotal0 = models.FloatField(blank=True, null=True)
    steps0 = models.FloatField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'sim_one'


class SimOneRaw(models.Model):
    caseid = models.ForeignKey('Simresults', db_column='caseid', blank=True, null=True)
    sa0 = models.FloatField(blank=True, null=True)
    comm0 = models.FloatField(blank=True, null=True)
    commtotal0 = models.FloatField(blank=True, null=True)
    steps0 = models.FloatField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'sim_one_raw'


class SimOneRawSingle(models.Model):
    caseid = models.ForeignKey('SimresultsSingle', db_column='caseid', blank=True, null=True)
    sa0 = models.FloatField(blank=True, null=True)
    comm0 = models.FloatField(blank=True, null=True)
    commtotal0 = models.FloatField(blank=True, null=True)
    steps0 = models.FloatField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'sim_one_raw_single'
