# Quick Start Guide - Django Wallet API

## 🚀 Get Started in 5 Minutes

### Prerequisites
- Python 3.8 or higher
- Git

### Step 1: Clone and Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd django_wallet

# Run the automated setup script
python setup.py
```

### Step 2: Start the Server
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

# Navigate to project directory
cd walletsite

# Start the development server
python manage.py runserver
```

### Step 3: Test the API
Open your browser and visit:
- **API Documentation**: http://localhost:8000/docs/
- **API Test**: http://localhost:8000/api/test/

## 🌐 Live Demo
- **API Documentation**: https://ammr-django-wallet.onrender.com/docs/
- **API Test**: https://ammr-django-wallet.onrender.com/api/test/

## 📚 Quick API Examples

### Test API
```bash
curl http://localhost:8000/api/test/
```

### Credit Money
```bash
curl -X POST http://localhost:8000/api/wallet/update/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "amount": "100.00", "transaction_type": "credit", "description": "Test deposit"}'
```

### Get Users
```bash
curl http://localhost:8000/api/users/
```

## 🆘 Need Help?
- Check the full [README.md](README.md) for detailed instructions
- Review [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md) for technical details
- The API documentation at `/docs/` provides interactive examples

## ✅ What's Working
- ✅ User management
- ✅ Wallet balance tracking
- ✅ Transaction history
- ✅ Credit/debit operations
- ✅ RESTful API design
- ✅ Interactive documentation
- ✅ CORS support
- ✅ Error handling

---
**Ready to go!** Your Django Wallet API is now running locally. 🎉
