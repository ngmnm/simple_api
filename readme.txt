Task1: API’s Documentation
View:
	/device/
	To view all records in DeviceModel database.
	e.g. http://127.0.0.1:8000/device/
	/vender/
	To view all records in VendorModel database.
	e.g. http://127.0.0.1:8000/vender/

Retrieve one record:
	/device/<x>/
	To retrieve the record with primary key equal x from DeviceModel database
	/vender/<x>/
	To retrieve the record with primary key equal x from VendorModel database

Delete and modify:
	for any record to be modified or deleted it has to be retrieved as one record. 
	e.g. e.g. http://127.0.0.1:8000/device/1/

Post:
	there are three way to insert data
		1- from django admin page
		2- from django rest framwork UI
		3- from any program that enable post (e.g. postman)

Pagination:
	/vender/?page_size=x&page=y
	To determine the size of page and how many records in a single page by x. While page 	number is decided by the value of  y.
	e.g. http://127.0.0.1:8000/device/1/all?page=2&page_size=1