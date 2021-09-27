import sys
import subprocess
import matplotlib.pyplot as plt

#Parameters for MAT parameters
tau = 5.0
R = 50.0
E_L = -65
v = E_L

#parameters for Adaptive Threshold
t_f = 0; t_ref = 20
x = [0, 0]
tau_1 = 10; tau_2 = 200
file = sys.argv[1]
alpha = [float(sys.argv[2]), float(sys.argv[3])]
omega = float(sys.argv[4])

#Simulation Parameters
num = 0; dt = 0.1

cmd = "wc -l " + file
num = int(subprocess.check_output(cmd.split()).decode().split()[0])
print('num: {}\n'.format(num))
print('T: {} [ms]\n'.format(int(num*dt)))

with open(file, 'r') as f_cur:
    data = list(map(float, f_cur.read().splitlines()))
f_volt = open('voltage.txt', 'w', encoding='UTF-8')
f_sp = open('spiketime.txt', 'w', encoding='UTF-8')

y_list = [] #List of recorded voltage
v_th_list = [] #List of threshold

for i in range(num):
    I_ex = data[i]
    #v = (1 - 1.0/tau*dt) * v + (R/tau) * dt * I_ex
    v = v + (R*I_ex - (v - E_L))/tau * dt

    #Adapting Threshold
    x[0] = (1 - 1.0/tau_1*dt) * x[0] #Fast $B!' (Btau_1= 10 ms
    x[1] = (1 - 1.0/tau_2*dt) * x[1] #Slow: tau_2= 200 ms
    v_th = omega + x[0] + x[1]
    y = v
    #Condition for Spike Generation (v_th: threshold, t_ref: reflactory period)
    if v_th < v and t_f + t_ref < i + 1:
        x[0] += alpha[0]
        x[1] += alpha[1]
        t_f = i + 1
        f_volt.write('{:.6f} 0\n'.format(i*dt)) #Output Voltage
        f_sp.write('{:.6f}\n'.format(t_f*dt)) #Output SpikeTime
        y = 0
    else:
        f_volt.write('{:.6f} {:.6f}\n'.format(i*dt, v))
    y_list.append(y)
    v_th_list.append(v_th)


#Graph
time = [i*dt for i in range(num)]
fig = plt.figure()
plt.plot(time, y_list, label="voltage")
plt.plot(time, v_th_list, label="threshold")
plt.xlabel("time [ms]")
plt.ylabel("voltage [mV]")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()
fig.savefig("spike.eps")
fig.savefig("spike.png")


f_volt.close()
f_sp.close()
