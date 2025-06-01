# Content Management System

A comprehensive full-stack content management system built with Django (backend) and Next.js (frontend), featuring GraphQL API integration, JWT authentication, role-based access control, and Celery task processing.

## Project Structure

```
├── backend/                 # Django backend
│   ├── content/            # Content management app
│   ├── backend/            # Django project settings
│   ├── users/              # User management & authentication
│   ├── recommendations/    # Recommendations feature
│   └── celery_app/         # Celery task processing
└── frontend/               # Next.js frontend
    ├── src/
    │   ├── app/            # Next.js 13+ app directory
    │   │   ├── dashboard/  # Admin dashboard pages
    │   │   ├── preview/    # Content preview system
    │   │   └── auth/       # Authentication pages
    │   ├── components/     # Reusable React components
    │   ├── lib/            # Apollo client & API utilities
    │   ├── context/        # React context providers
    │   ├── config/         # Environment configuration
    │   └── types/          # TypeScript type definitions
    └── public/
```

## Features

### Backend (Django)
- **GraphQL API** with Graphene-Django
- **JWT Authentication** with refresh token support
- **Role-Based Access Control** (Admin, Editor, Viewer)
- **Content Management** with rich text support
- **Publishing Workflow** with draft/published states
- **Celery Task Processing** for background jobs
- **Content Preview System** with secure tokens
- **SEO Optimization** with meta tags and slugs
- **User Management** with permission controls
- **CORS Support** for frontend integration

### Frontend (Next.js + TypeScript)
- **Modern Next.js 13+** with app directory structure
- **Comprehensive Dashboard** for content management
- **Apollo Client** for GraphQL integration
- **JWT Authentication** with automatic token refresh
- **Role-Based UI** with permission-based access
- **Rich Text Editor** with TinyMCE integration
- **Content Preview** with live editing capabilities
- **User Management** for admin users
- **Task Monitoring** for Celery integration
- **Responsive Design** with Tailwind CSS
- **Error Handling** with custom error pages
- **Type Safety** with comprehensive TypeScript

### Content Management Features
- **CRUD Operations** for all content types
- **Rich Text Editing** with media upload support
- **SEO Management** with meta tags and descriptions
- **Content Scheduling** with publish/unpublish dates
- **Content Preview** with secure token-based access
- **Search & Filtering** with advanced query options
- **Bulk Operations** for content management
- **Content Versioning** and revision history
- **Permission-Based Access** by user roles

### User Management Features
- **User Registration & Login** with JWT tokens
- **Role Assignment** (Admin, Editor, Viewer)
- **Permission Controls** for resource access
- **User Profile Management** with preferences
- **Activity Monitoring** and audit logs
- **Account Status Control** (active/inactive)

### Task Processing Features
- **Celery Integration** for background tasks
- **Task Monitoring** with real-time status
- **Queue Management** with health indicators
- **Task History** and result tracking
- **Auto-Refresh** dashboard for live updates

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.8+** (Download from [python.org](https://www.python.org/downloads/))
- **Node.js 18+** and **npm** (Download from [nodejs.org](https://nodejs.org/))
- **Redis Server** (Required for Celery task processing)
  - **macOS:** `brew install redis`
  - **Ubuntu/Debian:** `sudo apt-get install redis-server`
  - **Windows:** Download from [redis.io](https://redis.io/download) or use WSL
- **Git** (Download from [git-scm.com](https://git-scm.com/))

## Quick Start Guide

### 1. Clone the Repository

```bash
git clone https://github.com/omar-bouhdida/Web-Programming-in-Python-Exam.git
cd Nest.Js-Django
```

### 2. Backend Setup (Django)

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate a Python virtual environment:**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   # venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser account:**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user account.

6. **Start Redis server (required for Celery):**
   ```bash
   # On macOS/Linux:
   redis-server
   # On Windows (if installed directly):
   # redis-server.exe
   ```

7. **Start the Celery worker (in a new terminal):**
   ```bash
   # Make sure you're in the backend directory with virtual environment activated
   cd backend
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   celery -A backend worker --loglevel=info
   ```

8. **Start the Django development server (in another new terminal):**
   ```bash
   # Make sure you're in the backend directory with virtual environment activated
   cd backend
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   python manage.py runserver
   ```

   The backend will be available at:
   - **Main API:** http://localhost:8000
   - **GraphQL Playground:** http://localhost:8000/graphql/
   - **Django Admin:** http://localhost:8000/admin/

### 3. Frontend Setup (Next.js)

1. **Open a new terminal and navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Create environment configuration file:**
   ```bash
   # Create a .env.local file with the following content:
   cp .env.example .env.local  # if .env.example exists, otherwise create manually
   ```
   
   Create `.env.local` file with the following content:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   NEXT_PUBLIC_GRAPHQL_URL=http://localhost:8000/graphql/
   NEXT_PUBLIC_APP_NAME=Content Management System
   NEXT_PUBLIC_APP_DESCRIPTION=A comprehensive CMS platform
   NEXT_PUBLIC_DEFAULT_PAGINATION_LIMIT=10
   ```

4. **Start the Next.js development server:**
   ```bash
   npm run dev
   ```

   The frontend will be available at: http://localhost:3000

## Detailed Installation Instructions

### System Requirements

- **Operating System:** macOS, Linux, or Windows 10/11
- **RAM:** Minimum 4GB, recommended 8GB+
- **Storage:** At least 2GB free space for dependencies and project files

### Installing Prerequisites

#### Python 3.8+ Installation

1. **Download Python:** Visit [python.org](https://www.python.org/downloads/) and download the latest Python 3.8+ version
2. **Install Python:** Run the installer and make sure to check "Add Python to PATH"
3. **Verify installation:**
   ```bash
   python --version
   pip --version
   ```

#### Node.js and npm Installation

1. **Download Node.js:** Visit [nodejs.org](https://nodejs.org/) and download the LTS version
2. **Install Node.js:** Run the installer (npm comes bundled with Node.js)
3. **Verify installation:**
   ```bash
   node --version
   npm --version
   ```

#### Redis Installation

**macOS (using Homebrew):**
```bash
brew install redis
brew services start redis
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install redis-server
sudo systemctl start redis-server
sudo systemctl enable redis-server
```

**Windows:**
- Download Redis from [releases page](https://github.com/microsoftarchive/redis/releases)
- Or use WSL (Windows Subsystem for Linux) and follow Linux instructions

**Verify Redis installation:**
```bash
redis-cli ping
# Should return: PONG
```

### Running the Complete Application

1. **Start Redis server** (if not already running)
2. **Start the Django backend** (with virtual environment activated)
3. **Start the Celery worker** (in a separate terminal)
4. **Start the Next.js frontend** (in a separate terminal)

You should now have:
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **GraphQL Playground:** http://localhost:8000/graphql/
- **Django Admin:** http://localhost:8000/admin/

### Creating Sample Data (Optional)

After setting up the backend, you can create some sample content:

```bash
# In the backend directory with virtual environment activated
python manage.py shell
```

Then run this Python code:
```python
from django.utils import timezone
from content.models import PageContent
from users.models import CustomUser

# Get the superuser you created
user = CustomUser.objects.filter(is_superuser=True).first()

# Create sample content
PageContent.objects.create(
    title="Welcome to Our CMS",
    body="<p>Welcome to our comprehensive content management system! This is a sample page to get you started.</p>",
    meta_description="Welcome page for our CMS platform",
    is_published=True,
    publish_date=timezone.now(),
    author=user
)

print("Sample content created successfully!")
```

Type `exit()` to leave the Django shell.

## Usage

### Accessing the Application

1. **Public Pages:**
   - **Home:** http://localhost:3000 - Landing page
   - **Login:** http://localhost:3000/auth/login - User authentication
   - **Register:** http://localhost:3000/auth/register - New user registration

2. **Dashboard (Authenticated Users):**
   - **Overview:** http://localhost:3000/dashboard - Main dashboard with statistics
   - **Content Management:** http://localhost:3000/dashboard/content - Content CRUD operations
   - **Content Creation:** http://localhost:3000/dashboard/content/create - Create new content
   - **User Management:** http://localhost:3000/dashboard/users - Admin-only user management
   - **Task Monitor:** http://localhost:3000/dashboard/tasks - Celery task monitoring

3. **Backend Services:**
   - **GraphQL Playground:** http://localhost:8000/graphql/ - API testing interface
   - **Django Admin:** http://localhost:8000/admin/ - Django administration
   - **API Endpoints:** http://localhost:8000/api/ - REST API endpoints

### Authentication Flow

1. **Register/Login:** Use the authentication pages to create an account or log in
2. **JWT Tokens:** The system automatically manages access and refresh tokens
3. **Role-Based Access:** Different features are available based on user roles:
   - **Admin:** Full access to all features including user management
   - **Editor:** Content creation, editing, and management capabilities
   - **Viewer:** Read-only access to content and basic dashboard

### Content Management Workflow

1. **Create Content:**
   - Navigate to Dashboard → Content → Create New
   - Use the rich text editor to compose content
   - Add SEO metadata (title, description, keywords)
   - Set publication status and schedule
   - Preview content before publishing

2. **Edit Content:**
   - Browse content in the content management page
   - Click edit on any content item
   - Make changes and preview before saving
   - Manage publication status and scheduling

3. **Content Preview:**
   - Use preview mode during editing
   - Generate shareable preview links
   - Public preview access with secure tokens

### User Management (Admin Only)

1. **User Overview:**
   - View all registered users and their roles
   - Monitor user activity and status
   - Access user statistics and metrics

2. **Role Management:**
   - Assign and modify user roles
   - Control permissions and access levels
   - Activate or deactivate user accounts

### Task Monitoring

1. **Celery Integration:**
   - Monitor background task execution
   - View task status and results
   - Track queue health and performance
   - Auto-refreshing dashboard for real-time updates

## API Documentation

### GraphQL Queries

**Authentication:**
```graphql
mutation Login($username: String!, $password: String!) {
  login(username: $username, password: $password) {
    access
    refresh
    user {
      id
      username
      email
      role
    }
  }
}
```

**Content Operations:**

**Get All Content (with filtering):**
```graphql
query GetContent($isPublished: Boolean, $search: String, $limit: Int, $offset: Int) {
  allPageContents(isPublished: $isPublished, search: $search, limit: $limit, offset: $offset) {
    edges {
      node {
        id
        title
        slug
        body
        metaDescription
        publishDate
        isPublished
        author {
          username
          email
        }
        createdAt
        updatedAt
      }
    }
    totalCount
  }
}
```

**Get Content by ID:**
```graphql
query GetContent($id: ID!) {
  pageContent(id: $id) {
    id
    title
    slug
    body
    metaDescription
    keywords
    publishDate
    isPublished
    author {
      id
      username
      email
    }
    createdAt
    updatedAt
  }
}
```

**Create Content:**
```graphql
mutation CreateContent($input: PageContentInput!) {
  createPageContent(input: $input) {
    pageContent {
      id
      title
      slug
      body
      metaDescription
      isPublished
      publishDate
    }
    success
    errors
  }
}
```

**Update Content:**
```graphql
mutation UpdateContent($id: ID!, $input: PageContentInput!) {
  updatePageContent(id: $id, input: $input) {
    pageContent {
      id
      title
      slug
      body
      metaDescription
      isPublished
      publishDate
    }
    success
    errors
  }
}
```

**Delete Content:**
```graphql
mutation DeleteContent($id: ID!) {
  deletePageContent(id: $id) {
    success
    errors
  }
}
```

**User Management:**
```graphql
query GetUsers($role: String, $isActive: Boolean) {
  allUsers(role: $role, isActive: $isActive) {
    edges {
      node {
        id
        username
        email
        firstName
        lastName
        role
        isActive
        dateJoined
        lastLogin
      }
    }
    totalCount
  }
}
```

**Task Monitoring:**
```graphql
query GetTasks($status: String, $taskType: String) {
  celeryTasks(status: $status, taskType: $taskType) {
    edges {
      node {
        id
        taskId
        name
        status
        result
        createdAt
        startedAt
        completedAt
        retries
      }
    }
    totalCount
  }
}
```

### REST API Endpoints

**Authentication:**
- `POST /api/auth/login/` - User login
- `POST /api/auth/register/` - User registration
- `POST /api/auth/refresh/` - Token refresh
- `POST /api/auth/logout/` - User logout

**Content Management:**
- `GET /api/content/` - List all content
- `POST /api/content/` - Create new content
- `GET /api/content/{id}/` - Get specific content
- `PUT /api/content/{id}/` - Update content
- `DELETE /api/content/{id}/` - Delete content
- `POST /api/content/{id}/preview/` - Generate preview token

**User Management:**
- `GET /api/users/` - List users (admin only)
- `GET /api/users/{id}/` - Get user details
- `PUT /api/users/{id}/` - Update user
- `POST /api/users/{id}/activate/` - Activate user
- `POST /api/users/{id}/deactivate/` - Deactivate user

**Task Management:**
- `GET /api/tasks/` - List Celery tasks
- `GET /api/tasks/{id}/` - Get task details
- `POST /api/tasks/{id}/retry/` - Retry failed task



## Architecture & Technology Stack

### Backend Technologies
- **Django 5.2+** - Web framework
- **Graphene-Django** - GraphQL implementation
- **Django REST Framework** - REST API support
- **Django CORS Headers** - Cross-origin resource sharing
- **Celery** - Background task processing
- **Redis** - Message broker for Celery
- **PostgreSQL** - Production database (SQLite for development)
- **JWT Authentication** - Token-based authentication
- **Python 3.8+** - Programming language

### Frontend Technologies
- **Next.js 13+** - React framework with app directory
- **TypeScript** - Type-safe JavaScript
- **Apollo Client** - GraphQL client with caching
- **Tailwind CSS** - Utility-first CSS framework
- **TinyMCE** - Rich text editor
- **React Hook Form** - Form handling
- **Lucide React** - Icon library
- **Next.js Router** - Client-side routing

## Configuration

### Environment Variables

**Backend (.env):**
```env
DEBUG=True
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/cms_db
REDIS_URL=redis://localhost:6379/0
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
JWT_SECRET_KEY=your_jwt_secret_here
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
```

**Frontend (.env.local):**
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_GRAPHQL_URL=http://localhost:8000/graphql/
NEXT_PUBLIC_APP_NAME=Content Management System
NEXT_PUBLIC_APP_DESCRIPTION=A comprehensive CMS platform
NEXT_PUBLIC_DEFAULT_PAGINATION_LIMIT=10
NEXT_PUBLIC_TINYMCE_API_KEY=your_tinymce_api_key_here
```

## Development Guidelines

### Adding New Features

1. **Backend Development:**
   - Create new Django apps for major features
   - Define models with proper relationships
   - Create GraphQL schema and resolvers
   - Add REST API endpoints if needed
   - Write tests for all functionality
   - Update documentation

2. **Frontend Development:**
   - Create reusable components in `/components`
   - Add pages in `/app` directory structure
   - Define TypeScript types in `/types`
   - Update Apollo queries and mutations
   - Implement proper error handling
   - Add loading states and user feedback

### Code Style & Standards

- **Backend:** Follow Django best practices and PEP 8
- **Frontend:** Use TypeScript strict mode and ESLint rules
- **Git:** Use conventional commits for clear history
- **Testing:** Write unit tests for components and API endpoints
- **Documentation:** Keep README and inline docs updated

### Security Considerations

- **Authentication:** JWT tokens with refresh mechanism
- **Authorization:** Role-based access control
- **Input Validation:** Server-side validation for all inputs
- **CSRF Protection:** Django CSRF tokens for forms
- **CORS:** Properly configured origins
- **Environment Variables:** Sensitive data in environment files
- **Preview Tokens:** Secure token-based content preview

## Testing

### Backend Testing
```bash
cd backend
python manage.py test
```

### Frontend Testing
```bash
cd frontend
npm run test
npm run test:coverage
```

### End-to-End Testing
```bash
cd frontend
npm run e2e
```

## Deployment

### Production Setup

1. **Database Setup:**
   - Use PostgreSQL for production
   - Configure connection pooling
   - Set up database backups

2. **Backend Deployment:**
   - Use Gunicorn as WSGI server
   - Configure Nginx as reverse proxy
   - Set up Celery workers and beat scheduler
   - Configure Redis for Celery and caching

3. **Frontend Deployment:**
   - Build optimized production bundle
   - Deploy to Vercel, Netlify, or similar platform
   - Configure environment variables
   - Set up CDN for static assets

4. **Environment Configuration:**
   - Set DEBUG=False
   - Configure proper SECRET_KEY
   - Set up SSL certificates
   - Configure logging and monitoring

## Troubleshooting Installation Issues

### Common Backend Issues

**1. Python/pip command not found:**
- **Solution:** Make sure Python is installed and added to your system PATH
- **Windows:** Reinstall Python with "Add Python to PATH" checked
- **macOS/Linux:** Use `python3` and `pip3` instead of `python` and `pip`

**2. Virtual environment activation fails:**
- **Solution:** 
  ```bash
  # Try absolute path
  source /full/path/to/venv/bin/activate
  
  # Or recreate the virtual environment
  rm -rf venv
  python -m venv venv
  source venv/bin/activate
  ```

**3. Redis connection errors:**
- **Solution:** Make sure Redis server is running
  ```bash
  # Check if Redis is running
  redis-cli ping
  
  # Start Redis if not running
  # macOS: brew services start redis
  # Linux: sudo systemctl start redis-server
  ```

**4. Celery worker connection issues:**
- **Solution:** Ensure Redis is running and accessible
- Check CELERY_BROKER_URL in Django settings matches your Redis configuration

**5. Database migration errors:**
- **Solution:** Delete database and recreate migrations
  ```bash
  rm db.sqlite3
  python manage.py makemigrations
  python manage.py migrate
  ```

**6. Permission denied errors (macOS/Linux):**
- **Solution:** Use virtual environment and avoid using `sudo` with pip
- If needed, use: `pip install --user package_name`

### Common Frontend Issues

**1. Node.js/npm command not found:**
- **Solution:** Install Node.js from [nodejs.org](https://nodejs.org/)
- Restart terminal after installation

**2. npm install fails with permission errors:**
- **Solution:** 
  ```bash
  # Clear npm cache
  npm cache clean --force
  
  # Delete node_modules and package-lock.json
  rm -rf node_modules package-lock.json
  npm install
  ```

**3. Port 3000 already in use:**
- **Solution:** 
  ```bash
  # Kill process using port 3000
  lsof -ti:3000 | xargs kill -9
  
  # Or use a different port
  npm run dev -- -p 3001
  ```

**4. Module not found errors:**
- **Solution:** Clear cache and reinstall dependencies
  ```bash
  rm -rf node_modules package-lock.json .next
  npm install
  npm run dev
  ```

**5. Environment variables not loading:**
- **Solution:** Ensure `.env.local` file is in the frontend root directory
- Restart the development server after creating/modifying environment variables

### Network and CORS Issues

**1. CORS errors when frontend calls backend:**
- **Solution:** Verify CORS settings in Django settings.py
- Make sure `http://localhost:3000` is in `CORS_ALLOWED_ORIGINS`

**2. GraphQL endpoint not accessible:**
- **Solution:** Check that Django server is running on port 8000
- Visit http://localhost:8000/graphql/ directly in browser

**3. API connection refused:**
- **Solution:** Ensure both frontend and backend are running
- Check that API URLs in frontend environment variables are correct

### Platform-Specific Issues

**Windows:**
- Use Command Prompt or PowerShell as administrator if needed
- Use `python` instead of `python3` and `pip` instead of `pip3`
- For virtual environment activation: `venv\Scripts\activate`

**macOS:**
- Use Homebrew for installing Redis and other dependencies
- May need to use `python3` and `pip3` explicitly

**Linux:**
- Use package manager (apt, yum, etc.) for system dependencies
- May need `sudo` for system-wide package installations

### Getting Additional Help

If you encounter issues not covered here:

1. **Check the terminal/console output** for specific error messages
2. **Verify all prerequisites** are properly installed
3. **Ensure all services are running** (Django, Redis, Node.js)
4. **Check firewall/antivirus** settings that might block local servers
5. **Try restarting all services** and your development environment

For persistent issues, please check the project's issue tracker or create a new issue with:
- Your operating system and version
- Python and Node.js versions
- Complete error messages
- Steps you've already tried

## Advanced Troubleshooting

### Common Issues

**Backend:**
- **CORS Errors:** Check CORS_ALLOWED_ORIGINS setting
- **Database Connection:** Verify database settings and connection
- **Celery Tasks:** Ensure Redis is running and properly configured
- **Authentication:** Check JWT secret keys and token expiration

**Frontend:**
- **API Connection:** Verify API URL configuration
- **Authentication:** Check token storage and refresh logic
- **Build Errors:** Ensure all dependencies are installed
- **Type Errors:** Update TypeScript types after API changes

### Debug Mode

Enable debug logging:

**Backend:**
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

**Frontend:**
```bash
NEXT_PUBLIC_DEBUG=true npm run dev
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support and questions:
- Create an issue in the GitHub repository
- Check the documentation and troubleshooting section
- Review the API documentation and examples

## Roadmap

- [ ] Advanced content versioning system
- [ ] Multi-tenant support
- [ ] Advanced SEO optimization tools
- [ ] Content workflow and approval process
- [ ] Advanced analytics and reporting
- [ ] Plugin system for extensibility
- [ ] Mobile app with React Native
- [ ] Advanced caching strategies
- [ ] Content import/export functionality
- [ ] Advanced user role management
- SQLite (development)

### Frontend
- React 19.1.0
- TypeScript
- Apollo Client
- React Router DOM
- Styled Components
- Lucide React (icons)

## Troubleshooting

### Common Issues

1. **CORS Errors:**
   - Ensure Django server is running on port 8000
   - Check CORS settings in Django settings

2. **GraphQL Connection Issues:**
   - Verify GraphQL endpoint is accessible at http://localhost:8000/graphql/
   - Check network tab for request details

3. **Frontend Build Issues:**
   - Delete `node_modules` and run `npm install` again
   - Check for TypeScript errors

4. **Backend Import Errors:**
   - Ensure virtual environment is activated
   - Verify all dependencies are installed

### Getting Help
- Check the browser console for JavaScript errors
- Check Django server logs for backend errors
- Use GraphQL playground to test queries
- Verify sample content exists in the database

## Next Steps

Consider adding:
- User authentication and authorization
- Content editing interface in the frontend
- Image upload and management
- Full-text search capabilities
- Content categories and tags
- Comments system
- SEO optimization features
