'''
This function calculates the bacon number of different actors a/c to the data provided by IMDB 2005 and also draws a histogram with the degree of the graph
Pritam Basnet
MovieNetwork.py
17th November 2017
'''
import matplotlib.pyplot as pyplot
def multiSplit (str1,str2):
    '''
    This function implements a multiple split functionality.  String str1 is
    split into multiple pieces.  The individual characters in string str2 are
    used as the split points.  Each character is used individually.
    Parameters:
        str1 - a string that is to be split
        str2 - a string containing characters used to split string1
    Return Value:
        a list of strings from the splitting
    '''
    ret = [str1]                                 #initialises the ret with the first string
    for c in str2:                               #takes one character from str2 at a time for splitting
        temp = []
        for s in ret:                            #takes each character from the ret
            lst = s.split(c)                     #splits the strings from ret using character from str2
            for word in lst:
                if word != '':
                    temp.append(word)            #appends the strings in temp
        ret = temp                               #ret is set as temp at the end of the loop

    return ret
def studyGraph(filename):
    '''
    This function creates a dictionary with the actors in the movies 2005 as key and the actors connected to that actor as the values.
    Parameter:
        filename: The filename movies2005.txt
    Return Value:
        dic: a dictionary with the actors in the movies 2005 as key and the actors connected to that actor as the values.
    '''
    dic = {}                                     #the empty dictionary is created
    alist = []
    f = open(filename, 'r', encoding = 'utf-8')  #the txt file called in the main function is opened and read
    for line in f:
        temp = multiSplit(line,'\t\n')           #each line in the text file is splitted using the Multisplit function
        alist = temp[1:len(temp)+1]              #the list of the actors are created ignoring the movie name
        for a1 in alist:
            for a2 in alist:                     #the loop takes place for both a1 and a2 variables in alist
                #if the two strings aren't equal if the first string is in dictionary but second is not in the values of first dictionary is created
                if a1 != a2:
                    if a1 in dic:
                        if a2 not in dic[a1]:    
                            dic[a1].append(a2)
                    else:
                        dic[a1] = [a2]
            
    f.close()
    return dic
    
    
def degreeCount(filename):
    '''
    This function creates a list of all the number of the actors who are connected to the certain actor(degree of each node in python language)
    Parameter:
        filename: The filename movies2005.txt
    Return Value:
        alist:  of all the number of the actors who are connected to the certain actor(degree of each node in python language)
    '''
    alist = []                                 #empty list is created
    call1 = studyGraph(filename)               #the function studyGraph is called to study the graph
    for j in call1:
        alist.append(len(call1[j]))            #for each key in graph the values of the key is appended in a list named as alist
    return alist                               #the list is returned which contains the values of different keys

def baconNumber(filename, source):
    '''
    This function determines the distance of each node of the graph from the source also including how many nodes have the same distance creating a dictionary
    Parameters:
        filename: the file movies2005.txt
        source: the string Kevin Bacon
    Return Value:
        distance: the dictionary with Kevin Bacon as the key and the distance from different nodes to Bacon as the values is returned
    '''
    #three different empty dictionaries are created
    distance = {}
    visited = {}
    predecessor = {}
    call3 = studyGraph(filename)              #the function studyGraph is called to study the graph
    for node in call3:                        #for each key in the graph
        #three things are set, first the node is not visited, next if not visited the distance is infinity and it's predecessor is None
        visited[node] = False
        distance[node] = float('inf')
        predecessor[node] = None
    #three things as mentioned in the previous comment is done in case of the source itself
    visited[source] = True
    distance[source] = 0
    queue = [source]
    while queue != []:                        #the iteration takes place till the queue isnot empty
        front = queue.pop(0)                  #the first character of the list is taken out and stored as front
        for neighbor in call3[front]:         #the iteration proceedes for the neighbors of the first character taken out from the list
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[front] + 1   #the distance is increased 1 each times moving outward from the source
                predecessor[neighbor] = front
                queue.append(neighbor)        #the queue is appended with the neighbor to start iteration for the next time
    return distance                           #the dictionary with Kevin Bacon as the key and the distance from different nodes to Bacon as the values is returned

def createTable(filename,source):
    '''
    This function creates the dictionary with the distance from Bacon to particular actor as key and the number of actors with same key as values
    Parameters:
        filename: The movies2005.txt file
        source: The string Kevin Bacon
    Return Value:
        table: a dictionary with the dictionary with the distance from Bacon to particular actor as key and the number of actors with same key as values
    '''
    table = {}                                #the new dictionary is created
    call4 = baconNumber(filename,source)      #the function baconNumber is called
    for key in call4:                         #the iteration takes place for each key in the dictionary
        #if that key is in dictionary(table) the count of the word/key is increased 1 each time and dictionary is created
        if call4[key] in table: 
            table[call4[key]] += 1
        else:
            table[call4[key]] = 1
    return table                              #the dictionary with bacon Number as key and the no of nodes with same bacon number as value is returned
                
def main():
    filename = 'movies2005.txt'
    studyGraph(filename)
    call2 = degreeCount(filename)
    source = 'Kevin Bacon'
    baconNumber(filename, source)
    call5 = createTable(filename, source)
    print('Bacon Number\tNumber of Nodes')    #the print format as described in the handout is created
    print('------------\t-----------------')
    keys1 = list(call5.keys())
    keys1.sort()                              #the keys of the dictionary table is sorted
    for k in keys1:                           #iteration takes place for every key in the sorted list
        print(k, '\t\t' ,call5[k])
    #the histogram with the degrees as the plot is plotted with 500 bins
    pyplot.hist(call2, 500)
    pyplot.show()
main()

