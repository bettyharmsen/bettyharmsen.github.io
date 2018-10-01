#!/usr/bin/python
#
# {Program name}
#
# {Program description}
#
import os
import os.path
import re

pattern = re.compile("")
count = 0

for entry in os.listdir("."):
    if entry.startswith("Artifact") == False:
        continue
    oldfile = file(entry, "r")
    newfile = file(entry + ".new", "w")
    while True:
        oldline = oldfile.readline()
        if len(oldline) == 0:
            break
        newline = re.sub(r"http://192.168.0.202/images/camera/Paintings/\d{6}xx/\d{8}",
                         r"images", oldline)
        newfile.write(newline)
    newfile.close()
    oldfile.close()
    count += 1
    
print "%d file processed" % count
        
