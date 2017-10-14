def evaluate(char* code):
    bracemap = buildbracemap(code)

    cells = [0]
    cdef int codeptr = 0
    cdef int cellptr = 0

    while codeptr < len(code):
        command = code[codeptr]

        if command == ">":
            cellptr += 1
            if cellptr == len(cells): cells.append(0)

        if command == "<":
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        if command == "+":
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

        if command == "-":
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

        try:
            if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
            if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
        except KeyError:
            print code
            return None

        codeptr += 1

    return cells

def buildbracemap(char* code):
    temp_bracestack, bracemap = [], {}

    for position, command in enumerate(code):
        if command == "[": temp_bracestack.append(position)
        if command == "]":
            start = temp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap

def getRegister(wtv):
    tmp = ""
    number = ""
    for line in wtv:
        if "What value is" in line:
            tmp += line
    for char in tmp:
        if char.isdigit():
            number += char
    try:
        return int(number)
    except ValueError:
        return wtv

def getCode(x):
    bf = set(['<', '>', '+', '-', '[', ']'])
    tmp = ""
    for line in x:
        for char in line:
            if char in bf and line != "+-+-+-+-+-+-+-+-+-+-":
                tmp += line
                break
    return tmp

def decode(char* src):
    if len(src) == 0: return
    cdef int left = 0
    cdef int right = len(src) - 1
    arr = [0] * 16
    cdef int ptr = 0
    cdef int i = left
    while i <= right:
        s = src[i]
        if s == '>':
            ptr += 1
            # wrap if out of range
            if ptr >= len(arr):
                ptr = 0
        elif s == '<':
            ptr -= 1
            # wrap if out of range
            if ptr < 0:
                ptr = len(arr) - 1
        elif s == '+':
            if arr[ptr] == 255:
                arr[ptr] = 0
            else:
                arr[ptr] += 1
        elif s == '-':
            if arr[ptr] == 0:
                arr[ptr] = 255
            else:
                arr[ptr] -= 1
        elif s =='[':
            if arr[ptr] == 0:
                loop = 1
                while loop > 0:
                    i += 1
                    c = src[i]
                    if c == '[':
                        loop += 1
                    elif c == ']':
                        loop -= 1
        elif s == ']':
            loop = 1
            while loop > 0:
                i -= 1
                c = src[i]
                if c == '[':
                    loop -= 1
                elif c == ']':
                    loop += 1
            i -= 1
        i += 1
    return arr