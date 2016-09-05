#/usr/bin/env python

#### import statements
import pickle
import pygal

#### constants
STORAGE = 'f4-traffic-stats.p'
#### functions and classes
def creat_chart(in_packets, out_packets, in_octets, out_octets):
	# Create a Chart of type Line
	line_chart = pygal.Line()

	# Title
	line_chart.title = 'Input/Output Packets and Bytes'

	# X-axis labels (samples were every five minutes)
	line_chart.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']

	# Add each one of the above lists into the graph as a line with corresponding label
	line_chart.add('InPackets', in_packets)
	line_chart.add('OutPackets',  out_packets)
	line_chart.add('InBytes', in_octets)
	line_chart.add('OutBytes', out_octets)

	# Create an output image file from this
	line_chart.render_to_file('test.svg')

def lister(some_data, data_position):
	output=[]
	for item in some_data:
#		print('\nthis is the value of item ')
#		print(item)
		get_one = item[data_position]
#		print(get_one)
		output.append(int(get_one))
	return output
	
def calc_diffs(a_list_raw):
	list_length = len(a_list_raw)
	a_counter=-1
	output=[]
	for item in a_list_raw:
		if item != a_list_raw[0]:
			if (item - a_list_raw[a_counter]) > 0:
				output.append(item - a_list_raw[a_counter])
			else: 
				output.append((item + 4294967295)  - a_list_raw[a_counter])
#		print(output)
		a_counter += 1
	return output
				
# main function (this is the main execution code for your program)
def main():
	 # I would define any variables that are specific to this script here
	a_list_list = pickle.load( open( STORAGE, "rb"))
	in_packets = calc_diffs(lister(a_list_list, 1))
	print ('\nIn Packets are: \n')
	print (in_packets)
	out_packets = calc_diffs(lister(a_list_list, 2))
	print ('\nOut Packets are: \n')
	print (out_packets)
	in_octets = calc_diffs(lister(a_list_list, 3))
	print ('\nIn Octets are: \n')
	print (in_octets)
	out_octets = calc_diffs(lister(a_list_list, 4))
	print ('\nOut Octets are: \n')
	print (out_octets)
	creat_chart(in_packets, out_packets, in_octets, out_octets)


if __name__ == "__main__":                    # program execution starts here
	main()                                                   # first action is to call main function
