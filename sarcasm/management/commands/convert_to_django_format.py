import json
import re
import os

from django.core.management import BaseCommand

from django.conf import settings



class Command(BaseCommand):

    def __init__(self):
        self.sarcasm_url = settings.SARCASM_DATA_URL + '/Sarcasm_Headlines_Dataset.json'
        self.brand_mapping = []


    def execute(self, *args, **options):
        data = {}
        data['records'] = []
        pk = 0
        with open(self.sarcasm_url) as sarcasm_json_file:
            sarcasm_data = json.load(sarcasm_json_file)
            for index, record  in enumerate(sarcasm_data):
                formatted_record = {
                    'model': 'sarcasm.headline',
                    'pk': index + 1,
                    'fields': {
                        'article_link': record['article_link'],
                        'headline': record['headline'],
                        'is_sarcastic': record['is_sarcastic']

                    }
                }
                data['records'].append(formatted_record)

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

