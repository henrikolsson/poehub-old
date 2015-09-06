#!/usr/bin/env python
import sys
import struct
import mmap
import copy
import os.path
from util.utils import *

class GGPK:
    def __init__(self, fn):
        self.fn = fn
        self.files = {}

    def read(self):
        self.fd = open(self.fn, "rb")
        self._read_header()
        self._read_entries()
        data = self.read_file("Data/SkillGems.dat")
        for fn in self.files:
            if fn.endswith(".dat"):
                with open(fn, "wb") as f:
                    data = self.read_file(fn)
                    f.write(data)
        self.fd.close()
        
    def read_file(self, fn):
        f = self.files[fn]
        self.fd.seek(f['offset'])
        return self.fd.read(f['size'])
        
    def _read_header(self):
        # Version U32 | Identifier 'GGPK' | Unknown U32 | Root offset U64 | Unknown U64
        data = read_struct(self.fd, "<I4sIQQ")
        self.header = {"version": data[0],
                       "identifier": data[1],
                       "root": data[3]}
        
    def _read_entries(self):
        self.fd.seek(self.header['root'])
        self._read_entry([])

    def _read_entry(self, path):
        curoffset = self.fd.tell()
        nextoffset, entry_type = read_struct(self.fd, '<I4s')
        if entry_type == b'PDIR':
            #print("dir")
            name_length, childcount = read_struct(self.fd, '<II')
            self.fd.seek(0x20, 1)
            name = self.fd.read(name_length * 2).decode("utf16").rstrip('\x00')
            #print(name_length, childcount)
            for i in range(childcount):
                _, childoffs = read_struct(self.fd, '<IQ')
                nextpos = self.fd.tell()
                #print("child offset", childoffs)
                self.fd.seek(childoffs)
                foo = copy.copy(path)
                if not name == "":
                    foo.append(name)
                self._read_entry(foo)
                self.fd.seek(nextpos)
        elif entry_type == b'FILE':
            #print("file")
            name_length = read_struct(self.fd, '<I')[0]
            self.fd.seek(0x20, 1)
            d = self.fd.read(name_length * 2)
            #print("cur: %d" % curoffset)
            #print("next: %d" % nextoffset)
            offs = self.fd.tell()
            size =  (curoffset + nextoffset) - offs
            #self.fd.seek(curoffset + nextoffset)
            name = d.decode("utf16").rstrip('\x00')
            foo = copy.copy(path)
            foo.append(name)
            s = "/".join(foo)
            self.files[s] = {"path": foo, "offset": offs, "size": size}
        elif entry_type == b'FREE':
            #print("free")
            pass
        else:
            print("unknown: %s" % entry_type)
