import sys

if sys.argv[2] == '1.0.0' or sys.argv[2] == '1.0.1':
    with open(sys.argv[1],'rb') as smm2binary:
        smm2data = smm2binary.read()
        smm2data = bytearray(smm2data)
        if sys.argv[2] == '1.0.0':
            smm2data[0x5AA7CF:8] = b'\x1f\x20\x03\xd5'
            with open(sys.argv[1],'wb') as smm2binary:
                smm2binary.write(smm2data)
                print('Nop Instruction Successfully Patched To 0x7100adffe4 [Offset 0x5AA7CF]!')
        if sys.argv[2] == '1.0.1':
            smm2data[0x5DF341:8] = b'\x1f\x20\x03\xd5'
            with open(sys.argv[1],'wb') as smm2binary:
                smm2binary.write(smm2data)
                print('Nop Instruction Successfully Patched To 0x7100b3ce00! [Offset 0x5DF341]')
else:
    print('Invalid Version Number!')
