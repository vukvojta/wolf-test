#!/usr/bin/python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server, WSGIServer
from SocketServer import ThreadingMixIn
import wolf


class ThreadingWSGIServer(ThreadingMixIn, WSGIServer):
    pass


wolf.template_environment('templates')

application = wolf.Router(
    (wolf.Static('static/stylesheets'), 'stylesheets/'),
    (wolf.Static('static/fonts'), 'fonts/'),
    (wolf.Static('static/javascripts'), 'javascripts/'),
    (wolf.Static('static/images'), 'images/'),
)


@application.route('(?P<name>[A-Z][a-z]*)?')
@wolf.controller
def home(name='Home'):
    return wolf.Response().template('home.html', name=name)


def main():
    print application
    httpd = make_server('', 8000, application, ThreadingWSGIServer)
    print 'Listening on port 8000....'
    httpd.serve_forever()


if __name__ == "__main__":
    main()
