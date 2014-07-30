from rest_framework import serializers
from .models import Simresults


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        kwargs['context']['request'].QUERY_PARAMS._mutable = True
        fields = kwargs['context']['request'].QUERY_PARAMS.pop('fields', None)[0].split(', ')
        kwargs['context']['request'].QUERY_PARAMS._mutable = False

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class SimresultSerializer(DynamicFieldsModelSerializer):
    """Serializes a Simresult object"""
    class Meta:
        model = Simresults
        fields = ('caseid', 'graphtype', 'radius', 'numagents', 'numtrials',
                  'agent_per_fact', 'fact', 'noise', 'competence',
                  'willingness', 'spammer', 'selfish', 'trust_used',
                  'trust_filter_on', 'inbox_trust_sorted', 'ratio',
                  'behavtype', 'behavvalue', 'sa', 'comm', 'steps', 'maxsa',
                  'comm_maxsa', 'steps_maxsa', 'sa0', 'steps0', 'commtotal0',
                  'comm0', 'all_comm')
