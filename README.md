# Django Wallet API

A complete REST API for wallet management system built with Django and Django REST Framework.

## 🌟 Features

- **User Management**: Create and manage users
- **Wallet Balance Tracking**: Real-time balance updates
- **Transaction History**: Complete transaction records
- **Credit/Debit Operations**: Secure money transactions
- **RESTful API Design**: Standard HTTP methods
- **JSON Response Format**: Consistent API responses
- **Error Handling**: Comprehensive error management
- **CORS Enabled**: Cross-origin resource sharing support
- **API Documentation**: Interactive documentation

## 🚀 Live Demo

**API Documentation**: https://ammr-django-wallet.onrender.com/docs/

**API Test Endpoint**: https://ammr-django-wallet.onrender.com/api/test/

## 🛠️ Technology Stack

- **Backend**: Django 4.2.23
- **API Framework**: Django REST Framework 3.16.1
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Documentation**: Swagger/OpenAPI
- **CORS**: django-cors-headers
- **Deployment**: Render.com

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)
- Git

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd django_wallet
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
cd walletsite
pip install -r requirements.txt
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## 📚 API Endpoints

### Base URL
```
https://ammr-django-wallet.onrender.com
```

### Available Endpoints

#### 1. Test API
- **URL**: `/api/test/`
- **Method**: `GET`
- **Description**: Test endpoint to verify API is working
- **Response**: JSON with API status and available endpoints

#### 2. Get All Users
- **URL**: `/api/users/`
- **Method**: `GET`
- **Description**: Get all users in the system
- **Response**: List of users with their details

#### 3. Update Wallet Balance
- **URL**: `/api/wallet/update/`
- **Method**: `POST`
- **Description**: Credit or debit money from user wallet
- **Request Body**:
```json
{
    "user_id": 1,
    "amount": "100.50",
    "transaction_type": "credit",
    "description": "Deposit"
}
```
- **Response**: Updated wallet information

#### 4. Get User Transactions
- **URL**: `/api/transactions/{user_id}/`
- **Method**: `GET`
- **Description**: Get all transactions for a specific user
- **Response**: List of transactions for the user

#### 5. API Documentation
- **URL**: `/docs/`
- **Method**: `GET`
- **Description**: Interactive API documentation

## 🔄 API Usage Examples

### Using curl

#### Test API
```bash
curl https://ammr-django-wallet.onrender.com/api/test/
```

#### Get All Users
```bash
curl https://ammr-django-wallet.onrender.com/api/users/
```

#### Credit Money
```bash
curl -X POST https://ammr-django-wallet.onrender.com/api/wallet/update/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "amount": "100.00", "transaction_type": "credit", "description": "Test deposit"}'
```

#### Debit Money
```bash
curl -X POST https://ammr-django-wallet.onrender.com/api/wallet/update/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "amount": "50.00", "transaction_type": "debit", "description": "Test withdrawal"}'
```

#### Get User Transactions
```bash
curl https://ammr-django-wallet.onrender.com/api/transactions/1/
```

### Using JavaScript/Fetch

#### Test API
```javascript
fetch('https://ammr-django-wallet.onrender.com/api/test/')
  .then(response => response.json())
  .then(data => console.log(data));
```

#### Credit Money
```javascript
fetch('https://ammr-django-wallet.onrender.com/api/wallet/update/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    user_id: 1,
    amount: "100.00",
    transaction_type: "credit",
    description: "Test deposit"
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## 📊 Data Models

### User Model
```python
class User:
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
```

### Wallet Model
```python
class Wallet:
    id: int
    user: User (OneToOneField)
    balance: Decimal
    created_at: DateTime
    updated_at: DateTime
```

### Transaction Model
```python
class Transaction:
    id: int
    user: User (ForeignKey)
    amount: Decimal
    transaction_type: str (choices: 'credit', 'debit')
    description: str
    created_at: DateTime
```

## 🔒 Security Features

- **Input Validation**: All inputs are validated
- **SQL Injection Protection**: Django ORM prevents SQL injection
- **CSRF Protection**: Built-in CSRF protection
- **CORS Configuration**: Proper CORS headers
- **Error Handling**: Comprehensive error responses

## 🚀 Deployment

This project is deployed on Render.com with the following configuration:

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn config.wsgi:application`
- **Environment**: Python 3.12
- **Database**: PostgreSQL (provided by Render)

## 📝 Environment Variables

Create a `.env` file in the `walletsite` directory:

```env
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=your-database-url
ALLOWED_HOSTS=.onrender.com,.vercel.app,localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=https://*.onrender.com,https://*.vercel.app
```

## 🧪 Testing

Run the Django test suite:

```bash
python manage.py test
```

## 📈 API Response Examples

### Successful Response
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

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**AMMR** - Django Wallet API Project

## 📞 Support

For support and questions, please contact the project maintainer.

---

**Note**: This is a demonstration project for educational purposes. For production use, additional security measures should be implemented.
