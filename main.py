import turtle
import random

def drawSquare(myturtle=None, width=0, top_left_x=0, top_left_y=0):
    myturtle.up()
    myturtle.goto(top_left_x, top_left_y)
    myturtle.down()
    for i in range(4):
      myturtle.forward(width)
      myturtle.right(90)
    myturtle.up()

def drawLine(myturtle=None, x_start=0, y_start=0, x_end=0, y_end=0):
    myturtle.goto(x_start, y_start)
    myturtle.down()
    myturtle.goto(x_end, y_end)
    myturtle.up()
def drawCircle(myturtle=None, radius=0):
    myturtle.up()
    myturtle.goto(0,-1)
    myturtle.down()
    myturtle.circle(radius, 360, 100)
    myturtle.up()
  
def setUpDartboard(myscreen=None, myturtle=None):
  myscreen.setworldcoordinates(-2,-2, 2, 2)
  drawSquare(myturtle, 2, -1, 1)   
  drawLine(myturtle, -1, 0, 1, 0)
  drawLine(myturtle, 0, -1, 0, 1 )
  drawCircle(myturtle, 1)



def isInCircle(myturtle=None, circle_center_x=0, circle_center_y=0, radius=0):
  distance = myturtle.distance(circle_center_x, circle_center_y)
  if distance <= radius:
    return True
  else:
    return False
    
def throwDart(myturtle=None):
    myturtle.up()
    random_x = random.uniform(-1,1)
    random_y = random.uniform(-1,1)
    myturtle.goto(random_x, random_y)
    if isInCircle(myturtle, 0, 0, 1) is True:
      myturtle.dot(10, "red")
    else:
      myturtle.dot(10, "blue")
  

      

    
def playDarts(myturtle=None):
  score_a = 0
  score_b = 0
 
  for i in range(10):
    throwDart(myturtle)
    if isInCircle(myturtle, 0,0,1) is True:
      score_a = score_a + 1
      
    throwDart(myturtle)
    if isInCircle(myturtle, 0,0,1) is True:
      score_b = score_b + 1

  if score_a > score_b:
    print("Player A has won")
  elif score_a < score_b:
    print("Player B has won")
  else:
    print("The game was a tie")
      

    

  
#Part C

def montePi(myturtle=None, num_darts=0):
  inside_count=0
  for i in range(num_darts):
    throwDart(myturtle)
    if isInCircle(myturtle, 0, 0, 1) is True:
      inside_count = inside_count + 1
  
  pi = inside_count / num_darts * 4
  return pi


#midterm  
#I come up with a different way to approximate pi value creating a function that calculates the sum of finite series using the knowledge of Leibniz formula
#the leibniz infinite series converges to pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 -...

#this function takes a number of terms and returns a pi approximation by calculating the sum of the infinite series by the n-th term.
def piApprox(number_of_terms=0):
  sum = 0
  for i in range(1, number_of_terms):
    if (i % 2 == 0): #the number of terms is even
      nth_term = - 1/(2*i - 1)
    else: #the number of terms is odd
      nth_term = 1/(2*i - 1)
    sum += nth_term
  
   #Leibniz formula gives us the value for pi/4, so I multiply it by 4 to get the approximation for pi value
  approx_pi = sum*4
  return approx_pi


#this function uses the values you get from the previous function as the approximation for pi, and graphs how those values are converging to pi value, and prints the closest pi approximation so far.
def graphofpiApprox(upperbound=0, myturtle=None, myscreen=None):
  myscreen.setworldcoordinates(0,0,10,10)
  myturtle.up()
  myturtle.home()
  myturtle.down()
  for i in range(1, upperbound):
    myturtle.goto(i, piApprox(i))
    myturtle.dot(5, "blue")
    myscreen.setworldcoordinates(0,0,i, 10)
  print("Approximation for pi using", upperbound,"terms: ", piApprox(upperbound))
   
    
   

  
#########################################################



#########################################################
#         Do not alter any code below here              #
#       Your code must work with the main proivided     #
#########################################################

def main():
  # Get number of darts for simulation from user
  # Note continuation character <\> so we don't go over 78 columns:
  print("This is a program that simulates throwing darts at a dartboard\n" \
        "in order to approximate pi: The ratio of darts in a unit circle\n"\
        "to the total number of darts in a 2X2 square should be\n"\
        "approximately  equal to pi/4")
  print("=========== Part A ===========")

    #Create window, turtle, set up window as dartboard
  window = turtle.Screen()
  darty = turtle.Turtle()
  darty.speed(0) # as fast as it will go!
  setUpDartboard(window, darty)

    # Loop for 10 darts to test your code
  for i in range(10):
        throwDart(darty)
  print("\tPart A Complete...")
  print("=========== Part B ===========")
  darty.clear()
  setUpDartboard(window, darty)
  playDarts(darty)
  print("\tPart B Complete...")
    # Keep the window up until dismissed
  print("=========== Part C ===========")
  darty.clear()
  setUpDartboard(window, darty)
    
    # Includes the following code in order to update animation periodically
    # instead of for each throw (saves LOTS of time):
  BATCH_OF_DARTS = 5000
  window.tracer(BATCH_OF_DARTS)

    # Conduct simulation and print result
  number_darts = int(input("\nPlease input the number of darts to be thrown in the simulation:  "))
  approx_pi = montePi(darty, number_darts)
  print("\nThe estimation of pi using "+str(number_darts)+" virtual darts is " + str(approx_pi))
  print("\tPart C Complete...")
    # Don't hide or mess with window while it's 'working'
  
  print("============= Midterm ==============")
  print("This is a program that approximates pi value from calculating the sum of finite series using Leibniz formula with an input of the number of terms, and that graphs how those values are converging to pi value")
  myturtle = turtle.Turtle()
  myscreen = turtle.Screen()
  upperbound = int(input("Please input the upperbound for the range of the approximation for pi: "))
  darty.clear()
  graphofpiApprox(upperbound, myturtle, myscreen)

  window.exitonclick() 
  

main()
