# Sales Craft - Centralized CRM Web Application

Sales Craft is a centralized CRM (Customer Relationship Management) web application built using Django and other web technologies. It helps businesses manage their customer interactions, sales, and other essential CRM functionalities.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Secure user authentication and registration system.
- **Customer Management**: Add, update, and manage customer profiles.
- **Sales Pipeline**: Track sales leads and monitor the sales process.
- **Task Management**: Assign and manage tasks related to customer interactions.
- **Responsive Design**: A user-friendly and mobile-responsive interface.

## Tech Stack

- **Django**: A high-level Python web framework for rapid development.
- **HTML/CSS**: Used for frontend development and styling.
- **JavaScript**: Enhanced user experience and interactivity.
- **Bootstrap**: A front-end framework for responsive design.
- **Railway Hosting**: The project is hosted on Railway, making it accessible to users online.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sidhu2003/Sales-Craft.git
   cd Sales-Craft
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
3. Apply DataBase migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
4. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
5. Start the development server:
   ```bash
   python manage.py runserver

## Usage

- Access the admin panel by visiting `http://localhost:8000/admin/` and log in with your superuser credentials.
- Start by adding customers, sales leads, and tasks to your CRM system.
- Explore the various features of the application, such as reporting and customization.

## Contributing

We welcome contributions from the open-source community. If you'd like to contribute to Sales Craft, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
3. Commit your changes and push to your fork:
   ```bash
   git commit -m "Add your feature or fix"
   git push origin feature/your-feature-name
4. Create a pull request on the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to modify and expand this README according to the specifics of your project. Don't forget to update it as your project evolves. Good luck with Sales Craft!


   

