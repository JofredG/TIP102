flights = {'LAX':['JFK'], 'JFK':['LAX', 'DFW'], 'DFW':['JFK', 'ATL'], 'ATL':['DFW']}
print(list(flights.keys()))
print(list(flights.values()))
print(flights["JFK"])



#def bidirectional_flights(flights):
#    n = len(flight)
#
#    for i in range(n):
#        for j in flights[i]:
#            for 


'''
Iterate through the embedded lists adding the curr value as a key and the adjacent value as the value
'''
def get_adj_dict(flights):
    d = {}    
    for i in range(len(flights)):
        if not d[flights[i][0]]:
            d[flights[i][0]]
        #d[flights[i][0]] = [].append(flights[i][1])
        #d[flights[i][1]] = [].append(flights[i][0])
    return d


flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))

