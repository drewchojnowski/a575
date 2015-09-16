#!/bin/bash

echo -n "Which computer do you want to check? > "
read comp1
echo "CPU info for $comp1 will be checked"

compinfo=`df -hl --total | tail -1`

dsize=`df -hl --total | tail -1 | awk '{printf("%s\n",$2)}'`
dused=`df -hl --total | tail -1 | awk '{printf("%s\n",$3)}'`
davail=`df -hl --total | tail -1 | awk '{printf("%s\n",$4)}'`
dpercent=`df -hl --total | tail -1 | awk '{printf("%s\n",$5)}'`
model=`cat /proc/cpuinfo | grep "model name" | head -1 | awk '{print substr($0,14)}'`
cache=`cat /proc/cpuinfo | grep "cache size" | head -1 | awk '{print substr($0,14)}'`


htmlfile="/home/httpd/html/drewski/a575/computing_resource_info.html"
rm -f $htmlfile
touch $htmlfile

echo "<HTML>" >> $htmlfile
echo "<HEAD>" >> $htmlfile
echo "<TITLE>NMSU Computing Resource Info</title>" >> $htmlfile
echo "</HEAD>" >> $htmlfile
echo "<BODY>" >> $htmlfile
echo "<p> This page lists resource info for NMSU machines.</p>" >> $htmlfile
echo "<HR>" >> $htmlfile

echo "<table border=1 bgcolor=#DDDDDD>" >> $htmlfile
echo "<tr>" >> $htmlfile
echo "<th><font size=2>Computer Name</font></th>" >> $htmlfile
echo "<th><font size=2>CPU Model</font></th>" >> $htmlfile
echo "<th><font size=2>Disk Size</font></th>" >> $htmlfile
echo "<th><font size=2>Disk Used</font></th>" >> $htmlfile
echo "<th><font size=2>Disk Avail.</font></th>" >> $htmlfile
echo "<th><font size=2>Use %</font></th>" >> $htmlfile
echo "<th><font size=2>Cache Size</font></th>" >> $htmlfile
echo "</tr>" >> $htmlfile
echo "<tr>" >> $htmlfile
echo "<td align="center"><font size=2>"$comp1"</font></td>" >> $htmlfile
echo "<td align="center"><font size=2>"$model"</font></td>" >> $htmlfile
echo "<td align="center"><font size=2>"$dsize"B</font></td>" >> $htmlfile
echo "<td align="center"><font size=2>"$dused"B</font></td>" >> $htmlfile
echo "<td align="center"><font size=2>"$davail"B</font></td>" >> $htmlfile
echo "<td align="center"><font size=2>"$dpercent"</font></td>" >> $htmlfile
echo "<td align="center"><font size=2>"$cache"</font></td>" >> $htmlfile
echo "</tr>" >> $htmlfile
echo "</BODY>" >> $htmlfile
echo "</HTML>" >> $htmlfile











