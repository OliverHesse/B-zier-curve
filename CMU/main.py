from cmu_graphics import *
import math
line = []
max_line = 4
current_lines = 0
last_pos = []
show = True
class lineObj:
  def __init__(self,pos1,pos2):
    self.pos1 = pos1
    self.pos2 = pos2

    self.currentPos = pos1
    self.type = "skeleton"
    self.mag = math.sqrt((pos2[0]-pos1[0])**2+(pos2[1]-pos1[1])**2)
  def step(self,TotalT,stepRate):
    #TotalT total time to fully interpolate
    #stepRate a step every second or a step every 0.1
    #dividing by totalT gives me step per second
    new_X = (self.pos2[0]-self.pos1[0])/TotalT
    new_X = self.currentPos[0] + (new_X)*stepRate
    new_Y = (self.pos2[1]-self.pos1[1])/TotalT
    new_Y = self.currentPos[1] + (new_Y)*stepRate
    self.currentPos = [new_X,new_Y]

    return [new_X,new_Y]
class constructLine:
  def __init__(self,line1 : lineObj,line2 : lineObj):
    self.line1 = line1
    self.line2 = line2

    self.type ="construct"
    self.currentTime = 0
    self.currentPos = line1.currentPos
  def step(self,TotalT,stepRate):
    self.currentTime += stepRate
    new_X = (self.line2.currentPos[0]-self.line1.currentPos[0])/TotalT
    new_X = self.line1.currentPos[0] + (new_X)*self.currentTime
    new_Y = (self.line2.currentPos[1]-self.line1.currentPos[1])/TotalT
    new_Y = self.line1.currentPos[1] + (new_Y)*self.currentTime
    self.currentPos = [new_X,new_Y]

    return [new_X,new_Y]


lines = [[ ]]

def draw_curve(time_step):
  #first draw skeleton lines
  if show == True:
    for each in lines[0]:
      new_line = Line(each.pos1[0],each.pos1[1],each.pos2[0],each.pos2[1])

  #how often per second a step should occur
  max_time = 1
  current_time = 0
  #basic interpolation function
  points = [[lines[0][0].pos1[0],lines[0][0].pos1[1]]]
  while current_time < max_time:

    for itr in lines:
      for unique_line in itr:
        if len(itr) == 1:

          new_pos = unique_line.step(max_time,time_step)
          points.append(new_pos )
          
        else:
          unique_line.step(max_time,time_step)
    #time.sleep(time_step)
    current_time += time_step
  for i in range(0,len(points)-1):
    new_line = Line(points[i][0],points[i][1],points[i+1][0],points[i+1][1],fill="teal")
  #t.penup()
  #t.goto(points[0][0],points[0][1])
  #t.pendown()
  #for point in points:
    #t.goto(point[0],point[1])
  #screen.update()
def create_construction():
  global max_line
  global lines
  max_line -= 1
  temp_lines = []
  for potential_line in range(0,max_line):
    line1 = lines[-1][potential_line]
    line2 = lines[-1][potential_line+1]
    temp_lines.append(constructLine(line1,line2))
  lines.append(temp_lines)
  print(max_line)
  print(len(lines))
  if max_line > 0:
    create_construction()
  else:
    draw_curve(0.001)
def draw_line(point1,point2):

  lines[-1].append(lineObj(point1,point2))
def create_curve(x,y):
  global line
  global last_pos
  global current_lines
  global max_line
  global lines
  print(max_line)
  print(current_lines)
  if max_line == 0:
    print("waas jer")
    current_lines = 0
    max_line = 4
    last_pos = []
    lines = [[]]
    line = []
 
  if current_lines != max_line:
    if last_pos == []:
      line.append([x,y])
      last_pos.append([x,y])
    else:
      line.append([x,y])
      draw_line(line[0],line[1])
      last_pos.append([x,y])
      line = [[x,y]]
      current_lines += 1
      if max_line == current_lines:
        #create construction lines
        print("starting drawing")
        create_construction()
  
# Write your code here
# Not sure where to start?
def onMousePress(mouseX, mouseY):
  create_curve(mouseX,mouseY)

#r = Rect(50, 50, 200, 300, fill='dodgerBlue')
#c = Circle(300, 200, 75, fill='crimson')

# Check out README.md under "Files"

cmu_graphics.run()