class checker():
    # Similarity Checker V.0.1.0 | Made by Jekkow
    def __init__(self, Set_Difference = 1, Length_Difference = 2, Minimum_Percentage = 0.75):
        # Set Variables
        self.Set_Difference = Set_Difference # Public Variable
        self.Length_Difference = Length_Difference  # Public Variable
        self.Minimum_Percentage = Minimum_Percentage  # Public Variable
        self.__Results = {}  # Private Variable
        self.__Set_Dictionary = {}  # Private Variable
        self.__String_Sets = {}  # Private Variable

    def Check(self, string, list):
        self.__Check(string, list)  # Call Private method
        return self.__Results  # Return results

    def __Check(self, string, list):  # Private method Check
        self.__Set_Dictionary = self.__Create_Keys(list)
        self.__String_Sets = self.__Create_Keys([string])
        self.__Results = self.__Compare_Sets(self.__String_Sets, self.__Set_Dictionary)

    def __Create_Keys(self, list):
        dictionary = {}  # Create new dictionry
        for item in list:
            uppercased = ""  # Reset value
            for letter in item:
                if(letter != " "):  # If the letter is a blank, remove the blank space
                    uppercased += letter.upper()  # Make the letter uppercased
            # Set dictionary key with empty nested dictionary
            dictionary[uppercased] = []
            # When uppercased name in completed, create the sets of this name
            self.__Create_Set(uppercased, dictionary)
        return dictionary
    
    def __Create_Set(self, item, dictionary):
        # Set variables necessary for creating sets
        count = len(item)
        first_index = 0
        second_index = 2
        set_position = 0
        while(second_index < count+1):
            set = item[first_index:second_index]  # Make a set of 2 letters
            # Set the set value als new key in the nested dictionary and add the set position as value
            dictionary[item].append(set) 
            # Add 1 to the variables
            first_index += 1
            second_index += 1
            set_position += 1

    def __Valid_Sets_Length(self, given_key, compared_key):
        # Create Minimum_Length for string
        Minimum_Length = len(given_key) - self.Length_Difference
        # Create Maximum_Length for string
        Maximum_Length = len(given_key) + self.Length_Difference

        if(Minimum_Length <= len(compared_key) <= Maximum_Length):
            return True
        else:
            return False
    
    def __Valid_Sets_Index(self, given_set, compared_set, given_position, compared_position):
        # Create Minimum Set ofset
        Minimum_Set = int(given_position) - self.Set_Difference
        # Create Maximum Set ofset
        Maximum_Set = int(given_position) + self.Set_Difference

        if(given_set == compared_set and Minimum_Set <= int(compared_position) <= Maximum_Set):
            return True
        else:
            return False

    def __Compare_Sets(self, given_dic, compared_dic):
        results = {}
        given_key = list(given_dic)[0]
        given_sets = given_dic[given_key]
        count_sets = len(given_dic[given_key])
        
        for compared_key in compared_dic.keys():
            count = 0
            if(self.__Valid_Sets_Length(given_key, compared_key)):
                for i in range(len(given_sets)):
                    if str(given_sets[i]) in str(compared_key):
                        compared_set_position = compared_dic[compared_key].index(given_sets[i])
                        try:
                            if(self.__Valid_Sets_Index(given_sets[i], compared_dic[compared_key][i], i, compared_set_position)):
                                count += 1
                        except IndexError:
                            pass #The length of the given key it longer then the compared key. This will prevent IndexError

            average = count / count_sets
            limited_average = "{:.6f}".format(average)  # Limit Everage to .6 decimals
            # Force Limited_Average to float value
            limited_average = float(limited_average)
            # Limit_Average is in the selected scope
            if(limited_average >= self.Minimum_Percentage):
                results[compared_key] = limited_average
        return results
