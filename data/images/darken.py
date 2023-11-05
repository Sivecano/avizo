#!/usr/bin/python
import os

pairs = [(f, f.replace(".svg", "_dark.svg")) 
         for f in os.listdir(".") if f.endswith(".svg") and not f.endswith("_dark.svg")]

for (l, d) in pairs:
    with open(l, "r") as fl, open(d,"w") as fd:
        fd.write(fl.read().replace("#000000", "#b4b4b4"))

for f in (j for i in pairs for j in i):
    os.system(f"inkscape {f} -o {f.replace('.svg', '.png')}")

