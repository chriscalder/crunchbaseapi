import urllib2
import urllib
import simplejson as json

API_BASE_URL = "http://api.crunchbase.com/"
API_VERSION  = "1"
API_URL      = API_BASE_URL + "v" + "/" + API_VERSION + "/"

class crunchbase:

	def __init__(self, key):
		self.apikey = key

	def __format(self, query):
		return query.lower().replace(' ','-')

	def __request(self, url):
		response = urllib2.urlopen(url + "?api_key=" + self.apikey)
		result = response.read()
		print result
		return result
		
	def __getJson(self, namespace, query=""):
		url = API_URL + namespace + query + ".js"
		response = json.loads(self.__request(url))
		return response

	def getCompany(self, name):
		return self.__getJson("company", "/%s" % self.__format(name))

	def getPerson(self, name):
		return self.__getJson("person", "/%s" % self.__format(name))

	def getFinancialOrg(self, name):
		return self.__getJson("financial-organization", "/%s" % self.__format(name))

	def getProduct(self, name):
		return self.__getJson("product", "/%s" % self.__format(name))

	def getProvider(self, name):
		return self.__getJson("service-provider", "/%s" % self.__format(name))

	def listCompanies(self, categories=None):
		if categories:
			print categories
			return [x for x in self.__getJson("companies") if x["category_code"] in categories]
		else:
			return self.__getJson("companies")

	def listPeople(self):
		return self.__getJson("people")

	def listFinancialOrgs(self):
		return self.__getJson("financial-organizations")

	def listProducts(self):
		return self.__getJson("products")

	def listProviders(self):
		return self.__getJson("service-providers")
