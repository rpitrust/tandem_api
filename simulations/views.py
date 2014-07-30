from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.http import HttpResponseForbidden, HttpResponseBadRequest
import json
from rest_framework import viewsets
from .models import Simresults
from .serializers import *


class SimresultViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Simresults.objects.all()
    serializer_class = SimresultSerializer
    paginate_by = None


def noise_vs_x(request):
    plot_factor = request.GET.get('plot_factor', 'competence')
    plot_y_axis = request.GET.get('plot_y_axis', 'sa')
    trust_used = request.GET.get('trust_used', 'FALSE')

    agf_str = request.GET.get('agf', '1')
    agf = agf_str.split(',')
    agf = set([int(x) for x in agf if x.isdigit()])

    if not agf.intersection(set([1, 3])):
        return HttpResponse(json.dumps({'status': 'failed',
                                        'reason': 'invalid agents per fact'}),
                            content_type='application/json')

    results = Simresults.objects.noise_sa(plot_factor=plot_factor,
                                          plot_y_axis=plot_y_axis,
                                          agf=agf_str,
                                          trust_used=trust_used.upper())

    results_hash = {}
    results_arr = []

    for r in results:
        result_dict = r.__dict__
        results_hash[result_dict[plot_factor]] = {}
        results_hash[result_dict[plot_factor]]['agf'] = {}
        for agf in agf_str.split(','):
            results_hash[result_dict[plot_factor]]['agf'][agf] = {}

    for r in results:
        result_dict = r.__dict__
        results_hash[result_dict[plot_factor]]['agf'][str(result_dict['agent_per_fact'])][result_dict['noise']] = result_dict[plot_y_axis]

    results_arr.append(results_hash)
    return HttpResponse(json.dumps({'results': results_arr}),
                        content_type='application/json')
