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

def Change_SM3DW_Camera_Rotation(float):
    global main_binary
    hex = hex(struct.unpack('<I', struct.pack('<f', float))[0])
    hex = bytes(hex)
    hex = bytearray(hex)
    hex.reverse()
    hex = bytes(hex)
    with open(main_binary,'rb') as smm2binary:
        smm2data = smm2binary.read()
        smm2data = bytearray(smm2data)
        smm2data[0x2516311:0x2516315] = b'\x1f\x20\x03\xd5'
        with open(main_binary,'wb') as smm2binary:
            smm2binary.write(smm2data)
            print('Done!')
    

def Remove_Edit_Mode_Timer_Check(): # Removes the annoying 'invalid time limit' check for SMM2's edit mode
    global main_binary
    with open(main_binary,'rb') as smm2binary:
        smm2data = smm2binary.read()
        smm2data = bytearray(smm2data)
        smm2data[0x14D4391:0x14D4395] = b'\x1f\x20\x03\xd5'
        with open(main_binary,'wb') as smm2binary:
            smm2binary.write(smm2data)
            print('Nop Instruction Successfully Patched To 0x14D4390!')

def Remove_Corrupted_Course_Check(): # Removes the annoying 'corrupted course' check for SMM2
    global main_binary
    with open(main_binary,'rb') as smm2binary:
        smm2data = smm2binary.read()
        smm2data = bytearray(smm2data)
        smm2data[0x15924C1:0x15924C9] = b'\x20\x00\x80\xD2\xC0\x03\x5F\xD6'
        with open(main_binary,'wb') as smm2binary:
            smm2binary.write(smm2data)
            print('Successfully Removed Corrupted Course Check!')
