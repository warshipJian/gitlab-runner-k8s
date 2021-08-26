#!/usr/bin/env python
# coding:utf8

import oss2
import os
import sys

class upload:

    def __init__(self,bucket):
        auth = oss2.Auth('ABC', 'DEF2')
        self.bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', bucket)

    def uploadFile(self,remoteName,localName):
        result = self.bucket.put_object_from_file(remoteName,localName)
        print('http status: {0}'.format(result.status))

    def uploadDir(self,dirName, distName):
        for path, subdirs, files in os.walk(dirName):
            for name in files:
                localName = os.path.join(path, name)
                remoteName = localName.replace(dirName,distName)
                self.uploadFile(remoteName,localName)

if __name__ == '__main__':

    branch = sys.argv[3]
    if branch == 'test':
        bucket = 'custom-gitlab-test'
    elif branch == 'release':
        bucket = 'custom-gitlab'
    else:
        sys.exit(0)

    a = upload(bucket)
    a.uploadDir(sys.argv[1],sys.argv[2])
