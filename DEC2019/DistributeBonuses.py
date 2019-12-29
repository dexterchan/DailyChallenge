# skill: array traversal
# difficulty : very easy
#You are the manager of a number of employees who all sit in a row. The CEO would like to give bonuses to all of your employees, but since the company did not perform so well this year the CEO would like to keep the bonuses to a minimum.

#The rules of giving bonuses is that:
#- Each employee begins with a bonus factor of 1x.
#- For each employee, if they perform better than the person sitting next to them, the employee is given +1 higher bonus (and up to +2 if they perform better than both people to their sides).

#Given a list of employee's performance, find the bonuses each employee should get.

#Example:
#Input: [1, 2, 3, 2, 3, 5, 1]
#Output: [1, 2, 3, 1, 2, 3, 1]
#Here's your starting point:

#Analysis:
#Trivial:
# traverse the array,
# bonus of current element is 1
# if prev element  lower than current element,
# bonus of current element +1
# if next element  lower than current element,
# bonus of current element +1


def getBonuses(performance):
    # Fill this in.
    bonuslst = []
    for i in range(len(performance)):
        bonus = 1
        if i-1>=0 and performance[i-1] < performance[i]:
            bonus += 1
        if i+1 < len(performance) and performance[i] > performance[i+1]:
            bonus += 1
        bonuslst.append(bonus)

    return bonuslst

print (getBonuses([1, 2, 3, 2, 3, 5, 1]))
# [1, 2, 3, 1, 2, 3, 1]