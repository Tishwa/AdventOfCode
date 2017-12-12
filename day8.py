import sys
sys.dont_write_bytecode = True

TEST_SET_1 = {
    """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""": 1
}

TEST_SET_2 = {}

INPUT = open('input8.txt', 'r').read()


def parse_input(x):
    delimiter = '\t' if '\t' in x else ' '
    result = []
    for line in [l for l in x.split('\n') if len(l)>0]:
        instructions = line.split(delimiter)
        result.append({
            'var': instructions[0],
            'action': instructions[1],
            'value': instructions[2],
            'condition': {
                'var': instructions[4],
                'operator': instructions[5],
                'value': instructions[6]
            }
        })
    return result

def condition_is_met(condition, variables):
    var = variables[condition['var']] if condition['var'] in variables else 0
    op = condition['operator']
    value = int(condition['value'])
    if op == '>':
        return var > value
    elif op == '<':
        return var < value
    elif op == '>=':
        return var >= value
    elif op == '<=':
        return var <= value
    elif op == '==':
        return var == value
    elif op == '!=':
        return var != value

def execute_instruction_line(line, variables):
    if condition_is_met(line['condition'], variables):
        if line['var'] not in variables:
            variables[line['var']] = 0
        if line['action'] == 'inc':
            variables[line['var']] += int(line['value'])
        elif line['action'] == 'dec':
            variables[line['var']] -= int(line['value'])
    return variables


def solve_1(x):
    x = parse_input(x)
    variables = {}
    for line in x:
        variables = execute_instruction_line(line, variables)
    return max(variables.values())

def solve_2(x):
    return x