def validate_handoff(item):
    if not isinstance(item, dict):
        raise TypeError('Handoff must be a dictionary')
    if set(item) != {'source', 'facts'}:
        raise ValueError('Expected source and facts')
    if not isinstance(item['source'], str) or not item['source']:
        raise ValueError('Source is required')
    if not isinstance(item['facts'], list):
        raise ValueError('Facts must be a list')
    if len(item['facts']) > 10:
        raise ValueError('Too many facts')
    if not all(isinstance(x, str) and len(x) <= 200
               for x in item['facts']):
        raise ValueError('Invalid fact')
    return item
 
handoff = {'source': 'Approved teaching notes',
           'facts': ['RAG retrieves supporting passages']}
print(validate_handoff(handoff)['facts'][0])

