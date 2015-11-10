import sys
import time
import xml.dom.minidom
from lxml import etree
from xml.etree.ElementTree import ElementTree,Element


# Read danmaku xml ass a tree
def Read(fn):
    #tree = ElementTree()
    #tree.parse(fn)
    tree = etree.parse(fn)
    return tree

def Push(tree,pt):
    nodes = tree.findall("d")
    cnt = 0
    for node in nodes:
        p = str(node.get("p")).split(',') # danmaku setting p
        nt = float(p[0]) + float(pt)
        p[0] = str(nt)
        print(",".join(p))
        node.set("p",",".join(p))

        #node.set("p",ds)

        #print(ds)
        cnt += 1
    print(cnt)


def main():
    fn = sys.argv[1] # filename as fn
    pt = sys.argv[2] # pushtime as pt

    tree = Read(fn)
    Push(tree,pt)
    tree.write("output.xml", pretty_print=True)
    #tree.write("output1.xml") 



    print(fn,"has been pushed for ",pt," seconds.")


if __name__ == "__main__":
    main()