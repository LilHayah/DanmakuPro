#!/usr/bin/env python3

# timepush.py - pushing the display time of comments in a danmaku xml file
#   Copyright (C) 2015  LilHayah

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import time
import xml.dom.minidom
from lxml import etree
from xml.etree.ElementTree import ElementTree,Element


# Read danmaku xml ass a tree
def Read(fn):
    #tree = ElementTree()
    #tree.parse(fn)
    with open(fn, encoding='utf-8') as f:
        tree = etree.parse(f)
    #tree = etree.parse(fn)
    return tree

def Push(tree,pt):
    nodes = tree.findall("d")
    cnt = 0
    for node in nodes:
        p = str(node.get("p")).split(',') # danmaku setting p
        nt = float(p[0]) + float(pt)
        p[0] = str(nt)
        #print(",".join(p))
        node.set("p",",".join(p))

        #node.set("p",ds)

        #print(ds)
        cnt += 1
    print(cnt)


def main():
    fn = sys.argv[1] # filename as fn
    pt = sys.argv[2] # pushtime as pt
    ou = sys.argv[3] # outputname as ou

    tree = Read(fn)
    Push(tree,pt)
    tree.write(ou,encoding="UTF-8", pretty_print=True)
    #tree.write("output1.xml") 



    print(fn,"has been pushed for ",pt," seconds.")


if __name__ == "__main__":
    main()