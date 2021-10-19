#!/bin/env python
# -*- coding: utf-8 -*-
import os
from pcloud import PyCloud
import time
import datetime
import requests

DATETIME = time.strftime('%Y%m%d-%H%M%S')
pc = PyCloud('email', 'senha')

lista = pc.listfolder(folderid=0)

#criar pasta no pcloud
pc.createfolder(path='/backup_'+DATETIME)


#fazer upload de arquivos
pc.uploadfile(files=['2.jpg'], path='/')
