#!/usr/bin/python3

#### Script to select subset of particles from 3D classification with helical symmetry
#### Copyright Frank Moss 2021 - UCSF - frank.moss@ucsf.edu

import os
import sys

#Input
print('Please specify:')
print('--folder         path to input job                     (default: Class3D/17asu)')
print('--output         path to output job                    (default: External/17asu)')
print('--name           name of output particle star file     (default: particles17.star)')
print('--type           2D or 3D classification               (default: 3D)')
print('--twist_low      lower twist cutoff (3D)               (default: 20.6)')
print('--twist_high     upper twist cutoff (3D)               (default: 21)')
print('--rise_low       lower rise cutoff  (3D)               (default: 3.05)')
print('--rise_high      upper rise cutoff  (3D)               (default: 3.18)')
print('--res            minimum resolution                    (default: 8)')

folder = 'Class3D/17asu'
output = 'External/17asu'
name = 'particles17.star'
class_type = '3D'
twist_low = 20.6
twist_high = 21
rise_low = 3.05
rise_high = 3.18
res = 8

for si, s in enumerate(sys.argv):
    if s == '--folder':
        folder = sys.argv[si+1]
for si, s in enumerate(sys.argv):
    if s == '--output':
        output = sys.argv[si+1]
for si, s in enumerate(sys.argv):
    if s == '--name':
        name = sys.argv[si+1]
for si, s in enumerate(sys.argv):
    if s == '--type':
        class_type = sys.argv[si+1]
for si, s in enumerate(sys.argv):
    if s == '--twist_low':
        twist_low = sys.argv[si+1]
for si, s in enumerate(sys.argv):
    if s == '--twist_high':
        twist_high = sys.argv[si+1]
for si, s in enumerate(sys.argv):
    if s == '--rise_low':
        rist_low = sys.argv[si+1]
for si, s in enumerate(sys.argv):
    if s == '--rise_high':
        rise_high = sys.argv[si+1]
for si, s in enumerate(sys.argv):
    if s == '--res':
        res = sys.argv[si+1]

if class_type == "3D":
    with open("%s/run_it025_data.star"%(folder), "r") as f, open("%s/%s"%(output, name), "w") as g, open("%s/run_it025_model.star"%(folder), "r") as h:
    #Selects classes from model star file
        classes = []
        for l in h:
            if l.startswith("_rlnHelicalRise #"):
                m = l.split("#")
                r = int(m[1])
            if l.startswith("_rlnHelicalTwist #"):
                n = l.split("#")
                t = int(n[1])
            if l.startswith("_rlnEstimatedResolution #"):
                o = l.split("#")
                p = int(o[1])
            d = l.split()
            if l.startswith("Class3D"):
                c = l.split()
                if float(c[r-1]) > float(rise_low) and float(c[r-1]) < float(rise_high) and float(c[t-1]) > float(twist_low) and float(c[t-1]) < float(twist_high) and float(c[p-1]) < float(res):
                    a = (c[0].split("class"))
                    b = float((a[1].split("."))[0])
                    classes.append(b)
    #Writes headers for particle star file
        count = 0
        num = 0
        for l in f:
            if l.startswith("_") or l.startswith("optics") or l.startswith("data") or l.startswith("loop") or l.startswith("#") or l.startswith("\n"):
                g.write(l)
    #Find particles from good classes in particle star file
            if l.startswith("_rlnClassNumber"):
                e = l.split("#")
                num = int(e[1])
            d = l.split()
            if len(d) > 2 and float(d[num-1]) in classes:
                g.write(l)
                count += 1
    print("Written %s with"%(name), count, "particles.")
    out = open("%s/RELION_JOB_EXIT_SUCCESS"%(output), "w")
    out.close()
    
if class_type == "2D":
    with open("%s/run_it025_data.star"%(folder), "r") as f, open("%s/%s"%(output, name), "a") as g, open("%s/run_it025_model.star"%(folder), "r") as h:
    #Selects classes from model star file
        classes = []
        for l in h:
            if l.startswith("_rlnEstimatedResolution #"):
                o = l.split("#")
                p = int(o[1])
            d = l.split()
            if l.startswith("000"):
                c = l.split()
                if float(c[p-1]) < float(res):
                    a = (c[0].split("@"))
                    b = float(a[0])
                    classes.append(b)
    #Writes headers for particle star file
        count = 0
        num = 0
        for l in f:
            if l.startswith("_") or l.startswith("optics") or l.startswith("data") or l.startswith("loop") or l.startswith("#") or l.startswith("\n"):
                g.write(l)
    #Find particles from good classes in particle star file
            if l.startswith("_rlnClassNumber"):
                e = l.split("#")
                num = int(e[1])
            d = l.split()
            if len(d) > 2 and float(d[num-1]) in classes:
                g.write(l)
                count += 1
    print("Written %s with"%(name), count, "particles.")
    out = open("%s/RELION_JOB_EXIT_SUCCESS"%(output), "w")
    out.close()