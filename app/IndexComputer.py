import IndeedInfoGetter
import PopulationCPIHolder

import pandas

class IndexComputer:
    @staticmethod
    def ComputeIndex(Skill):

        CompleteObjArray = []

        print(type(PopulationCPIHolder.PopulationCPIHolder.getPopCpi()))

        colOne = []
        colTwo = []
    
        for x in PopulationCPIHolder.PopulationCPIHolder.getPopCpi():
            
            x.numOfJobs = IndeedInfoGetter.IndeedInfoGetter.getNumberOfJobs(Skill, x.City.split(', ')[0], x.City.split(', ')[1])
            x.avgSalary = IndeedInfoGetter.IndeedInfoGetter.getAverageSalary(Skill, x.City.split(', ')[0], x.City.split(', ')[1])

            

            colOne.append(float(x.numOfJobs.replace(',',''))/x.Population)
            colTwo.append(x.avgSalary/x.CPI)
                          
            CompleteObjArray.append(x)

        df = pandas.DataFrame(data={'One':colOne,'Two':colTwo})
##        df.to_csv('someFileIndex', index=False)

        colOneStDev = df.std(0)[0]
        colTwoStDev = df.std(0)[1]

        colOneMean = df.mean(0)[0]
        colTwoMean = df.mean(0)[1]


        print("col one dev: " + str(colOneStDev))
        print("col one mean: " + str(colOneMean))

        print("col two mean: " + str(colTwoMean))
        print("col two dev: "+str(colTwoStDev))

        for x in CompleteObjArray:
            print("index: " + x.getIndex(colOneMean,colOneStDev,colTwoMean,colTwoStDev))

        

        #at this point have complete array of data.     
        return CompleteObjArray
##            if(x.City == str(City+", "+ Province)):
##                pop = x.Population
##                CPI = x.CPI

    

                

        
                 
IndexComputer.ComputeIndex("Software Engineering") 

                
