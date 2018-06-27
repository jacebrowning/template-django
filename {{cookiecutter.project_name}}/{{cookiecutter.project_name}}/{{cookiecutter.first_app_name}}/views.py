from django.http import HttpResponse
import datetime

import log


def current_datetime(request):
    log.debug(request)
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
