#!/bin/bash
# for i in {8..10} #8-15
# do
# for j in {320..321} #320-340
# do
#     echo "s/EXP_.*/EXP_${i}_${j}/g"
#     sed -i -e "s/EXP_.*/EXP_${i}_${j}/g" ../../modeling/config/test.ini
# done
# done


for i in {8..18} #8-15
do
for j in {320..340} #320-340
do
    echo "${i},${j}"
    # sed -i -e "s/EXP_.*/EXP_${i}_${j}/g" ../../modeling/config/snowpack_bash.ini
    sed -i -e "s/SlopeAngle.*/SlopeAngle       = ${i}/g" ../../modeling/config/test.ini
    sed -i -e "s/SlopeAzi.*/SlopeAzi       = ${j}/g" ../../modeling/config/test.ini
    #snowpack -c ../../modeling/config/snowpack_bash.ini -e 2021-04-29T00:00 -b 2020-11-01T00:00
done
done