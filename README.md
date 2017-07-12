RavenPack API - Python client
=====

A Python library to consume the [RavenPack API](https://www.ravenpack.com).

[Access the documention here.](https://www.ravenpack.com/support/)

## Installation

	pip install ravenpackapi
	
## Basic usage

The Python client helps managing the API calls to the RavenPack dataset server
 in a Pythonic way, here are some examples of usage, you can find more in the tests.
 
To use the API you need to have a RavenPack API KEY.

Start defining an instance of the RPApi giving your key (or you can set it in your
environment like `export RP_API_KEY=your_api_key`).
	
```python
from ravenpackapi.core import RPApi

api = RPApi(api_key='your_api_key')
```
	
Then, for example to get a file with all the events for the entity 69ADD9 given a data range
you can use:

```python
# specify your query:
# here everything about 69ADD9 in 2015
query = dict(
    start_date='2015-12-01', end_date='2016-01-01',
    return_type='dump',
    entities=['69ADD9']
)

data_filename = 'output.csv'
# do the query and save it to file
analytics = api.get_analytics_file(filename=data_filename,
                                   **query)
```

## Entity mapping

Here is an example of the entity mapping endpoint to get the RavenPack
entity ids given some known company

```python
entities = [{'ticker': 'AAPL'},
            {'ticker': 'JPM'},
            {'listing': 'XNYS:DVN'}]

# get the ravenpack entity id using the mapping API
mapping = api.get_entity_mapping(entities)
rp_entities_id = [e['RP_ENTITIES'][0]['RP_ENTITY_ID'] for e in mapping['IDENTIFIERS_MAPPED']]
print("Entities mapped to this ids: {}".format(rp_entities_id))
```

## Using filters

RavenPack APIs support a wide variety of filters, [See the documention](https://www.ravenpack.com/support/).
Here some examples:

```python
rp_entities_id = ['D8442A'] # query news about Apple Inc.

# I create a common base query querying 2016
query = dict(
    start_date='2016-01-01', end_date='2017-01-01',
    return_type='dump',
)
# get the analytics with news_type = 'RNS-SEC10K' or 'RNS-SEC10Q'
query.update(dict(
    entities=rp_entities_id,
    filters=dict(
        NEWS_TYPE={'$in': ['RNS-SEC10K', 'RNS-SEC10Q']}
    ),
))

# then we can enumerate all the analytics

for row in api.get_analytics(**query):
    print(row)
    
# or save them to a csv file

api.get_analytics_file('test.csv', **query)
```
