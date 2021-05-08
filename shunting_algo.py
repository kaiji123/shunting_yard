## shunting yard
string = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"
def shunting(string):
    arr= string.split()
    output= []
    op= []
    dictionary = {1:["+","-"], 2:["*","/"],3:["^"]}
    for i in arr:
        if i.isdigit():
            output.append(i)
        elif i == "sin":
            op.append(i)
        elif i in ["+","-","*","/","^"]:
            while op!=[]:
                count1=0
                count2 =0
                
                
                    
                for key, value in dictionary.items():
                    #assigning precedence value
                    if op[-1] in value:
                        count1 = key
                    if i in value :
                        count2 = key
                if count1 > count2:
                    s= op[-1]
                    op.remove(op[-1])
                    output.append(s)
                elif count1 == count2 and op[-1] in["+","-","*","/"]:
                    s= op[-1]
                    op.remove(op[-1])
                    output.append(s)
                else:
                    break
            op.append(i)
        elif i =="(":
            op.append(i)
        elif i ==")":
            while op[-1] != "(":
                s= op[-1]
                output.append(s)
                op.remove(op[-1])
            #discarding parentheses
            if op[-1] == "(":
               op.remove(op[-1])
    while op!= []:
        s= op[-1]
        output.append(s)
        op.remove(op[-1])
    return " ".join(output)
print(shunting(string))
                    