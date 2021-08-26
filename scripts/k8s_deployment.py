#!/usr/bin/env python
# coding:utf8

import re
import sys
from k8s_base_server import kubernetes

template = '''apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: '1'
  generation: 1
  labels:
    app: {name}
  name: {name}
  namespace: {namespace}
spec:
  progressDeadlineSeconds: 600
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app: {name}
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: {name}
    spec:
      containers:
        - image: 'registry-vpc.cn-shenzhen.aliyuncs.com/abc/{name}:{tag}'
          imagePullPolicy: IfNotPresent
          name: yapi2
          resources:
            requests:
              cpu: 10m
              memory: 16Mi
'''

project_name = sys.argv[1]
tag = sys.argv[2]
# namespace 取tag的字母
namespace = ''.join(re.findall(r'[A-Za-z]', tag))
specific_yaml = template.format(name=project_name, tag=tag , namespace=namespace)

k8s = kubernetes(project_name,specific_yaml,namespace)
t = re.sub("\D", "", tag)
if int(t) == 1:
    k8s.create()
else:
    k8s.update()
