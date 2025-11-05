# ⚡ Quick Start Guide (5 minutes)

## 🚀 Get Running in 5 Steps

### Step 1: Create Admin User (1 min)
```bash
python manage.py createsuperuser
```
Enter username, email, and password when prompted.

### Step 2: Start Server (30 sec)
```bash
python manage.py runserver
```

### Step 3: Add Products via Admin (2 min)
1. Go to http://localhost:8000/admin
2. Login with your superuser credentials
3. Click "Add Category" → Create "Electronics"
4. Click "Add Product" → Create a test product

### Step 4: Test Shopping (1.5 min)
1. Visit http://localhost:8000
2. Browse products
3. Add to cart
4. Proceed to checkout (optional - use test card)

## 🎯 Most Important URLs

| URL | What It Does |
|-----|--------------|
| http://localhost:8000 | Home page |
| http://localhost:8000/admin | Admin panel |
| http://localhost:8000/products | Shop/catalog |
| http://localhost:8000/account/register | Sign up |
| http://localhost:8000/cart | Shopping cart |

## 💳 Test Payment Info

**Card Number:** 4242 4242 4242 4242
**Expiry:** Any future date (12/25)
**CVC:** Any 3 digits (123)

## 🐛 Quick Fixes

| Problem | Solution |
|---------|----------|
| "Module not found" | Run `pip install -r requirements.txt` |
| Database locked | Delete `db.sqlite3` and run `python manage.py migrate` |
| Port in use | Run `python manage.py runserver 8001` |
| Images not showing | Check `/media/` folder exists |
| Static files not loading | Run `python manage.py collectstatic --noinput` |

## 📁 File Structure You Need to Know

```
ECOMMDJ/
├── manage.py           ← Run Django commands
├── db.sqlite3          ← Database (auto-created)
├── templates/          ← HTML files
├── static/             ← CSS, JS, fonts
├── media/              ← User uploads (product images)
└── ecommerce/          ← Main settings folder
```

## 🔧 Common Commands

```bash
# Create admin user
python manage.py createsuperuser

# Start development server
python manage.py runserver

# Apply database changes
python manage.py migrate

# Create database changes from models
python manage.py makemigrations

# Enter Python shell
python manage.py shell

# Reset everything (be careful!)
python manage.py flush
```

## 📝 File Changes You Might Make

### Change Website Title
Edit `templates/base.html`, line 4:
```html
<title>{% block title %}YOUR SITE NAME{% endblock %}</title>
```

### Change Primary Color
Edit `ecommerce/settings.py`, add:
```python
PRIMARY_COLOR = '#your-color-code'
```

Then update `static/css/style.css`:
```css
--primary-color: #your-color-code;
```

### Add Your Stripe Keys
Edit `ecommerce/settings.py`:
```python
STRIPE_PUBLIC_KEY = 'pk_test_YOUR_KEY'
STRIPE_SECRET_KEY = 'sk_test_YOUR_KEY'
```

## 🎨 Quick Customization Tips

### Add Products via Shell
```bash
python manage.py shell
```

```python
from products.models import Category, Product
from decimal import Decimal

cat = Category.objects.create(name='Test', slug='test')
Product.objects.create(
    name='Product Name',
    slug='product-name',
    description='Description',
    price=Decimal('99.99'),
    category=cat,
    stock=10
)
exit()
```

### Change Template Colors
Edit `templates/base.html` - modify color variables in `<style>` tag.

### Add New Field to Product
Edit `products/models.py`:
```python
brand = models.CharField(max_length=100, default='')
```

Then run:
```bash
python manage.py makemigrations
python manage.py migrate
```

## 📞 Support & Resources

- **Django Docs**: https://docs.djangoproject.com/
- **Stripe Docs**: https://stripe.com/docs
- **Bootstrap Docs**: https://getbootstrap.com/docs/

## ✅ Verification Checklist

- [ ] Server runs without errors
- [ ] Admin login works
- [ ] Can view products
- [ ] Can add to cart
- [ ] Can view order history

## 🎉 Next Steps After Getting Comfortable

1. Upload real product images
2. Add more products via admin
3. Test the complete checkout flow
4. Configure Stripe production keys
5. Deploy to live server (Heroku, AWS, etc.)

---

**You're ready to go! Happy selling! 🛍️**