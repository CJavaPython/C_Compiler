import sys
#terminal
#token type matching
vtype = 'vtype'
num = 'int'
id = 'id'
#terminals : 'if', 'else', 'while', 'for', 'return'
literal = 'literal'
addsub = 'addsub'
multdiv = 'multdiv'
assign = 'assign'
comp = 'comp'
semi = 'semi'
comma = 'comma'
lparen = 'lparen'
rparen = 'rparen'
lbrace = 'lbrace'
rbrace = 'rbrace'
float = 'float'

# non terminals
CODE = 'CODE'
VDECL = 'VDECL'
ASSIGN = 'ASSIGN'
FDECL = 'FDECL'
ARG = 'ARG'
MOREARGS = 'MOREARGS'
BLOCK = 'BLOCK'
STMT = 'STMT'
ELSE = 'ELSE'
RHS = 'RHS'
EXPR = 'EXPR'
TERM = 'TERM'
FACTOR = 'FACTOR' 
COND  = 'COND' 
RETURN = 'RETURN'
#goto : in stack, new state push
def goto(state):
    stack.append(state)
#shift : goto and bar
def shift(state, bar):
    bar += 1
    goto(state)
    return bar
#"goto" after reduce
#only terminals
def R_goto(cur_state, next, bar):
    if cur_state == 1:
        if next == VDECL:
            goto(77)
        elif next == FDECL:
            goto(78)
        elif next == CODE:
            goto(85)

    if cur_state == 2:
        if next == ASSIGN:
            goto(4)

    elif cur_state == 7:
        if next == RHS:
            goto(8)
        elif next == EXPR:
            goto(10)
        elif next == TERM:
            goto(11)
        elif next == FACTOR:
            goto(14)
    elif cur_state == 12:
        if next == EXPR:
            goto(13)
        elif next == TERM:
            goto(11)
        elif next == FACTOR:
            goto(14)
    
    elif cur_state == 15:
        if next == TERM:
            goto(16)
        elif next == FACTOR:
            goto(14)

    elif cur_state == 17:
        if next == EXPR:
            goto(18)
        elif next == TERM:
            goto(11)
        elif next == FACTOR:
            goto(14)

    elif cur_state == 23:
        if next == ARG:
            goto(31)

    elif cur_state == 25:
        if next == MOREARGS:
            goto(26)

    elif cur_state == 29:
        if next == MOREARGS:
            goto(30)

    elif cur_state == 33:
        if next == BLOCK:
            goto(34)
        elif next == VDECL:
            goto(40)
        elif next == ASSIGN:
            goto(41)
        elif next == STMT:
            goto(83)
        elif next == RETURN:
            goto(35)

    elif cur_state == 34:
        if next == RETURN:
            goto(35)

    elif cur_state == 37:
        if next == FACTOR:
            goto(38)

    elif cur_state == 44:
        if next == FACTOR:
            goto(51)
        elif next == COND:
            goto(45)

    elif cur_state == 47:
        if next == BLOCK:
            goto(48)
        elif next == ASSIGN:
            goto(41)
        elif next == STMT:
            goto(83)
        elif next == VDECL:
            goto(40)
    
    elif cur_state == 49:
        if next == ELSE:
            goto(50)
    
    elif cur_state == 52:
        if next == FACTOR:
            goto(53)

    elif cur_state == 55:
        if next == BLOCK:
            goto(56)
        elif next == ASSIGN:
            goto(41)
        elif next == STMT:
            goto(83)
        elif next == VDECL:
            goto(40)

    elif cur_state == 59:
        if next == COND:
            goto(60)
        elif next == FACTOR:
            goto(51)

    elif cur_state == 62:
        if next == BLOCK:
            goto(63)
        if next == STMT:
            goto(83)
        elif next == VDECL:
            goto(40)
        elif next == ASSIGN:
            goto(41)
            
    elif cur_state == 66:
        if next == ASSIGN:
            goto(67)
    elif cur_state == 68:
        if next == COND:
            goto(69)
        elif next == FACTOR:
            goto(51)
    elif cur_state == 70:
        if next == ASSIGN:
            goto(71)

    elif cur_state == 73:
        if next == BLOCK:
            goto(74)
        if next == STMT:
            goto(83)
        elif next == VDECL:
            goto(40)
        elif next == ASSIGN:
            goto(41)

    elif cur_state == 77:
        if next == CODE:
            goto(79)
        elif next == VDECL:
            goto(77)
        elif next == FDECL:
            goto(78)

    elif cur_state == 78:
        if next == CODE:
            goto(80)    
        elif next == VDECL:
            goto(77)
        elif next == FDECL:
            goto(78)

    elif cur_state == 81:
        if next == ASSIGN:
            goto(4)

    elif cur_state == 83:
        if next == STMT:
            goto(83)
        elif next == VDECL:
            goto(40)
        elif next == ASSIGN:
            goto(41)
        elif next == BLOCK:
            goto(84)

    

#epsilon? : -> true
ep1 = False        #CODE's epsilon
ep5 = False        #ARG's epsilon
ep6 = False        #MOREARGS's epsilon
ep7 = False        #BLOCK's epsilon
ep12 = False       #ELSE's epsilon
epsilon = []       #epsilon's list
epsilon.append(ep1)
epsilon.append(ep5)
epsilon.append(ep6)
epsilon.append(ep7)
epsilon.append(ep12)

#reduce before goto
#Reduce to CFG
def R(cur_state, cfg, bar):
    i = 1
    #1. CODE -> VDECL CODE | FDECL CODE | epsilon 
    if cfg == 1:
        while i <= bar:
            #CODE -> VDECL CODE
            if input1[bar - i - 1] == VDECL and input1[bar - i] == CODE:
                next = CODE
                input1.pop(bar - i)
                input1[bar - i - 1] = next
                for j in range(2):
                    stack.pop()
                bar = bar - 2 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #CODE -> FDECL CODE
            elif input1[bar - i - 1] == FDECL and input1[bar - i] == CODE:
                next = CODE
                input1.pop(bar - i)
                input1[bar - i - 1] = next
                for j in range(2):
                    stack.pop()
                bar = bar - 2 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #bar - i can zero so.
            #CODE -> epsilon
            elif input1[bar - i] == VDECL:
                next = CODE
                epsilon[0] = False
                #CODE, $ only
                input1[bar - i] = next
                stack.pop()
                bar = bar - 1 + 1	
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            elif input1[bar - i] == FDECL:
                next = CODE
                epsilon[0] = False
                #CODE, $ only
                input1[bar - i] = next
                stack.pop()
                bar = bar - 1 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
                
            i += 1
	#no input inside
	if epsilon[0] == True and len(input1) == 1:
		next = CODE
		epsilon[0] = False
		if input1[bar] == '$':
			input1.append('$')
		input1[bar] = next
		R_goto(cur_state, next, bar)
		return bar
        epsilon[0] = True
        return bar


    #02: VDECL -> vtype id semi | vtype ASSIGN semi
    elif cfg == 2:
        while i <= bar:
            #VDECL -> vtype id semi
            if bar - i > 1 and input1[bar - i - 2] == vtype and input1[bar - i - 1] == id and input1[bar - i] == semi: 
                next = VDECL
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #VDECL -> vtype ASSIGN semi
            elif bar-i > 1 and input1[bar - i - 2] == vtype and input1[bar - i - 1] == ASSIGN and input1[bar - i] == semi:
                next = VDECL
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar 
            i += 1
        error = "CFG2 ERROR"
        print("reject")
        
        return bar
    #03: ASSIGN -> id assign RHS
    elif cfg == 3:
        while i <= bar:
            if bar - i > 1 and input1[bar - i - 2] == id and input1[bar - i - 1] == assign and input1[bar - i] == RHS: 
                next = ASSIGN
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        error = "CFG3 ERROR"
        print("reject")
        return bar
    #FDECL : pop num change according to epsilon!
    #4. FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace 
    #epsilon check : ARG and BLOCK
    elif cfg == 4:
        while i <= bar:
            #no epsilon
            if bar - i > 7 and input1[bar - i - 8] == vtype and input1[bar - i - 7] == id and input1[bar - i - 6] == lparen and input1[bar - i - 5] == ARG and input1[bar - i - 4] == rparen and input1[bar - i - 3] == lbrace and input1[bar - i - 2] == BLOCK and input1[bar - i - 1] == RETURN and input1[bar - i] == rbrace:
                next = FDECL
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1.pop(bar - i - 5)
                input1.pop(bar - i - 6)
                input1.pop(bar - i - 7)
                input1[bar - i - 8] = next
                for j in range(9):
                    stack.pop()
                bar = bar - 9 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #ARG : epsilon
            elif bar - i > 6 and input1[bar - i - 7] == vtype and input1[bar - i - 6] == id and input1[bar - i - 5] == lparen and input1[bar - i - 4] == rparen and input1[bar - i - 3] == lbrace and input1[bar - i - 2] == BLOCK and input1[bar - i - 1] == RETURN and input1[bar - i] == rbrace:
                next = FDECL
                epsilon[1] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1.pop(bar - i - 5)
                input1.pop(bar - i - 6)
                input1[bar - i - 7] = next
                for j in range(8):
                    stack.pop()
                bar = bar - 8 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #BLOCK :  epsilon
            elif bar - i > 6 and input1[bar - i - 7] == vtype and input1[bar - i - 6] == id and input1[bar - i - 5] == lparen and input1[bar - i - 4] == ARG and input1[bar - i - 3] == rparen and input1[bar - i - 2] == lbrace and input1[bar - i - 1] == RETURN and input1[bar - i] == rbrace:
                next = FDECL
                epsilon[3] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1.pop(bar - i - 5)
                input1.pop(bar - i - 6)
                input1[bar - i - 7] = next
                for j in range(8):
                    stack.pop()
                bar = bar - 8 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #Both epsilon
            elif bar - i > 5 and input1[bar - i - 6] == vtype and input1[bar - i - 5] == id and input1[bar - i - 4] == lparen and input1[bar - i - 3] == rparen and input1[bar - i - 2] == lbrace and input1[bar - i - 1] == RETURN and input1[bar - i] == rbrace:
                next = FDECL
                epsilon[1] = False
                epsilon[3] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1.pop(bar - i - 5)
                input1[bar - i - 6] = next
                for j in range(7):
                    stack.pop()
                bar = bar - 7 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1

        error = "CFG4 ERROR"
        print("reject")       
        return bar
        
    #5. ARG -> vtype id MOREARGS | epsilon 
    elif cfg == 5:
        while i <= bar:
            #ARG -> vtype id MOREARGS
            if bar - i > 1 and input1[bar - i - 2] == vtype and input1[bar - i - 1] == id and input1[bar - i] == MOREARGS:
                next = ARG
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #ARG -> vtype id epsilon
            #MOREARGS : epsilon
            elif input1[bar - i - 1] == vtype and input1[bar - i] == id:
                next = ARG
                epsilon[2] = False
                input1.pop(bar - i)
                input1[bar - i - 1] = next
                for j in range(2):
                    stack.pop()
                bar = bar - 2 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        #ARG -> epsilon
        epsilon[1] = True
        next = ARG
        R_goto(cur_state, next, bar)
        return bar

    #6. MOREARGS -> comma vtype id MOREARGS | epsilon 
    elif cfg == 6:
        while i <= bar:
            #MOREARGS -> comma vtype id MOREARGS
            if bar - i > 2 and input1[bar - i - 3] == comma and input1[bar - i - 2] == vtype and input1[bar - i - 1] == id and input1[bar - i] == MOREARGS:
                next = MOREARGS
                epsilon[2] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1[bar - i - 3] = next
                for j in range(4):
                    stack.pop()
                bar = bar - 4 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #MOREARGS -> comma vtype id epsilon
            elif bar - i > 1 and input1[bar - i - 2] == comma and input1[bar - i - 1] == vtype and input1[bar - i] == id and epsilon[2] == True:
                next = MOREARGS
                epsilon[2] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        #MOREARGS -> epsilon
        epsilon[2] = True
        next = input1[bar]
        cur_state = stack[len(stack) - 1]
        R_goto(cur_state, next, bar)
        return bar

    #7. BLOCK -> STMT BLOCK | epsilon 
    elif cfg == 7:
        while i <= bar:
            if input1[bar - i - 1] == STMT and input1[bar - i] == BLOCK:
                next = BLOCK
                epsilon[3] = False
                input1.pop(bar - i)
                input1[bar - i - 1] = next
                for j in range(2):
                    stack.pop()
                bar = bar - 2 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            elif input1[bar - i] == STMT and epsilon[3] == True:
                next = BLOCK
                epsilon[3] = False
                input1[bar - i] = next
                stack.pop()
                bar = bar - 1 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        epsilon[3] = True
        next = input1[bar]
        cur_state = stack[len(stack) - 1]
        R_goto(cur_state, next, bar)
        return bar
            
    #8. STMT -> VDECL | ASSIGN semi 
    elif cfg == 8:
        while i <= bar:
            if input1[bar - i] == VDECL:
                epsilon[3] = False
                next = STMT
                input1[bar - i] = next
                stack.pop()
                bar = bar - 1 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            elif input1[bar - i - 1] == ASSIGN and input1[bar - i] == semi:
                epsilon[3] = False
                next = STMT
                input1.pop(bar - i)
                input1[bar - i - 1] = next
                for j in range(2):
                    stack.pop()
                bar = bar - 2 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        error = "CFG8 ERROR"
        print("reject")
        return bar
    #check BLOCK epsilon
    #9. STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
    elif cfg == 9:
        while i <= bar:
            #no epsilon
            if bar - i > 6 and input1[bar - i - 7] == 'if' and input1[bar - i - 6] == lparen and input1[bar - i - 5] == COND and input1[bar - i - 4] == rparen and input1[bar - i - 3] == lbrace and input1[bar - i - 2] == BLOCK and input1[bar - i - 1] == rbrace and input1[bar - i] == ELSE:
                next = STMT
                epsilon[3] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1.pop(bar - i - 5)
                input1.pop(bar - i - 6)
                input1[bar - i - 7] = next
                for j in range(8):
                    stack.pop()
                bar = bar - 8 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #BLOCK epsilon
            elif bar - i > 5 and input1[bar - i - 6] == 'if' and input1[bar - i - 5] == lparen and input1[bar - i - 4] == COND and input1[bar - i - 3] == rparen and input1[bar - i - 2] == lbrace and input1[bar - i - 1] == rbrace and input1[bar - i] == ELSE:
                next = STMT
                epsilon[3] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1.pop(bar - i - 5)
                input1[bar - i - 6] = next
                for j in range(7):
                    stack.pop()
                bar = bar - 7 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #ELSE epsilon
            elif bar - i > 5 and input1[bar - i - 6] == 'if' and input1[bar - i - 5] == lparen and input1[bar - i - 4] == COND and input1[bar - i - 3] == rparen and input1[bar - i - 2] == lbrace and input1[bar - i - 1] == BLOCK and input1[bar - i] == rbrace:
                next = STMT
                epsilon[3] = False
                epsilon[4] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1.pop(bar - i - 5)
                input1[bar - i - 6] = next
                for j in range(7):
                    stack.pop()
                bar = bar - 7 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #Both epsilon
            elif bar - i > 4 and input1[bar - i - 5] == 'if' and input1[bar - i - 4] == lparen and input1[bar - i - 3] == COND and input1[bar - i - 2] == rparen and input1[bar - i - 1] == lbrace and input1[bar - i] == rbrace:
                next = STMT
                epsilon[3] = False
                epsilon[4] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1[bar - i - 5] = next
                for j in range(6):
                    stack.pop()
                bar = bar - 6 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        error = "CFG9 ERROR"
        print("reject")
        return bar
        
    #10. STMT -> while lparen COND rparen lbrace BLOCK rbrace 
    elif cfg == 10:
        while i <= bar:
            #no epsilon 
            if bar - i > 5 and input1[bar - i - 6] == 'while' and input1[bar - i - 5] == lparen and input1[bar - i - 4] == COND and input1[bar - i - 3] == rparen and input1[bar - i - 2] == lbrace and input1[bar - i - 1] == BLOCK and input1[bar - i] == rbrace:
                next = STMT
                epsilon[3] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1.pop(bar - i - 5)
                input1[bar - i - 6] = next
                for j in range(7):
                    stack.pop()
                bar = bar - 7 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #BLOCK epsilon
            elif bar - i > 4 and input1[bar - i - 5] == 'while' and input1[bar - i - 4] == lparen and input1[bar - i - 3] == COND and input1[bar - i - 2] == rparen and input1[bar - i - 1] == lbrace and input1[bar - i] == rbrace:
                next = STMT
                epsilon[3] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1[bar - i - 5] = next
                for j in range(6):
                    stack.pop()
                bar = bar - 6 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        error = "CFG10 ERROR"
        print("reject")        
        return bar

    #STMT -> for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace 
    elif cfg == 11:
        while i <= bar:
            #no epsilon
            if bar - i > 9 and input1[bar - i - 10] == 'for' and input1[bar - i - 9] == lparen and input1[bar - i - 8] == ASSIGN and input1[bar - i - 7] == semi and input1[bar - i - 6] == COND and input1[bar - i - 5] == semi and input1[bar - i - 4] == ASSIGN and input1[bar - i - 3] == rparen and input1[bar - i - 2] == lbrace and input1[bar - i - 1] == BLOCK and input1[bar - i] == rbrace:
                next = STMT
                epsilon[3] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1.pop(bar - i - 5)
                input1.pop(bar - i - 6)
                input1.pop(bar - i - 7)
                input1.pop(bar - i - 8)
                input1.pop(bar - i - 9)
                input1[bar - i - 10] = next
                for j in range(11):
                    stack.pop()
                bar = bar - 11 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #BLOCK epsilon
            elif bar - i > 8 and input1[bar - i - 9] == 'for' and input1[bar - i - 8] == lparen and input1[bar - i - 7] == ASSIGN and input1[bar - i - 6] == semi and input1[bar - i - 5] == COND and input1[bar - i - 4] == semi and input1[bar - i - 3] == ASSIGN and input1[bar - i - 2] == rparen and input1[bar - i - 1] == lbrace and input1[bar - i] == rbrace:
                next = STMT
                epsilon[3] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1.pop(bar - i - 3)
                input1.pop(bar - i - 4)
                input1.pop(bar - i - 5)
                input1.pop(bar - i - 6)
                input1.pop(bar - i - 7)
                input1.pop(bar - i - 8)
                input1[bar - i - 9] = next
                for j in range(10):
                    stack.pop()
                bar = bar - 10 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        error = "CFG11 ERROR"
        print("reject")        
        return bar
    
    #12. ELSE -> else lbrace BLOCK rbrace | epsilon 
    elif cfg == 12:
        while i <= bar:
            #no epsilon
            if bar - i > 2 and input1[bar - i - 3] == 'else' and input1[bar - i - 2] == lbrace and input1[bar - i - 1] == BLOCK and input1[bar - i] == rbrace:
                next = ELSE
                epsilon[3] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1.pop(bar - i - 2)
                input1[bar - i - 3] = next
                for j in range(4):
                    stack.pop()
                bar = bar - 4 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #BLOCK epsilon
            elif bar - i > 1 and input1[bar - i - 2] == 'else' and input1[bar - i - 1] == lbrace and input1[bar - i] == rbrace:
                next = ELSE
                epsilon[3] = False
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar    
            i += 1
        #ELSE -> epsilon
        epsilon[4] = True
        next = ELSE
        R_goto(cur_state, next, bar)
        return bar

    #13. RHS ->  EXPR | literal
    elif cfg == 13:
        while i <= bar:
            #RHS -> EXPR
            if input1[bar - i] == EXPR:
                next = RHS
                input1[bar - i] = next
                stack.pop()
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                bar = bar
                return bar
            #RHS -> literal
            elif input1[bar - i] == literal:
                next = RHS
                input1[bar - i] = next
                stack.pop()
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                bar = bar
                return bar
            i += 1
        error = "CFG13 ERROR"
        print("reject")        
        return bar
    #14. EXPR -> TERM addsub EXPR | TERM 
    elif cfg == 14:
        while i <= bar:
            #EXPR -> TERM addsub EXPR
            if bar - i > 1 and input1[bar - i - 2] == TERM and input1[bar - i - 1] == addsub and input1[bar - i] == EXPR:
                next = EXPR
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #EXPR -> TERM
            elif input1[bar - i] == TERM:
                next = EXPR
                input1[bar - i] = next
                stack.pop()
                bar = bar
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        error = "CFG14 ERROR"
        print("reject")        
        return bar
    #15. TERM -> FACTOR multdiv TERM | FACTOR 
    elif cfg == 15:
        while i <= bar:
            #TERM -> FACTOR multdiv TERM
            if bar - i > 1 and input1[bar - i - 2] == FACTOR and input1[bar - i - 1] == multdiv and input1[bar - i] == TERM: 
                next = TERM
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #TERM -> FACTOR
            elif input1[bar - i] == FACTOR:
                next = TERM
                input1[bar - i] = next
                stack.pop()
                bar = bar
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        error = "CFG15 ERROR"
        print("reject")        
        return bar
    #16. FACTOR -> lparen EXPR rparen | id | num | float 
    elif cfg == 16:
        while i <= bar:
            #FACTOR -> lparen EXPR rparen
            if bar - i > 1 and input1[bar - i - 2] == lparen and input1[bar - i - 1] == EXPR and input1[bar - i] == rparen: 
                next = FACTOR
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            #FACTOR -> id
            elif input1[bar - i] == id:
                next = FACTOR
                input1[bar - i] = next
                stack.pop()
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                bar = bar - 1 + 1
                return bar
            #FACTOR -> num
            elif input1[bar - i] == num: 
                next = FACTOR
                input1[bar - i] = next
                stack.pop()
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                bar = bar - 1 + 1
                return bar
            #FACTOR -> float
            elif input1[bar - i] == float: 
                next = FACTOR
                input1[bar - i] = next
                stack.pop()
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                bar = bar - 1 + 1
                return bar
            i += 1
        error = "CFG16 ERROR"
        print("reject")        
        return bar
    #17. COND -> FACTOR comp FACTOR   
    elif cfg == 17:
        while i <= bar:
            if bar - i > 1 and input1[bar - i - 2] == FACTOR and input1[bar - i - 1] == comp and input1[bar - i] == FACTOR: 
                next = COND
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        error = "CFG17 ERROR"
        print("reject")        
        return bar
    #18. RETURN -> return FACTOR semi
    elif cfg == 18:
        while i <= bar:
            if bar - i > 1 and input1[bar - i - 2] == 'return' and input1[bar - i - 1] == FACTOR and input1[bar - i] == semi: 
                next = RETURN
                input1.pop(bar - i)
                input1.pop(bar - i - 1)
                input1[bar - i - 2] = next
                for j in range(3):
                    stack.pop()
                bar = bar - 3 + 1
                cur_state = stack[len(stack) - 1]
                R_goto(cur_state, next, bar)
                return bar
            i += 1
        error = "CFG18 ERROR"
        print("reject")        
        return bar


# get value to use ":" 

f_input = open(sys.argv[1], 'r')
text = f_input.read()
#delete first line : not a data
lex_output = text[13:]

dot = 0
seq = 0
token = ''
input1 = []
input2 = []

#
#TYPE : until comma
#after : wait \n
while dot < len(lex_output) :
    if lex_output[dot] == ':' and seq == 0:
        dot += 1
        while lex_output[dot] != ',':
            token += lex_output[dot] 
            dot += 1
        input1.append(token)
        token = ''
        seq = 1
    elif lex_output[dot] == ':' and seq == 1:
        dot += 1    
        while lex_output[dot] != '\n' and lex_output[dot] != None:
            token += lex_output[dot]
            dot += 1
        input2.append(token)
        token = ''
        seq = 0
    if lex_output[dot] == None:
        break
    dot += 1

input1.append('$')#input 1 is terminal lists
input2.append('$')


#initialize
#state
stack = []
#start : 1
stack.append(1)
#bar : location
bar = 0
#cur_state : current state
cur_state = 1
#next : next value
next = input1[bar]

#error
error = ''


#DFA state
def ACTION(cur_state, bar, next, error):
    if cur_state == 1:
        if next == vtype:
            bar = shift(2, bar)
        elif next == '$':
            bar = R(cur_state, 1, bar)
        else:
            print("reject")
            error = "State1 ERROR"
    elif cur_state == 2:
        if next == id:
            bar = shift(3, bar)
        else:
            print("reject")
            
            error = "State2 ERROR"
    elif cur_state == 3:
        if next == assign:
            bar = shift(7, bar)
        elif next == semi:
            bar = shift(5, bar)
        elif next == lparen:
            bar = shift(23, bar)
        else:
            print("reject")
            
            error = "State2 ERROR"
    elif cur_state == 4:
        if next == semi:
            bar = shift(6, bar)
        else:
            print("reject")
            
            error = "State4 ERROR"
    elif cur_state == 5:
        if next == vtype:
            bar = R(cur_state, 2, bar)
        elif next == id:
            bar = R(cur_state, 2, bar)
        elif next == 'if':
            bar = R(cur_state, 2, bar)
        elif next == 'while':
            bar = R(cur_state, 2, bar)
        elif next == 'for':
            bar = R(cur_state, 2, bar)
        elif next == 'return':
            bar = R(cur_state, 2, bar)
        elif next == rbrace:
            bar = R(cur_state, 2, bar)
        elif next == '$':
            bar = R(cur_state, 2, bar)
        else:
            print("reject")
            
            error = "State5 ERROR"
    elif cur_state == 6:
        if next == vtype:
            bar = R(cur_state, 2, bar)
        elif next == id:
            bar = R(cur_state, 2, bar)
        elif next == 'if':
            bar = R(cur_state, 2, bar)
        elif next == 'while':
            bar = R(cur_state, 2, bar)
        elif next == 'for':
            bar = R(cur_state, 2, bar)
        elif next == 'return':
            bar = R(cur_state, 2, bar)
        elif next == rbrace:
            bar = R(cur_state, 2, bar)
        elif next == '$':
            bar = R(cur_state, 2, bar)
        else:
            
            print("reject")
            error = "State6 ERROR"
    elif cur_state == 7:
        if next == num:
            bar = shift(21, bar)
        elif next == float:
            bar = shift(22, bar)
        elif next == literal:
            bar = shift(9, bar)
        elif next == id:
            bar = shift(20, bar)
        elif next == lparen:
            bar = shift(17, bar)
        else:
            
            print("reject")
            error = "State7 ERROR"
    elif cur_state == 8:
        if next == semi:
            bar = R(cur_state, 3, bar)
        elif next == rparen:
            bar = R(cur_state, 3, bar)
        else:
            
            error = "State8 ERROR"
    elif cur_state == 9:
        if next == semi:
            bar = R(cur_state, 13, bar)
        elif next == rparen:
            bar = R(cur_state, 13, bar)
        else:
            print("reject")
            
            error = "State9 ERROR"
    elif cur_state == 10:
        if next == semi:
            bar = R(cur_state, 13, bar)
        elif next == rparen:
            bar = R(cur_state, 13, bar)
        else:
            error = "State10 ERROR"          
    elif cur_state == 11:
        if next == addsub:
            bar = shift(12, bar)
        elif next == semi:
            bar = R(cur_state, 14, bar)
        elif next == rparen:
            bar = R(cur_state, 14, bar)
        else:
            print("reject")
            
            error = "State11 ERROR"
    elif cur_state == 12:
        if next == num:
            bar = shift(21, bar)
        elif next == float:
            bar = shift(22, bar)
        elif next == id:
            bar = shift(20, bar)
        elif next == lparen:
            bar = shift(17, bar)
        else:
            
            print("reject")
            error = "State12 ERROR"
    elif cur_state == 13:
        if next == semi:
            bar = R(cur_state, 14, bar)
        elif next == rparen:
            bar = R(cur_state, 14, bar)
        else:
            
            error = "State13 ERROR"
    elif cur_state == 14:
        if next == multdiv:
            bar = shift(15, bar)
        elif next == addsub:
            bar = R(cur_state, 15, bar)
        elif next == addsub:
             bar = shift(15, bar)
        elif next == semi:
            bar = R(cur_state, 15, bar)
        elif next == rparen:
            bar = R(cur_state, 15, bar)
        else:
            
            print("reject")
            error = "State14 ERROR"
    elif cur_state == 15:
        if next == num:
            bar = shift(21, bar)
        elif next == float:
            bar = shift(22, bar)
        elif next == id:
            bar = shift(20, bar)
        elif next == lparen:
            bar = shift(17, bar)
        elif next == TERM:
            goto(16)
        elif next == FACTOR:
            goto(14)
        else:
            print("reject")
            
            error = "State15 ERROR"
    elif cur_state == 16:
        if next == addsub:
            bar = R(cur_state, 15, bar)
        elif next == semi:
            bar = R(cur_state, 15, bar)
        elif next == rparen:
            bar = R(cur_state, 15, bar)
        else:
            
            print("reject")
            error = "State16 ERROR"
    elif cur_state == 17:
        if next == num:
            bar = shift(21, bar)
        elif next == float:
            bar = shift(22, bar)
        elif next == id:
            bar = shift(20, bar)
        elif next == lparen:
            bar = shift(17, bar)
        else:
            
            error = "State18 ERROR"
    elif cur_state == 18:
        if next == rparen:
            bar = shift(19, bar)       
        else:
            print("reject")
            
            error = "State18 ERROR"
    elif cur_state == 19:
        if next == addsub:
            bar = R(cur_state, 16, bar)
        elif next == multdiv:
            bar = R(cur_state, 16, bar)
        elif next == comp:
            bar = R(cur_state, 16, bar)
        elif next == semi:
            bar = R(cur_state, 16, bar)
        elif next == rparen:
            bar = R(cur_state, 16, bar)
        else:
            print("reject")
            error = "State19 ERROR"
    elif cur_state == 20:
        if next == addsub:
            bar = R(cur_state, 16, bar)
        elif next == multdiv:
            bar = R(cur_state, 16, bar)
        elif next == comp:
            bar = R(cur_state, 16, bar)
        elif next == semi:
            bar = R(cur_state, 16, bar)
        elif next == rparen:
            bar = R(cur_state, 16, bar)
        else:
            
            print("reject")
            error = "State20 ERROR"
    elif cur_state == 21:
        if next == addsub:
            bar = R(cur_state, 16, bar)
        elif next == multdiv:
            bar = R(cur_state, 16, bar)
        elif next == comp:
            bar = R(cur_state, 16, bar)
        elif next == semi:
            bar = R(cur_state, 16, bar)
        elif next == rparen:
            bar = R(cur_state, 16, bar)
        else:
            print("reject")
            
            error = "State21 ERROR"
    elif cur_state == 22:
        if next == addsub:
            bar = R(cur_state, 16, bar)
        elif next == multdiv:
            bar = R(cur_state, 16, bar)
        elif next == comp:
            bar = R(cur_state, 16, bar)
        elif next == semi:
            bar = R(cur_state, 16, bar)
        elif next == rparen:
            bar = R(cur_state, 16, bar)
        else:
            
            print("reject")
            error = "State22 ERROR"
    elif cur_state == 23:
        if next == vtype:
            bar = shift(24, bar)
        #ARG -> epsilon : FOLLOW(ARG)
        elif next == rparen:
            bar = shift(32, bar)
        else:
            
            error = "State23 ERROR"
    elif cur_state == 24:
        if next == id:
            bar = shift(25, bar)
        else:
            print("reject")
            
            error = "State24 ERROR"
    elif cur_state == 25:
        if next == comma:
            bar = shift(27, bar)
        #MOREARGS -> epsilon : FOLLOW(MOREARGS)
        elif next == rparen:
            bar = R(cur_state, 5, bar)
        else:
            
            error = "State25 ERROR"
    elif cur_state == 26:
        if next == rparen:
            bar = R(cur_state, 5, bar)
        else:
            
            print("reject")
            error = "State26 ERROR"
    elif cur_state == 27:
        if next == vtype:
            bar = shift(28, bar)
        else:
            
            error = "State27 ERROR"
    elif cur_state == 28:
        if next == id:
            bar = shift(29, bar)
        else:
            
            print("reject")
            error = "State28 ERROR"
    elif cur_state == 29:
        if next == comma:
            bar = shift(27, bar)
        #MOREARG -> epsilon
        elif next == rparen:
            bar = R(cur_state, 6, bar)
        elif next == rparen:
            bar = R(cur_state, 6, bar)
        else:
            
            print("reject")
            error = "State29 ERROR"
    elif cur_state == 30:
        if next == rparen:
            bar = R(cur_state, 6, bar)
        else:
            
            print("reject")
            error = "State30 ERROR"
    elif cur_state == 31:
        if next == rparen:
            bar = shift(32, bar)
        else:
            print("reject")
            error = "State31 ERROR"
            
    elif cur_state == 32:
        if next == lbrace:
            bar = shift(33, bar)
        else:
            print("reject")
            error = "State32 ERROR"
            
    elif cur_state == 33:
        if next == vtype:
            bar = shift(81, bar)
        elif next == id:
            bar = shift(76, bar)
        elif next == 'if':
            bar = shift(43, bar)
        elif next == 'while':
            bar = shift(58, bar)
        elif next == 'for':
            bar = shift(65, bar)
        #BLOCK -> epsilon
        elif next == 'return':
            bar = shift(37, bar)
        else:
            print("reject")
            
            error = "State33 ERROR"
    elif cur_state == 34:
        if next == 'return':
            bar = shift(37, bar)
        else:
            
            error = "State34 ERROR"
    elif cur_state == 35:
        if next == rbrace:
            bar = shift(36, bar)
        else:
            
            print("reject")
            error = "State35 ERROR"
    elif cur_state == 36:
        if next == vtype:
            bar = R(cur_state, 4,bar)
        elif next == '$':
            bar = R(cur_state, 4,bar)
        else:
            
            print("reject")
            error = "State36 ERROR"
    
    elif cur_state == 37:            
        if next == num:
            bar = shift(21, bar)
        elif next == float:
            bar = shift(22, bar)
        elif next == id:
            bar = shift(20, bar)
        elif next == lparen:
            bar = shift(17, bar)
        else:
            print("reject")
            
            error = "State37 ERROR"
    elif cur_state == 38:
        if next == semi:
            bar = shift(39, bar)
        else:
            
            error = "State38 ERROR"
    elif cur_state == 39:
        if next == rbrace:
            bar = R(cur_state, 18, bar)
        else:
            print("reject")
            
            error = "State39 ERROR"
    elif cur_state == 40:
        if next == vtype:
            bar = R(cur_state, 8, bar)
        elif next == id:
            bar = R(cur_state, 8, bar)
        elif next == 'if':
            bar = R(cur_state, 8, bar)
        elif next == 'while':
            bar = R(cur_state, 8, bar)
        elif next == 'for':
            bar = R(cur_state, 8, bar)
        elif next == 'return':
            bar = R(cur_state, 8, bar)
        elif next == rbrace:
            bar = R(cur_state, 8, bar)
        else:
            
            print("reject")
            error = "State40 ERROR"
    elif cur_state == 41:
        if next == semi:
            bar = shift(42, bar)
        else:
            
            error = "State41 ERROR"
    elif cur_state == 42:
        if next == vtype:
            bar = R(cur_state, 8, bar)
        elif next == id:
            bar = R(cur_state, 8, bar)
        elif next == 'if':
            bar = R(cur_state, 8, bar)
        elif next == 'while':
            bar = R(cur_state, 8, bar)
        elif next == 'for':
            bar = R(cur_state, 8, bar)
        elif next == 'return':
            bar = R(cur_state, 8, bar)
        elif next == rbrace:
            bar = R(cur_state, 8, bar)
        else:
            print("reject")
            
            error = "State42 ERROR"
    elif cur_state == 43:
        if next == lparen:
            bar = shift(44, bar)
        else:
            
            print("reject")
            error = "State43 ERROR"
    elif cur_state == 44:            
        if next == num:
            bar = shift(21, bar)
        elif next == float:
            bar = shift(22, bar)
        elif next == id:
            bar = shift(20, bar)
        elif next == lparen:
            bar = shift(17, bar)
        else:
            
            error = "State44 ERROR"

    elif cur_state == 45:
        if next == rparen:
            bar = shift(46, bar)
        else:
            print("reject")
            
            error = "State45 ERROR"
    elif cur_state == 46:
        if next == lbrace:
            bar = shift(47, bar)
        else:
            
            error = "State46 ERROR"
    elif cur_state == 47:
        if next == vtype:
            bar = shift(81, bar)
        elif next == id:
            bar = shift(76, bar)
        elif next == 'if':
            bar = shift(43, bar)
        elif next == 'while':
            bar = shift(58, bar)
        elif next == 'for':
            bar = shift(65, bar)
        #BLOCK epsilon
        elif next == rbrace:
            bar = shift(49, bar)
        else:
            
            print("reject")
            error = "State47 ERROR"
    elif cur_state == 48:
        if next == rbrace:
            bar = shift(49, bar)
        else:
            
            print("reject")
            error = "State48 ERROR"
    elif cur_state == 49:
        if next == vtype:
            bar = R(cur_state, 9, bar)
        elif next == id:
            bar = R(cur_state, 9, bar)
        elif next == 'if':
            bar = R(cur_state, 9, bar)
        elif next == 'while':
            bar = R(cur_state, 9, bar)
        elif next == 'for':
            bar = R(cur_state, 9, bar)
        elif next == 'return':
            bar = R(cur_state, 9, bar)
        elif next == rbrace:
            bar = R(cur_state, 9, bar)
        elif next == 'else':
            bar = shift(54, bar)
        else:
            print("reject")
            
            error = "State49 ERROR"
    elif cur_state == 50:
        if next == vtype:
            bar = R(cur_state, 9, bar)
        elif next == id:
            bar = R(cur_state, 9, bar)
        elif next == 'if':
            bar = R(cur_state, 9, bar)
        elif next == 'while':
            bar = R(cur_state, 9, bar)
        elif next == 'for':
            bar = R(cur_state, 9, bar)
        elif next == 'return':
            bar = R(cur_state, 9, bar)
        elif next == rbrace:
            bar = R(cur_state, 9, bar)
        else:
            print("reject")
            
            error = "State50 ERROR"
    elif cur_state == 51:
        if next == comp:
            bar = shift(52, bar)
        else:
            
            print("reject")
            error = "State51 ERROR"
    elif cur_state == 52:            
        if next == num:
            bar = shift(21, bar)
        elif next == float:
            bar = shift(22, bar)
        elif next == id:
            bar = shift(20, bar)
        elif next == lparen:
            bar = shift(17, bar)
        else:
            print("reject")
            
            error = "State52 ERROR"

    elif cur_state == 53:
        if next == semi:
            bar = R(cur_state, 17, bar)
        elif next == rparen:
            bar = R(cur_state, 17, bar)
        else:
            print("reject")
            
            error = "State53 ERROR"

    elif cur_state == 54:
        if next == lbrace:
            bar = shift(55, bar)
        else:
            print("reject")
            
            error = "State54 ERROR"

    elif cur_state == 55:
        if next == vtype:
            bar = shift(81, bar)
        elif next == id:
            bar = shift(76, bar)
        elif next == 'if':
            bar = shift(43, bar)
        elif next == 'while':
            bar = shift(58, bar)
        elif next == 'for':
            bar = shift(65, bar)
        #BLOCK epsilon
        elif next == rbrace:
            bar = shift(57, bar)
        else:
            print("reject")
            
            error = "State55 ERROR"
    elif cur_state == 56:
        if next == rbrace:
            bar = shift(57, bar)
        else:
            print("reject")
            
            error = "State56 ERROR"
    elif cur_state == 57:
        if next == vtype:
            bar = R(cur_state, 12, bar)
        elif next == id:
            bar = R(cur_state, 12, bar)
        elif next == 'if':
            bar = R(cur_state, 12, bar)
        elif next == 'while':
            bar = R(cur_state, 12, bar)
        elif next == 'for':
            bar = R(cur_state, 12, bar)
        elif next == 'return':
            bar = R(cur_state, 12, bar)
        elif next == rbrace:
            bar = R(cur_state, 12, bar)
        else:
            print("reject")
            
            error = "State57 ERROR"
    elif cur_state == 58:
        if next == lparen:
            bar = shift(59, bar)
        else:
            print("reject")
            
            error = "State58 ERROR"
    elif cur_state == 59:
        if next == num:
            bar = shift(21, bar)
        elif next == float:
            bar = shift(22, bar)
        elif next == id:
            bar = shift(20, bar)
        elif next == lparen:
            bar = shift(17, bar)
        else:
            print("reject")
            
            error = "State59 ERROR"
    elif cur_state == 60:
        if next == rparen:
            bar = shift(61, bar)
        else:
            print("reject")
            
            error = "State60 ERROR"
    elif cur_state == 61:
        if next == lbrace:
            bar = shift(62, bar)
        else:
            print("reject")
            
            error = "State61 ERROR"
    elif cur_state == 62:
        if next == vtype:
            bar = shift(81, bar)
        elif next == id:
            bar = shift(76, bar)
        elif next == 'if':
            bar = shift(43, bar)
        elif next == 'while':
            bar = shift(58, bar)
        elif next == 'for':
            bar = shift(65, bar)
        
        elif next == rbrace:
            bar = shift(64, bar)
        else:
            
            print("reject")
            error = "State62 ERROR"
    elif cur_state == 63:
        if next == rbrace:
            bar = shift(64, bar)
        else:
            
            error = "State63 ERROR"
    elif cur_state == 64:
        if next == vtype:
            bar = R(cur_state, 10, bar)
        elif next == id:
            bar = R(cur_state, 10, bar)
        elif next == 'if':
            bar = R(cur_state, 10, bar)
        elif next == 'while':
            bar = R(cur_state, 10, bar)
        elif next == 'for':
            bar = R(cur_state, 10, bar)
        elif next == 'return':
            bar = R(cur_state, 10, bar)
        elif next == rbrace:
            bar = R(cur_state, 10, bar)
        else:
            print("reject")
            
            error = "State64 ERROR"

    elif cur_state == 65:
        if next == lparen:
            bar = shift(66, bar)
        else:
            print("reject")
            
            error = "State65 ERROR"
    elif cur_state == 66:
        if next == ASSIGN:
            goto(67)
        elif next == id:
            bar = shift(76, bar)
        else:
            print("reject")
            
            error = "State66 ERROR"
    elif cur_state == 67:
        if next == semi:
            bar = shift(68, bar)
        else:
            print("reject")
            
            error = "State67 ERROR"
    elif cur_state == 68:
        if next == num:
            bar = shift(21, bar)
        elif next == float:
            bar = shift(22, bar)
        elif next == id:
            bar = shift(20, bar)
        elif next == lparen:
            bar = shift(17, bar)
        else:
            print("reject")
            
            error = "State68 ERROR"
    elif cur_state == 69:
        if next == semi:
            bar = shift(70, bar)
        else:
            
            error = "State69 ERROR"
    elif cur_state == 70:
        if next == id:
            bar = shift(76, bar)
        else:
            
            print("reject")
            error = "State70 ERROR"
    elif cur_state == 71:
        if next == rparen:
            bar = shift(72, bar)
        else:
            
            print("reject")
            error = "State71 ERROR"
    elif cur_state == 72:
        if next == lbrace:
            bar = shift(73, bar)
        else:
            
            print("reject")
            error = "State72 ERROR"
    elif cur_state == 73:
        if next == vtype:
            bar = shift(81, bar)
        elif next == id:
            bar = shift(76, bar)
        elif next == 'if':
            bar = shift(43, bar)
        elif next == 'while':
            bar = shift(58, bar)
        elif next == 'for':
            bar = shift(65, bar)
        
        elif next == rbrace:
            bar = shift(75, bar)
        else:
            print("reject")
            
            error = "State73 ERROR"
    elif cur_state == 74:
        if next == rbrace:
            bar = shift(75, bar)
        else:
            
            print("reject")
            error = "State74 ERROR"
    elif cur_state == 75:
        if next == vtype:
            bar = R(cur_state, 11, bar)
        elif next == id:
            bar = R(cur_state, 11, bar)
        elif next == 'if':
            bar = R(cur_state, 11, bar)
        elif next == 'while':
            bar = R(cur_state, 11, bar)
        elif next == 'for':
            bar = R(cur_state, 11, bar)
        elif next == 'return':
            bar = R(cur_state, 11, bar)
        elif next == rbrace:
            bar = R(cur_state, 11, bar)
        else:
            
            print("reject")
            error = "State75 ERROR"

    elif cur_state == 76:
        if next == assign:
            bar = shift(7, bar)
        else:
            
            print("reject")
            error = "State76 ERROR"

    elif cur_state == 77:
        if next == vtype:
            bar = shift(2, bar)
        elif next == '$':
            bar = R(cur_state, 1, bar)
        else:
            
            print("reject")
            error = "State77 ERROR"
            
    elif cur_state == 78:
        if next == vtype:
            bar = shift(2, bar)
        elif next == '$':
            bar = R(cur_state, 1, bar)
        else:
            print("reject")
            
            error = "State78 ERROR"
            
    elif cur_state == 79:
        if next == '$' :
            bar = R(cur_state, 1, bar)
        else:
            print("reject")
            
            error = "State79 ERROR"
    elif cur_state == 80:
        if next == '$' :
            bar = R(cur_state, 1, bar)
        else:
            
            print("reject")
            error = "State80 ERROR"

    elif cur_state == 81:
        if next == id:
            bar = shift(82, bar)
        else:
            print("reject")
            
            error = "State81 ERROR"
    elif cur_state == 82:
        if next == assign:
            bar = shift(7, bar)
        elif next == semi:
            bar = shift(5, bar)
        else:
            print("reject")
            
            error = "State82 ERROR"
    elif cur_state == 83:
        if next == vtype:
            bar = shift(81, bar)
        elif next == id:
            bar = shift(76, bar)
        elif next == 'if':
            bar = shift(43, bar)
        elif next == 'while':
            bar = shift(58, bar)
        elif next == 'for':
            bar = shift(65, bar)
        elif next == rbrace:
            bar = R(cur_state, 7, bar)
        elif next == 'return':
            bar = R(cur_state, 7, bar)
        else:
            
            print("reject")
            error = "State83 ERROR"
    elif cur_state == 84:
        if next == 'return':
            bar = R(cur_state, 7, bar)
        elif next == 'rbrace':
            bar = R(cur_state, 7, bar)
        else:
            
            print("reject")
            error = "State84 ERROR"

    elif cur_state == 85:
        if input1 == [CODE, '$']:
            error = 'accepted'
        else:
            print("reject")
            error = "State85 ERROR"

    next = input1[bar]

    return bar, next, error

while error == '':
    bar, next, error = ACTION(cur_state, bar, next, error)
    cur_state = stack[len(stack) - 1]
print(error)
