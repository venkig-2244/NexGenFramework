from typing import ParamSpec
from kubernetes import client, config

class NexGenEngine(object):
    def __init__(self):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()

    def printPods(self):    
        ret = self.v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    