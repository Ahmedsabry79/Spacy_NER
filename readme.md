# Named Entity Recognition Model 

## Description
This app takes an input text or sence and extracts the entites from it. 
It can also retrun all the entities that the model support.


## How it works
The app has two end points, one is to get the entities present in an input text 'get_entities', and the other is to list the available entites supported by the model.


## Running the Docker container
### build the docker image using the following command:
docker build -t spacy_ner .

### Run the docker image using the command below:
docker run -p 5000:5000 spacy_ner


## End Points

### Listing Avaulable Entities
Listing all the available Entities supported by the model.

`
response = requests.post("http://127.0.0.1:5000/get_available_entities")
`

the response is expected to be as follows:

`
{"success":"true",
 "result": ['Geographical Entity',
 	    'Organization',
  	    'Person',
 	    'Geopolitical Entity',
 	    'Time indicator',
  	    'Artifact',
 	    'Event',
 	    'Natural Phenomenon']
}
`

### Extracting Entities from a given sentence
This end point takes a text string as input and returns the entities if present in it.

you can extract the intent via this post request:


`
intent_response = requests.post("http://127.0.0.1:5000/get_entities", json = {"text": "Ahmed Sabry Lives in Cairo.",
                                                                              })
`

the response is expected to be as follows:
`
{"success": "true",
 "result" : {'Ahmed Sabry': 'PERSON', 
 	     'Cairo': 'GPE'}}
`

