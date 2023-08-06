def grade(marks: int) -> str:
  '''
    This function will grade the student based on 
    their marks in range 0 to 100
  '''
  if marks > 80:
    return "1st Grade"
  elif marks >= 60:
    return "2nd Grade"
  elif marks >= 40 :
    return "3rd Grade"
  else:
    return "Failed"

# Actual execution of program starts here
while 1:
  marks = int(input("Enter your marks: "))
  # Validate the input value for the range
  if marks < 0 or marks > 100:
    print("Invalid input!", "Please enter a valid number from 0 to 100")
  else:
    print(grade(marks))

  decide = str(input("Do you want to continue(Y)? "))
  # Promt to decide if user want to continue further to evaluate grade for other students
  if decide == "Y" or  decide == "y":
    continue
  else:
    break
