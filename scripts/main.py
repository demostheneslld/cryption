#!/usr/bin/python

# SET I/O
inputs = {'cryption' : 'C:/Users/Nathan/Dropbox/GitHub/cryption/inputs'}
outputs = {'cryption' : 'C:/Users/Nathan/Dropbox/GitHub/cryption/outputs'}

# LIBRARIES
import os
os.chdir("C:/Users/Nathan/Dropbox/GitHub/cryption/scripts")
from X_Imports import *
#script = str(os.path.realpath(__file__)) if '__file__' in globals() else 'Current Script Unknown'
#header.scriptsummary(script, inputs, outputs)
pd.options.mode.chained_assignment = None
#####################################################################################################

# PARAMS
key = -6
preserve = ['\n']
sendtofile = True
inputstring = ''

# READ FILE
if (inputstring == ''):
    fn = 'US_Constitution.txt'
    path = inputs['cryption'] + '/' + fn
    i = open(path, 'r')
    unencrypted_string = i.read()
    i.close()
else:
    unencrypted_string = inputstring

# TURN TO LIST
unencrypted_list = list(unencrypted_string)

# ACTUAL ENCRYPTION
nl = []
for c in unencrypted_list:
    if (c in preserve):
        nl.append(c)
    else:
        nc = ord(c)+key
        nc = unichr(nc)
        nl.append(nc)

# TURN TO STRING
encrypted_list = nl
encrypted_string = str(''.join(encrypted_list))

# WRITE FILE
if (sendtofile):
    fn = 'e_' + fn
    path = outputs['cryption'] + '/' + fn
    o = open(path, 'w')
    o.write(encrypted_string)
    o.close()
else:
    print(encrypted_string)