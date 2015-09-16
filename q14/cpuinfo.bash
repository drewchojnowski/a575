#!/bin/bash

#type="html"
type="latex"

if [[ $type == "html" ]]; then
	echo "<HTML>"
	echo "<HEAD>"
	echo "<TITLE>NMSU Astronomy Computing Resource Info</title>"
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
else
	echo "\documentclass{article}"
	echo "\renewcommand{\arraystretch}{2}"
	echo "\usepackage{rotating}"
	echo "\begin{document}"
	echo "\begin{sidewaystable}[t]"
	echo "\caption{NMSU Astronomy Computing Resource Info}"
	echo "\centering"
	echo "\begin{tabular}{|c|c|c|c|c|c|c|c|}"
	echo "\hline"
	echo "\textbf{Computer} & \textbf{\#}   & \textbf{CPU}   & \textbf{Disk} & \textbf{Disk} & \textbf{Disk}   & \textbf{\%}   & \textbf{Cache} \\\\"
	echo "\textbf{Name}     & \textbf{CPUs} & \textbf{Model} & \textbf{Size} & \textbf{Used} & \textbf{Avail.} & \textbf{Used} & \textbf{Size} \\\\"
	echo "\hline \hline"
	for host in $* ; do
		echo $host" & "
		ssh $host getcpuinfo.bash
		echo "\hline"
	done
	echo "\end{tabular}"
	echo "\end{sidewaystable}"
	echo "\end{document}"
fi

