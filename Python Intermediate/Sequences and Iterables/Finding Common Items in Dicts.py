'''
Assume we have to find the common items present in two different dictionaries (either keys or values)
'''

#Consider two dictionaries each containing a certain number of keys and values
#We need to find similarities or dissimilarities between the items either it be keys or values

#Suppose a dictionary containing the requirements necessary to get the certain job
#Suppose another dicitonary containing the names of students with their experiences
#We need to get all the students who satisfy the job criteria provided in the job dictionary

jobDict = {
    'FrontEnd Developer':'Afiniti',
    'ML Engineer':'10Pearls',
    'Data Analyst':'Gaditek',
    'ML Engineer':'Folio3',
    'BackEnd Developer':'Panacloud'
}

studentDict = {
    'ML Engineer':'Touseef',
    '.NET Developer':'Usman',
    'Android Developer':'Ehsan',
    'FrontEnd Developer':'Darain',
    'BackEnd Developer':'Daniyal',
    'Data Engineer':'Anas',
    'Data Analyst':'Hassan',
}

#Now to find which people are eligile for the provided list of jobs 
#To perform this we can use the set operations on the dictionary methods keys() or items()
#Since we need to find the common keys in this case i.e. which represent the Jobs that the company wants or the students have experience in
#We will use the keys() method and apply different set operations on it

#To find the eligible candidates for the provided jobs
common_keys = jobDict.keys() & studentDict.keys()
for k in common_keys:
    print('\n' + studentDict[k] + ' is eligible for a job at ' + jobDict[k])
    
#To find candidates that are not elgiible for the provided jobs
noneligible_keys = studentDict.keys() - jobDict.keys()
for k in noneligible_keys:
    print('\n' + studentDict[k] + ' is not eligible for the provided job list')
    

#Now consider another case where there is a dictionary of subjects containing the name of student and their marks in that particular subject
#Suppose the institue is to give prices to the top 5 students in each subject but they cannot give present to the same student
#If he has highest marks in two same subjects i.e. if that student has already obtained a price, he cannot do so in the other one
#Thus, we have to remove the record of such students if there are any from the provided set of dicitonary of top 10 students in the respective subject

mathsDict = {
    'Abdul Wahab': 100,
    'Touseef': 90,
    'Daniyal': 96,
    'Darain': 78,
    'Moiz': 69
}

engDict = {
    'Touseef': 91,
    'Adnan': 89,
    'Abdul Wahab': 80,
    'Hassan': 78,
    'Daniyal': 77
}

#We can use the operation mentioned before to get the common ones and remove them

remove_keys = engDict.keys() &  mathsDict.keys()
print(remove_keys)

# In case we need to find the students which are not common, we can use the following approach
keep_keys = engDict.keys() - mathsDict.keys()
print(keep_keys)

# We can also use these techniques to filter out content from a dictionary
#Suppose from the job offers being listed jobs, somebody else got hired for the FrontEnd Development and Data Analysis technologies
#So now there are no FrontEnd jobs remaining out there, we will use these operations to filter out these jobs and maintain the jobList

newjobDict = {key: jobDict[key] for key in (jobDict.keys() - {'FrontEnd Developer', 'Data Analyst'})}
print('The current available jobs are: {}'.format(newjobDict))

