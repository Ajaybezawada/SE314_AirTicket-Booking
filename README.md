# SE314
Software Engineering <br>


Topic: Airline Seat Selection, Boarding Pass Issuance And Aircraft Boarding<br>
Group: 8<br>
Dept-Sec: CSE-C<br>


# About the project<br>
We will be creating an Airline Booking System which will help the customers to book a flight ticket. The customers can modify and cancel the ticket.<br>
Given that the passenger hasn't already registered, will allow creating an account<br>
The boarding pass will contain the passenger details, scannable QR code of their PNR number, seat number.<br>
The airport agent can enter the flight ID and grab the passenger list.<br>
The airport agent can enter the PNR  and grab the passenger details.<br>
The main purpose of this software is to reduce the manual errors involved in the airline reservation process and makes it convenient for the customers to book the flights <br>when they require so that they can utilize this software to make reservations, modify reservations or cancel a particular reservation.<br>

# Stakeholders <br>
Employees<br>
Passengers<br>
Government Authorities<br>
Airline Clients<br>
Modules<br>
Login Module<br>
Booking Module<br>
Search Module<br>
Check Availability Module<br>
Boarding Pass Issual Module<br>
Payment Module<br>
Purchase Module<br>
Exit Module<br>

Table(Master/Transaction)
Primary key — Master table (Flight Info Table)
Foreign key — Transaction table
Ticket Price Table-price,flight boarding point,flight destination,flight name,flight-ID.
Ticket Cancellation Status Table-price,flight boarding point,flight destination,flight name,flight-ID(change if any requirements)
Flight Schedule Table-flight-ID,flight_name,date,time,flight_boarding point,flight_destination_point,path_taken.
Login Details Table-name ,username,user_id,address,aadhaar_number,passport_number,phone_number,date_of_birth,password.
Flight Info Table-flight_name,airline_name,no_of_tickets_available,_cost_of_ticket,flight_destination,travel_date,time,seat_vacancy,passenger_id
Flight Route Table-flight_name,flight_id,flight_destination,flight_starting_from,path_taken,date,time
Airport Staff Table-staff__id,staff_name,staff_shift_hour,aadhar_no,date_of_birth
Passenger Table-passenger_id,passenger_name,passenger_mobile,passenger_username,passenger_password,passenger_address,aadhar_no,date_of_birth
Transaction Table-Transaction_ID,price,payment_method.
User_id, payment_id, 

# Tools/Languages:
VScode, MongoDB,Android Studio(Java)+SQLite
Javascript (NodeJS,EJS,ReactJS), HTML/CSS
Bootstrap

# Reports
Name:  Airline Booking
Purpose: For booking Flight tickets using our product
This report is to convey all the modules that we are using in this project along with the tables. This project consists of tables that include the details of Flight, passengers, and different modules which will help the user to freely interact with the application.
Suppliers: They are interested in gaining more profits. However, they will be affected if the tickets are sold less which means less purchase of the flight tickets will lead to less profit.
Competitors:  They will charge less price for the same traveling journey to attract more customers, and they will keep eye on each other to do better and get more sales.

# Assumptions: 
Mobile and web Platform
When the Ticket is canceled by the user, only some percent of the user ticket amount will be re-sent .(Ticket Cancellation Charges).
Admin will be able to search booking enquiry and has permission to edit , add and delete any booking enquiry
Passenger will be able to generate a report of airline ticket booking
Admin can update  the price of the Flight Ticket.

Requirements:
	User
Passenger : 
Login
KYC Details and Update 
Search Ticket
Book Ticket 
Payment 
After payment receives receipt and schedule
 Government Authorities:
Login 
KYC Details and Update
PNR Searching 
Ticket cancellations module
      c)  Admin(Airline reservation system)
Display list of vacant schedules
Display reservation info and payment
Receives the payment and transaction
Generates reservation form and release receipt
        d)  Airline Clients
 Login
 Price updation portal 
**********************************
