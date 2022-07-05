# ParsingData
 This project includes the parsing of a very messy file, pulled from a data logger OMC-048. Data is being pulled from the internal sensors of the OMC-048, but also from an external sensor connected to the OMC-049 (Starflow QSD). In this project, there's also a connection to a local SQL Server that's being created. A new table, called data, is created on the database named "datalogger" which is found on the local SQL server and all the data after the parsing is sent there.
 
 The initial messy file is the "ex2.csv". The data logger didn't create a certain pattern to be followed, so the data was very hard to read/understand at first glance. That's why the parsing of the data was inevitable. The results of the parsing are put into a new csv file called "data11.csv". On that file the data is more user friendly, and very comprehensible. As mentioned before, this data is then also sent to the "datalogger" database in the local SQL server.
 
 ## Local SQL Server
 
 The local SQL server was created with the help of SQL Server 2014 Management studio. Here's a video tutorial from youtube to show you how to setup SQL Server 2014 Management Studio, and also how to create the local SQL Server: [SQL Server Setup](https://www.youtube.com/watch?v=E_zFM7mzFUg).
 
 When creating the connection string (conn_string in the pandas_example.py file), make sure to replace YOUR_SERVER_NAME with the name of your local SQL Server and replace PORT_NUMBER with the number of the server port, which can be found like in the Sql Server Configuration Manager like this:
-Go to SQL Server Network Configuration
-Then click on "Protocols for YOUR_SERVER_NAME" and if you 
-Right click on TCP/IP, you 
-Click on properties, 
-Then you click on IP Addresses.
-Scroll all the way to the bottom until you see IPAll and copy the TCP Dynamic Ports, that is your PORT_NUMBER.

*** If your TCP/IP is not enabled, then you need to open the Sql Server Configuration Manager as administrator, and right click on TCP/IP, and click on Enable. ***

 After all this replace YOUR_DATABASE, with the name you gave your database, and then replace YOUR_USERNAME and YOUR_PASSWORD with the credentials that allow you to have access to editing the database.
