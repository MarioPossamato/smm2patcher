import sys

smm2patcher = sys.argv[1]
main_binary = sys.argv[2]

def remove_timer_check(): # Removes the annoying 'invalid time limit' check
    global smm2patcher,main_binary
    if main_binary == '1.0.0' or main_binary == '1.0.1':
        with open(smm2patcher,'rb') as smm2binary:
            smm2data = smm2binary.read()
            smm2data = bytearray(smm2data)
            if main_binary == '1.0.0':
                smm2data[0x5AA7CF:0x5AA7D3] = b'\x1f\x20\x03\xd5'
                with open(smm2patcher,'wb') as smm2binary:
                    smm2binary.write(smm2data)
                    print('Nop Instruction Successfully Patched To 0x7100adffe4 [Offset 0x5AA7CF]!')
            if main_binary == '1.0.1':
                smm2data[0x5DF341:0x5AA7D3] = b'\x1f\x20\x03\xd5'
                with open(smm2patcher,'wb') as smm2binary:
                    smm2binary.write(smm2data)
                    print('Nop Instruction Successfully Patched To 0x7100b3ce00! [Offset 0x5DF341]')
    else:
        print('Invalid Version Number!')

def change_koopa_state(state_int): # Change the state of a Koopa Troopa when spun on/hit with a shell, only on 1.0.1
    global smm2patcher,main_binary
    if main_binary == '1.0.1':
        with open(smm2patcher,'rb') as smm2binary:
            smm2data = smm2binary.read()
            smm2data = bytearray(smm2data)
            if state_int == 0:
                state = b'\x01\x00\x80\x52'
            if state_int == 1:
                state = b'\x21\x00\x80\x52'
            if state_int == 2:
                state = b'\x41\x00\x80\x52'
            if state_int == 3:
                state = b'\x61\x00\x80\x52'
            if state_int == 4:
                state = b'\x81\x00\x80\x52'
            if state_int == 5:
                state = b'\xA1\x00\x80\x52'
            if state_int == 6:
                state = b'\xC1\x00\x80\x52'
            if state_int == 7:
                state = b'\xE1\x00\x80\x52'
            if state_int == 8:
                state = b'\x01\x01\x80\x52'
            if state_int == 9:
                state = b'\x21\x01\x80\x52'
            if state_int == 10:
                state = b'\x01\x02\x80\x52'
            if state_int > 10:
                state = b'\x01\x02\x80\x52'
            smm2data[0x39DA3F:0x39DA43] = state
            with open(smm2patcher,'wb') as smm2binary:
                smm2binary.write(smm2data)
                print(str(state) + ' written to 0x71007b031c [0x39DA3F]')
    else:
        print('Invalid Version Number!')
