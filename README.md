# ECommerce Website - Django

A complete, production-ready ecommerce platform built with Django, featuring product management, shopping cart, secure checkout, and Stripe payment integration.

## 🚀 Features

### ✅ Core Features
- **Product Catalog**: Browse products with categories, search, and filtering
- **Product Details**: Detailed product pages with images and descriptions
- **Shopping Cart**: Add/remove items, update quantities
- **User Authentication**: Register, login, profile management
- **Order Management**: Create orders, track status, view history
- **Admin Dashboard**: Full Django admin for product and order management

### 💳 Payment
- **Stripe Integration**: Secure payment processing
- **Order Confirmation**: Email-ready order receipts

### 📦 Additional Features
- Product reviews and ratings
- Responsive design with Bootstrap 5
- Order tracking and history
- Inventory management
- Professional UI/UX

## 📋 Requirements

- Python 3.8+
- Django 4.2+
- SQLite3 (or PostgreSQL for production)

## 🔧 Installation

### 1. Clone and Setup
```bash
cd ECOMMDJ
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Setup
```bash
python manage.py migrate
```

### 4. Create Superuser
```bash
python manage.py createsuperuser
```

### 5. Add Sample Data (Optional)
```bash
python manage.py shell
```

```python
from products.models import Category, Product
from decimal import Decimal

# Create categories
electronics = Category.objects.create(name='Electronics', slug='electronics')
clothing = Category.objects.create(name='Clothing', slug='clothing')

# Create products
Product.objects.create(
    name='Laptop Pro',
    slug='laptop-pro',
    description='High-performance laptop',
    price=Decimal('999.99'),
    category=electronics,
    stock=10,
    is_active=True
)

exit()
```

### 6. Run Server
```bash
python manage.py runserver
```

Visit `http://localhost:8000`

## 🏪 Admin Access

1. Navigate to `http://localhost:8000/admin`
2. Login with superuser credentials
3. Add products, categories, and manage orders

## 📁 Project Structure

```
ECOMMDJ/
├── manage.py
├── requirements.txt
├── ecommerce/           # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/            # Product app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── cart/                # Shopping cart app
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── orders/              # Order management app
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── accounts/            # User authentication app
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── templates/           # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── products/
│   ├── cart/
│   ├── orders/
│   └── accounts/
├── static/              # CSS, JS, images
└── media/               # User-uploaded files
```

## 🛣️ URL Routes

### Public Routes
- `/` - Home page
- `/products/` - Product listing
- `/product/<slug>/` - Product details
- `/account/register/` - User registration
- `/account/login/` - User login
- `/account/logout/` - User logout

### Cart Routes
- `/cart/` - View shopping cart
- `/cart/add/<id>/` - Add to cart
- `/cart/update/<id>/` - Update quantity
- `/cart/remove/<id>/` - Remove from cart

### Order Routes (Requires Login)
- `/orders/checkout/` - Checkout page
- `/orders/payment/<id>/` - Payment page
- `/orders/confirmation/<id>/` - Order confirmation
- `/orders/list/` - Order history
- `/orders/detail/<id>/` - Order details

## 💳 Stripe Setup

1. Create a [Stripe account](https://stripe.com)
2. Get your API keys from Dashboard
3. Update `ecommerce/settings.py`:
   ```python
   STRIPE_PUBLIC_KEY = 'pk_test_your_key_here'
   STRIPE_SECRET_KEY = 'sk_test_your_key_here'
   ```

### Test Card Numbers
- **Success**: 4242 4242 4242 4242
- **Decline**: 4000 0000 0000 0002
- **Expiry**: Any future date
- **CVC**: Any 3 digits

## 📱 Responsive Design

The site is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile devices

## 🔐 Security Features

- CSRF protection on all forms
- Secure password hashing
- SQL injection protection
- XSS protection
- HTTPS ready

## 🚀 Production Deployment

### 1. Update Settings
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = 'your-production-secret-key'
```

### 2. Use PostgreSQL
```bash
pip install psycopg2-binary
```

Update `DATABASES` in settings.py

### 3. Collect Static Files
```bash
python manage.py collectstatic
```

### 4. Deploy with Gunicorn
```bash
pip install gunicorn
gunicorn ecommerce.wsgi
```

## 📧 Email Configuration

Add email settings to `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

## 🤝 Contributing

Feel free to fork and submit pull requests for any improvements.

## 📝 License

This project is open source and available under the MIT License.

## 💬 Support

For issues or questions, please create an issue in the repository.

---

**Built with ❤️ using Django**

## 📸 Screenshots

- **Home Page**: Featured products and hero section
- **Product Catalog**: Browse with categories and search
- **Shopping Cart**: Manage items before checkout
- **Checkout**: Secure order confirmation
- **Payment**: Stripe integration for secure payments
- **Order Tracking**: View past orders and status

Enjoy your new ecommerce platform! 🎉