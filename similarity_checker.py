class Similarity_Checker:
    #Similarity Checker V.0.3 | Made by Jekkow
    def __init__(self):
        #Set Variables
        self.Set_Difference = 1 #Public Variable
        self.Length_Difference = 2 #Public Variable
        self.Minimum_Percentage = 0.75 #Public Variable
        self.__Results = [] #Private Variable
        self.__Set_Dictionary = {} #Private Variable
        self.__String_Sets = {} #Private Variable
    
    def Check(self, string, list):
        self.__Check(string, list) #Call Private method
        self.__Results = self.__Compare_Sets(self.__String_Sets, self.__Set_Dictionary) #Create results
        return self.__Results #Return results

    def __Check(self, string, list): #Private method Check
        self.__Set_Dictionary = self.__Create_Keys(list)
        self.__String_Sets = self.__Create_String_Set(string)
        self.__Results = self.__Compare_Sets(self.__String_Sets, self.__Set_Dictionary)

    def __Create_Keys(self, list): #Private method Create Keys
        dictionary = {} #Create new dictionry
        for item in list:
            uppercased = "" #Reset value
            for letter in item:
                if(letter == " "): #If the letter is a blank, remove the blank space
                    pass
                else:
                    uppercased += letter.upper() #Make the letter uppercased
            dictionary[uppercased] = {} #Set dictionary key with empty nested dictionary
            self.__Create_Set(uppercased, dictionary) #When uppercased name in completed, create the sets of this name
        return dictionary

    def __Create_String_Set(self, string): #Private method Create String Set
        uppercased = "" #Make the string uppercased
        dictionary = {} #Create new dictionary
        for letter in string:
            if(letter == " "): #If the letter is a blank, remove the blank space
                pass
            else:
                uppercased += letter.upper()
        dictionary[uppercased] = {} #Set value
        self.__Create_Set(uppercased, dictionary) #Create the sets of the uppercased string
        return dictionary

    def __Create_Set(self, name, dictionary): #Private method Create Sets
        #Set variables necessary for creating sets
        count = len(name)
        first_index = 0
        second_index = 2
        set_position = 0
        while(second_index < count+1):
            set = name[first_index:second_index] #Make a set of 2 letters
            dictionary[name][set] = set_position #Set the set value als new key in the nested dictionary and add the set position as value
            #Add 1 to the variables
            first_index += 1
            second_index += 1
            set_position += 1

    def __Compare_Sets(self, given_dic, compared_dic):
        result_list = []
        for given_key in given_dic.keys():
            count_sets = len(given_dic[given_key].items()) #Setcount for calculating average
            for compared_key in compared_dic.keys():
                count = 0
                Minimum_Length = len(given_key) - self.Length_Difference #Create Minimum_Length for string
                Maximum_Length = len(given_key) + self.Length_Difference #Create Maximum_Length for string
                for given_set, given_position in given_dic[given_key].items():
                    if(Minimum_Length <= len(compared_key) <= Maximum_Length): #Check with the Maximum and Minimum Length Difference
                        if(str(given_set) in str(compared_key)):
                            for compared_set, compared_position in compared_dic[compared_key].items():
                                Minimum_Set = int(given_position) - self.Set_Difference #Create Minimum Set ofset
                                Maximum_Set = int(given_position) + self.Set_Difference #Create Maximum Set ofset
                                if(given_set == compared_set and Minimum_Set <= int(compared_position) <= Maximum_Set):
                                    count += 1 #Count set in in word, needed for calculating average
                average = count / count_sets #Calculate Average
                limited_average = "{:.6f}".format(average) #Limit Everage to .6 decimals
                limited_average = float(limited_average) #Force Limited_Average to float value
                if(limited_average >= self.Minimum_Percentage): #Limit_Average is in the selected scope
                    result_list.append(compared_key)
                    result_list.append(limited_average)
        return result_list