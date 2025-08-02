# Python-beginner-project
I made this project with basic knowledge of python
# Student Portal System

A simple command-line based student management system that allows students to access their academic information including fees, course registration, and results.

## Features

- **Secure Login System**: Username, registration number, and password authentication
- **Dashboard Navigation**: Easy-to-use menu system with multiple options
- **Home Panel**: View upcoming events and announcements
- **Student Fees**: Check payment status and remaining balance
- **Course Registration**: View registered courses
- **Results**: Check academic grades and notifications
- **Security**: Limited login attempts with lockout mechanism

## System Requirements

- Python 3.x
- No external dependencies required (uses only built-in Python modules)

## Installation

1. Clone or download the script file
2. Ensure Python 3.x is installed on your system
3. Run the script using: `python student_portal.py`

## Usage

### Login Credentials

The system currently has one registered student:

- **Username**: Ivy Leah
- **Registration Number**: DPP3/6633/2023
- **Password**: Ivy22

### Running the Application

1. Execute the Python script
2. Enter your login credentials when prompted
3. Navigate through the dashboard using the numbered menu options

### Dashboard Options

1. **Home**: View upcoming events and announcements
2. **Student Fees**: Check fee payment status and balance
3. **Course Registration**: View your registered courses
4. **Results**: Check academic grades and supplementary exam notifications
5. **Logout**: Exit the system

## Security Features

- **Authentication Required**: All three credentials (username, registration, password) must match
- **Limited Attempts**: Maximum of 3 login attempts before system lockout
- **Session Management**: Secure logout functionality
- **Input Validation**: Strips whitespace from user inputs

## Sample Data

### Student Information
- **Name**: Ivy Leah
- **Registration**: DPP3/6633/2023
- **Fees Paid**: KSH 200,000
- **Balance**: KSH 40,000

### Registered Courses
1. Project Planning Tools and Techniques
2. Micro-economics
3. Macro Economics
4. Procurement and Supply Chain Management
5. Fundamentals of Accounting

### Academic Results
- Micro Economics: A
- Macro Economics: B
- Project Planning Tools and Techniques: C
- Microeconomics: A
- Fundamentals of Accounting: E (Supplementary exam required)
- Procurement and Supply Chain Management: A

## Code Structure

```python
# Main Components:
├── students{}          # Student credentials dictionary
├── authenticate()      # Login validation function
├── show_dashboard()    # Main menu system
└── login()            # Login attempt management
```

## Customization

### Adding New Students

To add more students, update the `students` dictionary:

```python
students = {
    "Student Name": {
        "registration": "REGISTRATION_NUMBER",
        "password": "PASSWORD"
    },
    # Add more students here
}
```

### Modifying Dashboard Content

Each dashboard option can be customized by editing the corresponding `elif` block in the `show_dashboard()` function.

## Error Handling

- **Invalid Credentials**: System provides feedback on failed login attempts
- **Invalid Menu Selection**: User is prompted to select valid options (1-5)
- **Session Security**: Automatic logout after maximum failed attempts

## Future Enhancements

Potential improvements could include:

- Database integration for persistent data storage
- Web-based interface
- Email notifications for supplementary exams
- Fee payment integration
- Course enrollment functionality
- Multi-semester support
- Admin panel for managing students

## Troubleshooting

### Common Issues

1. **Login Failed**: Ensure all credentials are entered exactly as stored (case-sensitive)
2. **Script Won't Run**: Verify Python 3.x is installed and script has proper permissions
3. **Menu Not Working**: Check for typos in menu selection (enter numbers 1-5 only)

### Support

For technical issues or feature requests, contact the system administrator.

## License

This is a demonstration/educational project. Modify and use according to your institution's requirements.

## Version History

- **v1.0**: Initial release with basic login and dashboard functionality

---

**Note**: This system is designed for educational purposes. For production use, consider implementing proper database storage, encryption for passwords, and additional security measures.
