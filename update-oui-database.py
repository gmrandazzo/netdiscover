#/usr/bin/env python

import time
import urllib

day = time.strftime("%d")
month = time.strftime("%m")
year = time.strftime("%Y")
ouifname = "oui.txt-%s-%s-%s" % (year, month, day)
urllib.urlretrieve("http://standards.ieee.org/regauth/oui/oui.txt", filename=ouifname)
foui = open(ouifname, "r")
fouih = open("src/oui.h", "w")
fouih.write("/*")
fouih.write("* Organizationally Unique Identifier list at date %s-%s-%s\n" % (day, time.strftime("%b"), year))
fouih.write("* Automatically generated from http://standards.ieee.org/regauth/oui/oui.txt\n")
fouih.write("* For Netdiscover by Giuseppe Marco Randazzo\n")
fouih.write("*\n")
fouih.write("*/\n\n")
fouih.write("struct oui {\n")
fouih.write("   char *prefix;   /* 24 bit global prefix */\n")
fouih.write("   char *vendor;   /* Vendor id string     */\n")
fouih.write("};\n\n")
fouih.write("struct oui oui_table[] = {\n")
for line in foui:
    if "base 16" in line:
        var = filter(None, str.split(line.strip(), "\t"))
        if len(var) == 2:
            fouih.write("   { \"%s\", \"%s\" },\n" % (str.split(var[0], " ")[0], var[1].replace("\"", "")))
        elif len(var) == 1:
            fouih.write("   { \"%s\", \"\" },\n" % (str.split(var[0], " ")[0]))
        else:
          print("Error in line: %s" % (line))
    else:
        continue
foui.close()
fouih.write("   { NULL, NULL }\n")
fouih.write("};\n")
fouih.close()