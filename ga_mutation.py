
# coding: utf-8

# In[13]:


import random
import numpy as np
from random import randint
import re

mutation_type = ['M', 'N', 'I', 'D', 'U','R']


def main():

    count = 0

    filepath = "dna_sequences.dat"  

    with open(filepath,'r') as fp:  
    
        file_content = fp.readlines()

    fp1 = open('mutation_results.dat', 'w+')

    for eachline in file_content:

        #count= count+1
        
        #print(count)

        types=random.choice(mutation_type)  #  randomly generating mutation type
    

        #mutation

        if types=='U' or types=='R':
            
            integer=randint(0, 20)

            mutate_result=mutate(str(eachline).rstrip(),types,integer)
        
        else:

            mutate_result=mutate(str(eachline).rstrip(),types)

        fp1.write(str(mutate_result))

    fp1.close()   
    
    fp.close() 



def mutation_code(mutationlist):

    code =random.choice(mutationlist)
    return code


def mutate(dna_sequence,location_type,option=None):

    u_sequence =''
    r_sequence = ''
    rfin=''
    random_number= randint(0,len(dna_sequence)-1)

    m_sequence = mutation_code(['A','G','T','C'])

    if(location_type == 'M' and dna_sequence[random_number]=='A'):
        dna_sequence = dna_sequence[:random_number-1] + m_sequence + dna_sequence[random_number:]

    if(location_type == 'I'):
        i_sequence = mutation_code(['A','G','T','C'])
        dna_sequence = dna_sequence[:random_number-1] + i_sequence + dna_sequence[random_number:]

    if(location_type ==  'D'):
        dna_sequence = dna_sequence[:random_number-1] + dna_sequence[random_number:]

    if(location_type ==  'U'):
        for k in range (0,option):
            i_sequence = mutation_code(['A','G','T','C'])
            u_sequence = u_sequence + i_sequence
        dna_sequence = dna_sequence[:random_number-1]+u_sequence+ dna_sequence[random_number:]

    if(location_type == 'N'):
        
        space = 0
        randomlist = []
        regex = re.compile('AG')
    
        for i in regex.finditer(dna_sequence):
            randomlist.append(i.start())

        if(len(randomlist) > 0):
         
            space = randomlist[randint(0,len(randomlist)-1)] - 1
        
        dna_sequence = dna_sequence[:space] + 'T' + dna_sequence[space+1:]

        random_number = space 


    if(location_type == 'R'):

        random_number= randint(0,len(dna_sequence)-1)

        formatted_string = ''

        if(option+1 > len(dna_sequence)+1):
            formatted_string = dna_sequence[random_number-1:]
        else:
            formatted_string = dna_sequence[random_number:random_number+option]

       
        rfin = dna_sequence[:random_number+option].rstrip()

        for i in range(0,option):
            rfin = rfin.rstrip() + formatted_string.rstrip()
    
        dna_sequence = rfin.rstrip() + dna_sequence[random_number+option:].rstrip()


    return (dna_sequence,random_number,location_type)

if __name__== "__main__":
  main()
