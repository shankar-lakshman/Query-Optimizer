'''
Test Cases Generation Code
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 08.02.2015
'''

import random

def generateTestCases(numberOfQueries):
    '''
    Returns the JSON object with queries
    Args:
        numberOfQueries : number of queries which needed to be generated
    Returns:
        outputQuery : JSON object
    '''
    
    outputQuery = []
    ## Output JSON object
    for user in xrange(numberOfQueries):
        tempQuery = {} 
        ## Temporary Query which is later 
    
        fieldsToBeAdded = []
        ## A Boolean array containing what all is there in query
        for i in xrange(10):
            fieldsToBeAdded.append(random.choice([0,1]))
       
        userId = random.randint(1, 10000000)
        queryId = random.randint(1, 10000000)
        ## Assuming userId is maximum number of 7 digits.
        tempQuery["userId"] = userId
        tempQuery["queryId"] = queryId
        
        beginDay = random.randint(1, 27)
        beginMonth = random.randint(1, 12)
        beginYear = random.randint(2015, 2020)
        beginDate = str(str(beginDay) + "-" + str(beginMonth) + "-" + str(beginYear))
        endDate = str(str(random.randint(beginDay+1,28)) + "-" + 
                    str(random.randint(beginMonth,12)) + "-" + 
                    str(random.randint(beginYear,2025)))
        if(fieldsToBeAdded[1]):
            tempQuery["beginDate"] = beginDate
        else:
            tempQuery["beginDate"] = None
        if(fieldsToBeAdded[2]):
            tempQuery["endDate"] = endDate
        else:
            tempQuery["endDate"] = endDate
        
        
        cfpDay = random.randint(1, 27)
        cfpMonth = random.randint(1, 12)
        cfpYear = random.randint(2015, 2020)
        cfpDate = str(str(beginDay) + "-" + str(beginMonth) + "-" + str(beginYear))
        if(fieldsToBeAdded[3]):
            tempQuery["cfpDate"] = cfpDate
        else:
            tempQuery["cfpDate"] = cfpDate
                
        location = []
        states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", 
        "Chhatisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", 
        "Jammu & Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
        "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Orissa",
        "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Tripura", "Uttar Pradesh",
        "Uttaranchal", "West Bengal"]
        cities = []
        country = ["India"]
        numberOfLocations = random.randint(1,25)
        for state in xrange(numberOfLocations):
            location.append({"country" : country[0],
                            "state" : states[random.randint(0,25)],
                            "city": None })
        if(fieldsToBeAdded[4]):
            tempQuery["location"] = location
        else: 
            tempQuery["location"] = None
        
        interest = []
        broadDomain = ["CSE", "ME", "Meta", "Mining", "EE", "ECE"]
        mapSpec = {}
        mapSpec["specificDomainCSE"] = ["Networks", "AI", "ML", "SE", "IS"]
        mapSpec["specificDomainME"] = ["Robotics", "Workshop", "Lathe"]
        mapSpec["specificDomainMeta"] = ["Soil", "Temperature" , "Rock"]
        mapSpec["specificDomainMining"] = ["Soil", "Temperature"]
        mapSpec["specificDomainEE"] = ["Signal", "Image" , "Transistor", "Power"]
        mapSpec["specificDomainECE"] = ["Signal", "Image" , "Transistor"]
        numberOfInterest = random.randint(1,5)
        for domain in xrange(numberOfInterest):
            interestSpec = random.randint(0,5)
            numberOfSpec = random.randint(1,3)
            for specification in xrange(numberOfSpec):
                interest.append({"broadDomain": broadDomain[interestSpec]
                , "specificDomain": 
                mapSpec["specificDomain"+str(broadDomain[interestSpec])]
                [random.randint(0,1)]})
        if(fieldsToBeAdded[5]):
            tempQuery["interest"] = interest
        else:
            tempQuery["interest"] = None

        affiliation = []
        affiliationNumber = random.randint(1,3)
        if i == 3 : 
            affiliation = ["IEEE", "ACM" , "Springer"]
        elif i==2 : 
            affiliation = random.choice([["IEEE","ACM"],
                            ["Springer","ACM"],["IEEE","Springer"]])
        else : 
            affiliation = random.choice(["Springer","IEEE","ACM"])
        if(fieldsToBeAdded[6]):
            tempQuery["publisher"] = affiliation
        else:
            tempQuery["publisher"] = None
        
        lowestRank = random.uniform(1,5);
        if(fieldsToBeAdded[7]):
            tempQuery["lowestRank"] = lowestRank
        else:
            tempQuery["lowestRank"] = 0
        
        if(fieldsToBeAdded[8]):
            tempQuery["highestRank"] = random.uniform(
                        lowestRank + 0.001, 5)
        else:
            tempQuery["highestRank"] = 6
        
        outputQuery.append(tempQuery)
    return outputQuery
        
if __name__ == '__main__':
    print generateTestCases(1)
