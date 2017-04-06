#Feature 4:

#Detect patterns of three failed login attempts from the same IP address over 20 seconds 
#so that all further attempts to the site can be blocked for 5 minutes. Log those possible 
#security breaches.

#Parse ip from the line
def get_ip(line):
    spt = line.split('[')
    ip = spt[0][:-5]
    return ip

#Parse date&time from the line
def get_dt(line):
    left, right = line.index('['), line.index(']')
    dt= line[left+1:right]
    return dt

#Get the date&time for 20 seconds window
def get_dt20(dt):
     r_dt = dt
     tmp = int(str(dt[-2:])) + 20
     if tmp < 60:
        r_dt = dt[:-2] + str(tmp)
        return r_dt
     else:
        tmp_s = tmp%60
        tmp_m = int(str(dt[-5:-3])) + 1
        if tmp_m < 60:
           r_dt = dt[:-5] + add_0(tmp_m) + str(tmp_m) + ':' + add_0(tmp_s) + str(tmp_s)
           return r_dt
        else:
           tmp_s = tmp - 60
           tmp_m = '00'
           tmp_h = int(str(dt[-8:-6])) + 1
           r_dt = dt[:-8] + add_0(tmp_h) + str(tmp_h) + ':' + str(tmp_m) + ':' + add_0(tmp_s) + str(tmp_s)
           return r_dt

# Add '0' in the front if hour, minute, and second is not a two-digit number
def add_0(s):
     a_0 = '0' if s < 9 else ''
     return a_0

#Open input log file
#input_file = '/home/tao/workspace/xiaojing/insight/tests/log_input/log.txt'
#output_file = '/home/tao/workspace/xiaojing/insight/tests/log_output/blocked.txt'
input_file = '/home/tao/workspace/xiaojing/insight/tests/own_log_input/own_log.txt'
output_file = '/home/tao/workspace/xiaojing/insight/tests/own_log_output/blocked.txt'

blocked = []
code = 304

# Read log.txt by line, pick up the lines with '304' and store them into arrays
with open(input_file, 'r') as i_file:
    line = i_file.readline()
    for l in i_file:
        line = i_file.readline()
        spt = line.split('"')
        tmp = spt[2][1:4]
        if tmp == 'HTT':
            #print(tmp, line)
            tmp = spt[3][1:4]
        icode = int(str(tmp))
        if icode == code:
            # stroe the line into array blocked
            blocked.append(line)
            
# Close input log file
i_file.close()

# Find the three failed login attempts from the same IP address
# Get all fails in 20 seconds window
s20 = []

ip = get_ip(blocked[0])
dt = get_dt(blocked[0])
line = blocked[0]
for i in range(1, len(blocked)):
    dt20 = get_dt20(dt)
    
    # check IP
    for j in range(i, len(blocked)):
        s_dt = get_dt(blocked[j])
        if s_dt > dt20: break
        else:
            if ip == get_ip(blocked[i]) and ip == get_ip(blocked[j]):
               s20.append(line)
               s20.append(blocked[i])
               s20.append(blocked[j])
    ip = get_ip(blocked[i])
    dt = get_dt(blocked[i])
    line = blocked[i]


#Open output file
o_file = open(output_file,'w')

#Write blocked.txt
for w in s20:
    o_file.write(w)

#Close output file
o_file.close() 

oo = '/home/tao/workspace/xiaojing/insight/tests/own_log_output/b304.txt'
#Open output file
o_file = open(oo,'w')

#Write blocked.txt
for w in blocked:
    o_file.write(w)

#Close output file
o_file.close() 

