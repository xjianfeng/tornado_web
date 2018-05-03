#!/usr/bin/env python
# -*- coding: utf-8 -*-

import views

route_handler = [
    (r"/", views.index.HomeHandler),
    (r"/payinfo/(\w+)/(\w+)/(\w+)[/]?", views.payinfo.PayInfoHandler),
    (r"/configinfo", views.configinfo.ConfigHandler),
]
