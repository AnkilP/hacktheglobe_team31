from IndexComputer import IndexComputer
from quickstart import survey_data

class interface(object):

	def __init__(self):
		self.locations = []
		self.services = []
        self.survey_responses = survey_data()

	def get_job_information(self, skills): 
		#something with skills		
		#return array of locations
		self.locations = IndexComputer.ComputeIndex(skills)

	def get_mentorship_information(self, skills):
		#return array of locations
		location = []
		self.locations.append(location)

	def get_service_information(self, city):
		#what kind of services are available in the city		
		service = []
		self.services.append(service)

	def get_housing_information(self, region):
		#return locations of optimal housing districts
		region = []
		return region


