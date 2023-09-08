#!/usr/bin/env python3

import pynetbox
import ipaddress, json
from pprint import pprint

nb = pynetbox.api(
    'http://ftp.int.durd.net:8000',
    token='3ea4b5590d0f53d583453e76dc1f5b86f0210ae4'
)

print('device\t\tsite\t\tsite id')
devices = list(nb.dcim.devices.all())
for device in devices:
    print('{}\t\t{}\t\t{}'.format(device, device.site, device.site.id))

#print('adding interfaces to {} in management...'.format(cluster['name']))
#print(json.dumps(dict(device), indent=2, skipkeys=1))
