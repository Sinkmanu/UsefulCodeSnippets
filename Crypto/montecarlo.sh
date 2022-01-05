#!/bin/bash

seed=$1
md=()
msg=()
for i in {0..99}
do
	md[0]=$seed
	md[1]=$seed
	md[2]=$seed
	for j in {3..1002}
	do
		msg[j]="${md[j-3]}${md[j-2]}${md[j-1]}"
		md[j]=$(echo -n "${msg[j]}" | xxd -r -p | sha224sum -t | awk '{printf $1}')
	done
	seed=${md[1002]}
	echo "$i: "$seed
done
