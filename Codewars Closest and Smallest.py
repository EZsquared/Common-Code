def split_and_weight(n_string):
    """ Takes a list of numbers in string or int, weighs them based on each num in split item.
    Return a list of weights in original order."""
    
    # Initiates an empty list to store item weights in
    weight_list = []

    # Iterates over split items to weight them
    for item in n_string:

        # Resets weight to 0 every item
        item_weight = 0

        # Adds each indiv. num in item together
        for num in item:
            item_weight += int(num)

        # Adds total weight to weight_list    
        weight_list.append(item_weight)
    
    return weight_list


def compare_weights(weight_list, n_string):
    """ Compares weight differences in a weight_list and returns all relevant information about the original numbers. """
    
    # Initiates a dictionary to store lowest weights and the respective information (weight, indice)
    final_weights_dict = {}

    # Iterates of the list of weights
    for i in range(len(weight_list)):

        # Creates an empty temp list to store all the compared difference between every value in the list
        temp_weights_list = []
        
        # Iterates over the list of weights again for each value in the list
        for j in range(len(weight_list)):

            # If this is the first number to be compared by, then initiate "diff"
            if j == 0:

                diff = False

            # Makes sure we are not comparing differences between the same number
            if i != j :

                # If difference between two numbers hasn't been calculated yet
                if not diff:
                    
                    # Calculate absolute difference between numbers
                    diff = abs(weight_list[i] - weight_list[j])
                    
                    # Store the Differences, Indicies, and weights (individual and total) in temp list
                    temp_weights_list.append([diff, i, j, i + j, weight_list[i] + weight_list[j]])
                
                #If difference has be calculated (not the first number compared)
                else:
                    
                    # If the difference in current numbers is lower then our previous diffence
                    if abs(weight_list[i] - weight_list[j]) < diff:
                        # Calculate absolute difference between numbers
                        diff = abs(weight_list[i] - weight_list[j])
                        # Store the Differences, Indicies, and weights (individual and total) in temp list
                        temp_weights_list.append([diff, i, j, i + j, weight_list[i] + weight_list[j]])

        # Iterates over a sorted temp_weights_list and compare the lowest differences even futher.
        for value in sorted(temp_weights_list):

            # Checks to see if current weight is already a key
            if value[0] not in final_weights_dict.keys():
                # Initiates that key if not.
                final_weights_dict[value[0]] = value

            else:
                # Checks total weight for both numbers to see if lower then current for that difference key
                if value[4] < final_weights_dict[value[0]][4]:
                    
                    # Overwrite that key's value to new lower number information.
                    final_weights_dict[value[0]] = value

                # If weights are the same, futher inspect Indice positions
                if value[4] == final_weights_dict[value[0]][4]:

                    # If total indicies is lower
                    if value[3] < final_weights_dict[value[0]][3]:
                        # Overwrite that key's value to new lower number information.
                        final_weights_dict[value[0]] = value
                else:
                    # Move to next difference if nothing lower.
                    continue
    
    # Store the first element of the sorted final_weights_dict, which will be lowest difference
    results = final_weights_dict[(sorted(final_weights_dict)[0])]

    # Break up results into returnable format
    # Take result indicies and grab weight and original number from starting lists.
    num1_weight = weight_list[results[1]]
    num1_indice = results[1]
    num1_orig = n_string[results[1]]

    num2_weight = weight_list[results[2]]
    num2_indice = results[2]
    num2_orig = n_string[results[2]]

    return [[num1_weight, num1_indice, int(num1_orig)], [num2_weight, num2_indice, int(num2_orig)]]

        
def closest(string):
    """ Takes string of Numbers and splits into a list to be passed to split_and_weight() function,
     then passes that to compare_weights to find lowest weight difference between numbers in string. """


    # Checks for empty string, and returns empty list.
    if string == "":
        return []
    
    # If string is not empty, perform all actions.
    else:
        # Splits numbers in string into individual items to be weighted.
        n_string = string.split()
        
        # Weighs split string and assigns to a list.
        weight_list = split_and_weight(n_string)

        # Take list of weights and compares them (difference, weight, indice)
        smallest_diff = compare_weights(weight_list, n_string)

    return smallest_diff
