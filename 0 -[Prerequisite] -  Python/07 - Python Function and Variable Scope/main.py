capitals = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'Rome'}
print(capitals)
#keys: Nepal, italy, England
#values: Kathmandu, Rome, Rome
capitals['Japan'] = 'Tokyo'
print(capitals)
capitals['Italy'] = 'Florence'
print(capitals)

print(capitals['England'])

key = 'Italy'
print(capitals[key])

del capitals[key]

print(capitals)

print(type(capitals))