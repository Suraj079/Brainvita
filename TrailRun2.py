# Play board randomly until no further move possible


##holes = [[-1,3],[0,3],[1,3],\
##       [-1,2],[0,2],[1,2],\
##[-3,1],[-2,1],[-1,1],[0,1],[1,1],[2,1],[3,1],\
##[-3,0],[-2,0],[-1,0],[0,0],[1,0],[2,0],[3,0],\
##[-3,-1],[-2,-1],[-1,-1],[0,-1],[1,-1],[2,-1],[3,-1],\
##       [-1,-2], [0,-2], [1,-2],\
##       [-1,-3], [0,-3], [1,-3]];


def findmoves(mar, pos):

    holes = [[-1,3],[0,3],[1,3],\
             [-1,2],[0,2],[1,2],\
    [-3,1],[-2,1],[-1,1],[0,1],[1,1],[2,1],[3,1],\
    [-3,0],[-2,0],[-1,0],[0,0],[1,0],[2,0],[3,0],\
    [-3,-1],[-2,-1],[-1,-1],[0,-1],[1,-1],[2,-1],[3,-1],\
           [-1,-2], [0,-2], [1,-2],\
           [-1,-3], [0,-3], [1,-3]];
    
    movs = [];
    
    if (([mar[0],mar[1]+1] in pos) and ([mar[0],mar[1]+2] in holes) and not ([mar[0], mar[1] + 2] in pos)):
        movs.append([mar, [mar[0],mar[1]+2], [mar[0],mar[1]+1]]); 
    # check right
    if (([mar[0]+1,mar[1]] in pos) and ([mar[0]+2, mar[1]] in holes) and not ([mar[0]+2, mar[1]] in pos)):        
        movs.append([mar, [mar[0]+2,mar[1]], [mar[0]+1,mar[1]]]);    
    # check bottom
    if ([mar[0], mar[1]-1] in pos) and ([mar[0], mar[1]-2] in holes) and not ([mar[0], mar[1]-2] in pos):        
        movs.append([mar, [mar[0],mar[1]-2], [mar[0],mar[1]-1]]);
    # check left
    if ([mar[0]-1, mar[1]] in pos) and ([mar[0]-2, mar[1]] in holes) and not ([mar[0]-2, mar[1]] in pos):
        movs.append([mar, [mar[0]-2,mar[1]], [mar[0]-1,mar[1]]]);

    return movs

def newpos(mov, pos):
    pos.remove(mov[0]);
    pos.append(mov[1]);
    pos.remove(mov[2]);
    return pos

def displayboard(pos):
    p = ['  ' for i in range(33)];

    if [-1,3] in pos:    p[0] = '* ';
    if [0,3] in pos:    p[1] = '* ';
    if [1,3] in pos:    p[2] = '* ';
    if [-1,2] in pos:    p[3] = '* ';
    if [0,2] in pos:    p[4] = '* ';
    if [1,2] in pos:    p[5] = '* ';
    if [-3,1] in pos:    p[6] = '* ';
    if [-2,1] in pos:    p[7] = '* ';
    if [-1,1] in pos:    p[8] = '* ';
    if [0,1] in pos:    p[9] = '* ';
    if [1,1] in pos:    p[10] = '* ';
    if [2,1] in pos:    p[11] = '* ';
    if [3,1] in pos:    p[12] = '* ';
    if [-3,0] in pos:    p[13] = '* ';
    if [-2,0] in pos:    p[14] = '* ';
    if [-1,0] in pos:    p[15] = '* ';
    if [0,0] in pos:    p[16] = '* ';
    if [1,0] in pos:    p[17] = '* ';
    if [2,0] in pos:    p[18] = '* ';
    if [3,0] in pos:    p[19] = '* ';
    if [-3,-1] in pos:    p[20] = '* ';
    if [-2,-1] in pos:    p[21] = '* ';
    if [-1,-1] in pos:    p[22] = '* ';
    if [0,-1] in pos:    p[23] = '* ';
    if [1,-1] in pos:    p[24] = '* ';
    if [2,-1] in pos:    p[25] = '* ';
    if [3,-1] in pos:    p[26] = '* ';
    if [-1,-2] in pos:    p[27] = '* ';
    if [0,-2] in pos:    p[28] = '* ';
    if [1,-2] in pos:    p[29] = '* ';
    if [-1,-3] in pos:    p[30] = '* ';
    if [0,-3] in pos:    p[31] = '* ';
    if [1,-3] in pos:    p[32] = '* ';


    print('    '+p[0]+p[1]+p[2]+'    \n'\
          '    '+p[3]+p[4]+p[5]+'    \n'\
          +p[6]+p[7]+p[8]+p[9]+p[10]+p[11]+p[12]+'\n'\
          +p[13]+p[14]+p[15]+p[16]+p[17]+p[18]+p[19]+'\n'\
          +p[20]+p[21]+p[22]+p[23]+p[24]+p[25]+p[26]+'\n'\
          '    '+p[27]+p[28]+p[29]+'    \n'\
          '    '+p[30]+p[31]+p[32]+'    \n');
    



def isvalid(mov, p):

    holes = [[-1,3],[0,3],[1,3],\
             [-1,2],[0,2],[1,2],\
    [-3,1],[-2,1],[-1,1],[0,1],[1,1],[2,1],[3,1],\
    [-3,0],[-2,0],[-1,0],[0,0],[1,0],[2,0],[3,0],\
    [-3,-1],[-2,-1],[-1,-1],[0,-1],[1,-1],[2,-1],[3,-1],\
           [-1,-2], [0,-2], [1,-2],\
           [-1,-3], [0,-3], [1,-3]];

    # Get pos after mov
    p_copy = p.copy();
    
    p_copy.remove(mov[0]);
    p_copy.append(mov[1]);
    p_copy.remove(mov[2]);

    # Sort board
    pos_sorted = [];
    for h in holes:
        if h in p_copy:
            pos_sorted.append(h);

    # Check if board belongs to ns
    if pos_sorted in ns:
        return False
    else:
        return True


def putinns(pos):
    
    holes = [[-1,3],[0,3],[1,3],\
             [-1,2],[0,2],[1,2],\
    [-3,1],[-2,1],[-1,1],[0,1],[1,1],[2,1],[3,1],\
    [-3,0],[-2,0],[-1,0],[0,0],[1,0],[2,0],[3,0],\
    [-3,-1],[-2,-1],[-1,-1],[0,-1],[1,-1],[2,-1],[3,-1],\
           [-1,-2], [0,-2], [1,-2],\
           [-1,-3], [0,-3], [1,-3]];
    
    # Sort pos
    pos_sorted = [];
    for h in holes:
        if h in pos:
            pos_sorted.append(h);

    if pos_sorted in ns:
        print('We are getting a duplicate, something must be wrong!');

    # Put pos in ns
    ns.append(pos_sorted);


def movback(mov, pos):

    # <check if back move possible>
    
    # remove "jumped marble"
    pos.remove(mov[1]);
    # put in old position
    pos.append(mov[0]);
    # put back taken out marble
    pos.append(mov[2]);

    return pos

##

pos = [[-1,3],[0,3],[1,3],\
        [-1,2],[0,2],[1,2],\
[-3,1],[-2,1],[-1,1],[0,1],[1,1],[2,1],[3,1],\
[-3,0],[-2,0],[-1,0],[1,0],[2,0],[3,0],\
[-3,-1],[-2,-1],[-1,-1],[0,-1],[1,-1],[2,-1],[3,-1],\
       [-1,-2], [0,-2], [1,-2],\
       [-1,-3], [0,-3], [1,-3]];    # Set board

# pos = [[-3, 1], [-2, -1], [1, -3], [1, -1], [1, 1], [-1, 2]];

# pos = [[-3, 1], [-2, -1], [1, -3], [1, -1], [1, 1], [-1, 0], [-1, 1]]

# pos = [[-3, 1], [-2, -1], [1, -3], [1, -1], [1, 1], [-1, 0], [-1, 1]]

# pos = [[-3, 1], [1, 3], [-2, -1], [1, 1], [-1, 2], [1, -3], [1, 0], [1, -1]];

displayboard(pos);

ns = []; # Set bag of no solution boards
    
# ns = [[[-1, 2], [-3, 1], [1, 1], [-2, -1], [1, -1], [1, -3]]];

# ns = [[[1, 3], [-1, 2], [-3, 1], [1, 1], [-2, -1], [1, -2], [1, -3]]];

complete = False; 
movthread = [];

while(complete == False and len(ns) < 10000):
    end = False; 
    # Find next move, if possible
    for mar in pos:
         # Find possible moves for marble
        movs = findmoves(mar, pos);
        # Select allowed moves
        movs_copy = movs.copy();
        for m in movs_copy:
            p = pos;
            if not isvalid(m, p):
                movs.remove(m);
        # If move found then break and go to make move
        if len(movs) != 0:
            mov = movs[0];
            print('move found:', mov);
            break;
        # If no move found even for "last marble"(any) on present board
        if mar == pos[-1]:
            print('End of board')
            end = True

            # If only one marble on board, then game complete
            if len(pos) == 1:
                complete = True;
                print(movthread);

            # If more than one marble on board,
            if len(pos)>1:
                # 1. put board in no solution bag
                putinns(pos);
                print('boards in ns:', len(ns));
                # 2. move back one step:
                # 2.1 remove last move from thread
                backmov = movthread.pop();
                # 2.2 move back in pos
                movback(backmov, pos);
                # 2.3 Display board
                displayboard(pos);
                #input();
            break;            
            
    # If next move found
    if end == False:
        # 1. Make move
        pos = newpos(mov, pos);

        # 2. Add move to movthread
        movthread.append(mov);

        # Display change on board
        displayboard(pos);
        #print(movthread);
        #input();
