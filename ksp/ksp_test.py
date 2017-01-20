#import the KSP source
import KSP

# parameters to be passed to the KSP algorithm
graph_file = 'OW.net'    # the graph of the traffic network (the file format is specified by the algorithm's help)
#ODpairs = ['A|L', 'B|M'] # the list of origins and destinations
K = 4                    # the number of paths to find
flow = 4.0               # the flow of vehicles to be used when computing the links' costs (the default is zero)

# generate the list of vertices and edges from the network file
V, E, OD = KSP.generateGraph(graph_file, flow)

print OD
# for each OD pair
for od in OD: # to look at all pairs, use the variable OD (above)

	#~ print 'Pair %s' % od
	origin, destination = od.split('|')
	
	# run the algorithm (return the K routes and associated costs of the given origin-destination pair)
	routes = KSP.getKRoutes(V, E, origin, destination, K)
	
	# print the routes
	for i in routes:
		
		# the route as a list of strings, where each element corresponds to a link's name
		route = i[0]
		
		# the cost of the route (a float value)
		cost = i[1]
		
		print '%s has cost %.2f\n' % (route, cost)

