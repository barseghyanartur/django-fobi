from six import text_type

from django.utils.html import format_html

__title__ = 'fobi.contrib.plugins.form_elements.fields.slider.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'generate_ticks',
)


def generate_ticks(choices, empty_labels=False):
    """Generate ticks.

    :param iterable choices: Iterable of tuples or lists:
    :param bool empty_labels:
    :return dict:
    """
    keys = [int(k) for (k, v) in choices]
    # values = [v for (k, v) in choices if v else text_type(k)]
    values = []

    if empty_labels:
        values = ["".encode('utf8') for k in keys]
    else:
        for k, v in choices:
            if v is not None:
                values.append(v.encode('utf8'))
            else:
                values.append(text_type(k).encode('utf8'))

    ticks = {
        'data-slider-ticks': format_html(str(keys)),
        'data-slider-ticks-labels': format_html(str(values).replace("'", '"')),
    }

    return ticks
