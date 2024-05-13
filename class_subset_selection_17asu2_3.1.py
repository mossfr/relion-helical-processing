#!/usr/bin/env python3

#### Script to select subset of CHMP1B/IST1 particles from 3D classification with 17 subunits per turn
#### Copyright Frank Moss 2020 - UCSF - frank.moss@ucsf.edu

with open("Class3D/17asu/run_it025_data.star", "r") as f, open("Class3D/17asu/particles17.star", "a") as g, open("Class3D/17asu/run_it025_model.star", "r") as h:
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
            if float(c[r-1]) > 3.05 and float(c[r-1]) < 3.2 and float(c[t-1]) > 20.6 and float(c[t-1]) < 21 and float(c[p-1]) < 8:
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
print("Written particles17.star with", count, "particles.")
out = open("External/17asu/RELION_JOB_EXIT_SUCCESS", "w")
out.close()
