#!/bin/python3	     	      	     	      			     	 
from random import randint     	     	 	     	     	    	       
	  	 	   	 	     	  	     	    	  
def main():      	      	       	   	  	 	 
	height = 10	     	    	   	       	    		     
	width = 30     	    	   	       	    			      
	groundH = 3  	     	       	       	    	  	      	  
	density = 5  	     	  	 	     	    	     	       
	bunnyOffset = 20       	    	  	  		  	 
	bunny = [" \\", "  \\ /\\", "  ( )", ".( o )."]       	      	 
	image = [] 	  	   	 	       	      	 	 
	for i in range(height):	    	     	    	    	  
		row = ""	 	       	      	     
		for i in range(width):
			if randint(1, density) == 1:
				row += "."
			else:
				row += " "
		image.append(row)

	bunny.reverse()
	for i, seg in enumerate(bunny):
		line = image[i][:bunnyOffset] + seg + image[i][bunnyOffset+len(seg)+1:]
		image.pop(i)
		image.insert(i, line)
	image.reverse()

	for i in range(groundH):
		image.append("▉"*width)

	for row in image:
		print(row)
	return

if __name__ == "__main__":
	main()
