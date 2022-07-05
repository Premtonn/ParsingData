# ParsingData
 This project includes the parsing of a very messy file, pulled from a data logger OMC-048. Data is being pulled from the internal sensors of the OMC-048, but also from an external sensor connected to the OMC-049 (Starflow QSD). In this project, there's also a connection to a local SQL Server that's being created. A new table, called data, is created on the database named "datalogger" which is found on the local SQL server and all the data after the parsing is sent there.
 
 The initial messy file is the "ex2.csv". The data logger didn't create a certain pattern to be followed, so the data was very hard to read/understand at first glance. That's why the parsing of the data was inevitable. The results of the parsing are put into a new csv file called "data11.csv". On that file the data is more user friendly, and very comprehensible. As mentioned before, this data is then also sent to the "datalogger" database in the local SQL server.
 
 ## Local SQL Server
 
 The local SQL server was created with the help of SQL Server 2014 Management studio. Here's a video tutorial from youtube to show you how to setup SQL Server 2014 Management Studio, and also how to create the local SQL Server: [SQL Server Setup](https://www.youtube.com/watch?v=E_zFM7mzFUg).
 
 ***When creating the connection string (conn_string in the pandas_example.py file), make sure to replace YOUR_SERVER_NAME with the name of your local SQL Server and replace YOUR_DATABASE with the name that you gave to the database created on the server. Also replace YOUR_USERNAME and YOUR_PASSWORD with the credentials that allow you to have access to editing the database.***
