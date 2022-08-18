position = [0,0]
matrix = [[{"name":"main door", "description": "main door oto house"},
           {"name": "living room", "description": "has couch"},
           {"name": "kitchen", "description":"where you make food"}],

          [{"name":"bedroom", "description": "master bedroom"},
           {"name": "basement", "description": "basement where the dungeon is"},
           {"name": "attic", "description": "spider webs all around"}],

          [{"name": "test", "description": "test"},
           {"name": "test2", "description": "test2"}]]






stop = False

while (not stop):
    i = input("Where to? (l,r,u,d,q,b,p):")
    if i == "q":
        print("you quit!")
        stop = True
    if i == "l":
      print("You are moving Left")
      print(position)
      row0 = matrix[1]
      print(len(row0))
      print(position[0])
      if position[1] == 0:
         position[1] = 2 -1
      else:
         position[1] = position[0] -1
    if i == "r":
        print("You are going right")
        print(position)
        row0 = matrix[1]
        if position[1] > 2 -2:
           position[1] = 0
        else: 
          position[1] = position[0] + 1
    if i == "b":
        print(matrix)
    if i == "p":
        x = position[0]
        y = position[1]
        print("x = " + str(x))
        print("y = " + str(y))
        print(matrix[x][y])
        
    if i == "d":
       print("You are going down")
       print(position)
       row0 = matrix[0]
    if position[0] > 2 -1:
       position[0] = 0
    else:
       position[0] = position[0] + 1
print(position)
         
  #  if i == "u":
    ##   print("You are going up")
     #  if position[0] > 0 + 1:
     #     position[0] = 0
      # else:
       ##  position[0] + 1 
    
           
       
          
          