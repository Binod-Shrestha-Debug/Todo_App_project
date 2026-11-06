# TaskFlow – Advanced Todo Management System

**Developed by: Binod Shrestha**

**GitHub Repository:** [Todo_App_project](https://github.com/Binod-Shrestha-Debug/Todo_App_project)

TaskFlow is a web-based task management application developed using Python, Django, Django REST Framework, HTML, CSS, and JavaScript.

The main purpose of this project is to help users organize their daily work, manage tasks, track deadlines, and monitor their productivity from one place.

I built this project to practice Django web development, database management, REST API development, and frontend design in a practical way.

## Features

### User Account
- Create a new account and log in securely.
- Log out when finished.
- Manage personal tasks separately.
- Each user can access only their own tasks.

### Task Management
- Create, view, edit, and delete tasks.
- Add task descriptions and due dates.
- Set task priorities: Low, Medium, High, and Urgent.
- Track progress using Pending, In Progress, and Completed statuses.
- Identify overdue tasks.

### Task Organization
- Create categories to organize tasks.
- Add tags to tasks.
- Search tasks by title or description.
- Filter tasks by status and priority.
- View upcoming deadlines.

### Dashboard
- View the total number of tasks.
- Check completed and pending tasks.
- Monitor tasks currently in progress.
- Keep track of overdue tasks.
- View recently created tasks.

### REST API
- Create and manage tasks through API endpoints.
- Retrieve individual task details.
- Update and delete existing tasks.
- Manage categories.
- Use JWT authentication.
- Apply API permissions, filtering, and pagination.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web application development |
| Django REST Framework | REST API development |
| HTML5 | Frontend structure |
| CSS3 | Styling and responsive design |
| JavaScript | Frontend interactions |
| SQLite | Database |
| Simple JWT | API authentication |
| Git & GitHub | Version control |

## Getting Started

Follow these steps to run the project on your computer.

### 1. Clone the Repository

```bash
git clone https://github.com/Binod-Shrestha-Debug/Todo_App_project.git
```

### 2. Open the Project

```bash
cd Todo_App_project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create an Admin Account

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

http://127.0.0.1:8000/

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET, POST | `/api/tasks/` | View and create tasks |
| GET | `/api/tasks/1/` | View task details |
| PUT, PATCH | `/api/tasks/1/` | Update a task |
| DELETE | `/api/tasks/1/` | Delete a task |
| GET, POST | `/api/categories/` | View and create categories |
| GET | `/api/dashboard/` | View dashboard statistics |
| POST | `/api/token/` | Generate JWT tokens |
| POST | `/api/token/refresh/` | Refresh access token |

## Run Tests

To run the project's automated tests:

```bash
python manage.py test
```

## Project Structure

```text
Todo_App_project/
│
├── accounts/
├── config/
├── tasks/
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

## Future Improvements

Some features I would like to add in future versions:

- A proper interactive calendar.
- Task reminders and email notifications.
- Drag-and-drop task management.
- More detailed productivity charts.
- Improved task collaboration.
- Deployment with PostgreSQL.

## What I Learned

While developing this project, I practiced:

- Building web applications using Django.
- Working with Django models and database relationships.
- Implementing CRUD operations.
- Developing REST APIs using Django REST Framework.
- Understanding authentication and permissions.
- Working with HTML forms and CSS layouts.
- Managing project code using Git and GitHub.

---

**Developer: Binod Shrestha**

**GitHub:** [https://github.com/Binod-Shrestha-Debug](https://github.com/Binod-Shrestha-Debug)

**Project Repository:** [Todo_App_project](https://github.com/Binod-Shrestha-Debug/Todo_App_project)