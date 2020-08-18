#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SMM2Patcher
# A Code Patcher For The Super Mario Maker 2 Binary.
# Version 0.2
# Created by MarioPossamato

# This file is part of SMM2Patcher.

# All Modifications In This Script Are For Either Version 2.0.0 Or 3.0.0 Of Super Mario Maker 2.
# To Apply Modifications Manually, I Recommend Using HxD Hex Editor <https://mh-nexus.de/downloads/HxDSetup.zip>.

# To Find These Offsets Using HxD, Use Ctrl+G (Goto), And Paste In The Offset.  Then, Copy The Data Press Ctrl+B (Paste Overrite).
# Alternatively, You Can Use HxD's Ctrl+E (Select Block), Paste In The Start And End Offsets, Then Right Click On The Selected Block, Click Fill Selection, Then Place The Data In There To Fill The Selection.

# Please Note That None Of The Modifications In This Script Will Work If Your Copy Of Block.rpx Is Not Decompressed!  Use wiiurpxtool <https://github.com/0CBH0/wiiurpxtool/releases>.

SMM1PatcherVersion = '0.2'

import sys
import struct



# Function To Convert Float To Hex
def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])[2:]

# Function To Convert Hex To Float
def hex_to_float(i):
    return struct.unpack('!f', int.to_bytes(i, 0x4, 'big'))[0]

# Create Dictionaries

# Useful Known Variables, Found By Mario Possamato

dict_0 = {'2.0.0':{'start_offset':0x251587D, 'end_offset':0x2515881},'3.0.0':{'start_offset':0x29614A1, 'end_offset':0x29614A5, 'size':0x4,}, 'size':0x4, 'default':0x3F800000, 'description':'SM3DW camera rotation', 'affected_modes':['3W']}

# Useful Known Variables, Found By Comex

dict_1 = {'2.0.0':{'start_offset':0x14D4391, 'end_offset':0x14D4395},'3.0.0':{'start_offset':0x16D28FD, 'end_offset':0x16D2901, 'size':0x4,}, 'size':0x4, 'default':0x08318A1A, 'description':'Remove Edit Mode Play Invalid Time Limit Check, Set To 0x1F2003D5', 'affected_modes':['M1','M3','MW','WU','3W']}
dict_2 = {'2.0.0':{'start_offset':0x15924C1, 'end_offset':0x15924C9},'3.0.0':{'start_offset':0x17BA221, 'end_offset':0x17BA229, 'size':0x4,}, 'size':0x4, 'default':0xFC0F1AF8FA6701A9, 'description':'No Corrupt Course Check, Set To 0x200080D2C0035FD6', 'affected_modes':['M1','M3','MW','WU','3W']}

# Create Function To Write Data
def Modify(x, y, z):
    with open(sys.argv[1],'rb') as file:
        data = bytearray(file.read())
        data[x[str(z)]['start_offset']:x[str(z)]['end_offset']] = int.to_bytes(y)
        with open(sys.argv[1],'wb') as file:
            file.write(data)

print('SMM2Patcher (Version 0.2)')
