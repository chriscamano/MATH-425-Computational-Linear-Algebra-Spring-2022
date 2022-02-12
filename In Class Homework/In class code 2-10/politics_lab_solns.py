# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.

# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.


#import vec 
from vecutil import list2vec, vec2list
from statistics import mean

## 1: (Task 2.12.1) Create Voting Dict
def create_voting_dict(strlist):
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of 
              - the senator's last name, 
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example: 
        >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
        True

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    return {sen.split()[0]:[int(k) for k in sen.split()[3:]] for sen in strlist}




## 2: (Task 2.12.2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    return list2vec(voting_dict[sen_a])*list2vec(voting_dict[sen_b])



## 3: (Task 2.12.3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'
        >>> vd == {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        True
        >>> vd = {'a': [1,1,1,0], 'b': [1,-1,0,0], 'c': [-1,0,0,0], 'd': [-1,0,0,1], 'e': [1, 0, 0,0]}
        >>> most_similar('c', vd)
        'd'

    Note that you can (and are encouraged to) re-use your policy_compare procedure.
    """
    
    # This is not the most obvious way. Just being a tad silly.
    comp_dict = {policy_compare(sen,sen2,voting_dict):sen2 
                 for sen2 in voting_dict.keys() if sen != sen2 }
    
    return comp_dict[max(comp_dict)]



## 4: (Task 2.12.4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
        >>> vd == {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        True
        >>> vd = {'a': [-1,0,0], 'b': [1,0,0], 'c': [-1,1,0], 'd': [-1,1,1]}
        >>> least_similar('c', vd)
        'b'
    """
    # This is not the most obvious way. Just being a tad silly.
    comp_dict = {policy_compare(sen,sen2,voting_dict):sen2 
                 for sen2 in voting_dict.keys() if sen != sen2 }
    
    return comp_dict[min(comp_dict)]



## 5: (Task 2.12.5) Chafee, Santorum
most_like_chafee    = ''
least_like_santorum = '' 



## 6: (Task 2.12.7) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        >>> sens = {'Fox-Epstein','Ravella','Oyakawa','Loery'}
        >>> find_average_similarity('Klein', sens, vd)
        -0.5
        >>> sens == {'Fox-Epstein','Ravella', 'Oyakawa', 'Loery'}
        True
        >>> vd == {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
        True
    """
    return mean([policy_compare(sen,sen2,voting_dict) for sen2 in sen_set])

most_average_Democrat = ... # give the last name (or code that computes the last name)



## 7: (Task 2.12.8) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> senators = {'Fox-Epstein','Ravella'}
        >>> find_average_record(senators, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> voting_dict == {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        True
        >>> senators
        {'Fox-Epstein','Ravella'}
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0]
    """
    
   # return list(((sum([list2vec(voting_dict[sen]) for sen in sen_set])/
   #         float(len(sen_set))).f).values())
    
    return vec2list(sum([list2vec(voting_dict[sen]) for sen in sen_set])/
            float(len(sen_set)))

average_Democrat_record = ... # give the vector as a list



## 8: (Task 2.12.9) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein':[-1,0,1], 'Fox-Epstein':[-1,-1,-1], 'Ravella':[0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Oyakawa') or br == ('Oyakawa', 'Fox-Epstein')
        True
    """
    return (..., ...)


"""
twosens = input('Enter the two senators you want to compare separted by \
                a space: ')
twosens = twosens.split()
compsens = policy_compare(twosens[0],twosens[1],votdict) 
print(f"The similarity between senators {twosens[0]} and {twosens[1]} is \
      {compsens}")

onesen = input('Enter the senator you want to study: ')
most_like = most_similar(onesen,votdict)
print(f"Senator {onesen} is most like senator {most_like} \
      with similarity measure {policy_compare(onesen,most_like,votdict)}")


least_like = least_similar(onesen,votdict)
print(f"Senator {onesen} is least like senator {least_like} \
      with similarity measure {policy_compare(onesen,least_like,votdict)}")

# Set of Democrats
Dem_Set = {sen.split()[0] for sen in senvoterec if sen.split()[1] == 'D'}
Rep_Set = {sen.split()[0] for sen in senvoterec if sen.split()[1] == 'R'}
av_sim = find_average_similarity('Collins',Dem_Set,votdict)

avR = find_average_record(Rep_Set,votdict)
avD = find_average_record(Dem_Set,votdict)
print(f"The average similarity between parties is \
      {list2vec(avR)*list2vec(avD)}")
     
 
   """
f = open('US_Senate_voting_data_109.txt')
senvoterec = list(f)

votdict = create_voting_dict(senvoterec)
   # Set of Democrats
Dem_Set = {sen.split()[0] for sen in senvoterec if sen.split()[1] == 'D'}
Rep_Set = {sen.split()[0] for sen in senvoterec if sen.split()[1] == 'R'}
OD=dict.fromkeys(Dem_Set, 0)
OR=dict.fromkeys(Rep_Set, 0)
for i in Dem_Set:
    for j in Dem_Set:
        if policy_compare(i, j, votdict) <21:
            OD[i].get(OD[i].key, 0) + 1
            
for i in Dem_Set:
    for j in Dem_Set:
        if policy_compare(i, j, votdict) <21:
            OR[i]+=1         
maxD=0
maxR=0
for i in OD:
    if OD[i]>maxD:
        maxD=OD[i]
for i in OD:
    if OD[i]>maxR:
        maxR=OD[i]


        


      
      
