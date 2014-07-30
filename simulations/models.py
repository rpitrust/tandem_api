# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class SimAll(models.Model):
    id = models.AutoField(primary_key=True)
    caseid = models.IntegerField(blank=True, null=True)
    sa = models.FloatField(blank=True, null=True)
    comm = models.FloatField(blank=True, null=True)
    steps = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sim_all'


class SimOne(models.Model):
    id = models.AutoField(primary_key=True)
    caseid = models.IntegerField(blank=True, null=True)
    sa0 = models.FloatField(blank=True, null=True)
    comm0 = models.FloatField(blank=True, null=True)
    commtotal0 = models.FloatField(blank=True, null=True)
    steps0 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sim_one'


class SimresultsQuerySet(models.QuerySet):
    def noise_sa(self, plot_factor, plot_y_axis, trust_used, agf='1', *args, **kwargs):
        variable_conditions = {
            'competence': """s.willingness = 1 AND
                             s.spammer = 0 AND
                             s.selfish = 0""",
            'willingness': """s.competence = 1 AND
                              s.spammer = 0 AND
                              s.selfish = 0""",
            'spammer': """s.competence = 1 AND
                          s.willingness = 1 AND
                          s.selfish = 0""",
            'selfish': """s.competence = 1 AND
                          s.willingness = 1 AND
                          s.spammer = 0"""
        }

        # TODO: group by s.{1}, agf, s.noise
        return self.model.objects.raw("""
            SELECT
              1 as caseid,
              s.{1},
              s.agent_per_fact,
              s.noise,
              sum(s.numtrials*s.{4})/sum(s.numtrials) as {4}
            FROM simresults s
            WHERE
              s.agent_per_fact IN ({0}) AND
              {2} AND
              trust_used IN ({3}) AND
              trust_filter_on = FALSE AND
              inbox_trust_sorted IN ({3})
            GROUP BY s.{1}, s.agent_per_fact, s.noise
            ORDER BY s.{1}, s.agent_per_fact, s.noise;
            """.format(agf, plot_factor, variable_conditions[plot_factor], trust_used, plot_y_axis))


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

