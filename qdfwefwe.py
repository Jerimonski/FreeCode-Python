def arithmetic_arranger(problems):
  
  if len(problems) > 5:
    return "Error: too many problems."
  
  firstNumbers = []
  operator = []
  SecondNumbers = []
  booo = []
  spaces = []
  result = []
  for i in problems:
    lines_1 = len(i.split()[0])  
    lines_2 = len(i.split()[2])   
    sitDown = max(lines_1,lines_2)

    firstNumbers.append((i.split()[0]).rjust(sitDown + 2))
    operator.append((i.split()[1]) + ' ' * ((sitDown + 1) - lines_2))
    SecondNumbers.append((i.split()[2]) + "    ")        
    spaces.append(("-" * (sitDown + 2)) + "    ")


  for j in range(len(problems)):
    booo.append(operator[j] + SecondNumbers[j])
    
  for k in range(len(problems)):
    print(operator[k])
    if operator[k] == "+":
      result.append(int(firstNumbers[k]) + int(SecondNumbers[k]))
      print(result[k], end= " ")
    else:
      return "Error: Operator must be '+' or '-'"

  bora = '    '.join(firstNumbers) + "\n" + ''.join(booo) + "\n" + ''.join(spaces)
  return bora   

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))
