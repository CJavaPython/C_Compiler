import sys

WHITESPACE = ' \n\t\r'
ABC = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGIT = '0123456789'
KEYWORDS = ['if', 'else', 'while', 'for', 'return'] # 
VARTYPE = ['int', 'char', 'bool', 'float'] # vtype
BOOL = ['true', 'false']
#Arithmetic without - operator
#to find number is negative or not

#ARTH = ['+', '*', '/']
addsub = ['+', '-']
multdiv = ['*', '/']

class lexems:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

f_input = open(sys.argv[1], 'r')
text = f_input.read()
#get txt from char by char
lx = lexems(text)
#check error line
line = 0
#storage of input file
#it will be lexem
tmp = ''
#error log
error = ''

#list about lexems
lst = []
#if previous is num
prev_num = False

while lx.current_char != None:
    if lx.current_char in WHITESPACE:
        if lx.current_char == '\n':
            line += 1
        prev_num = False
        lx.advance()
    else:
        tmp += lx.current_char
        lx.advance()
        #03. Literal
        #appear out = need to advance
        if tmp == '"':
            prev_num = False
            complete = False
            while lx.current_char != None:
                tmp += lx.current_char
                if lx.current_char == '"':
                    complete = True
                    break
                lx.advance()
                
            if complete == False:
                error = "no right apostrophe"
                break
            else:
                lst.append("TYPE:" + "literal" + ",VAL:" + tmp)
                tmp = ""
                lx.advance()
        #ID, Keyword, VarType, Boolean
        #not appear out : not need to appear
        elif tmp in '_' + ABC:
            prev_num = False
            while lx.current_char != None:
                if lx.current_char in ABC + DIGIT + "_":
                    tmp += lx.current_char
                    lx.advance()
                else:
                    break
        #07. Keyword
            if tmp in KEYWORDS:
                lst.append("TYPE:" + tmp + ",VAL:")
        #01. VarType
            elif tmp in VARTYPE:
                lst.append("TYPE:" + "vtype" + ",VAL:" + tmp)
        #04. Boolean
            elif tmp in BOOL:
                lst.append("TYPE:" + "bool" + ",VAL:" + str.upper(tmp))
        #06. ID
            else:
                lst.append("TYPE:" + "id" + ",VAL:" + tmp)
            tmp = ""
        #11. comparison operator <, >, ==, !=, <=, >=
        #09. bitwise <<, >>, &, |
        #10. assignment =
        #assignment vs compare  / = vs ==
        elif tmp == '=':
            prev_num = False
            #result = find -> should advance
            if lx.current_char == '=':
                tmp += lx.current_char
                lst.append("TYPE:" + "comp" + ",VAL:"+ tmp)
                tmp = ''
                lx.advance()
            #not appear out : not need to appear
            else:
                lst.append("TYPE:" + "assign" + ",VAL:" + tmp)
                tmp = ''
        #compare vs bitwise / <, >, >=, <= vs <<, >>
        elif tmp == '>' or tmp == '<':
            prev_num = False            
            #result = find -> should advance
            if tmp == lx.current_char:
                tmp += lx.current_char
                lst.append("TYPE:" + "BITWISE" + ",VAL:"+ tmp)
                tmp = ''
                lx.advance()
            #result = find -> should advance
            elif lx.current_char == '=':
                tmp += lx.current_char
                lst.append("TYPE:" + "comp" + ",VAL:" + tmp)
                tmp = ''
                lx.advance()
            #not appear out : not need to appear
            else:
                lst.append("TYPE:" + "comp" + ",VAL:" + tmp)
                tmp = ''
        #last bitwise operators
        elif tmp == "&" or tmp == "|":
            prev_num = False
            lst.append("TYPE:" + "BITWISE" + ",VAL:" + tmp)
            tmp = ''
        #last Comparison operators 
        elif tmp == "!":
            prev_num = False            
            if lx.current_char == "=":
                tmp += lx.current_char
                lst.append("TYPE:" + "comp" + ",VAL:" + tmp)
                tmp = ''
                lx.advance()
            else:
                if lx.current_char != None:
                    error = "unknown operator !" + lx.current_char
                else:
                    error = "unknown operator !"
                break
        #13. A pair of symbols for defining area/scope of variable and function
        #Brackets
        elif tmp == "{":
            prev_num = False            
            lst.append("TYPE:" + "lbrace" + ",VAL:" + tmp)
            tmp = ''
        elif tmp == '}':
            prev_num = False            
            lst.append("TYPE:" + "rbrace" + ",VAL:" + tmp)
            tmp = ''
        #14. A pair of symbols for indicating a function/statement
        #Paren PRN
        elif tmp == "(":
            prev_num = False            
            lst.append("TYPE:" + "lparen" + ",VAL:" + tmp)
            tmp = ''
        elif tmp == ")":
            prev_num = False            
            lst.append("TYPE:" + "rparen" + ",VAL:" + tmp)
            tmp = ''
        #12. Terminating symbol ;
        elif tmp == ";":
            prev_num = False            
            lst.append("TYPE:" + "semi" + ",VAL:" + tmp)
            tmp = ''
        #15. COMMA
        elif tmp == ',':
            prev_num = False            
            lst.append("TYPE:" + "comma" + ",VAL:" + tmp)
            tmp = ''
        #08 - 1. ARITHMETIC without - and in addsub
        elif tmp in addsub:
            prev_num = False
            lst.append("TYPE:" + "addsub" + ",VAL:" + tmp)
            tmp = ''
        #08 - 1. ARITHMETIC without - and in multdiv
        elif tmp in multdiv:
            prev_num = False
            lst.append("TYPE:" + "multdiv" + ",VAL:" + tmp)
            tmp = ''
        #02 and 05 : numbers about int and float
        #with arth '-'
        elif tmp in DIGIT + '-':
            dot_count = 0
        #if previous iter come number
        #this will be arithmetic operator
            if tmp == '-' and prev_num == True:
                prev_num = False
                lst.append("TYPE:" + "addsub" + ",VAL:" + tmp)
                tmp = ''
                continue
            
            while lx.current_char != None:
                if lx.current_char in DIGIT + '.':
                    tmp += lx.current_char
                    if lx.current_char == '.':
                        dot_count += 1
                else:
                    break
                lx.advance()
        #in this operation, if tmp is only -
        #this is arithmetic operation
            if tmp == '-':
                prev_num = False
                lst.append("TYPE:" + "addsub" + ",VAL:" + tmp)
                tmp = ''
                continue
            if tmp[0] == '-' and tmp[1] == '0' and len(tmp) == 2:
                error = "negative integer should be non zero"
                break
        #error cases
        #dot error
            if dot_count > 1:
                error = "too many dots"
                break
        #Final letter None check
            if lx.current_char == None:
                pass

        #case ID : number + string == error
        #ex) 5a
            elif lx.current_char in ABC + "_":
                error = "ID can't use DIGIT first"
                break
        #error or define float, int
            if tmp[0] == '0':
        #case : 0
                if len(tmp) == 1:
                    lst.append("TYPE:" + "int" + ",VAL:" + tmp)
                    tmp = ''
                    continue
        #case : left side empty error
                elif tmp[1] in DIGIT:
                    error = "Left side is empty sequence 0"
                    break
            if len(tmp) > 2:
                if tmp[len(tmp) - 1] == '0':
        #case : right side empty error
                    if dot_count != 0 and tmp[len(tmp) - 2] != '.':
                        error = "Right side is empty sequence 0"
                        break
            
        #if prev_num == TRUE
        #you can use - operator just for arithmetic operator
            prev_num = True
        #if it has dot
        #04. float
            if dot_count != 0:
                lst.append("TYPE:" + "float" + ",VAL:" + tmp)
                tmp = ''
        #05. int
            else:
                lst.append("TYPE:" + "int" + ",VAL:" + tmp)
                tmp = ''


TITLE = "<TYPE , VAR>"
f_output = open("output.txt", 'w')
if error != '':
    lstlen = 0
    f_output.write(TITLE + "\n")
    while lstlen < len(lst):
        f_output.write(lst[lstlen])
        f_output.write("\n")
        lstlen += 1
    f_output.write("\nline " + str(line + 1) + " : Error occur" + "\n")
    f_output.write(error)
    
else:
    lstlen = 0
    f_output.write(TITLE + "\n")
    while lstlen < len(lst):
        f_output.write(lst[lstlen])
        f_output.write("\n")
        lstlen += 1

    
print(line)
print(lst)
print(error)

f_output.close()
f_input.close()

