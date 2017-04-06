#Feature 2:
#Identify the 10 resources that consume the most bandwidth on the site

#Open input log file
#input_file = '/home/tao/workspace/xiaojing/insight/tests/log_input/log.txt'
#output_file = '/home/tao/workspace/xiaojing/insight/tests/log_output/resources.txt'
input_file = '/home/tao/workspace/xiaojing/insight/tests/own_log_input/own_log.txt'
output_file = '/home/tao/workspace/xiaojing/insight/tests/own_log_output/resources.txt'

resource = {}

# Read log.txt by line and count/store them into a dictionary
with open(input_file, 'r') as i_file:
    for l in i_file:
        line = i_file.readline()
        spt = line.split('"')
        if spt != ['']:
            idx = spt[1].index('/')
            tmp = spt[1][idx:]
            if tmp not in resource:
                resource[tmp] = 1
            else: resource[tmp] += 1
                        
# Close input log file
i_file.close()

#Open output file
o_file = open(output_file,'w')
flag = 0

#Write the 10 resources that consume the most bandwidth on the site
for w in sorted(resource, key=resource.get, reverse=True):
	if (flag >9): break
	otmp = w + '\n'
	o_file.write(otmp)
	flag += 1
#Close output file
o_file.close() 
