#!/bin/bash

dsize=`df -hl --total | tail -1 | awk '{printf("%s\n",$2)}'`
dused=`df -hl --total | tail -1 | awk '{printf("%s\n",$3)}'`
davail=`df -hl --total | tail -1 | awk '{printf("%s\n",$4)}'`
dpercent=`df -hl --total | tail -1 | awk '{printf("%s\n",$5)}'`
model=`cat /proc/cpuinfo | grep "model name" | head -1 | awk '{print substr($0,14)}'`
cache=`cat /proc/cpuinfo | grep "cache size" | head -1 | awk '{print substr($0,14)}'`
ncpu=`nproc`

echo "<td align="center"><font size=2>"$ncpu"</font></td>"
echo "<td align="center"><font size=2>"$model"</font></td>"
echo "<td align="center"><font size=2>"$dsize"B</font></td>"
echo "<td align="center"><font size=2>"$dused"B</font></td>"
echo "<td align="center"><font size=2>"$davail"B</font></td>"
echo "<td align="center"><font size=2>"$dpercent"</font></td>"
echo "<td align="center"><font size=2>"$cache"</font></td>"


