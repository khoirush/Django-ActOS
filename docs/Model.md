DJ - Model Architecture Planning
	Personnel
		ID Personnel - INT
		First Name - CHAR 20
		Last Name - CHAR 20
		Position - CHAR 20)
		Status (Employee, Outsource, Contract) - CHAR 20

	Project
		ID Project - INT
        SLUG - SLUG
		Title - CHAR 255
		Description - TEXT
		Start Date - DATE
		End Date - DATE
		Create Date - TIMESTAMP
		Update Date - TIMESTAMP

	ProjectTask 
		ID Task - INT
		ID Project (Foreign Key) - INTE
		Priority Level (High, Normal, Low) - CHAR 10
		Title - CHAR 255
		Description - TEXT
		Status (Ongoing, Done, Pending) - CHAR 10
		PctComplete - INT (MAX 100)
		PctWeight - FLOAT
		Create Date - TIMESTAMP
		Update Date - TIMESTAMP
		Start Date - DATE
		TargetFinish Date - DATE
		TargetDuration - INT
		PIC - CHAR 255 (EX : 16444,16445,...)
		*TOTALMANDAYS (JUMLAH PIC * TARGET DURATION)

	ProjectAssignment
		ID Assignment - INT
		ID Personnel (FOREIGN KEY) - INT
		ID Project (FOREIGN KEY) - INT
		Start Date - DATE
		End Date - DATE
		Create Date - TIMESTAMP
		Update Date - TIMESTAMP
	
	Activity Log
		Activity Date - Date
        ID Activity - INT
        ID Personnel (FOREIGN KEY) - INT
		ID Assignment (FOREIGN KEY) - INT
		Create Date - TIMESTAMP
		Update Date - TIMESTAMP
	
	Detail WorkActivity
        ID ProjectTask (FOREIGN KEY) - INT
		ID Activity (FOREIGN KEY) - INT
		DESCRIPTION - CHAR500
		Location - CHAR20 (Remote, Office, Customer Site)
		PctTaskComplete - FLOAT
		Create Date - TIMESTAMP
		Update Date - TIMESTAMP

	Customer
        ID Customer - INT
        Customer Name - CHAR 50
	Vendor
        ID Vendor - INT
        Vendor Name - CHAR 50