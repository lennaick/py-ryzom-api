##
## Copyright (c) 2014 Rodolphe Breard
## 
## Permission to use, copy, modify, and/or distribute this software for any
## purpose with or without fee is hereby granted, provided that the above
## copyright notice and this permission notice appear in all copies.
## 
## THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
## WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
## MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
## ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
## WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
## ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
## OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
##

from . import RYZOM_API_DOMAIN
from xml.etree.ElementTree import fromstring
import urllib.parse, http.client

def get(name, **kwargs):
    url = '/%s.php' % name
    params = urllib.parse.urlencode(kwargs)

    conn = http.client.HTTPConnection(RYZOM_API_DOMAIN)
    conn.request('GET', url, params)
    rep = conn.getresponse()
    if rep.status != 200:
        raise Exception

    data = rep.read()
    return fromstring(data)
