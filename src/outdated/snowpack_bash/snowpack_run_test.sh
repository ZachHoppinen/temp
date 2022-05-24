#!/bin/bash
# Sensitivity Analysis for Aspect and Slope

# cd ../../modeling/config/
# /bin/meteoio_timeseries -c meteoio_bash -b 2020-11-01T00:00:00 -e 2021-04-30T00:00:00
# snowpack -c snowpack_v20220222_bash.ini -e 2021-04-29T00:00 -b 2020-11-01T00:00

# echo "Bash version ${BASH_VERSION}..."

for i in {8..18} #8-15
do
for j in {320..340..2} #320-340
do
    echo "${i},${j}"
    sed -i -e "s/EXP_.*/EXP_${i}_${j}/g" ../../modeling/config/snowpack_bash.ini
    sed -i -e "s/SlopeAngle.*/SlopeAngle       = ${i}/g" ../../modeling/input/snowschool.sno
    sed -i -e "s/SlopeAzi.*/SlopeAzi       = ${j}/g" ../../modeling/input/snowschool.sno
    snowpack -c ../../modeling/config/snowpack_bash.ini -e 2021-04-29T00:00 -b 2020-11-01T00:00
done
done

# sed -i -e "s/SlopeAngle       = ${i}/SlopeAngle       = 7/g" ../../modeling/input/snowschool.sno
# sed -i -e "s/SlopeAzi       = ${i}/SlopeAzi       = 319/g" ../../modeling/input/snowschool.sno
# sed -i -e "s/EXP_${i}_${j}/EXP_7_319/g" ../../modeling/config/snowpack_bash.ini

# SlopeAngle       = 8-15.0
# SlopeAzi         = 320.0-324

# SlopeAngle       = 8