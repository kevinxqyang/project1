#Feature 3:
#List the top 10 busiest (or most frequently visited) 60-minute periods

#Open input log file
#input_file = '/home/tao/workspace/xiaojing/insight/tests/log_input/log.txt'
#output_file = '/home/tao/workspace/xiaojing/insight/tests/log_output/hours.txt'
input_file = '/home/tao/workspace/xiaojing/insight/tests/own_log_input/own_log.txt'
output_file = '/home/tao/workspace/xiaojing/insight/tests/own_log_output/hours.txt'

hour = {}

# Read log.txt by line and count/store them into a dictionary
with open(input_file, 'r') as i_file:
    #first_l = i_file.readline()
    first_l = i_file.readline()
    left, right = first_l.index('['), first_l.index(']')
    dt= first_l[left+1:right]
    hour[dt] = 1
    tmp = dt
    ihour = int(str(tmp[12:14]))
    for l in i_file:
        line = i_file.readline()
        left, right = line.index('['), line.index(']')
        tmp = line[left+1:right]
        if int(str(tmp[12:14])) == ihour: hour[dt] += 1
        else:
            ihour = int(str(tmp[12:14]))
            dt = tmp
            hour[dt] = 1
# Close input log file
i_file.close()

#Open output file
o_file = open(output_file,'w')
flag = 0

#Write 10 busiest (or most frequently visited) 60-minute periods
for w in sorted(hour, key=hour.get, reverse=True):
	if (flag >9): break
	otmp = w + ',' + str(hour[w]) + '\n'
	o_file.write(otmp)
	flag += 1
#Close output file
o_file.close() 
