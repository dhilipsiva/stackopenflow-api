from importlib import import_module
from json import dumps

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

CHOICES_TEMPLATE = """// DON'T EDIT. THIS FILE IS GENERATED BY
./manage.py export_client
// CHANGE MADES MANUALLY TO THIS FILE WILL BE LOST
// mynamespace/contribs/management/commands/export_client.py

const CHOICES = %s;

export default CHOICES;
"""


def _write(file_path, template, data):
    with open(file_path, "w") as fp:
        content = template % dumps(data, indent=2, sort_keys=True)
        fp.write(content)
        print(f"written to {fp.name}")


def export_choices():
    choices = {}
    for app in settings.INSTALLED_APPS:
        try:
            module = import_module(f"{app}.choices")
        except ImportError:
            continue
        for attrib in dir(module):
            klass = getattr(module, attrib)
            if not hasattr(klass, "choices"):
                continue
            if len(klass.choices) == 0:
                continue
            _ch_map = {}
            _ch_list = []
            for i in klass.__members__.items():
                _map = i[1]
                _ch_map[_map.value] = _map.label.translate("")
                _ch_list.append(dict(value=_map.value, label=_map.label.translate("")))
            _ch_list = sorted(_ch_list, key=lambda i: i["value"])
            _choices = {
                "CHOICE_MAP": _ch_map,
                "CHOICE_LIST": _ch_list,
            }
            for i in klass.__members__.items():
                _map = i[1]
                _choices[_map.name] = _map.value
            choices[klass.__name__] = _choices
    _write(settings.APP_CHOICES_JS, CHOICES_TEMPLATE, choices)


class Command(BaseCommand):
    help = "Produce client JS files"

    def handle(self, *args, **options):
        export_choices()
        management.call_command("graphql_schema")
