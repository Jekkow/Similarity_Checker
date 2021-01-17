# Similarity_Checker
A python similarity checker
V.0.0.3 | Made by: Jekkow

# What does this module:
This module compares strings on similarity and returns the name and a float percentage

# How to use:
    Create the Constructor:
        SC = Similarity_Checker()

    Set Values:
        SC.Set_Difference =
            (Default = 1)
        SC.Length_Difference =
            (Default = 2)
        SC.Minimum_Percentage =
            (Default = 0.75)

    Use the Check method:
        SC.Check("string that needs to be compared", ["List that contains the word(s) that the string will be compared with"])
