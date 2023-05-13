import picture
import time
import random

#function of "refreshing" the image (Prof.Blair,2022)
def clear_frame():
  picture.set_fill_color("white")
  picture.set_outline_color("white")
  picture.draw_filled_rectangle(0,0,600,500)


#function of the loading page
def loading():

  #basic setting
  picture.new_picture(600,500)
  picture.set_outline_color("white")
  picture.set_fill_color("white")
  
  picture.set_outline_color("black")
  picture.draw_text(100,50,"Tank War",90)
  picture.set_fill_color("black")

  #description of the game
  picture.draw_text(210,150,"DESCRIPTION",25)
  picture.draw_text(100,180,"For this game, you need to control a tank to fire and destroy enemies",15)
  picture.draw_text(70,195,"coming out from every direction. Since it is an old tank, you can only fire on",15)
  picture.draw_text(70,210,"the direction your tank is facing and when the moving commands are given,",15)
  picture.draw_text(70,225,"the tank will turn to the direction the first move and move along that direction",15)
  picture.draw_text(70,240,"starting from the second move. Keep in mind that you'd better not let them",15)
  picture.draw_text(70,255,"get close to you or you will lose. Enter anything to start if you are prepared!",15)


  picture.draw_filled_rectangle(247,345,100,30)
  picture.set_outline_color("white")
  picture.draw_text(250,350, " START",25)

  picture.display()

  #start loading
  start = input()
  if start != "" or start == "":

    picture.new_picture(600,500)
    picture.set_outline_color("white")
    picture.set_fill_color("white")
  
    picture.set_outline_color("black")
    picture.draw_text(100,50,"Tank War",90)
    picture.set_fill_color("black")

    picture.set_pen_x(100)
    picture.set_pen_y(246)
    picture.set_pen_width(5)
  
    picture.draw_forward(400)
    picture.rotate(90)
    picture.draw_forward(58)
    picture.rotate(90)
    picture.draw_forward(400)
    picture.rotate(90)
    picture.draw_forward(58)
    picture.rotate(90)
  
    picture.draw_text(245,310,"Loading ...",25)

    #the nested for loop
    for i in range(8):
      for j in range(5):
        if j % 2 == 0:
          picture.set_outline_color("black")
          picture.set_fill_color("black")
          
        else:
          picture.set_outline_color("white")
          picture.set_fill_color("white")
  
        x = 109 + 49 * i
        picture.draw_filled_rectangle(x, 255, 40, 40)

        time.sleep(0.4)
        picture.display()


#function of rotating the image
def rotate(tank, x, y):
  
  picture.draw_image(x,y,tank)
  
  picture.display()


#function of movement 
def move(tank, x, y):

  picture.draw_image(x,y,tank)
  
  picture.display()


#function of firing
def fire(x,y,info, info_e1, info_e2):
  
  picture.set_fill_color("brown")

  picture.draw_image(info[1],info[2],info[0])

  picture.draw_filled_circle(x, y, 8)
  
  if info_e1[3] == False:
    picture.draw_image(info_e1[1],info_e1[2],info_e1[0])

  if info_e2[3] == False:
    picture.draw_image(info_e2[1],info_e2[2],info_e2[0])

  picture.display() 

  
#funciton that cheks whether the bullet hits the enemies
def gethit(x, y, info_e):

  boom = picture.load_image("boom.png")
  if abs(x - info_e[1]) < 25 and abs(y - info_e[2]) < 25:
    
    picture.draw_image(info_e[1] - 40, info_e[2] - 40, boom)
    picture.display()
    return True

  else:
    return False

  
#function that determine how the enemies move      
def enemy_move(x_pos, y_pos, info_e, e_direction):
  x_diff = abs(x_pos - info_e[1])
  y_diff = abs(y_pos - info_e[2])

  if x_diff > y_diff:
    if x_pos > info_e[1]:#east
      info_e[1] += 10
      rotate(e_direction[1], info_e[1], info_e[2])
      move(e_direction[1], info_e[1], info_e[2])
  
      info_e[0] = e_direction[1]


    else:#west
      info_e[1] -= 10
      rotate(e_direction[2], info_e[1], info_e[2])
      move(e_direction[2], info_e[1], info_e[2])
  
      info_e[0] = e_direction[2]

    
  else:#south
    if y_pos > info_e[2]:
      info_e[2] += 10
      rotate(e_direction[3], info_e[1], info_e[2])
      move(e_direction[3], info_e[1], info_e[2])
    
      info_e[0] = e_direction[3]

      

    else:#north
      info_e[2] -= 10
      rotate(e_direction[0], info_e[1], info_e[2])
      move(e_direction[0], info_e[1], info_e[2])
    
      info_e[0] = e_direction[0]

  return info_e

  
#function ran when enemies are too close to our tank
def lose():

  clear_frame()

  picture.set_outline_color("black")
  picture.set_fill_color("black")
  picture.draw_text(80,150,"You Lose!",100)
  picture.run()


#function ran when both enemies are destroyed
def win():
  clear_frame()
  
  win = picture.load_image("win.png")
  picture.set_outline_color("black")
  picture.set_fill_color("black")
  picture.draw_image(0,0,win)
    
  picture.draw_text(80,150,"You Win!",100)

  picture.run()

  
def main():

  loading()
  
  picture.new_picture(600,500)
  picture.set_outline_color("white")
  picture.set_fill_color("white")
    
  #setups of the tank we control
  my_tank = picture.load_image("mytank.png")
  my_tank_east = picture.load_image("mytank(east).png")
  my_tank_south = picture.load_image("mytank(south).png")
  my_tank_west = picture.load_image("mytank(west).png")
  
  
  x_pos = 300
  y_pos = 250
  step = 20


  picture.draw_image(x_pos,y_pos,my_tank)

  
  #enemy1 settings (appear from the right or left edge)
  enemy = picture.load_image("enemy.png")
  enemy_east = picture.load_image("enemy(east).png")
  enemy_west = picture.load_image("enemy(west).png")
  enemy_south = picture.load_image("enemy(south).png")
  
  e_direction = [enemy, enemy_east, enemy_west, enemy_south]
  
  x_enemy1 = random.choice([-30,580])
  y_enemy1 = random.randrange(0,500)
  e_gethit1 = False

  #draw enemy1 and store its information in the list info_e1
  if x_enemy1 == -30:
    picture.draw_image(x_enemy1, y_enemy1, enemy_east)
    info_e1 = [enemy_east,x_enemy1,y_enemy1, e_gethit1]

  elif x_enemy1 == 580:
    picture.draw_image(x_enemy1, y_enemy1, enemy_west) 
    info_e1 = [enemy_west,x_enemy1,y_enemy1, e_gethit1]



  #enemy2 setting (appear from top or the bottom)
  x_enemy2 = random.randrange(0,600)
  y_enemy2 = random.choice([-30,480])
  e_gethit2 = False

  #draw enemy2 and store its information in the list info_e2
  if y_enemy2 == -30:
    picture.draw_image(x_enemy2, y_enemy2, enemy_south)
    info_e2 = [enemy_south,x_enemy2, y_enemy2, e_gethit2]

  elif y_enemy2 == 480:
    picture.draw_image(x_enemy2, y_enemy2, enemy)
    info_e2 = [enemy,x_enemy2, y_enemy2, e_gethit2]

  picture.display()


  #menu
  done = False
  info = [my_tank,x_pos,y_pos]
  print("Please give command to your tank!")
  
  while (not done):

    print()
    print("w: Move North")
    print("s: Move South")
    print("a: Move West")
    print("d: Move East")
    print("j: Fire")
    print()

    command = input("Your command:")

    if command == "j":
      x = info[1]
      y = info[2]
      i = 0
      if info[0] == my_tank:
        x = x + 12
        while i < 32:
          y = y - 20
          i += 1
          clear_frame()

          fire(x, y, info, info_e1, info_e2)
          
          e_gethit1 = gethit(x, y, info_e1)
          e_gethit2 = gethit(x, y, info_e2)
          
          if e_gethit1:
            i = 32
            info_e1[3] = True
          if e_gethit2:
            i = 32
            info_e2[3] = True

          
      elif info[0] == my_tank_south:
        x = x + 12
        y = y + 30
        while i < 32:
          y = y + 20
          i += 1
          clear_frame()

          fire(x, y, info, info_e1, info_e2)

          e_gethit1 = gethit(x, y, info_e1)
          e_gethit2 = gethit(x, y, info_e2)
          
          if e_gethit1:
            i = 32
            info_e1[3] = True
          if e_gethit2:
            i = 32
            info_e2[3] = True


          
      elif info[0] == my_tank_east:
        x = x + 30
        y = y + 12
        while i < 32:
          x = x + 20
          i += 1
          clear_frame()

          fire(x, y, info, info_e1, info_e2)
          
          e_gethit1 = gethit(x, y, info_e1)
          e_gethit2 = gethit(x, y, info_e2)
          
          if e_gethit1:
            i = 32
            info_e1[3] = True
          if e_gethit2:
            i = 32
            info_e2[3] = True

                
      elif info[0] == my_tank_west:
        y = y + 12
        while i < 32:
          x = x - 20
          i += 1
          clear_frame()

          fire(x, y, info, info_e1, info_e2)

          e_gethit1 = gethit(x, y, info_e1)
          e_gethit2 = gethit(x, y, info_e2)
          
          if e_gethit1:
            i = 32
            info_e1[3] = True
          if e_gethit2:
            i = 32
            info_e2[3] = True


    elif command == "w":
      y_pos = y_pos - step
      
      #reset the position when the tank gets to the edge
      if y_pos <= 0:
        y_pos = 480

      #rotate and move
      clear_frame()
      rotate(my_tank, x_pos, y_pos)
      move(my_tank, x_pos, y_pos)
      
      info[0] = my_tank
      info[1] = x_pos
      info[2] = y_pos

      if not info_e1[3]:
        info_e1 = enemy_move(x_pos, y_pos, info_e1, e_direction)

      if not info_e2[3]:
        info_e2 = enemy_move(x_pos, y_pos, info_e2, e_direction)
      

    elif command == "s":
      y_pos = y_pos + step

      #reset the position when the tank gets to the edge
      if y_pos >= 500:
        y_pos = -30

      #rotate and move
      clear_frame()
      rotate(my_tank_south, x_pos, y_pos)
      move(my_tank_south, x_pos, y_pos)

      info[0] = my_tank_south
      info[1] = x_pos
      info[2] = y_pos
      
      if not info_e1[3]:
        info_e1 = enemy_move(x_pos, y_pos, info_e1, e_direction)

      if not info_e2[3]:
        info_e2 = enemy_move(x_pos, y_pos, info_e2, e_direction)
      
      
      
    elif command == "a":
      x_pos = x_pos - step
      
      #reset the position when the tank gets to the edge
      if x_pos <= 0:
        x_pos = 580

      #rotate and move
      clear_frame()
      rotate(my_tank_west, x_pos, y_pos)
      move(my_tank_west, x_pos, y_pos)

      info[0] = my_tank_west
      info[1] = x_pos
      info[2] = y_pos

      if not info_e1[3]:
        info_e1 = enemy_move(x_pos, y_pos, info_e1, e_direction)

      if not info_e2[3]:
        info_e2 = enemy_move(x_pos, y_pos, info_e2, e_direction)
      
        

    elif command == "d":
      x_pos = x_pos + step
      
      #reset the position when the tank gets to the edge     
      if x_pos >= 600:
        x_pos = -30

      #rotate and move
      clear_frame()

      move(my_tank_east, x_pos, y_pos)

      info[0] = my_tank_east
      info[1] = x_pos
      info[2] = y_pos

      if not info_e1[3]:
        info_e1 = enemy_move(x_pos, y_pos, info_e1, e_direction)

      if not info_e2[3]:
        info_e2 = enemy_move(x_pos, y_pos, info_e2, e_direction)
      

    
                    
        
    else:
      print()
      print()
      print("Your command is not included")
      print("Please enter a valid command")


    #reset the location of enemies if they get hit in case of affecting other functinos
    if info_e1[3]:
      info_e1[1] = 0
      info_e1[2] = 0

    if info_e2[3]:
      info_e2[1] = 0
      info_e2[2] = 0
      
    #when losing
    if abs(x_pos - info_e1[1]) < 30 and abs(y_pos - info_e1[2]) < 50:
      lose()
      
    if abs(x_pos - info_e2[1]) < 30 and abs(y_pos - info_e2[2]) < 50:
      lose()
      

    #when winning
    if info_e1[3] and info_e2[3]:
      win()

        
 

if __name__ == "__main__":
  main()
        
