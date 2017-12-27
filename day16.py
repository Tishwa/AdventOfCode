import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    's3': 'nopabcdefghijklm',
    'x2/9': 'abjdefghicklmnop',
    'pc/g': 'abgdefchijklmnop',
    's1,x2/3,pe/b': 'pacedbfghijklmno'
}

TEST_SET_2 = {}

INPUT = open('input16.txt', 'r').read()

PROGRAMS = 'abcdefghijklmnop'


def parseInput(x):
    return x.replace('\n', '').split(',')

def dance(programs, instruction):
    if instruction[0] == 's':
        return spin(programs, instruction)
    if instruction[0] == 'x':
        return exchange(programs, instruction)
    if instruction[0] == 'p':
        return partner(programs, instruction)
    print 'Instruction not found:', instruction

def spin(programs, instruction):
    number_to_spin = int(instruction.replace('s', '')) % len(programs)
    moving_programs = programs[-number_to_spin:]
    static_programs = programs[:-number_to_spin]
    return moving_programs + static_programs

def exchange(programs, instruction):
    first_index, second_index = [int(i) for i in instruction[1:].split('/')]
    first_program = programs[first_index]
    second_program = programs[second_index]
    return rewrite_string(programs, first_index, second_index, second_program, first_program)

def partner(programs, instruction):
    first_program, second_program = [i for i in instruction[1:].split('/')]
    first_index = programs.index(first_program)
    second_index = programs.index(second_program)
    return rewrite_string(programs, first_index, second_index, second_program, first_program)

def rewrite_string(text, i, j, a, b):
    # Takes a text and set the letter in position i to a, and the letter in position j to b
    # ex: ('hillo zorld', 1, 6, 'e', 'w') => 'hello world'
    string_list = list(text)
    string_list[i] = a
    string_list[j] = b
    return ''.join(string_list)

def solve_1(x):
    instructions = parseInput(x)
    dancers = PROGRAMS
    for instruction in instructions:
        dancers = dance(dancers, instruction)
    return dancers

def solve_2(x):
    return x