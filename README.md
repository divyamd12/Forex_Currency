# MITWPU-team21-ForexDashboard
College Name: MIT-WPU
Team Number: 21
Members: 
1.	Divyam Dholwani
2.	Harsh Rane
3.	Khilee Singhal
4.	Manas Pal
5.	Manav Chandak


1. Introduction 
This documentation outlines the features, usage, and technical details of the Exchange Rate Analysis Dashboard. The dashboard provides users with the ability to analyse exchange rates between USD and another currency over various time periods.

2. Features 
●	Select weekly, monthly, quarterly, and yearly charts.
●	View the date on which the exchange rate was at its peak and trough.
●	Print the data in chart format.
●	Dynamic currency pair selection with USD as the base currency.
●	Also convert amount in one currency to another

3. Usage 
1.	Clone the repository.
2.	Install dependencies.
3.	Provide the currency exchange rate dataset in the specified format.
4.	Run the dashboard.

4. Input Data Format 
The input data should be in a CSV file format with columns:
●	Date (in YYYY-MM-DD format)
●	Exchange Rate

Example:
pythonCopy code
Date | ExchangeRate 2022-01-01 | 73.45 2022-01-02 | 73.60 ... | ... 

5. Dashboard Components <a name="dashboard-components"></a>
5.1 Year Range Selector
●	Users can select the desired time range for analysis (weekly, monthly, quarterly, yearly).
5.2 Currency Pair Selection
●	Users can choose the currency pair for analysis with base having default value of USD        (e.g., USD/INR, USD/GBP).
5.3 Chart Options
●	The appropriate graph is displayed.
5.4 Peak and Trough Information
●	Displays the date on which the exchange rate was at its highest, lowest and average of the given range.

6. Technical Details 
6.1 Technology Stack
●	Frontend: HTML, CSS, 
●	Backend: Flask is used for connecting frontend and backend, matplot library is used for plotting graphs
●	Data Storage: CSV file
6.2 Dependencies
●	Matplotlib
●	CSV parsing library
6.3 Installation
1.	Clone the repository.
6.4 Running the Dashboard
1.	Go to backend.py home path
2.	In the terminal write- python backend.py
3.	Open the browser and navigate to http://localhost:5000
4.	Further to run the test cases- pytest backend_test.py

7. Conclusion 
The Exchange Rate Analysis Dashboard provides users with a user-friendly interface to analyze exchange rates over time. Users can customize the analysis based on their preferences and print the data for further reference.