# !/usr/bin/python
import os
import sys
import xml.dom.minidom
import copy


def get_domain_name(argv):
    source_file=argv[2]

    dom = xml.dom.minidom.parse(source_file)
    root = dom.documentElement
    list = root.getElementsByTagName("name")
    root = list[0]

    print (root.childNodes[0].data)

def get_device_source_file(argv):
    source_file=argv[2]

    dom = xml.dom.minidom.parse(source_file)
    root = dom.documentElement
    devices_list = root.getElementsByTagName("devices")
    devices = devices_list[0]
    disk_list = devices.getElementsByTagName("disk")
    for disk in disk_list:
        disk_driver = disk.getElementsByTagName("driver")[0]
        if disk_driver.getAttribute("type") != 'qcow2':
            continue
        else:
            disk_source = disk.getElementsByTagName("source")[0]
            if disk_source.hasAttribute("file"):
                print (disk_source.getAttribute("file"))

def get_dom_attribute(file, dom_l, attribute=None):
    dom = xml.dom.minidom.parse(file)
    root = dom.documentElement
    dom_piece = root
    for i in range(0, len(dom_l)-1):
        if i < (len(dom_l)-2):
            dom_piece = dom_piece.getElementsByTagName(dom_l[i])[0]
        else:
            dom_item_list = dom_piece.getElementsByTagName(dom_l[i])

            for item in dom_item_list:
                item = item.getElementsByTagName(dom_l[i + 1])[0]
                if item.hasAttribute(attribute):
                    print (item.getAttribute(attribute))



if __name__ == '__main__':
    argv = sys.argv
    len_argv = len(argv)
    if len_argv < 3:
      print("Error wrong number param")
      exit(-1)

    if argv[1] == '-n':
        get_domain_name(argv)

    elif argv[1] == '-s':
        get_device_source_file(argv)

    elif argv[1] == '-a':
        get_dom_attribute(file=argv[2], dom_l=argv[3:(len_argv-1)], attribute=argv[len_argv-1])
        #print(argv[3:(len_argv-1)])
    else:
        print ("Error wrong param %s"%argv[1])
        exit(-1)






