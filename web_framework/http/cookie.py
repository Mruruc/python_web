import time
from http.cookies import SimpleCookie


class Cookie:
    def __init__(self, name, value, domain=None, path='/', expires=None,
                 max_age=None, secure=False, http_only=False,
                 same_site=None):
        self.name = name
        self.value = value
        self.domain = domain
        self.path = path
        self.expires = expires
        self.max_age = max_age
        self.secure = secure
        self.http_only = http_only
        self.same_site = same_site

    def set_expires(self, days):
        self.expires = time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(time.time() + days * 86400))

    def __str__(self):
        cookie = SimpleCookie()
        cookie[self.name] = self.value
        cookie[self.name]['path'] = self.path
        if self.domain:
            cookie[self.name]['domain'] = self.domain
        if self.expires:
            cookie[self.name]['expires'] = self.expires
        if self.max_age:
            cookie[self.name]['max-age'] = self.max_age
        if self.secure:
            cookie[self.name]['secure'] = True
        if self.http_only:
            cookie[self.name]['httponly'] = True
        if self.same_site:
            cookie[self.name]['samesite'] = self.same_site
        return cookie.output(header='', sep='')

