# This is the first project I made during my time at COMP10001 (Foundations of Computing)
# This is a bee-themed project. 
# P/S: This is my first project ever, most of this code's sections can be optimized,
# and I may re-optimize it and post it in a seperate file.
# I would not recommend using this project's code for reference, for it is filled with bad coding practices. 

def length_busyb(flowers, hive):
    '''
    Take the co-ordinates of the bee's hive and the flowers to
    calculate the total length of the bee's trajectory
    '''
    sum1 = []  # Collect the distance values between the flowers
    
    sum2 = []  # Collect the distance values between the hive and the first
    # flower and between the last flower and the hive            
    
    # Calculate the distances between flowers
    for i in range(0, len(flowers) - 1):
        distance2x = abs(flowers[i][0] - flowers[i + 1][0])
        distance2y = abs(flowers[i][1] - flowers[i + 1][1])
        distance2 = distance2x + distance2y
        sum2.append(distance2) 
    
    # Calculate distance between the hive and the first flower
    distance1x = abs(hive[0] - flowers[0][0])
    distance1y = abs(hive[1] - flowers[0][1])
    distance1 = distance1x + distance1y
    
    # Calculate distance between the last flower and the hive
    distance3x = abs(flowers[len(flowers) - 1][0] - hive[0])
    distance3y = abs(flowers[len(flowers) - 1][1] - hive[1])
    distance3 = distance3x + distance3y
    
    # Collect the two last distance value
    sum1.append(distance1) 
    sum1.append(distance3) 
   
    # Return the total distance the bee traveled
    return sum(sum1) + sum(sum2)
  
def locate_busyb(flowers, xmax, ymax):
    '''
    Take the co-ordinates of the flowers and the size of the assessing
    field to find the most optimal place to place the artificial flower based
    on distance
    '''
    cord = []  # Collect all the available co-ordinates aside the real flowers
    
    val = []  # Used for calculating the distance between the co-ordinates
    # and the flowers later
    
    total_distance = []  # Used for storing the value of the total distance
    # between the assessing co-ordinates and the flowers
    
    # Check if there is no flower
    if len(flowers) == 0:
        return None
    
    # Collect all available locations besides the flowers'
    for a in range(0, ymax + 1):
        for b in range(0, xmax + 1):
            if (b, a) not in flowers:
                cord.append((b, a))
    
    # Check if there is no position left
    if len(cord) == 0:
        return None
    
    # Collect the distance value between positions and flowers
    for c in range(0, len(cord)):
        for d in range(0, len(flowers)):
            distance1 = abs(cord[c][0] - flowers[d][0])
            distance2 = abs(cord[c][1] - flowers[d][1])
            distance = distance1 + distance2
            val.append(distance)
        total_distance.append(sum(val))
        val.clear()
    
    # Return the optimized position based on distance
    return cord[total_distance.index(max(total_distance))]
  
def popular_busyb(flowers, visits, hive):
    '''
    Take the dictionary of 'flowers', containing the types and the co-ordinates
    and visits, and the hive's co-ordinate to find out the most visited flower
    based on distance
    '''
    if flowers == {} or visits == {} or hive == ():
        return None
    else:
        cord = []  # Record the co-ordinates of the flowers
        
        dist = []  # Record the distance values between the hive and the flower
        
        dist_dic = {}  # Dictionary containing the type of flowers and the
        # total distance between it and the hive
        
        flower_cloud = []  # Record all the types of flowers
        
        valid = []  # Record all the flower types with the maximum distance
        
        # Convert 'visits' to list of tuple with flower types and co-ordinates
        # for later assessment
        assess_dict = list(flowers.items())
        assess_visits = list(visits)
        for a in range(0, len(assess_visits)):
            for b in range(0, len(assess_dict)):
                if assess_visits[a] == assess_dict[b][0]:
                    assess_visits[a] = assess_dict[b][1]
        
        # Collect types of flowers for later assessment
        for c in range(0, len(assess_visits)):
            flower_cloud.append(assess_visits[c][0])
        flower_cloud = list(set(flower_cloud))
        
        # Create a dictionary with type of flowers and total distance
        for d in range(0, len(flower_cloud)):
            for e in range(0, len(assess_visits)):
                if assess_visits[e][0] == flower_cloud[d]:
                    cord.append((assess_visits[e][1], assess_visits[e][2]))
            
            # Calculate the distance betweeen hive and flowers
            for f in range(0, len(cord)):
                distance1 = abs(cord[f][0] - hive[0])
                distance2 = abs(cord[f][1] - hive[1])
                distance = distance1 + distance2
                dist.append(distance)
            true_distance = sum(dist)
            
            # Add flower type and total distance to dictionary
            # and clear datas for later assessment
            dist_dic[flower_cloud[d]] = true_distance
            dist.clear()
            cord.clear()
    
    # Assess and see what flower has the most weight
    list_of_flowers = list(dist_dic.keys())
    weight = list(dist_dic.values())
    for g in range(0, len(weight)):
        if weight[g] == max(weight):
            valid.append(list_of_flowers[g])
    
    # Return the most visited flower based on alphabetical order 
    valid = sorted(valid)
    return valid[0]
  
def swarm_busyb(trajectories, duration):
    '''
    Take the trajectories of the bees in the form of a list and assess
    whether the longest trajectory of the bees is greater or equal to the 
    given duration's value
    '''
    count = []  # Used for counting the time when 2 bees are in the same 
    # co-ordinate for later assessment
    
    each_duration = []  # Record the longest mutual trajectory between the
    # assessing bee with other bees
    
    max_duration = []  # Record the longest mutual trajectory of the assessing
    # bee based on each_duration
    
    assess = []  # Used to group the consecutive co-ordinates where the  
    # assessing bees are 
    
    counter = 0  # 0 is for not in the same co-ordinate, 1 is for the same
    # co-ordinate
    
    # Assess every trajectory of every bee
    for a in range(0, len(trajectories)):
        
        # Compare the trajectory of one bee with the others'
        for b in range(0, len(trajectories)):
            if trajectories[b] == trajectories[a]:
                each_duration.append(0)
            else:
                
                # Count the number of mutual positions of assessing bees 
                for c in range(0, len(trajectories[b])):
                    if trajectories[b][c] == trajectories[a][c]:
                        count.append(1)
                    else: 
                        count.append(0)
                
                # Count the longest duration of each bee
                for d in range(0, len(count)):
                    if count[d] == 1:
                        if d == len(count) - 1:
                            counter += 1
                            assess.append(counter)
                        else:
                            counter += 1
                    if count[d] == 0:
                        assess.append(counter)
                        counter = 0
                
                # Add the longest mutual trajectory of each bee
                each_duration.append(max(assess))
                assess.clear()
                count.clear()
                counter = 0
        
        # Collect the maximum value of each bee's mutual trajaectory
        max_duration.append(max(each_duration))
        each_duration.clear()

    # Compare the longest trajectories duration to the given duration 
    return max(max_duration) >= duration
