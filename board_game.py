
from collections import deque

def dice_game(nspace):
    dq = deque([0,0,0,0,0,1])
    for roll in range( nspace-1):
        sumpartial = sum(dq)
        dq.append(sumpartial)
        dq.popleft()
    return sum(dq)

print(dice_game(610))

'''
14527490260516100855695859704819627818108010882741117227956927412305738742399171256642436462028811566617818991926058940988565927870172608545709804976244851391054850231415387973537361
'''
