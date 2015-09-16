#!/bin/bash

echo -n "Do you want an html table or a latex table? > "
read choice

if $choice == "html"; then
	echo "<HTML>"
	echo "<HEAD>"
	echo "<TITLE>NMSU Computing Resource Info</title>"
	echo "</HEAD>"
	echo "<BODY>"
	echo "<p> This page lists resource info for NMSU machines.</p>"
	echo "<HR>"

	echo "<table border=1 bgcolor=#DDDDDD>"
	echo "<tr>"
	echo "<th><font size=2>Computer Name</font></th>"
	echo "<th><font size=2># CPUs</font></th>"
	echo "<th><font size=2>CPU Model</font></th>"
	echo "<th><font size=2>Disk Size</font></th>"
	echo "<th><font size=2>Disk Used</font></th>"
	echo "<th><font size=2>Disk Avail.</font></th>"
	echo "<th><font size=2>% Used</font></th>"
	echo "<th><font size=2>Cache Size</font></th>"
	echo "</tr>"
	echo "<tr>"

	for host in $* ; do
		echo "<td align="center"><font size=2>"$host"</font></td>"
		ssh $host getcpuinfo.bash
		echo "</tr>"
	done

	echo "</BODY>"
	echo "</HTML>"
fi

