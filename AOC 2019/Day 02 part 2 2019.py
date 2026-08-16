
for i in range(100):
    for j in range(100):
        opcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,10,23,2,13,23,27,1,5,27,31,2,6,31,35,1,6,35,39,2,39,9,43,1,5,43,47,1,13,47,51,1,10,51,55,2,55,10,59,2,10,59,63,1,9,63,67,2,67,13,71,1,71,6,75,2,6,75,79,1,5,79,83,2,83,9,87,1,6,87,91,2,91,6,95,1,95,6,99,2,99,13,103,1,6,103,107,1,2,107,111,1,111,9,0,99,2,14,0,0]
        opcode[1] = i
        opcode[2] = j
        #print(len(opcode))
        #opcode = [1,9,10,3,2,3,11,0,99,30,40,50]
        curr_indent = 0
        while curr_indent<len(opcode)-2:
            replacer = opcode[curr_indent+3]
            #print(replacer)
            dig_1 = opcode[curr_indent+1]
            dig_2 = opcode[curr_indent+2]
            if opcode[curr_indent] == 1:
                curr_total = opcode[dig_1] + opcode[dig_2]
                opcode[replacer] = curr_total
            elif opcode[curr_indent] == 2:
                curr_total = opcode[dig_1] * opcode[dig_2]
                opcode[replacer] = curr_total
            elif opcode[curr_indent] == 99:
                curr_indent += 1
            if curr_total == 19690720:
                print((opcode[1]*100)+opcode[2])
                break
            if opcode[curr_indent] != 99:
                curr_indent += 4
