import System
import structure_form as sf


class Node:
    def __init__(self, name, expand=False):
        self.name = name
        self.expand = expand

    def __enter__(self):
        sf.StartNode(self.name)

    def __exit__(self, exc_type, exc_value, traceback):
        sf.EndNode(self.expand)


def AddByte(name):
    return sf.ReadToNode[System.Byte](name)


def AddSByte(name):
    return sf.ReadToNode[System.SByte](name)


def AddUShort(name):
    return sf.ReadToNode[System.UInt16](name)


def AddShort(name):
    return sf.ReadToNode[System.Int16](name)


def AddUInt(name):
    return sf.ReadToNode[System.UInt32](name)


def AddInt(name):
    return sf.ReadToNode[System.Int32](name)


def AddULong(name):
    return sf.ReadToNode[System.UInt64](name)


def AddLong(name):
    return sf.ReadToNode[System.Int64](name)


def AddFloat(name):
    return sf.ReadToNode[System.Single](name)


def AddDouble(name):
    return sf.ReadToNode[System.Double](name)


def AddBool(name):
    return sf.ReadToNode[System.Boolean](name)


def AddString(name):
    return sf.AddString(name)


def AddUnicodeString(name):
    return sf.AddUnicodeString(name)


def StartNode(name):
    sf.StartNode(name)


def EndNode(expand=False):
    sf.EndNode(expand)


def AddField(name, length=0):
    sf.AddField(name, length)


def Log(message, level="Info"):
    sf.Log(message, level)


def Remaining():
    return sf.Remaining()
