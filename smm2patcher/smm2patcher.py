import sys, struct, binascii
from binascii import hexlify, unhexlify
from ctypes import *

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

def double_to_hex(f):
    return hex(struct.unpack('<Q', struct.pack('<d', f))[0])

def convert(s):
    i = int(s, 16)
    cp = pointer(c_int(i))
    fp = cast(cp, POINTER(c_float))
    return fp.contents.value

main_binary = sys.argv[1]
uncompressed_main_binary = main_binary + '_uncompressed'

def Remove_Edit_Mode_Timer_Check(): # Removes the annoying 'invalid time limit' check for SMM2's edit mode
    global uncompressed_main_binary
    with open(uncompressed_main_binary,'rb') as smm2binary:
        smm2data = smm2binary.read()
        smm2data = bytearray(smm2data)
        smm2data[0x14D4391:0x14D4395] = b'\x1f\x20\x03\xd5'
        with open(uncompressed_main_binary,'wb') as smm2binary:
            smm2binary.write(smm2data)
            print("Successfully Removed Edit Mode's Invalid Timer Check!")

def Remove_Corrupted_Course_Check(): # Removes the annoying 'corrupted course' check for SMM2
    global uncompressed_main_binary
    with open(uncompressed_main_binary,'rb') as smm2binary:
        smm2data = smm2binary.read()
        smm2data = bytearray(smm2data)
        smm2data[0x15924C1:0x15924C9] = b'\x20\x00\x80\xD2\xC0\x03\x5F\xD6'
        with open(uncompressed_main_binary,'wb') as smm2binary:
            smm2binary.write(smm2data)
            print("Successfully Removed Corrupted Course Check!")