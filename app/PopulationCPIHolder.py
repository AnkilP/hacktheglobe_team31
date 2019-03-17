import pandas



class PopulationCPIHolder:


    def __init__(self, city1, cpi1, population1):
        self.City = city1
        self.CPI = cpi1
        self.Population = population1
        self.numOfJobs = 0
        self.avgSalary = 0

    def getIndex(self,mean1,std1,mean2,std2):
        print("\n Job Num Index: "+ '{:.20f}'.format(float(self.numOfJobs.replace(',',''))/float(self.Population)) + " Salary Index: " + str(float(self.avgSalary)/float(self.CPI)))
        print("num of jobs: "+str(float(self.numOfJobs.replace(',',''))) + " num of people: " + str(float(self.Population)))

        return ('{:.20f}'.format(((float(self.numOfJobs.replace(',',''))-mean1)/std1)/float(self.Population) +((float(self.avgSalary)/float(self.CPI))-mean2)/std2))
    
    
    @staticmethod
    def getPopCpi():
        
        csv = pandas.read_csv("popCPI.csv", encoding = "ISO-8859-1", names = ["City","Population","CPI"])
        objArr = []
##        objArr = [PopulationCPIHolder(csv.iloc[[count]]["City"],csv.iloc[[count]]["Population"], csv.iloc[[count]]["CPI"] )for count in xrange(34)]

        for index,row in csv.iterrows():

            City = str(row[0])
            Population = int(row[2])
            CPI = float(row[1])

            objArr.append(PopulationCPIHolder(City, Population, CPI))

        return objArr

##
##print(PopulationCPIHolder.getPopCpi())
        

        

