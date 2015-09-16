READ ME q14
================================================================================
There are two scripts here: 
	1. cpuinfo.bash: prepares the html or latex table code
	2. getcpuinfo.bash: acquires data and inserts data lines into table
================================================================================
User can make the html versus latex choice by commenting or uncommenting lines 3-4.
This currently must be done in both scripts.
================================================================================
The syntax is as follows
	"$ cpuinfo.bash host1 host2 host3"
for as many hosts as desired.
================================================================================
Output files can be made and viewed via
	"$ cpuinfo.bash host1 host2 host3 > cpuinfotable.html"
	"$ firefox cpuinfotable.html"
or
	"$ cpuinfo.bash host1 host2 host3 > cpuinfotable.tex"
	"$ pdflatex cpuinfotable.tex"
	"$ evince cpuinfotable.pdf"
================================================================================
I could have added a lot more info about each computer, but didn't. Maybe later
================================================================================
