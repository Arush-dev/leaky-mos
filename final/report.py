f = open('report.html','w')
x = '''<style>
main {
  display: flex;
    justify-content: center;
    
}
table {
  max-width: 100%; width: 75%;
  
}
tr:nth-child(odd) {
  background-color: #fff;
  
}
tr:nth-child(even) {
  background-color: #c6e4ee;
  
}
th {
  background-color: #03a9f4;
    color: #555;
    
}
th,
td {
  text-align: center;
    padding: 0.5em 1em;
        </style><center><h3>result comparison for '''
g = open('temp.txt','r')
g1 = g.readlines()
g.close()
m = g1[2].split()
s = g1[3].split()
x = x+g1[0].split()[0]+g1[0].split()[1]+ "*" + g1[1].split()[0]+g1[1].split()[1] + "\n" + '''</h3><br><br><br><table border="1" style="border-collapse:collapse">
<tr>
    <th> </th>
    <th> Modelling</th>
    <th> Simulation </th>
    <th> difference </th> 
</tr>
<tr>
    <td>Gate Leakage</td>
    <td>''' + m[1] +'''</td>
    <td>''' + s[1] +'''</td>
    <td>''' + str(abs(float(m[1]) - float(s[1]))) + '''</td>
</tr>
<tr>
    <td>Drain Leakage</td>
    <td>''' + m[0] + '''</td>
    <td>''' + s[0] + '''</td>
    <td>''' + s[0] + '''</td>
</tr>
<tr>
    <td>Body Leakage</td>
    <td>''' + m[2] + '''</td>
    <td>''' + s[2] + '''</td>
    <td>''' + str(abs(float(m[2]) - float(s[2]))) + '''</td>
</tr>
</table><br><br>'''
f.write(x)
