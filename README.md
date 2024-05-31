# Employee Management System

## Description
This is an Employee Management System built using Python and Tkinter for the GUI. It allows users to perform CRUD operations (Create, Read, Update, Delete) on employee records stored in a MySQL database.

## Features
- Add new employee records
- View all employee records
- Update existing employee records
- Delete individual or all employee records
- User-friendly GUI using Tkinter
- Data validation for input fields

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/your_username/employee-management-system.git
   ```
2. Navigate to the project directory:
   ```
   cd employee-management-system
   ```
3. Install the required dependencies:
   ```
   pip install mysql-connector-python
   ```
4. Set up a MySQL database with the appropriate credentials.
5. Update the database connection details in the `Database` class of `db.py`:
   - `host`: Hostname of the MySQL server
   - `user`: MySQL username
   - `password`: MySQL password
   - `database`: Name of the MySQL database
6. Run the application:
   ```
   python main.py
   ```

## Usage
- Launch the application by running `main.py`.
- Fill in the employee details in the provided fields.
- Click the appropriate button to perform CRUD operations.
- To update or delete an employee record, first select the record from the displayed table.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize the README.md file further to suit the specifics of your project!