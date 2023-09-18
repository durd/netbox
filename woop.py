#!/usr/bin/env python3

import pynetbox
import ipaddress, json, jsonpickle
from pprint import pprint

nb = pynetbox.api(
    'http://ftp.int.durd.net:8000',
    token='3ea4b5590d0f53d583453e76dc1f5b86f0210ae4'
)

print('device\t\tsite\t\tsite id')
devices = list(nb.dcim.devices.all())
for device in devices:
    print('{}\t\t{}\t\t{}'.format(device, device.site, device.site.id))

print('site\t\tstatus\t\tsite id')
sites = list(nb.dcim.sites.filter(status='planned',region_id='2'))
for site in sites:
    #pprint(site._full_cache)
    print('{}\t\t{}\t\t{}'.format(site, site.status, site.id))

exit()
ip4_parent = "10.0.0.0/8"
prefix = nb.ipam.prefixes.get(prefix=ip4_parent)
ip4_subnet = prefix.available_prefixes.create({"prefix_length": 26, "description": "what"})


#print('adding interfaces to {} in management...'.format(cluster['name']))
