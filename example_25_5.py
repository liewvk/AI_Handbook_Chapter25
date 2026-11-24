def description_agent():
    return {'description': 'Introductory AI handbook'}
 
def inventory_agent():
    return {'stock': 12}
 
def combine_reports(*reports):
    combined = {}
    for report in reports:
        overlapping = set(combined) & set(report)
        if overlapping:
            raise ValueError('Conflicting report keys')
        combined.update(report)
    return combined
 
report = combine_reports(description_agent(), inventory_agent())
print(report)

