LOGS ANALYSIS PROJECT

In this project the task is "to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database".

The Questions the reporting tool should answer

	1. What are the most popular three articles of all time?
	2. Who are the most popular article authors of all time?
	3. On which days did more than 1% of requests lead to errors?

What you need installed to run the reporting tool
Virtual Machine – This tool requires the use of a Linux-based virtual machine(VM) to run an SQL database server and an application that uses it.

1.	You will be using tools called Vagrant and VirtualBox to install and manage the VM.
2.	There are two ways to get the necessary configuration files for the VM.
a.	You can download and unzip this file: FSND-Virtual-Machine.zip
b.	Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

Launching the Virtual Machine from Git Bash or similar terminal
1.	Cd into the Vagrant subdirectory within the directory create from the zip or Github repository from step 2b.
2.	Launch VM with the command:  $ vagrant up 
3.	Log into the VM with:  $ vagrant ssh
4.	Cd into the   /vagrant directory.

Set up the news database and create necessary views.
1.	To load the data, cd into the vagrant directory and use the command: psql -d news -f newsdata.sql.
	Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, 		creating tables and populating them with data.
2.	Use the command:  psql -d news to connect to database.
3.	Create the following views:

article_view
	
	create view article_view as select title,author,
	count(*) as views from articles, log
	where log.path like concat(‘%’, articles.slug)
	group by articles.title, articles.author
	order by views desc;


author_view

	create view author_view as select name,
    	sum(article_view.views) as total
	from article_view, authors
	where authors.id = article_view.author
	group by authors.name
	order by total desc;

request_errors_view

	create view request_errors_view as select date(time),	
	round(100.0*sum(case log.status when '200 OK'
	then 0 else 1 end)
   	/count(log.status),2) as "Percent Error"
	from log group by date(time)
	order by "Percent Error" desc;

Running the queries requires.
1.	Clone this git depository to get the newslogs.py script:  
    	https://github.com/madtech2014/Log-Analysis-FSND.git
	
2.	Cd into the directory Log-Analysis-FSND and
   	run the following command:
   	$ python newslogs.py

Resources:
-Udacity 
    Programming Foundations with Python
-https://stacksocial.com/?aid=a-lzb57ptm
-http://www.postgresqltutorial.com/
-https://www.thinkful.com/learn/a-guide-to-using-github-pages
-https://www.codecademy.com/learn
-http://brackets.io/
-https://www.python.org/



