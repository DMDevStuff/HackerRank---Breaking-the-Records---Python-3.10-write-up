##    Maria plays college basketball and wants to go pro. Each season she
##    maintains a record of her play. She tabulates the number of times she
##    breaks her season record for most points and least points in a game.
##    Points scored in the first game establish her record for the season, and
##    she begins counting from there.

##    Given the scores for a season, determine the number of times Maria
##    breaks her records for most and least points scored during the season.

##### ##### ##### #####

#   Iterative solution
#   O(n)
#   n is the length of scores
#   Algo:
#       iterate over the scores and check them against the min and max
#       when a new min or max is found, increment the appropriate counter
#       return a list containing the counters

def breakingRecords(scores):

    min_score = scores[0]
    max_score = scores[0]
    min_count = 0
    max_count = 0

    for score in scores:

        if score < min_score:

            min_score = score
            min_count += 1

        elif score > max_score:

            max_score = score
            max_count += 1

    return [max_count, min_count]
