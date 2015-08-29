__title__ = 'fobi.contrib.plugins.form_handlers.db_store.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('DataExporter',)

XLWT_INSTALLED = False
try:
    import xlwt
    XLWT_INSTALLED = True
except ImportError:
    pass

import csv

#import json
import simplejson as json

from six import StringIO, BytesIO

from django.http import HttpResponse

from nine.versions import DJANGO_GTE_1_7

from fobi.exceptions import ImproperlyConfigured
from fobi.helpers import safe_text

from .settings import CSV_DELIMITER, CSV_QUOTECHAR

class DataExporter(object):
    """
    Exporting the data.
    """
    def __init__(self, queryset):
        self.queryset = queryset

    def _get_initial_response(self, mimetype="application/csv"):
        """
        For compatibility with older versions (`mimetype` vs `content_type`).
        """
        response_kwargs = {}
        if DJANGO_GTE_1_7:
            response_kwargs['content_type'] = mimetype
        else:
            response_kwargs['mimetype'] = mimetype
        return HttpResponse(**response_kwargs)

    def _get_data_headers(self):
        """
        Since we have to deal with non-structured form data, we want to make
        sure that we obtain all the possible headers, so that later on
        we can just fill the slots needed.
        """
        # Normal RDMBs
        try:
            qs = self.queryset.only('form_data_headers')
            qs = qs.distinct('form_data_headers')
            qs = [obj.form_data_headers for obj in qs]

        # Engines like SQLite
        except NotImplementedError:
            qs = self.queryset.only('form_data_headers')
            qs = [obj.form_data_headers for obj in qs]
            qs = list(set(qs))

        data_headers = {}
        for q in qs:
            try:
                headers = json.loads(q)
                data_headers.update(headers)
            except (ValueError, TypeError):
                pass

        return data_headers

    def _export_to_xls(self):
        """
        Export data to XLS format.
        """
        #cellstyle = xlwt.easyxf(
        #    'align: wrap on, vert top, horiz left;', num_format_str='general'
        #    )

        #response = HttpResponse(mimetype="application/csv")
        response = self._get_initial_response(mimetype="application/csv")
        response['Content-Disposition'] = \
            'attachment; filename=db_store_export_data.xls'
        wb = xlwt.Workbook(encoding="UTF-8")
        ws = wb.add_sheet('Data')

        algn1 = xlwt.Alignment()
        algn1.wrap = 1
        style1 = xlwt.XFStyle()
        style1.alignment = algn1

        row = 0

        data_headers = self._get_data_headers()
        data_keys = data_headers.keys()
        data_values = data_headers.values()

        for cell, value in enumerate(data_values):
            ws.write(row, cell, unicode(value), xlwt.easyxf('font: bold on'))
            ws.col(cell).width = 256 * 20 # about 20 chars wide
            cell += 1
        row += 1

        for obj in self.queryset:
            data = json.loads(obj.saved_data)
            for cell, key in enumerate(data_keys):
                ws.write(row, cell, unicode(data.get(key, '')))
                cell += 1

            row += 1

        wb.save(response)
        return response

    def export_to_xls(self):
        if XLWT_INSTALLED:
            return self._export_to_xls()
        else:
            raise ImproperlyConfigured(
                "For XLS export xlwt shall be installed."
                )

    def export_to_csv(self):
        """
        Export data to CSV.
        """
        #response = HttpResponse(mimetype="text/csv")
        response = self._get_initial_response(mimetype="text/csv")
        response['Content-Disposition'] = \
            'attachment; filename=db_store_export_data.csv'

        data_headers = self._get_data_headers()
        data_keys = data_headers.keys()
        data_values = data_headers.values()

        queue = StringIO()
        try:
            csv_obj = csv.writer(
                queue, delimiter=CSV_DELIMITER, quotechar=CSV_QUOTECHAR
                )
            writerow = csv_obj.writerow
        except TypeError:
            queue = BytesIO()
            delimiter = bytes(CSV_DELIMITER, encoding="utf-8")
            quotechar = bytes(CSV_QUOTECHAR, encoding="utf-8")
            csv_obj = csv.writer(
                queue, delimiter=delimiter, quotechar=quotechar
                )
            writerow = lambda row: csv.writerow(
                [safe_text(cell) for cell in row]
                )

        data_values = [safe_text(value) for value in data_values]

        writerow(data_values)

        for obj in self.queryset:
            data = json.loads(obj.saved_data)
            row_data = []
            for cell, key in enumerate(data_keys):
                row_data.append(data.get(key, ''))

            writerow(row_data)

        data = queue.getvalue()
        response.write(data)
        return response

    def graceful_export(self):
        """
        Export data into XLS/CSV depending on what is available.
        """
        if XLWT_INSTALLED:
            return self._export_to_xls()
        else:
            return self.export_to_csv()
