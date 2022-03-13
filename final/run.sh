#!/bin/bash
while true; do
  read -p "DO YOU WANT TO SEE REPORT? " yn
  case $yn in
    [Yy]* ) 
      firefox report_text.html
      break;;
    [Nn]* ) break;;
    *) echo "Please answer Y or N.";;
  esac
done
mkdir {nmos_on,nmos_off,pmos_on,pmos_off}
python3 scriptWriter.py 
for i in {nmos_on,nmos_off,pmos_on,pmos_off}
do
  for j in {W1,W2,W3,W4,W6,W8}
  do
    ngspice $i/$j.sp
  done
done
python3 resultToHtml.py
mkdir {abn_and,abn,zyn,ayp,zbp}
python3 interNode.py
for i in {abn_and,abn,zyn,zbp,ayp}
do 
  for j in {W1,W2,W3,W4,W6,W8}
  do 
    for k in {_0,_1,_2,_3}
    do 
      ngspice $i/$j$k.sp
    done
  done
done
while true; do
  read -p "DO YOU WANT TO SEE SINGLE MOS LEAKAGE CURRENT VALUES? " yn
  case $yn in
    [Yy]* ) 
      firefox results.html
      break;;
    [Nn]* ) break;;
    *) echo "Please answer Y or N.";;
  esac
done
python3 and.py
python3 xor.py
python3 mult.py
python3 simulation_scripting.py
ngspice simulation.sp
python3 simulation_solving.py
python3 report.py
rm simulation.txt
cat out.txt
while true; do
  read -p "DO YOU WANT TO SEE RESULTS? " yn
  case $yn in
    [Yy]* ) 
      firefox report.html
      break;;
    [Nn]* ) break;;
    *) echo "Please answer Y or N.";;
  esac
done
