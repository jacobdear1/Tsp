############
############ ALTHOUGH I GIVE YOU THIS TEMPLATE PROGRAM WITH THE NAME 'skeleton.py', 
############ YOU CAN RENAME IT TO ANYTHING YOU LIKE. HOWEVER, FOR THE PURPOSES OF 
############ THE EXPLANATION IN THESE COMMENTS, I ASSUME THAT THIS PROGRAM IS STILL 
############ CALLED 'skeleton.py'.
############
############ IF YOU WISH TO IMPORT STANDARD MODULES, YOU CAN ADD THEM AFTER THOSE BELOW.
############ NOTE THAT YOU ARE NOT ALLOWED TO IMPORT ANY NON-STANDARD MODULES! TO SEE
############ THE STANDARD MODULES, TAKE A LOOK IN 'validate_before_handin.py'.
############
############ DO NOT INCLUDE ANY COMMENTS ON A LINE WHERE YOU IMPORT A MODULE.
############

import os
import sys
import time
import random

############ START OF SECTOR 1 (IGNORE THIS COMMENT)
############
############ NOW PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS.
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############ BY 'DO NOT TOUCH' I REALLY MEAN THIS. EVEN CHANGING THE SYNTAX, BY
############ ADDING SPACES OR COMMENTS OR LINE RETURNS AND SO ON, COULD MEAN THAT
############ CODES MIGHT NOT RUN WHEN I RUN THEM!
############

def read_file_into_string(input_file, ord_range):
    the_file = open(input_file, 'r') 
    current_char = the_file.read(1) 
    file_string = ""
    length = len(ord_range)
    while current_char != "":
        i = 0
        while i < length:
            if ord(current_char) >= ord_range[i][0] and ord(current_char) <= ord_range[i][1]:
                file_string = file_string + current_char
                i = length
            else:
                i = i + 1
        current_char = the_file.read(1)
    the_file.close()
    return file_string

def remove_all_spaces(the_string):
    length = len(the_string)
    new_string = ""
    for i in range(length):
        if the_string[i] != " ":
            new_string = new_string + the_string[i]
    return new_string

def integerize(the_string):
    length = len(the_string)
    stripped_string = "0"
    for i in range(0, length):
        if ord(the_string[i]) >= 48 and ord(the_string[i]) <= 57:
            stripped_string = stripped_string + the_string[i]
    resulting_int = int(stripped_string)
    return resulting_int

def convert_to_list_of_int(the_string):
    list_of_integers = []
    location = 0
    finished = False
    while finished == False:
        found_comma = the_string.find(',', location)
        if found_comma == -1:
            finished = True
        else:
            list_of_integers.append(integerize(the_string[location:found_comma]))
            location = found_comma + 1
            if the_string[location:location + 5] == "NOTE=":
                finished = True
    return list_of_integers

def build_distance_matrix(num_cities, distances, city_format):
    dist_matrix = []
    i = 0
    if city_format == "full":
        for j in range(num_cities):
            row = []
            for k in range(0, num_cities):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    elif city_format == "upper_tri":
        for j in range(0, num_cities):
            row = []
            for k in range(j):
                row.append(0)
            for k in range(num_cities - j):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    else:
        for j in range(0, num_cities):
            row = []
            for k in range(j + 1):
                row.append(0)
            for k in range(0, num_cities - (j + 1)):
                row.append(distances[i])
                i = i + 1
            dist_matrix.append(row)
    if city_format == "upper_tri" or city_format == "strict_upper_tri":
        for i in range(0, num_cities):
            for j in range(0, num_cities):
                if i > j:
                    dist_matrix[i][j] = dist_matrix[j][i]
    return dist_matrix

def read_in_algorithm_codes_and_tariffs(alg_codes_file):
    flag = "good"
    code_dictionary = {}   
    tariff_dictionary = {}  
    if not os.path.exists(alg_codes_file):
        flag = "not_exist"  
        return code_dictionary, tariff_dictionary, flag
    ord_range = [[32, 126]]
    file_string = read_file_into_string(alg_codes_file, ord_range)  
    location = 0
    EOF = False
    list_of_items = []  
    while EOF == False: 
        found_comma = file_string.find(",", location)
        if found_comma == -1:
            EOF = True
            sandwich = file_string[location:]
        else:
            sandwich = file_string[location:found_comma]
            location = found_comma + 1
        list_of_items.append(sandwich)
    third_length = int(len(list_of_items)/3)
    for i in range(third_length):
        code_dictionary[list_of_items[3 * i]] = list_of_items[3 * i + 1]
        tariff_dictionary[list_of_items[3 * i]] = int(list_of_items[3 * i + 2])
    return code_dictionary, tariff_dictionary, flag

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ THE RESERVED VARIABLE 'input_file' IS THE CITY FILE UNDER CONSIDERATION.
############
############ IT CAN BE SUPPLIED BY SETTING THE VARIABLE BELOW OR VIA A COMMAND-LINE
############ EXECUTION OF THE FORM 'python skeleton.py city_file.txt'. WHEN SUPPLYING
############ THE CITY FILE VIA A COMMAND-LINE EXECUTION, ANY ASSIGNMENT OF THE VARIABLE
############ 'input_file' IN THE LINE BELOW iS SUPPRESSED.
############
############ IT IS ASSUMED THAT THIS PROGRAM 'skeleton.py' SITS IN A FOLDER THE NAME OF
############ WHICH IS YOUR USER-NAME, E.G., 'abcd12', WHICH IN TURN SITS IN ANOTHER
############ FOLDER. IN THIS OTHER FOLDER IS THE FOLDER 'city-files' AND NO MATTER HOW
############ THE NAME OF THE CITY FILE IS SUPPLIED TO THIS PROGRAM, IT IS ASSUMED THAT 
############ THE CITY FILE IS IN THE FOLDER 'city-files'.
############
############ END OF SECTOR 1 (IGNORE THIS COMMENT)

input_file = "AISearchfile012.txt"

############ START OF SECTOR 2 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if len(sys.argv) > 1:
    input_file = sys.argv[1]

############ END OF SECTOR 2 (IGNORE THIS COMMENT)
path_for_city_files = "../city-files"
############ START OF SECTOR 3 (IGNORE THIS COMMENT)
    
if os.path.isfile(path_for_city_files + "/" + input_file):
    ord_range = [[32, 126]]
    file_string = read_file_into_string(path_for_city_files + "/" + input_file, ord_range)
    file_string = remove_all_spaces(file_string)
    print("I have found and read the input file " + input_file + ":")
else:
    print("*** error: The city file " + input_file + " does not exist in the city-file folder.")
    sys.exit()

location = file_string.find("SIZE=")
if location == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
comma = file_string.find(",", location)
if comma == -1:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()
    
num_cities_as_string = file_string[location + 5:comma]
num_cities = integerize(num_cities_as_string)
print("   the number of cities is stored in 'num_cities' and is " + str(num_cities))

comma = comma + 1
stripped_file_string = file_string[comma:]
distances = convert_to_list_of_int(stripped_file_string)

counted_distances = len(distances)
if counted_distances == num_cities * num_cities:
    city_format = "full"
elif counted_distances == (num_cities * (num_cities + 1))/2:
    city_format = "upper_tri"
elif counted_distances == (num_cities * (num_cities - 1))/2:
    city_format = "strict_upper_tri"
else:
    print("*** error: The city file " + input_file + " is incorrectly formatted.")
    sys.exit()

dist_matrix = build_distance_matrix(num_cities, distances, city_format)
print("   the distance matrix 'dist_matrix' has been built.")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY!
############
############ YOU NOW HAVE THE NUMBER OF CITIES STORED IN THE INTEGER VARIABLE 'num_cities'
############ AND THE TWO_DIMENSIONAL MATRIX 'dist_matrix' HOLDS THE INTEGER CITY-TO-CITY 
############ DISTANCES SO THAT 'dist_matrix[i][j]' IS THE DISTANCE FROM CITY 'i' TO CITY 'j'.
############ BOTH 'num_cities' AND 'dist_matrix' ARE RESERVED VARIABLES AND SHOULD FEED
############ INTO YOUR IMPLEMENTATIONS.
############
############ THERE NOW FOLLOWS CODE THAT READS THE ALGORITHM CODES AND TARIFFS FROM
############ THE TEXT-FILE 'alg_codes_and_tariffs.txt' INTO THE RESERVED DICTIONARIES
############ 'code_dictionary' AND 'tariff_dictionary'. DO NOT AMEND THIS CODE!
############ THE TEXT FILE 'alg_codes_and_tariffs.txt' SHOULD BE IN THE SAME FOLDER AS
############ THE FOLDER 'city-files' AND THE FOLDER WHOSE NAME IS YOUR USER-NAME.
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############
############ END OF SECTOR 3 (IGNORE THIS COMMENT)

############ START OF SECTOR 4 (IGNORE THIS COMMENT)
path_for_alg_codes_and_tariffs = "../alg_codes_and_tariffs.txt"
############ END OF SECTOR 4 (IGNORE THIS COMMENT)

############ START OF SECTOR 5 (IGNORE THIS COMMENT)
code_dictionary, tariff_dictionary, flag = read_in_algorithm_codes_and_tariffs(path_for_alg_codes_and_tariffs)

if flag != "good":
    print("*** error: The text file 'alg_codes_and_tariffs.txt' does not exist.")
    sys.exit()

print("The codes and tariffs have been read from 'alg_codes_and_tariffs.txt':")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU NOW NEED TO SUPPLY SOME PARAMETERS.
############
############ THE RESERVED STRING VARIABLE 'my_user_name' SHOULD BE SET AT YOUR
############ USER-NAME, E.G., "abcd12"
############
############ END OF SECTOR 5 (IGNORE THIS COMMENT)

my_user_name = "hfjv29"

############ START OF SECTOR 6 (IGNORE THIS COMMENT)
############
############ YOU CAN SUPPLY, IF YOU WANT, YOUR FULL NAME. THIS IS NOT USED AT ALL BUT SERVES AS
############ AN EXTRA CHECK THAT THIS FILE BELONGS TO YOU. IF YOU DO NOT WANT TO SUPPLY YOUR
############ NAME THEN EITHER SET THE STRING VARIABLES 'my_first_name' AND 'my_last_name' AT 
############ SOMETHING LIKE "Mickey" AND "Mouse" OR AS THE EMPTY STRING (AS THEY ARE NOW;
############ BUT PLEASE ENSURE THAT THE RESERVED VARIABLES 'my_first_name' AND 'my_last_name'
############ ARE SET AT SOMETHING).
############
############ END OF SECTOR 6 (IGNORE THIS COMMENT)

my_first_name = "Jacob"
my_last_name = "Dear"

############ START OF SECTOR 7 (IGNORE THIS COMMENT)
############
############ YOU NEED TO SUPPLY THE ALGORITHM CODE IN THE RESERVED STRING VARIABLE 'algorithm_code'
############ FOR THE ALGORITHM YOU ARE IMPLEMENTING. IT NEEDS TO BE A LEGAL CODE FROM THE TEXT-FILE
############ 'alg_codes_and_tariffs.txt' (READ THIS FILE TO SEE THE CODES).
############
############ END OF SECTOR 7 (IGNORE THIS COMMENT)

algorithm_code = "AC"

############ START OF SECTOR 8 (IGNORE THIS COMMENT)
############
############ PLEASE SCROLL DOWN UNTIL THE NEXT BLOCK OF CAPITALIZED COMMENTS STARTING
############ 'HAVE YOU TOUCHED ...'
############
############ DO NOT TOUCH OR ALTER THE CODE IN BETWEEN! YOU HAVE BEEN WARNED!
############

if not algorithm_code in code_dictionary:
    print("*** error: the algorithm code " + algorithm_code + " is illegal")
    sys.exit()
print("   your algorithm code is legal and is " + algorithm_code + " -" + code_dictionary[algorithm_code] + ".")

############
############ HAVE YOU TOUCHED ANYTHING ABOVE? BECAUSE EVEN CHANGING ONE CHARACTER OR
############ ADDING ONE SPACE OR LINE RETURN WILL MEAN THAT THE PROGRAM YOU HAND IN
############ MIGHT NOT RUN PROPERLY! SORRY TO GO ON ABOUT THIS BUT YOU NEED TO BE 
############ AWARE OF THIS FACT!
############
############ YOU CAN ADD A NOTE THAT WILL BE ADDED AT THE END OF THE RESULTING TOUR FILE IF YOU LIKE,
############ E.G., "in my basic greedy search, I broke ties by always visiting the first 
############ city found" BY USING THE RESERVED STRING VARIABLE 'added_note' OR LEAVE IT EMPTY
############ IF YOU WISH. THIS HAS NO EFFECT ON MARKS BUT HELPS YOU TO REMEMBER THINGS ABOUT
############ YOUR TOUR THAT YOU MIGHT BE INTERESTED IN LATER.
############
############ END OF SECTOR 8 (IGNORE THIS COMMENT)

added_note = ""

############
############ NOW YOUR CODE SHOULD BEGIN.
############

import time

start_time = time.time()


def nearest_neighbour(dist_matrix):
    import queue as q 

    # intialise lists and variables
    cities = []
    new_tour = []

    # intialise tour_length to be nothing
    tour_length = 0


    # creation of a priority queue
    pq = q.PriorityQueue()

    # intialises the node as specified in lectures
    newid = 1

    node = [(newid, 0, '-', '-', 0, 0)]

    # adds the node to the queue
    pq.put(node)



    # tour_length acts as the goal node; as once this is 'full' we return the tour
    if tour_length == num_cities:
        print("done")

    else:
        # adds node to the fringe (which is a priority queue)

        # checks if fringe is not empty
        while pq.empty() == False:
            # pops node of highest priority
            f = pq.get()

            # undo all values from popped node
            id = f[0][0]
            state = f[0][1]
            parent_id = f[0][2]
            action = f[0][3]
            path_cost = f[0][4]
            depth = f[0][5]

            # adds the whole node contents to the list of visited cities
            # as only one node is popped for each city
            cities.append(f)

            # adds the state = city number to a list, allows us to make sure 
            # we get no duplicated cities
            for c in cities:
                new_tour.append(c[0][1])

            # represents the index for each child node
            child_num = 0

            # loops through each value for the current city = state            
            for child in dist_matrix[state]:

                # means this doesn't generate nodes that have already been visited, in new_tour
                # or the child equal to the state we are at, e.g. won't do a node for child 1 if the state is 1
                if child_num != state and child_num not in new_tour:
                    
                    # increments the id for the queue
                    newid = newid + 1

                    # define action to always be move, so don't worry about this?
                    # dist_matrix[state][child], represents the path_cost from the current state and child
                    new_node = [(newid, child_num, id, 'move', path_cost + dist_matrix[state][child_num], depth+1)]

                    # use this to compare the nodes
                    current_new_node_path_cost = new_node[0][4]

                    
                    # add evaulation function here, such that it only goes down path 1, not down 2 as well, as we are doing greedy. 

                    # we use the hueristic function of the shortest path cost to the next node. local optima
                    # if there is only one node in the queue, compare this to find one of shortest path
                    # we will only ever have one node in the queue at each time 
                    if pq.qsize() == 1:
                        # node to compare with
                        comparison_node = pq.get()
                        # gets the path cost, as it is greedy, we want the shortest path cost?
                        comparison_node_path_cost = comparison_node[0][4]
                        
                        # if the current node in the queue has a shorter path cost than the new node
                        # then we put the current node back on the queue
                        if comparison_node_path_cost < current_new_node_path_cost:
                            pq.put(comparison_node)

                        # else we add the new_node to the queue and get rid of the other node from the queue entirely
                        else:
                            pq.put(new_node)

                    # in the case that the size is equal to 0, we add the new_node (base case)
                    else:
                        pq.put(new_node)
                    # adds the child_num to the tour, as this is the next node to be added
                    # not sure how to backtrack currently.
            
            # increments the child_num, which allows us to look at the next city in the row
                child_num = child_num + 1

        # has now finished, so we need to construct the tour from the nodes we have in our cities list
        tour = []
        # loops through the list containing the visited cities and appends the value to the tour list
        # reconstructs the tours correctly
        for i in cities:
            # use i[0][1] as this holds state/city id
            tour.append(i[0][1])
            
        # calculates the length of the tour, adaptation of Iain's code
        for i in range(0, num_cities - 1):
            tour_length = tour_length + dist_matrix[tour[i]][tour[i + 1]]
        tour_length = tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
    # returns the local optimum tour length for nearest_neighbour algorithim
    return tour_length

# calculates the length of the tour
def calculate_path_length(x):
    tour_length = 0
    for i in range(0, num_cities - 1):
        tour_length = tour_length + dist_matrix[x[i]][x[i + 1]]
    tour_length = tour_length + dist_matrix[x[num_cities - 1]][x[0]]
    return tour_length


# set up core parameters, good params found in slide 8, lecture 8;
max_it = 1000 # just guessing here
num_of_ants = num_cities

alpha = 1
beta = 3.5 #(2<=beta<=5)

# pheromone
# works out the length of tour produced by nearest neighbour algorithm
Lnn = nearest_neighbour(dist_matrix)
intial_pheromone =  1/Lnn #num_of_ants / L^nn # tau, inital pheromone
pheromone_decay_rate = 0.01 # rho, evaporation rate

# delta_tau is defined later on

# stores the resulting best path/tour
best_tour = []


# fill each position with intial_pheromone
# creates an array of the same size as dist_matrix, with the intital pheromone as the value for each of the values
pheromone = [[intial_pheromone for col in range(num_of_ants)] for row in range(num_of_ants)]

# creates a random path, of unique values between and number of cities, which is dependent on file
best_path = random.sample(range(0, num_cities), num_cities)

# works out the tour_length of our randomly chosen 'best' path
best_tour_length = calculate_path_length(best_path)

# intialise iteration at t = 0
t = 0

# either stops when it reaches max iterations, or in the case it just takes too long -> no longer than 40 seconds
while t < max_it and time.time() - start_time < 45: # repeat for max_it iterations

    # has each of the (ants)'N' solutions in
    k_paths = []  
    k_paths_lengths = 0

    # looks through each ant, vertex is it on is represented by choosing a different start city each time

    #print("after it p", pheromone)
    for n in range(1,num_of_ants): # for each ant, in the range of number of total ants
        
        # contains the solution for each ant
        solution = []

        # randomly generate the first ant
        ant = random.randint(0, num_cities-1)
        solution.append(ant)

        # loops through all cities
        for i in range(num_cities):
            
            # iterates through until all cities have been appended to the solution
            if len(solution) != num_cities:

                # adds any values already in solution (visited cities to be forbidden)
                Fk = solution.copy()

                # intialises lists for when we need to work out the probability later 
                list_of_probs = []
                city_list = []
                sum = 0
                for j in range(num_cities):

                    # if the value is not in the forbidden list of values
                    if j not in Fk:

                        # just in case the value is 0, then gives it a heuristic desirability of 0, as we don't want to choose it
                        if dist_matrix[ant][j] == 0:
                            hueristic_desirability = 0.01
                        else:
                            hueristic_desirability = 1 /dist_matrix[ant][j]
                        # finds out the current pheronome level that corresponds to that position in the dist_matrix we are currently at
                        # pheromone is an array of the same shape and size to dist_matrix, so there is a value in this that corresponds to each
                        # value of the dist matrix
                        current_pheromone_level = pheromone[ant][j]

                        # probability of selecting city j, when we are currently at city i = (ant)
                        probability = ((current_pheromone_level * alpha) * (hueristic_desirability * beta))
                        # city related to probability, adds it to a list, which will allow us to find the next city to go to
                        city_list.append(j)
                        # appends the probability of selecting the current city to a list, notice done at the same time as city_list,
                        list_of_probs.append(probability)

                        # sums up all of the probabilites for each of the cities the ant could visit
                        sum = probability + sum

                        # adds the city to the forbidden list, as it has been visited so cannot be visited anymore 
                        Fk.append(j)

                list_of_sums = []
                # works out the probabilties for each of the cities, as we need to divide this by the sum
                for value in list_of_probs:
                    # divides the value by the sum of the probalities of all cities, 
                    value = value / sum
                    # adds to a list so we can compare these and extract the one of the probabilities 
                    list_of_sums.append(value)

                # takes a random choice of the next city to move to, using the list_of_sums, which has the probabilites in as the weighting
                # takes one value from the list
                next_city = random.choices(city_list, weights=list_of_sums, k=1)[0]
                # adds this city, with the highest probability to the solution, as this is the next_city we are going to visit
                solution.append(next_city)

            # ant takes the value of this city of highest prob as the next one to visit
            # will then work out the suitable neighbours of the new city
            ant = next_city
        # add each solution to the list, which we can then use to compare them at the end
        k_paths.append(solution)

    # intialise delta_tau here, so we can recalculate for each of the N tours
    # creates an array of the same size as dist_matrix, with the 0, represents delta_tau
    delta_tau = [[0 for col in range(num_of_ants)] for row in range(num_of_ants)]
    path_list_length = []
    # finds the path length of each of the (ants) 'N' paths
    for path in k_paths:
        # reset it each time, needs to be independent
        k_paths_lengths = calculate_path_length(path)
        # adds each length to a list
        path_list_length.append(k_paths_lengths)

        # finds the shortest path, as we want solution of shortest length
        min_path_length = min(path_list_length)
        # finds the index of the shortest path
        min_path_index = path_list_length.index(min_path_length)
        # finds the 'best' path, using the index of the shortest path on the list containing the 'N' paths
        min_path = k_paths[min_path_index]

    # update the values of delta_tau for those cities in any of the N tours generated, amount of pheromone is 
    # dependent on the length of the tour
        for city in range(0, num_cities-1):
            # finds the value of the pheromone at each edges in best_tour
            current_pheromone_value = delta_tau[path[city]][path[city+1]]

            # value added depends on the length of the path, less pheromone added if the path is less optimal
            pheromone_value = 1 / calculate_path_length(path)

            # adds the new pheromone to the pheromone that was already there
            delta_tau[path[city]][path[city+1]] = current_pheromone_value + pheromone_value
        # makes sure that all pheromone values, even for last city are correctly updated
        last_current = delta_tau[path[num_cities - 1]][path[0]] 
        # adds it to the final value that's not in the range as well
        delta_tau[path[num_cities - 1]][path[0]] = last_current + pheromone_value

    # compare the shortest path we have achieved from the N ants with the current best solution
    if min_path_length < best_tour_length:
        best_tour = min_path
        best_tour_length = min_path_length

    # deposit/evaporate pheromone on edges -> after best solution is found evaporating occuring
    for row in range(num_of_ants):
        for col in range(num_of_ants):
            pheromone[row][col] = (1-pheromone_decay_rate)*pheromone[row][col] + delta_tau[row][col]
    
    # next iteration
    t = t + 1

    
    # once the number of iterations has finished, set best_tour = tour, set tour_length as well
    tour = best_tour
    tour_length = best_tour_length


############ START OF SECTOR 9 (IGNORE THIS COMMENT)
############
############ YOUR CODE SHOULD NOW BE COMPLETE AND WHEN EXECUTION OF THIS PROGRAM 'skeleton.py'
############ REACHES THIS POINT, YOU SHOULD HAVE COMPUTED A TOUR IN THE RESERVED LIST VARIABLE 'tour', 
############ WHICH HOLDS A LIST OF THE INTEGERS FROM {0, 1, ..., 'num_cities' - 1} SO THAT EVERY INTEGER
############ APPEARS EXACTLY ONCE, AND YOU SHOULD ALSO HOLD THE LENGTH OF THIS TOUR IN THE RESERVED
############ INTEGER VARIABLE 'tour_length'.
############
############ YOUR TOUR WILL BE PACKAGED IN A TOUR FILE OF THE APPROPRIATE FORMAT AND THIS TOUR FILE'S,
############ NAME WILL BE A MIX OF THE NAME OF THE CITY FILE, THE NAME OF THIS PROGRAM AND THE
############ CURRENT DATE AND TIME. SO, EVERY SUCCESSFUL EXECUTION GIVES A TOUR FILE WITH A UNIQUE
############ NAME AND YOU CAN RENAME THE ONES YOU WANT TO KEEP LATER.
############
############ DO NOT TOUCH OR ALTER THE CODE BELOW THIS POINT! YOU HAVE BEEN WARNED!
############

flag = "good"
length = len(tour)
for i in range(0, length):
    if isinstance(tour[i], int) == False:
        flag = "bad"
    else:
        tour[i] = int(tour[i])
if flag == "bad":
    print("*** error: Your tour contains non-integer values.")
    sys.exit()
if isinstance(tour_length, int) == False:
    print("*** error: The tour-length is a non-integer value.")
    sys.exit()
tour_length = int(tour_length)
if len(tour) != num_cities:
    print("*** error: The tour does not consist of " + str(num_cities) + " cities as there are, in fact, " + str(len(tour)) + ".")
    sys.exit()
flag = "good"
for i in range(0, num_cities):
    if not i in tour:
        flag = "bad"
if flag == "bad":
    print("*** error: Your tour has illegal or repeated city names.")
    sys.exit()
check_tour_length = 0
for i in range(0, num_cities - 1):
    check_tour_length = check_tour_length + dist_matrix[tour[i]][tour[i + 1]]
check_tour_length = check_tour_length + dist_matrix[tour[num_cities - 1]][tour[0]]
if tour_length != check_tour_length:
    flag = print("*** error: The length of your tour is not " + str(tour_length) + "; it is actually " + str(check_tour_length) + ".")
    sys.exit()
print("You, user " + my_user_name + ", have successfully built a tour of length " + str(tour_length) + "!")

local_time = time.asctime(time.localtime(time.time()))
output_file_time = local_time[4:7] + local_time[8:10] + local_time[11:13] + local_time[14:16] + local_time[17:19]
output_file_time = output_file_time.replace(" ", "0")
script_name = os.path.basename(sys.argv[0])
if len(sys.argv) > 2:
    output_file_time = sys.argv[2]
output_file_name = script_name[0:len(script_name) - 3] + "_" + input_file[0:len(input_file) - 4] + "_" + output_file_time + ".txt"

f = open(output_file_name,'w')
f.write("USER = " + my_user_name + " (" + my_first_name + " " + my_last_name + "),\n")
f.write("ALGORITHM CODE = " + algorithm_code + ", NAME OF CITY-FILE = " + input_file + ",\n")
f.write("SIZE = " + str(num_cities) + ", TOUR LENGTH = " + str(tour_length) + ",\n")
f.write(str(tour[0]))
for i in range(1,num_cities):
    f.write("," + str(tour[i]))
f.write(",\nNOTE = " + added_note)
f.close()
print("I have successfully written your tour to the tour file:\n   " + output_file_name + ".")

############ END OF SECTOR 9 (IGNORE THIS COMMENT)
    
    











    


