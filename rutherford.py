#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import pyrax

class Mapping:
    prefix=""
    lbname=""
    port=0
    
    def __init__(self, prefix, lbname, port):
        self.prefix = prefix
        self.lbname = lbname
        self.port = port

def ensure_clb(server, loadbalancer, lbport):
    print("Ensuring",server.name,"to",loadbalancer.name)
    
    # don't add a duplicate node
    if(hasattr(loadbalancer, 'nodes')): # if nodes exist
        for node in loadbalancer.nodes: # loop through them
            if(node.address == server.accessIPv4): # return if we find it
                return
    
    new_node = clb.Node(address=server.accessIPv4, port=lbport, condition="ENABLED")
    lb.add_nodes([new_node])
    return

pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.raxpub")
pyrax.set_credential_file(creds_file)

mapping = []
mapping.append(Mapping('chat', 'chatlb', 123))
mapping.append(Mapping('wifi', 'dnelb', 456))

clb = pyrax.cloud_loadbalancers
loadbalancers = clb.list()

# build a hash of names one time
loadbalancer_map = {}
for lb in loadbalancers:
    loadbalancer_map[lb.name]=lb

cs = pyrax.cloudservers
servers = cs.list()

serverlist = []
# look through servers that exist, see if any should be added
for server in servers:
    
    # build a list of every server
    serverlist.append(server.accessIPv4)
    
    # look through mappings that exist
    for m in mapping:
        # if there's a mapping and we know about this load balancer
        if server.name.startswith(m.prefix) and m.lbname in loadbalancer_map.keys():
            ensure_clb(server,loadbalancer_map.get(m.lbname), m.port)

# now loop through all the clbs, remove servers that don't exist
for lb in loadbalancer_map.values():
    
    # don't touch anything that has no nodes
    if(not hasattr(lb, 'nodes')):
        continue
    
    # check each node to see if we've seen that address
    for node in lb.nodes:
        if(node.address not in serverlist):
            print('remove', node.address)
            node.delete()


                
