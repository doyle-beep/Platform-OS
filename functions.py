import platform
import os
import sys


def platcomprehensive():
    allthings = []

    proc = platform.processor()
    allthings.append(("Processor Family: ", proc))

    syste = platform.system()
    allthings.append(("Operating System: ", syste))

    machine = platform.machine()
    allthings.append(("Machine: ", machine))

    arch = platform.architecture()
    allthings.append(("Architecture: ", arch))

    nod = platform.node()
    allthings.append(("Node: ", nod))

    plat = platform.platform()
    allthings.append(("Platform: ", plat))

    build = platform.python_build()
    allthings.append(("Python Build: ", build, ".python_build"))

    compiler = platform.python_compiler()
    allthings.append(("Python Compiler: ", compiler, ".python_compiler"))

    implementation = platform.python_implementation()
    allthings.append(("Python Implementation: ", implementation))

    pyversion = platform.python_version()
    allthings.append(("Python Version: ", pyversion))

    version = platform.version()
    allthings.append(("Version: ", version))

    return allthings




def oscomprehensive():
    allthings = []

    pwd = os.getcwd()
    allthings.append(("Current Working Directory: ", pwd))

    getlogin = os.getlogin()
    allthings.append(("Current User: ", getlogin))

    uname = os.uname()
    allthings.append(("Uname: ", uname))


    cpu_count = os.cpu_count()
    allthings.append(("CPU Count: ", cpu_count))

    getloadavg = os.getloadavg()
    allthings.append(("Load Average: ", getloadavg))

    return allthings

def systhings():
    allthings = []

    byteorder = sys.byteorder
    allthings.append(("Byte Order: ", byteorder))

    return allthings
