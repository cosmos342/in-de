from elasticsearch import Elasticsearch
import sys

cluster = ['ip-10-0-0-5', 'ip-10-0-0-6', 'ip-10-0-0-8', 'ip-10-0-0-10']

'''
 include_in_all means there is _all index search do you want the field to be included in that
 or no. for text search it is useful otherwise you can have it removed to make things more efficient
''' 


def create_indices():
	print("creating driver and sender indices")

	driver_mapping = {
	  'settings' : {
		'number_of_shards' : 2,
		'number_of_replicas' : 2
	  },
	  'mappings': {
	    'alldriver': {
	      'properties': {
		'id': {'type': 'integer'},
		'space': {'type': 'integer'},
		'price': {'type': 'integer'},
		'review': {'type': 'integer'},
		'sloc': {'type': 'geo_point'},
		'dloc': {'type': 'geo_point'},
	      }
	    }
	  }
	}


	sender_mapping = {
	  'settings' : {
		'number_of_shards' : 2,
		'number_of_replicas' : 2
	  },
	  'mappings': {
	    'allsender': {
	      'properties': {
		'id': {'type': 'integer'},
		'space': {'type': 'integer'},
		'sloc': {'type': 'geo_point'},
		'dloc': {'type': 'geo_point'},
	      }
	    }
	  }
	}

	es = Elasticsearch(cluster, http_auth=('elastic','changeme'))
	es.indices.create(index="driver",body=driver_mapping);
	es.indices.create(index="sender",body=sender_mapping);
	print("created driver and sender indices")

def delete_indices():
	print("deleting driver and sender indices")
	es = Elasticsearch(cluster, http_auth=('elastic','changeme'))
	es.indices.delete(index='driver')
	es.indices.delete(index='sender')
	print("deleted driver and sender indices")


def main():
    # print command line arguments
    if(len(sys.argv) == 2):
	if (sys.argv[1] == "add"):
		create_indices()
	elif(sys.argv[1] == "rem"):
		delete_indices()
	else:
		print("WRONG OPTIONS. PROVIDE add or rem option")
    else:
	print("PROVIDE add or rem as options")
	

if __name__ == "__main__":
    main()