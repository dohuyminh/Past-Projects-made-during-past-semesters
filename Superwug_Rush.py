# This is the code for COMP10001 (Foundations of Computing)
# Theme around the wugs and genetics
# P/S: Though this project's code is a distinct improvement from the last project's, 
# there are still things that can be optimized.
# The optimized version can be posted soon in the future.

# The DNA strand in question is a 16-element list of 0 and 1. 

def genome2features(genome):
    '''
    Function used to indicate whether a specific characteristic of a
    wug is considered superior or not
    '''
    # TODO: Write your function here
    
    dict_gene = {}  # Dictionary with the format "Characteristic: True/
    # False
    
    gene_com = []  # A 2-element list including the categorised charact-
    # eristic's superior gene format and the wug's characteristic
    # gene format
    
    join_gene_sup = []  # A list consisting of genomes that form the for-
    # mat of the characteristic's superior gene format
    
    join_gene = []  # A list consistig of genomes that form the format of
    # the wug's characteristic gene format
    
    # Assess every given characteristic 
    for a in range(len(characteristics)):
        
        # Form the format of the characteristic's superior gene format
        for b in range(len(superwug_genome)):
            if gene_zones[b] == a:
                join_gene_sup.append(str(superwug_genome[b]))
        sup_gene = ''.join(join_gene_sup)
        
        # Form the format of the wug's characteristic gene format
        for c in range(len(genome)):
            if gene_zones[c] == a:
                join_gene.append(str(genome[c]))
        gene = ''.join(join_gene)
        
        # Compare the formats in the gene_com list
        gene_com.append(sup_gene)
        gene_com.append(gene)
        dict_gene[characteristics[a]] = bool(len(set(gene_com)) == 1)
        
        # Clear everything to proceed to other characteristics
        join_gene_sup.clear()
        join_gene.clear()
        gene_com.clear()    
    
    # Return whether the wug's characteristics gene formats are the
    # same with the given superior gene format
    return list(dict_gene.values())
  
def report_population(population):
    '''
    Function used for recording all of the wugs' features and the count
    of the wugs with similar features
    '''
    # TODO: Write your function here
    
    feat = []  # A list consisting of all recorded features of the wugs
    
    feat_dict = {}  # A dictionary with the format of "(Features, sex): 
    # count"
    
    result = []  # A list with the elements' format of 
    # ((Features, sex), count)
    
    # Create the format (features, sex) for every wug
    for a in range(len(population)):
        feat.append(list(genome2features(population[a][0])))
    for b in range(len(feat)):
        feat[b].append(population[b][1])
    for c in range(len(feat)):
        feat[c] = tuple(feat[c])
    
    # Count the wugs with similar features and sexes
    for labeled in feat:
        if labeled in feat_dict:
            feat_dict[labeled] += 1
        else:
            feat_dict[labeled] = 1
    
    # Adding the elements of ((Features, sex), count) into the list
    features = list(feat_dict.keys())
    count = list(feat_dict.values())
    for f in range(len(count)):
        result.append((tuple(features[f]), count[f]))
    
    # Sorting and returning the list
    return sorted(result, reverse=True)
  
def rank(wug):
    '''
    Used to rank the wug based on how many superior characteristics 
    there are
    '''
    # TODO: Write your function here
    
    # Using the genome2features function for wug's assesment 
    assessing = genome2features(wug[0])
    count = 0
    
    # See how many superior characteristics there are 
    for element in assessing:
        if element:
            count += 1
    
    # Return the count
    return count
  
def insert_ranked(population, new_wug, limit=64):
    '''
    Modify the population list whenever a new wug is introduced to 
    population based on ranking
    '''
    # TODO: Write your function here
        
    # Adding the new wug, re-arranging wugs and removing those beyond
    # the given limit
    population.append(new_wug)
    population.sort(key=lambda x: rank(x), reverse=True)
    del population[limit:]
    
def proliferate(population, limit=64):
  '''
  Modify (and setting at the limit of) the population list through 
  cloning of the wugs in the population 
  '''
  # TODO: Write your function here
  new_gene = []  # Used to store the cloned wugs 

  # Assess every wug in population
  for a in range(len(population)):

      # Assess the genome of each wug
      for b in range(len(population[a][0])):

          # Reset, modify gene and form the cloned wug
          assess = population[a][0].copy()
          assess[b] = 1 if assess[b] == 0 else 0
          new_gene.append((assess, population[a][1]))

  # Adding the cloned wugs into the population using the 
  # insert_ranked function
  for c in range(len(new_gene)):
      insert_ranked(population, new_gene[c])
        
def custom_proliferate(paired):
    '''
    Function used to produce the outcome of the intercourse of the paired
    wugs in the population list, and the cloning based on the 2 
    offsprings from the intercourse, where the modification of the 1st
    half of the genome means Male, and Female if otherwise
    '''
    
    # Create the male offspring's format after intercousrse
    orig_male = (paired[1][0][:8] + paired[0][0][8:], 'M')
    
    new_population = []  # A list to store the cloned wugs and the 
    # offsprings after intercourse
    
    # Cloning the wugs based on the genome of the male's offspring
    for a in range(len(orig_male[0])):
        
        # Reset the genome to its original genome format and modify
        reset_gene = orig_male[0].copy()
        reset_gene[a] = 1 if reset_gene[a] == 0 else 0
        
        # Male for 1st half of genome's modification and Female for 
        # the other half
        if a <= 7:
            new_population.append((reset_gene, 'M'))
        else:
            new_population.append((reset_gene, 'F'))
    
    # Adding back the offsprings
    new_population.append(orig_male)
    new_population.append((orig_male[0], 'F'))
    return new_population

def scoring(female, male, coincidence_bonus=0):
    '''
    Calculating the sustainability score to see which male wug is 
    most suitable for the assessing female wug
    '''
    score = rank(male)  # Initial points based on rank
    
    # Assessing the genome2features of the male and the female
    for d in range(len(genome2features(female[0]))):
        
        # Additional/Minus points for every superior feature coincidence
        if genome2features(male[0])[d] and genome2features(female[0])[d]:
            score += coincidence_bonus
    
    # Return the score
    return score

def pairing(female_wug, male_wugs_list):
    '''
    Function used to determine the best male wug to pair with the 
    assessing female wug based on sustainability scores and ranking of 
    the wug
    '''
    top_males = []  # A list consisting of male wugs with the highest
    # sustainability score
    
    male_pts_list = []  # A list consisting of male wugs along with their
    # sustainability score
    
    # Scoring each male wug
    for male_wug in male_wugs_list:
        male_pts_list.append(scoring(female_wug, male_wug))
    
    # Check for male wugs with the highest sustainability scores
    for z in range(len(male_wugs_list)):
        if male_pts_list[z] == max(male_pts_list):
            insert_ranked(top_males, male_wugs_list[z])
    
    # Take the male wug with the lowest index for pairing
    return (female_wug, top_males[0])

def breed(population, limit=64, hermaphrodite=False, coincidence_bonus=0):
    '''
    Modifying the population list via breeding and cloning, with pairs of
    wugs based on sustainability score of the male wugs, or wugs in the 
    role of male if hermaphrodite is True 
    '''
    # TODO: Write your function here
    
    remaining = []  # A list of remaining wugs after pairing is finished
    
    intercourse = []  # A 2-element list consisting of the paired wugs
    
    # Sorting male and female wugs into their respective lists
    males = [wug1 for wug1 in population if wug1[1] == 'M']
    females = [wug2 for wug2 in population if wug2[1] == 'F']
    
    # Assess every female wug
    for fe in females:
        
        # Case of there being no male wug left to pair
        if males == []:
            remaining.append(fe)
        
        # Otherwise
        else:
            
            # Prepare the female wug for pairing
            intercourse.append(fe)
            
            # Pairing female with male, breeding and cloning 
            intercourse = pairing(fe, males)
            males.remove(intercourse[1])  
            intercourse = custom_proliferate(intercourse)
            for bred in intercourse:
                insert_ranked(population, bred)
            
            # Clear everything to assess other female wugs
            intercourse.clear()
    
    # Case of remaining male wugs not paired yet
    if males != []:
        for left in males:
            remaining.append(left)
    
    # If hermaphrodite is True, then proceed with pairing, breeding and
    # cloning with the remaining wugs 
    if hermaphrodite is True:
        while len(remaining) > 1:
            g = len(remaining)
            
            # Choosing the last one as "female" and the rest being "male"
            supposed_fe = remaining[g - 1]
            intercourse.append(supposed_fe)
            remaining.remove(supposed_fe)
            supposed_mas = remaining[:g - 1]
            
            # Pairing "female" with "male", breeding and cloning
            intercourse = pairing(supposed_fe, supposed_mas)
            remaining.remove(intercourse[1])
            intercourse = custom_proliferate(intercourse)
            for bred in intercourse:
                insert_ranked(population, bred)
            
            # Clearing everything for the next "Female" wug
            intercourse.clear()
