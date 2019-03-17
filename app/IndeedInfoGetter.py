import requests
import bs4 as BeautifulSoup

##what = "Software+Developer"
##City = "Regina"
##Province ="Saskatchewan"


          
class IndeedInfoGetter:
    @staticmethod
    def getNumberOfJobs(what, City, Province):
          
        url = "https://ca.indeed.com/jobs?q=\""+what+"\"&l="+City+"%2C+"+Province

        session = requests.Session()

        page = session.get(url)

        bs = BeautifulSoup.BeautifulSoup(page.text, "html.parser")

        data = bs.find("div", {"id":"searchCount"})
        try:
            numberOfJobs = data.decode_contents().strip()[10:-5]
        except:
            numberOfJobs = "0"
            print(City)
            pass

        return(numberOfJobs)

    def getAverageSalary(what, City,Province):

        url = "https://ca.indeed.com/jobs?q="+what+"&l="+City+"%2C+"+Province

        session = requests.Session()

        page = session.get(url)

        bs = BeautifulSoup.BeautifulSoup(page.text, "html.parser")

        uls = bs.find("div", {"id":"SALARY_rbo"}).findChildren("ul", recursive = False)[0].findChildren("li", recursive = False)

        average = 0
        counter = 0

        for x in uls:
        
            
            title = x.findChildren("a", recursive = False)[0]["title"]
            numOfJobs = title.split("(")[1][:-1].replace(',','')
            valOfJobs = title.split(" (")[0][1:].replace(',','')
            counter += int(numOfJobs)
            average += int(numOfJobs)*int(valOfJobs)

        average = average/counter

        return average




