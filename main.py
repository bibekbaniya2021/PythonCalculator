class Operation:
  def __init__(self, operation, number):
    self.operation=operation
    self.number = number
  
def intro():
  print("===============PYTHON BASIC CALCULATOR===============\n\n")

def print_instructions():  
  instructions = "Type your command in this format "
  instructions += "add 1,2,...\n"
  instructions += "Possible operations add, subtract, multiply, divide\n"
  print(instructions)

def get_user_input():
  user_input = input("Enter your command\n")
  return user_input

def parce_input(user_input):
  # add 30, 50 --> 80
  # op, number, list  
  # split string into op. and numbers
  user_input_parsed = user_input.split(" ")
  # print(user_input_parsed)
  #  make list of numbers
  user_input_numbers = user_input_parsed[1].split(",")
  # print(user_input_numbers)
  for number in user_input_numbers:
    number = int(number)

  #  create instance op class and return
  operation = Operation(user_input_parsed[0], user_input_numbers)
  # print(operation)
  return operation 
  

def run_operation(task):  
  answer = 0
  if task.operation == 'add': # add
    answer = int(task.number[0])    
    for number in task.number[1:]:
      answer += int(number)
    return answer
  elif task.operation == 'subtract': # subtract
    answer = int(task.number[0])
    for number in task.number[1:]:
      answer -= int(number)
    return answer   
  elif task.operation == 'multiply': # multiply
    answer = int(task.number[0])   
    for number in task.number[1:]:
      answer *= int(number)
    return answer
  elif task.operation == 'divide': # divide
    answer = int(task.number[0]) 
    for number in task.number[1:]:
      answer /= int(number)
    return answer
  return "Please type correctly"

def answer_user(solution):
  answer = "\nYour answer is: "
  answer += str(solution)
  answer += "\n"
  print(answer)

def ask_again():
  again = input("Would you like to enter another command?\nPlease type 'y' for yes and 'n' for no\n")
  # if yes, true
  if again == 'y':
    return True
  if again == 'n':
    return False

def main():
  again = True
  while again == True:  
    intro()
    print_instructions()
    user_input = get_user_input()
    task = parce_input(user_input)
    answer = run_operation(task)
    answer_user(answer)
    again = ask_again()

main()