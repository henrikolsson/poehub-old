import struct

def read_struct(fd, fmt):
    data = fd.read(struct.calcsize(fmt))
    return struct.unpack(fmt, data)
