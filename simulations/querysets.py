from django.db.models import QuerySet

class SimresultsQuerySet(QuerySet):
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
            """.format(agf, plot_factor, variable_conditions[plot_factor],
                       trust_used, plot_y_axis))

    # and ss.graphtype IN ('barabasi_albert_graph', 'watts_strogatz_graph',
    # 'random')


class SimresultsSingleQuerySet(QuerySet):
    def comm_per_sa(self):
        return self.model.objects.raw("""
        SELECT 
          1 as caseid,
          ss.gname || '__' || cast(ss.density as char(4)) as fullgname
          , ss.cc
          , avg(cast(ss.comm as float)/cast(ss.sa as float)) as val
        FROM
          simresults_single ss
        WHERE 
          ss.competence = 1
          and ss.willingness = 1
          and ss.spammer = 0
          and ss.selfish = 0
          and ss.trust_used = False
          and ss.trust_filter_on = False
          and ss.inbox_trust_sorted = False
          and ss.ratio is null
          and ss.cc is not null -- this is important
               -- this is what the user can specify in the interface, if not
               -- all graphtypes are used
        GROUP BY 
          ss.gname
          , ss.density
          , ss.cc
        ORDER BY
          fullgname asc
          , cc asc ;   
        """)

    def sa_gain(self):
        return self.model.objects.raw("""
        SELECT
           1 as caseid,
           ss.gname || '__' || cast(ss.density as char(4)) as fullgname
           , ss.bc
           , avg(cast(ss.sa as float)/cast(ssnull.sa as float)) as val
        FROM
           simresults_single ss
           , simresults_single ssnull
        WHERE 
           ss.id_of_null_graph = ssnull.caseid
           and ss.competence = 1
           and ss.willingness = 1
           and ss.spammer = 0
           and ss.selfish = 0
           and ss.trust_used = False
           and ss.trust_filter_on = False
           and ss.inbox_trust_sorted = False
           and ss.ratio is null
           and ss.cc is not null -- this is important
               -- this is what the user can specify in the interface, if not
               -- all graphtypes are used
        GROUP BY 
           ss.gname
           , ss.density
           , ss.bc
        ORDER BY
          fullgname asc
          , bc asc ;
        """)