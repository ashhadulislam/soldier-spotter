# soldier-spotter
Find the minimum distance a soldier must travel in order to be in a position to direclty hit the target.

There are some bullet proof walls that deflect the bullet.

However the soldier can walk through those.


For example, take a look at the grid below

![sample grid](https://raw.githubusercontent.com/ashhadulislam/soldier-spotter/master/img2.jpg)


There are 5 rows and 4 columns in this grid

The soldier is standing at (4,3)

The cells are bullet proof at (3,1 and 2,2)

However the soldier can walk through those

The target is at (1,2)


Possible cells from which the soldier can hit the target are

(1,1)

(1,3)

(1,4)

(2,2)

(2,3)

(3,4)


Considering the starting position of the soldier, the distances it has to travel are

{


	(1, 1): 5, 

	(1, 3): 3, 
	
	(1, 4): 4, 
	
	(2, 1): 4, 
	
	(2, 2): 3, 
	
	(2, 3): 2, 
	
	(3, 4): 2

}

On sorting by distance:

[


	((2, 3), 2), 

	((3, 4), 2), 

	((1, 3), 3), 

	((2, 2), 3), 

	((1, 4), 4), 

	((2, 1), 4), 

	((1, 1), 5)

]


The 1st tuple being the co ordinate and the next element being the distance the soldier has to travel in order to reach the cell from where it can hit the target.

The final output is thus sorted by 

a. distance from the original position

b. lexicographically, row wise


To run the same example, 

run test.py with the following input


5 4

4 3

1 2

3#1,2#2

