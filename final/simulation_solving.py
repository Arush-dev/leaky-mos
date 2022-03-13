f = open('simulation.txt','r')
f1 = f.readlines()
f.close()
fg = f1[0].split()
fb = f1[1].split()
I_gate = 0.0
I_body = 0.0
for ii in fg:
    if ii == "1.20000000e+00":
        continue
    I_gate = I_gate + abs(float(ii))
for ii in fb:
    if ii == "1.20000000e+00":
        continue
    I_body = I_body + abs(float(ii))
print(f"GATE LEAKAGE CURRENT: {I_gate}")
print(f"BODY LEAKAGE CURRENT: {I_body}")
f = open('temp.txt','a')
f.write('-- ')
f.write(str(I_gate)+" ")
f.write(str(I_body)+"\n")
f.close()
