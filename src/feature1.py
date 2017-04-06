#Feature 1:
#List the top 10 most active host/IP addresses that have accessed the site.

#Open input log file
#input_file = '/home/tao/workspace/xiaojing/insight/tests/log_input/log.txt'
#output_file = '/home/tao/workspace/xiaojing/insight/tests/log_output/hosts.txt'
input_file = '/home/tao/workspace/xiaojing/insight/tests/own_log_input/own_log.txt'
output_file = '/home/tao/workspace/xiaojing/insight/tests/own_log_output/hosts.txt'

host = {}

# Read log.txt by line and count/store them into a dictionary
with open(input_file, 'r') as i_file:
    for l in i_file:
        line = i_file.readline()
        spt = line.split('[')
        tmp = spt[0][:-5]
        if tmp not in host:
            host[tmp] = 1
        else: host[tmp] += 1
# Close input log file
i_file.close()

#Open output file
o_file = open(output_file,'w')
flag = 0

#Write the 10 most active hosts/IP addresses in descending order
for w in sorted(host, key=host.get, reverse=True):
	if (flag >9): break
	otmp = w + ',' + str(host[w]) + '\n'
	o_file.write(otmp)
	flag += 1
#Close output file
o_file.close() 
