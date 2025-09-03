# Django Wallet API - Project Documentation

## 📋 Project Overview

The Django Wallet API is a comprehensive REST API for managing digital wallets, user accounts, and financial transactions. It provides a secure and scalable solution for wallet management with real-time balance tracking and transaction history.

## 🏗️ Architecture

### Technology Stack
- **Backend Framework**: Django 4.2.23
- **API Framework**: Django REST Framework 3.16.1
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Documentation**: Swagger/OpenAPI with drf-yasg
- **CORS**: django-cors-headers 4.3.1
- **Deployment**: Render.com with Gunicorn
- **Static Files**: WhiteNoise for static file serving

### Project Structure
```
django_wallet/
├── README.md                    # Project overview and setup instructions
├── setup.py                     # Automated setup script
├── PROJECT_DOCUMENTATION.md     # This file - detailed documentation
├── .gitignore                   # Git ignore rules
├── walletsite/                  # Main Django project
│   ├── manage.py               # Django management script
│   ├── requirements.txt         # Python dependencies
│   ├── config/                 # Django settings
│   │   ├── settings.py         # Main settings file
│   │   ├── urls.py            # Main URL configuration
│   │   ├── wsgi.py            # WSGI configuration
│   │   └── asgi.py            # ASGI configuration
│   ├── wallet/                 # Main app
│   │   ├── models.py          # Database models
│   │   ├── views.py           # API views
│   │   ├── serializers.py     # DRF serializers
│   │   ├── urls.py            # App URL patterns
│   │   └── tests.py           # Unit tests
│   ├── Dockerfile             # Docker configuration
│   ├── render.yaml            # Render deployment config
│   └── runtime.txt            # Python version specification
```

## 🗄️ Database Design

### User Model
```python
class User(models.Model):
    # Inherits from Django's AbstractUser
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
```

### Wallet Model
```python
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### Transaction Model
```python
class Transaction(models.Model):
    CREDIT = 'credit'
    DEBIT = 'debit'
    TRANSACTION_TYPES = [
        (CREDIT, 'Credit'),
        (DEBIT, 'Debit'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
```

## 🔌 API Endpoints

### Base URL
```
https://ammr-django-wallet.onrender.com
```

### Endpoint Specifications

#### 1. Test API
- **URL**: `/api/test/`
- **Method**: `GET`
- **Description**: Health check and API status
- **Response**: JSON with API status and available endpoints
- **Status Codes**: 200

#### 2. User Management
- **URL**: `/api/users/`
- **Method**: `GET`
- **Description**: Retrieve all users
- **Response**: List of user objects
- **Status Codes**: 200, 400, 500

#### 3. Wallet Operations
- **URL**: `/api/wallet/update/`
- **Method**: `POST`
- **Description**: Credit or debit wallet balance
- **Request Body**:
  ```json
  {
    "user_id": 1,
    "amount": "100.50",
    "transaction_type": "credit|debit",
    "description": "Transaction description"
  }
  ```
- **Response**: Updated wallet information
- **Status Codes**: 200, 400, 404

#### 4. Transaction History
- **URL**: `/api/transactions/{user_id}/`
- **Method**: `GET`
- **Description**: Get user's transaction history
- **Parameters**: `user_id` (path parameter)
- **Response**: List of transaction objects
- **Status Codes**: 200, 404, 500

#### 5. Documentation
- **URL**: `/docs/`
- **Method**: `GET`
- **Description**: Interactive API documentation
- **Response**: HTML documentation page

## 🔒 Security Implementation

### Input Validation
- All API inputs are validated using Django REST Framework serializers
- Amount validation ensures positive decimal values
- Transaction type validation restricts to 'credit' or 'debit'
- User ID validation ensures user exists

### Database Security
- SQL injection protection through Django ORM
- Atomic transactions for wallet updates
- Proper foreign key constraints
- Database-level constraints

### API Security
- CSRF protection enabled
- CORS configuration for cross-origin requests
- Input sanitization
- Error handling without exposing sensitive information

### Error Handling
```python
# Example error response
{
    "detail": "Insufficient balance."
}
```

## 🚀 Deployment Configuration

### Render.com Configuration
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn config.wsgi:application`
- **Environment**: Python 3.12
- **Auto-deploy**: Enabled on git push

### Environment Variables
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=postgresql://user:pass@host:port/dbname
ALLOWED_HOSTS=.onrender.com,.vercel.app,localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=https://*.onrender.com,https://*.vercel.app
```

### Docker Configuration
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application"]
```

## 📊 API Response Formats

### Success Response (Wallet Update)
```json
{
    "id": 1,
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User"
    },
    "balance": "150.00",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T12:00:00Z"
}
```

### Error Response
```json
{
    "detail": "Insufficient balance."
}
```

### List Response (Users)
```json
[
    {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "first_name": "John",
        "last_name": "Doe"
    },
    {
        "id": 2,
        "username": "user2",
        "email": "user2@example.com",
        "first_name": "Jane",
        "last_name": "Smith"
    }
]
```

## 🧪 Testing Strategy

### Unit Tests
- Model validation tests
- API endpoint tests
- Serializer tests
- Business logic tests

### Integration Tests
- Database transaction tests
- API workflow tests
- Error handling tests

### Test Commands
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test wallet

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 📈 Performance Considerations

### Database Optimization
- Proper indexing on frequently queried fields
- Efficient query patterns using select_related and prefetch_related
- Database connection pooling

### API Optimization
- Pagination for large datasets
- Caching for frequently accessed data
- Efficient serialization

### Monitoring
- Application performance monitoring
- Database query monitoring
- Error tracking and logging

## 🔄 Development Workflow

### Local Development
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Run migrations
5. Start development server

### Code Quality
- PEP 8 style guide compliance
- Type hints where appropriate
- Comprehensive docstrings
- Code reviews

### Version Control
- Feature branch workflow
- Meaningful commit messages
- Pull request reviews

## 🚨 Error Handling

### Common Error Scenarios
1. **Insufficient Balance**: User tries to debit more than available
2. **User Not Found**: Invalid user_id provided
3. **Invalid Amount**: Non-positive or non-numeric amount
4. **Invalid Transaction Type**: Non-credit/debit transaction type

### Error Response Format
```json
{
    "detail": "Error message description"
}
```

## 📚 API Documentation

### Interactive Documentation
- Swagger UI at `/swagger/`
- ReDoc at `/redoc/`
- Custom documentation at `/docs/`

### Code Examples
- curl commands for all endpoints
- JavaScript/fetch examples
- Python requests examples

## 🔧 Configuration Management

### Settings Structure
- Environment-based configuration
- Separate settings for development and production
- Secure secret management
- Database configuration flexibility

### Environment Variables
- Database connection strings
- Secret keys
- Debug settings
- Allowed hosts configuration

## 📊 Monitoring and Logging

### Application Logging
- Request/response logging
- Error logging
- Performance metrics
- Database query logging

### Health Checks
- API health endpoint
- Database connectivity checks
- External service monitoring

## 🔮 Future Enhancements

### Planned Features
1. **Authentication**: JWT token-based authentication
2. **Authorization**: Role-based access control
3. **Rate Limiting**: API rate limiting
4. **Webhooks**: Real-time notifications
5. **Analytics**: Transaction analytics and reporting
6. **Multi-currency**: Support for multiple currencies
7. **Mobile API**: Mobile-optimized endpoints

### Scalability Considerations
- Horizontal scaling with load balancers
- Database sharding strategies
- Caching layer implementation
- Microservices architecture

## 📞 Support and Maintenance

### Documentation
- Comprehensive README
- API documentation
- Code comments
- Setup instructions

### Maintenance
- Regular dependency updates
- Security patches
- Performance monitoring
- Backup strategies

---

**Note**: This documentation is maintained alongside the codebase and should be updated as the project evolves.
