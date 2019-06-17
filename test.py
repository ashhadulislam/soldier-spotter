import sys
import operator

#inputs

'''
1. size of battlefield (mXn)
2. starting point of the soldier(i,j)
3. position of the target (x,y)
4. position of all bullet proof points (a#b,c#d)


example input
2 2
2 1
2 2
1#1,1#2

'''


def get_all_input():
    '''this function takes in
    all the necessary input

    '''
    numbers = list(map(int, input().split()))
    m,n=numbers[0],numbers[1]
    
    numbers = list(map(int, input().split()))
    startx,starty=numbers[0],numbers[1]

    numbers = list(map(int, input().split()))
    targetx,targety=numbers[0],numbers[1]

    bullet_proof_points=list(input().split(','))
    bullet_proof_position=[]
    for point in bullet_proof_points:
        two_points=list(map(int,point.split('#')))
        tup=two_points[0],two_points[1]
        bullet_proof_position.append(tup)
    print(bullet_proof_position)

    return m,n,startx,starty,targetx,targety,bullet_proof_position

def get_vision(direction,sourcex,sourcey,nrows,ncols,bullet_proof_position,targetx,targety):
    vision=[]
    x=sourcex
    y=sourcey
    if direction=="up_left":        
        while x>1 and y>1:
            x-=1
            y-=1
            if (x,y) not in bullet_proof_position:
                vision.append((x,y))
            else:
                break
    elif direction=="up":
        while x>1:
            x-=1
            if (x,y) not in bullet_proof_position:
                vision.append((x,y))
            else:
                break
    elif direction=="up_right":
        while x>1 and y<ncols:
            x-=1
            y+=1
            if (x,y) not in bullet_proof_position:
                vision.append((x,y))
            else:
                break
    elif direction=="left":
        while y>1:
            y-=1
            if (x,y) not in bullet_proof_position:
                vision.append((x,y))
            else:
                break

    elif direction=="right":
        while y<ncols:
            y+=1
            if (x,y) not in bullet_proof_position:
                vision.append((x,y))
            else:
                break


    elif direction=="below_left":
        while x<nrows and y>1:
            x+=1
            y-=1
            if (x,y) not in bullet_proof_position:
                vision.append((x,y))
            else:
                break

    elif direction=="below":
        while x<nrows:
            x+=1
            if (x,y) not in bullet_proof_position:
                vision.append((x,y))
            else:
                break


    elif direction=="below_right":
        while x<nrows and y<ncols:
            x+=1
            y+=1
            if (x,y) not in bullet_proof_position:
                vision.append((x,y))
            else:
                break                



    if (targetx,targety) in vision:
        print("target ",targetx,targety,"in vision")
        print("Standing at ",sourcex,sourcey)
        print("direction is ",direction)
        print(vision)
        return vision
    else:
        return None





def get_scope_of_rifle(sourcex,sourcey,nrows,ncols,bullet_proof_position,targetx,targety):
    vision1=get_vision("up_left",sourcex,sourcey,nrows,ncols,bullet_proof_position,targetx,targety)
    vision2=get_vision("up",sourcex,sourcey,nrows,ncols,bullet_proof_position,targetx,targety)
    vision3=get_vision("up_right",sourcex,sourcey,nrows,ncols,bullet_proof_position,targetx,targety)
    vision4=get_vision("left",sourcex,sourcey,nrows,ncols,bullet_proof_position,targetx,targety)
    vision5=get_vision("right",sourcex,sourcey,nrows,ncols,bullet_proof_position,targetx,targety)
    vision6=get_vision("below_left",sourcex,sourcey,nrows,ncols,bullet_proof_position,targetx,targety)
    vision7=get_vision("below",sourcex,sourcey,nrows,ncols,bullet_proof_position,targetx,targety)
    vision8=get_vision("below_right",sourcex,sourcey,nrows,ncols,bullet_proof_position,targetx,targety)
    return [vision1,vision2,vision3,vision4,vision4,vision5,vision6,vision7,vision8]



def start_travelling(startx,starty,m,n,bullet_proof_position,targetx,targety,matrix_traversal):

    this_dict={}

    for i in range(1,m+1):
        for j in range(1,n+1):
            if matrix_traversal[i][j]==0:
                
                all_visions=get_scope_of_rifle(i,j,m,n,bullet_proof_position,targetx,targety)
                # print("Len of visions ",(all_visions))
                
                if not all(v is None for v in all_visions):
                    this_dict[(i,j)]=abs(i-startx)+abs(j-starty)
                matrix_traversal[i][j]=1

    return this_dict













    



def main():
    m,n,startx,starty,targetx,targety,bullet_proof_position=get_all_input()
    print("Input taken successfully")

    # m,n=5,4
    # startx,starty=4,3
    # targetx,targety=1,2
    # bullet_proof_position=[
    # (2,2),(3,1)
    # ]

    matrix_traversal=[[0] * (n+1) for i in range(m+1)]

    for line in matrix_traversal:
        print(line)


    travel_diaries=start_travelling(startx,starty,m,n,bullet_proof_position,targetx,targety,matrix_traversal)
    print(travel_diaries)


    sorted_travel_diaries = sorted(travel_diaries.items(), key=operator.itemgetter(1))

    print(sorted_travel_diaries)


    



    

if __name__=="__main__":
    main()
