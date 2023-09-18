#!/usr/bin/env python3

import pynetbox
import ipaddress, json, jsonpickle
from flask import Flask, render_template
from pprint import pprint

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('regions.html', nb=nb_regions())

@app.route('/region/<region>')
def region(region):
    return render_template('sites.html', nb=nb_sites(region))

def bleh():
    return "name"

nb = pynetbox.api(
    'http://ftp.int.durd.net:8000',
    token='3ea4b5590d0f53d583453e76dc1f5b86f0210ae4'
)

def nb_devices():
    print('device\t\tsite\t\tsite id')
    devices = list(nb.dcim.devices.all())
    #pprint(devices)
    #return devices
    for device in devices:
        print('{}\t\t{}\t\t{}'.format(device, device.site, device.site.id))

#nb_devices()
def nb_sites(j2_region):
    #print('site\t\tstatus\t\tsite id')
    x = list(nb.dcim.sites.filter(status='planned',region_id=j2_region))
    return x

def nb_regions():
    #print('site\t\tstatus\t\tsite id')
    x = list(nb.dcim.regions.all())
    return x

#for site in nb_sites():
#    print('{}\t\t{}\t\t{}'.format(site, site.status, site.id))

#print(json.dumps(json.loads(jsonpickle.encode(nb_sites())), indent=2))
#pprint(dict(nb_devices()))
app.run(host='0.0.0.0', port=5001, debug=True)
exit()

#ip4_parent = "10.0.0.0/8"
#prefix = nb.ipam.prefixes.get(prefix=ip4_parent)
#ip4_subnet = prefix.available_prefixes.create({"prefix_length": 26, "description": "what"})


#print('adding interfaces to {} in management...'.format(cluster['name']))
#print(json.dumps(dict(ip4_subnet), indent=2, skipkeys=1))

