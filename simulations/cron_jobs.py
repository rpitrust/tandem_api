from django_cron import CronJobBase, Schedule
from .models import Simresults, SimresultsSingle, Graph


class CommPerSACronJob(CronJobBase):
    RUN_EVERY_MINS = 1440 # every day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'simulations.comm_per_sa'    # a unique code

    def do(self):
        results = SimresultsSingle.objects.comm_per_sa()
        results_hash = {}
        results_arr = []

        for r in results:
            if r.__dict__['fullgname'].startswith('ba'):
                graph_type = 'barabasi_albert_graph'
            elif r.__dict__['fullgname'].startswith('ws'):
                graph_type = 'watts_strogatz_graph'
            elif r.__dict__['fullgname'].startswith('ra'):
                graph_type = 'random'

            try: 
                results_hash[r.__dict__['fullgname']]
            except:
                results_hash[r.__dict__['fullgname']] = {'graph_type': graph_type,
                                                         'values': []}

            result_dict = r.__dict__
            results_hash[result_dict['fullgname']]['values'].append({'cc': result_dict['cc'],
                                                      'val': result_dict['val']})

        results_arr.append(results_hash)

        for obj in Graph.objects.filter(name='comm_per_sa'):
            obj.delete()

        Graph.objects.create(name='comm_per_sa', data=results_arr)