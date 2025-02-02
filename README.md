# Django FAQ API

## Description
The Django FAQ API is a web application that allows users to manage Frequently Asked Questions (FAQs) with multilingual support. It is built using Django and Django REST Framework to provide a robust API for creating, retrieving, and managing FAQs. The application integrates a WYSIWYG editor for enhanced text formatting of answers and employs Redis for caching to improve performance. This project supports multiple languages, allowing users to manage FAQs in different languages like Hindi and Bengali, with a fallback to English.

## Installation Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Redis (for caching)

### Steps to Install and Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vishal2314/bharatfd-Assignment-.git
2.Navigate to the Project Directory:
cd bharatfd-Assignment-

3.Create and Activate a Virtual Environment:
python -m venv venv

.\venv\Scripts\activate

4.Install Required Packages: Make sure you have a requirements.txt file in the root directory. If it’s not present, create it and include the following packages:
Django
djangorestframework
django-ckeditor
redis
googletrans==4.0.0-rc1
psycopg2-binary  # If you plan to use PostgreSQL
Then install the dependencies:
   pip install -r requirements.txt
5.Run Migrations:
python manage.py migrate
6.Run the Development Server:
python manage.py runserver


API Usage Examples
Fetch All FAQs
Endpoint: GET http://127.0.0.1:8000/api/faqs/
Description: Retrieve a list of all FAQs in English (default language).
Response Example
[
    {
        "id": 1,
        "question": "What is Django?",
        "answer": "<p>Django is a web framework.</p>",
        "question_hi": "डजैंगो क्या है?",
        "question_bn": "ডজেঙ্গো কি?"
    },
    {
        "id": 2,
        "question": "How do I install Django?",
        "answer": "<p>You can install Django using pip.</p>",
        "question_hi": "मैं Django कैसे स्थापित करूँ?",
        "question_bn": "আমি Django কিভাবে ইনস্টল করব?"
    }
]

Here's a fully prepared README.md content for your Django FAQ API project. You can paste this directly into your README.md without the need for customization or modifications.

markdown

Copy
# Django FAQ API

## Description
The Django FAQ API is a web application that allows users to manage Frequently Asked Questions (FAQs) with multilingual support. It is built using Django and Django REST Framework to provide a robust API for creating, retrieving, and managing FAQs. The application integrates a WYSIWYG editor for enhanced text formatting of answers and employs Redis for caching to improve performance. This project supports multiple languages, allowing users to manage FAQs in different languages like Hindi and Bengali, with a fallback to English.

## Installation Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Redis (for caching)

### Steps to Install and Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vishal2314/bharatfd-Assignment-.git
Navigate to the Project Directory:

bash

Copy
cd bharatfd-Assignment-  # Change to the directory where the project is located
Create and Activate a Virtual Environment:

bash

Copy
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
Install Required Packages: Make sure you have a requirements.txt file in the root directory. If it’s not present, create it and include the following packages:

plaintext

Copy
Django
djangorestframework
django-ckeditor
redis
googletrans==4.0.0-rc1
psycopg2-binary  # If you plan to use PostgreSQL
Then install the dependencies:

bash

Copy
pip install -r requirements.txt
Run Migrations:

bash

Copy
python manage.py migrate
Run the Development Server:

bash

Copy
python manage.py runserver
Now your application should be running at http://127.0.0.1:8000/.

API Usage Examples
Fetch All FAQs
Endpoint: GET http://127.0.0.1:8000/api/faqs/
Description: Retrieve a list of all FAQs in English (default language).
Response Example:
json

Copy
[
    {
        "id": 1,
        "question": "What is Django?",
        "answer": "<p>Django is a web framework.</p>",
        "question_hi": "डजैंगो क्या है?",
        "question_bn": "ডজেঙ্গো কি?"
    },
    {
        "id": 2,
        "question": "How do I install Django?",
        "answer": "<p>You can install Django using pip.</p>",
        "question_hi": "मैं Django कैसे स्थापित करूँ?",
        "question_bn": "আমি Django কিভাবে ইনস্টল করব?"
    }
]
Fetch FAQs in Hindi
Endpoint: GET http://127.0.0.1:8000/api/faqs/?lang=hi
Response Example:
[
    {
        "id": 1,
        "question": "डजैंगो क्या है?",
        "answer": "<p>Django एक वेब फ़्रेमवर्क है।</p>",
        "question_hi": "डजैंगो क्या है?",
        "question_bn": "ডজেঙ্গো কি?"
    }
]
Here's a fully prepared README.md content for your Django FAQ API project. You can paste this directly into your README.md without the need for customization or modifications.

markdown

Copy
# Django FAQ API

## Description
The Django FAQ API is a web application that allows users to manage Frequently Asked Questions (FAQs) with multilingual support. It is built using Django and Django REST Framework to provide a robust API for creating, retrieving, and managing FAQs. The application integrates a WYSIWYG editor for enhanced text formatting of answers and employs Redis for caching to improve performance. This project supports multiple languages, allowing users to manage FAQs in different languages like Hindi and Bengali, with a fallback to English.

## Installation Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Redis (for caching)

### Steps to Install and Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vishal2314/bharatfd-Assignment-.git
Navigate to the Project Directory:

bash

Copy
cd bharatfd-Assignment-  # Change to the directory where the project is located
Create and Activate a Virtual Environment:

bash

Copy
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
Install Required Packages: Make sure you have a requirements.txt file in the root directory. If it’s not present, create it and include the following packages:

plaintext

Copy
Django
djangorestframework
django-ckeditor
redis
googletrans==4.0.0-rc1
psycopg2-binary  # If you plan to use PostgreSQL
Then install the dependencies:

bash

Copy
pip install -r requirements.txt
Run Migrations:

bash

Copy
python manage.py migrate
Run the Development Server:

bash

Copy
python manage.py runserver
Now your application should be running at http://127.0.0.1:8000/.

API Usage Examples
Fetch All FAQs
Endpoint: GET http://127.0.0.1:8000/api/faqs/
Description: Retrieve a list of all FAQs in English (default language).
Response Example:
json

Copy
[
    {
        "id": 1,
        "question": "What is Django?",
        "answer": "<p>Django is a web framework.</p>",
        "question_hi": "डजैंगो क्या है?",
        "question_bn": "ডজেঙ্গো কি?"
    },
    {
        "id": 2,
        "question": "How do I install Django?",
        "answer": "<p>You can install Django using pip.</p>",
        "question_hi": "मैं Django कैसे स्थापित करूँ?",
        "question_bn": "আমি Django কিভাবে ইনস্টল করব?"
    }
]
Fetch FAQs in Hindi
Endpoint: GET http://127.0.0.1:8000/api/faqs/?lang=hi
Response Example:
json

Copy
[
    {
        "id": 1,
        "question": "डजैंगो क्या है?",
        "answer": "<p>Django एक वेब फ़्रेमवर्क है।</p>",
        "question_hi": "डजैंगो क्या है?",
        "question_bn": "ডজেঙ্গো কি?"
    }
]
Fetch FAQs in Bengali
Endpoint: GET http://127.0.0.1:8000/api/faqs/?lang=bn
Response Example: 
[
    {
        "id": 1,
        "question": "ডজেঙ্গো কি?",
        "answer": "<p>Django একটি ওয়েব ফ্রেমওয়ার্ক।</p>",
        "question_hi": "डजैंगो क्या है?",
        "question_bn": "ডজেঙ্গো কি?"
    }
]
