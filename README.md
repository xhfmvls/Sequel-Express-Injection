# Sequel Express Injection

Secure Programming Challenge Against SQL Injection Threat with Express.js

## Scenario
In this challenge, participants are tasked with addressing a SQL Injection vulnerability within an Express.js API connected to a MySQL database. The current code permits users to submit an item name via a POST request body, subsequently returning the requested item's data through the API response. However, the absence of input validation and parameterized queries exposes the API to potential SQL Injection attacks, enabling users to manipulate the SQL query to access or modify unauthorized data.
  
Participants are required to to fortify the application's defenses against SQL Injection attacks. Successful resolution of the vulnerability demands that the API maintains its functionality while effectively neutralizing the identified security risk.

The vulnerability lies within the direct concatenation of user-provided input (item_name) into the SQL query string without proper validation or parameterization. Specifically, the vulnerable code segment is as follows:

```js
const connection = await pool.getConnection();
const query = 'SELECT id, name, description FROM items WHERE name = \'' + item_name + '\'';
const [results] = await connection.execute(query);
```
  
Submissions for this challenge must comprise solely of the amended code, confined within the **app.js** file. To find hints or clues on fixing the vulnerability, refer to the Resource section below (Prevention against SQL Injection in Node.js).

## Requirements

- Node.js
- MySQL
- Git
- Quanchecker package

## Setup

### 1. Clone the Repository
   - Clone this repository to your local machine using the following command:
     ```
     git clone https://github.com/xhfmvls/Sequel-Express-Injection.git
     ```

### 2. Install Dependencies
   - Navigate to the project directory.
   - Install the required dependencies using the following command:
     ```
     npm install
     ```

### 3. Setup the Database
   - Ensure you have MySQL installed on your local machine.
   - Create a new database.
   - Execute the queries in the **query.sql** file to create the necessary tables and populate them with initial data.

### 4. Configure Environment Variables
   - Update the .env file in the project directory by filling the variables:
     ```
     DB_HOST=your_db_host
     DB_HOST=your_db_host
     DB_USER=your_db_user
     DB_PASSWORD=db_password
     DB_NAME=your_db_name
     DB_PORT=your_db_port
     ```

### 5. Run the Application
   - Run the Express.js application using the following command:
     ```
     node app.js
     ```
   - The application will start running locally on `http://localhost:8080`.

## Testing and Submission

### 1. Testing Procedure
  - To run the test, execute the following command in your terminal:
    ```
    python checker.py
    ```
  - Before running the tests, ensure that you have installed the Quanchecker package. You can do so by executing:

    ```
    pip install quanchecker
    ```
  - Please note that the test cases executed (in`checker.py` file) are only examples provided for your reference. There are additional test cases that are kept confidential and will only be run when you submit your code.


#### Input Format:
- **Description**: The input consists of a string representing an item name.
- **Format**: 
  - The string has a length between 10 and 50 characters, inclusive.

#### Output Format:
- **Description**: The expected output can be one of the following:
  1. **Item Details**: An object containing the item details if the input is valid and the corresponding item exists.
  2. **Error Message**: If the input is invalid or the corresponding item does not exist, an appropriate error message should be produced.
  - **Item not found!**: If the item corresponding to the input item name does not exist.

### 2. Submission Guidelines
   - Once you have fixed the vulnerability, upload your solution to the web application.
   - The web application will validate whether the code is secure against the complete prepared payload.

## Resources

- [Prevention against SQL Injection in Node.js](https://planetscale.com/blog/how-to-prevent-sql-injection-attacks-in-node-js)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [SQL Injection Payloads](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection)

## Credits
- **[xhfmvls](https://github.com/xhfmvls)** - Quan C Lead Developer
