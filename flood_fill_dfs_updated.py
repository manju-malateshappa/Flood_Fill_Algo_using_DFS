
#dimension of the M * N matrix of colors
M = 8
N = 8

# arrays storing values of all 8 possible movements
row= [-1, -1, -1, 0, 0,  1, 1, 1 ]
col = [ -1,  0,  1, -1, 1, -1, 0, 1 ]


# check if it is possible to go to pixel (x, y) from current
#  pixel. The function returns false if the pixel has different
# color or it is not a valid pixel

def isSafe(image, x, y, target_color):

	return ((x >= 0 and x < M and y >= 0 and y < N) and (image[x][y] == target_color))


#method  - print_matrix
# prints the matrix
def print_matrix():
  for i in range(M): 
    for j in range(N): 
        print(image[i][j], end = ' ') 
    print()

def floodFill(image, x, y, replacement_color):

	# get target color
	target_color = image[x][y];
	
	# replace current pixel color with that of replacement
	image[x][y] = replacement_color;
 
	# process all 8 adjacent pixels of current pixel and
	# recursively for each valid pixel
	for k in range(8):
		#if the adjacent pixel at position (x + row[k], y + col[k]) is
		#a valid pixel and have same color as that of the current pixel
		if (isSafe(image, x + row[k], y + col[k], target_color)):
			floodFill(image, x + row[k], y + col[k], replacement_color)

# entry point for the driver
if __name__ == "__main__": 

  image = [[1, 1, 1, 1, 1, 1, 2, 1],  
            [1, 1, 0, 1, 1, 1, 0, 0],  
            [1, 0, 0, 1, 1, 0, 1, 1],  
            [1, 2, 2, 2, 2, 0, 1, 0],  
            [1, 1, 1, 2, 2, 0, 1, 0],  
            [1, 1, 1, 2, 2, 2, 2, 0],  
            [1, 1, 1, 0, 1, 2, 1, 1],  
            [2, 1, 1, 1, 1, 2, 2, 1]] 
    
  # start node
  x = 3
  y = 3
  #replacement color
  replacement_color = 4
  print(" starting position ", )
  print(" orginial M * N matrix of colors ")
  print_matrix()
  floodFill(image, x, y, replacement_color)
    
  print ("Updated M * N matrix of colors after call to floodFill:") 
  print_matrix()
