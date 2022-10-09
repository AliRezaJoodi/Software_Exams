# https://github.com/AliRezaJoodi
def arithmetic_arranger(problems_initial, status=False):

    # Check the number of problems_initial
    if len(problems_initial) > 5:
        return "Error: Too many problems."
    
    # Separate problems
    first_number = []
    second_number = []
    operator = []
    for problem in problems_initial:
        pieces = problem.split()
        first_number.append(pieces[0])
        operator.append(pieces[1])
        second_number.append(pieces[2])

    # Check for * or /
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    # Does each operand is containing digits?
    for i in range(len(first_number)):
        if not (first_number[i].isdigit() and second_number[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Check the length
    for i in range(len(first_number)):
        if len(first_number[i]) > 4 or len(second_number[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Formatting first line to right-aligned
    first_line = []
    for i in range(len(first_number)):
        if len(first_number[i]) > len(second_number[i]):
            first_line.append("  " + first_number[i])
        else:
            first_line.append("  "+ " "*(len(second_number[i]) - len(first_number[i])) + first_number[i])

    # Formatting second line to right-aligned
    second_line = []
    for i in range(len(second_number)):
        if len(second_number[i]) > len(first_number[i]):
            second_line.append(operator[i] + " " + second_number[i])
        else:
            second_line.append(operator[i] + " "+ " "*(len(first_number[i]) - len(second_number[i])) + second_number[i])

    # Formatting third line
    third_line = []
    for i in range(len(first_number)):
        third_line.append("--" + "-"*(max(len(first_number[i]), len(second_number[i]))))

    fourth_line = []
    if status==True:
        for i in range(len(first_number)):
            # Calculate answer
            if operator[i] == "+":
                answer = str(int(first_number[i]) + int(second_number[i]))
            else:
                answer = str(int(first_number[i]) - int(second_number[i])) 

            # Formatting fourth line to right-aligned  
            if len(answer) > max(len(first_number[i]), len(second_number[i])):
                fourth_line.append(" " + answer)
            else:
                fourth_line.append("  " + " "*(max(len(first_number[i]), len(second_number[i])) - len(answer)) + answer)    
      
    # Formatting return value
    if status==True:
        problems_vertical = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        problems_vertical = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
    
    # Ending code
    return problems_vertical
