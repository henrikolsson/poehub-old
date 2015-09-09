import struct
import os.path
from util.utils import *
import configobj
import validate
import pprint
import sys

MAGIC = 0xBBbbBBbbBBbbBBbb

class Dat:
    def __init__(self):
        self.spec = configobj.ConfigObj(infile=relative_file("dat.specification.ini"),
                                        configspec=relative_file("dat.specification.configspec.ini"))
        self.spec.validate(validate.Validator())

    def _parse(self, fn):
        rec = None
        for rs in self.definitions.records.record:
            if fn.endswith("%s.dat" % rs.file):
                rec = rs
                break
        if rec is None:
            raise Exception("Missing record definition for %s" % fn)
        
        result = []
        size = os.path.getsize(fn)
        self.fd = open(fn, "rb")
        count = read_struct(self.fd, "<I")[0]
        if count == 0:
            return result
        record_length = 0
        data_section_offset = 0
        for i in range(size - 8):
            magic = read_struct(self.fd, "<Q")[0]
            if magic == MAGIC:
                data_section_offset = self.fd.tell() - 8
                record_length = i
                break
            # magic should be at least count bytes from here
            self.fd.seek(-8 + count, 1)
        if not record_length == rec.length:
            print("mismatched record length: %d, expected: %d" % (record_length, rec.length))

        for i in range(count):
            self.fd.seek(4 + record_length * i)
            ss = fields_to_struct(rs.field)
            data = read_struct(self.fd, ss)
            record = map_data(data_section_offset, rs.field, self.fd, data)
            result.append(record)
            
        self.fd.close()
        return result



    def parse(self, fn):
        rec = None
        for rs in self.spec:
            if fn.endswith("%s" % rs):
                rec = self.spec[rs]["fields"]
                break
        if rec is None:
            raise Exception("Missing record definition for %s" % fn)

        result = []
        size = os.path.getsize(fn)
        self.fd = open(fn, "rb")
        count = read_struct(self.fd, "<I")[0]
        if count == 0:
            return result
        record_length = 0
        data_section_offset = 0
        for i in range(size - 8):
            magic = read_struct(self.fd, "<Q")[0]
            if magic == MAGIC:
                data_section_offset = self.fd.tell() - 8
                record_length = i
                break
            # magic should be at least count bytes from here
            self.fd.seek(-8 + count, 1)
        #if not record_length == rec.length:
        #    print("mismatched record length: %d, expected: %d" % (record_length, rec.length))

        for i in range(count):
            self.fd.seek(4 + record_length * i)
            ss = fields_to_struct(rec)
            data = read_struct(self.fd, ss)
            record = map_data(data_section_offset, rec, self.fd, data)
            result.append(record)
            
        self.fd.close()
        return result

def read_field(fd, t):
    if t == "string":
        bs = bytearray()
        c = fd.read(2)
        if len(c) < 2:
            print("broken string!")
            return bs.decode("utf16")
        while c[0] > 0 or c[1] > 0:
            bs.append(c[0])
            bs.append(c[1])
            c = fd.read(2)
        return bs.decode("utf16")
    elif t == "long":
        return read_struct(fd, "q")[0]
    elif t == "ulong":
        return read_struct(fd, "Q")[0]
    elif t == "int":
        return read_struct(fd, "i")[0]
    elif t == "uint":
        return read_struct(fd, "I")[0]
    elif t == "byte":
        return read_struct(fd, "b")[0]
    elif t == "ubyte":
        return read_struct(fd, "B")[0]
    else:
        raise Exception("Unhandled field type: %s" % t)
        
def map_data(data_section_offset, fields, fd, data):
    record = {}
    idx = 0
    for k in fields:
        field = fields[k]
        if field['type'].startswith("ref|list"):
            length, offset = struct.unpack("2I", struct.pack("Q", data[idx]))
            fd.seek(data_section_offset + offset)
            subtype = field['type'].split("|")[2]
            result = []
            try:
                for i in range(length):
                    result.append(read_field(fd, subtype))
            except:
                print("error reading: %s" % k)
                raise
            record[k] = result
        elif field['type'].startswith("ref|"):
            subtype = field['type'].split("|")[1]
            fd.seek(data_section_offset + data[idx])
            record[k] = read_field(fd, subtype)
        else:
            record[k] = data[idx]
        idx = idx + 1
    return record

def fields_to_struct(fields):
    ss = "<"
    for field_name in fields:
        field = fields[field_name]
        if field['type'] == "long":
            ss = ss + "q"
        elif field['type'] == "ulong":
            ss = ss + "Q"
        elif field['type'] == "int":
            ss = ss + "i"
        elif field['type'] == "uint":
            ss = ss + "I"
        elif field['type'] == "byte":
            ss = ss + "b"
        elif field['type'] == "ubyte":
            ss = ss + "B"
        elif field['type'].startswith("ref|list"):
            ss = ss + "Q"
        elif field['type'].startswith("ref|"):
            ss = ss + "I"
        elif field['type'] == "bool":
            ss = ss + "?"
        else:
            raise Exception("unhandled type: %s" % field['type'])
    return ss

def relative_file(fn):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), fn)

if __name__ == "__main__":
    fn = sys.argv[1]
    dat = Dat()
    try:
        parsed = dat.parse(fn)
        for row in parsed:
            print(row)
    except:
        print("failed to parse: %s", fn)
        raise
    
