
Django Rule Engine with AST
This project implements a 3-tier rule engine using Django. It allows users to create dynamic rules based on attributes such as age, department, income, and experience. The rules are converted into Abstract Syntax Trees (ASTs), enabling dynamic evaluation.

Features
Create complex rules using logical operators (AND, OR) and comparisons.
Store rules in a database.
Evaluate rules dynamically against provided input data.
Secure AST-based evaluation to prevent unsafe code execution.
Simple UI for rule creation and evaluation.
Tech Stack
Backend: Django
Frontend: Django Templates (HTML)
Database: SQLite (default Django database)
Installation
Clone the Repository

bash
Copy code
git clone <your-repo-url>
cd django-rule-engine
Set up Virtual Environment (Optional but Recommended)

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy code
pip install django
Run Migrations

bash
Copy code
python manage.py migrate
Create a Superuser for Django Admin

bash
Copy code
python manage.py createsuperuser
Run the Development Server

bash
Copy code
python manage.py runserver
Access the Application

Admin Panel: http://127.0.0.1:8000/admin
Create and Evaluate Rules: http://127.0.0.1:8000/api/
Usage
1. Create Rule
Navigate to /api/create/ to enter new rules.
Example Rule:
plaintext
Copy code
(age > 30 and department == 'Sales') or (experience > 5)
2. Evaluate Rule
Navigate to /api/evaluate/ to evaluate an existing rule.
Select the rule and provide attributes in JSON format:
json
Copy code
{
    "age": 35,
    "department": "Sales",
    "salary": 60000,
    "experience": 3
}
3. Admin Panel
Use the Django admin panel to view or modify stored rules.
Project Structure
bash
Copy code
django-rule-engine/
│
├── rule_engine_project/          # Main Django project folder
│   ├── settings.py               # Django settings file
│   ├── urls.py                   # Project-level URLs
│   └── wsgi.py                   # WSGI entry point for deployment
│
├── rule_engine/                  # App containing the rule engine logic
│   ├── migrations/               # Database migrations
│   ├── templates/                # HTML templates
│   │   ├── create_rule.html      # Template for creating rules
│   │   └── evaluate_rule.html    # Template for evaluating rules
│   ├── models.py                 # Rule model
│   ├── views.py                  # Views for create and evaluate actions
│   ├── engine.py                 # AST-based rule processing logic
│   └── urls.py                   # App-level URLs
│
├── db.sqlite3                    # SQLite database (default)
├── manage.py                     # Django management script
└── README.md                     # Documentation
Example Rule Strings
Rule 1:
scss
Copy code
((age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')) 
AND (salary > 50000 OR experience > 5)
Rule 2:
scss
Copy code
(age > 30 AND department == 'Marketing') AND (salary > 20000 OR experience > 5)
API Endpoints
Create Rule: /api/create/

Accepts a rule string and stores it in the database.
Evaluate Rule: /api/evaluate/

Accepts a rule ID and a JSON object with attributes to evaluate the rule.
Error Handling
Invalid Rule Syntax: The system raises a ValueError for malformed rules.
Invalid JSON Input: The system raises a JSONDecodeError for incorrect JSON data.
Rule Not Found: If the rule ID is invalid, the user will be notified.
How to Contribute
Fork the repository.
Create a new feature branch:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Add your message here"
Push to the branch:
bash
Copy code
git push origin feature-name
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contact
If you encounter any issues, feel free to reach out:

Email: abhishekbhagat6654@gmail.com
GitHub: https://github.com/krAbhishek09
