# 🥬 Sayur-Lokal Backend API

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![UV](https://img.shields.io/badge/Package%20Manager-UV-purple.svg)](https://github.com/astral-sh/uv)
[![Supabase](https://img.shields.io/badge/Database-Supabase-green.svg)](https://supabase.com/)
[![SQLite](https://img.shields.io/badge/Local%20DB-SQLite-lightblue.svg)](https://sqlite.org/)

API backend untuk aplikasi **Sayur-Lokal**, sebuah platform e-commerce yang menghubungkan pembeli dengan penjual produk lokal yang ramah lingkungan.

## 📋 Daftar Isi

- [🚀 Quick Start](#-quick-start)
- [🏗️ Arsitektur Proyek](#️-arsitektur-proyek)
- [⚙️ Instalasi](#️-instalasi)
- [🗄️ Database Setup](#️-database-setup)
- [🔐 Authentication](#-authentication)
- [📚 API Documentation](#-api-documentation)
- [🧪 Testing](#-testing)
- [🌐 Deployment](#-deployment)

## 🚀 Quick Start

### Base URLs

- **Production**: `https://fsse-oct24-group-k-gfp-be.onrender.com`
- **Local Development**: `http://localhost:5000`

### Authentication Header

```bash
Authorization: Bearer <your_jwt_token>
```

## 🏗️ Arsitektur Proyek

```
sayur-lokal-be/
├── app/
│   ├── controllers/          # Business logic layer
│   │   ├── auth_controller.py
│   │   ├── user_controller.py
│   │   ├── product_controller.py
│   │   ├── category_controller.py
│   │   ├── order_controller.py
│   │   └── rating_controller.py
│   ├── routes/              # Route definitions
│   │   ├── auth_routes.py
│   │   ├── user_routes.py
│   │   ├── product_routes.py
│   │   ├── category_routes.py
│   │   ├── order_routes.py
│   │   └── rating_routes.py
│   ├── services/            # Service layer
│   ├── models/              # Database models
│   ├── schemas/             # Pydantic schemas
│   ├── utils/               # Utilities & helpers
│   └── config.py            # Configuration
├── migrations/              # Database migrations
├── instance/
│   └── dev.db              # SQLite database (local only)
├── tests/                  # Test files
├── pyproject.toml          # UV project configuration
├── uv.lock                 # UV lock file
└── run.py                 # Application entry point
```

## ⚙️ Instalasi

### Prerequisites

- Python 3.11+
- [UV](https://github.com/astral-sh/uv) - Python package manager

### 1. Install UV

```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify installation
uv --version
```

### 2. Clone Repository

```bash
git clone https://github.com/Satriaa11/sayur-lokal-be.git
cd sayur-lokal-be
```

### 3. Setup Project dengan UV

```bash
# Install dependencies dengan UV
uv sync

# Aktivasi virtual environment
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 4. Setup Environment Variables

Buat file `.env` di root directory:

```env
# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=jwt-secret-key-here

# Database Configuration
# Local Development (SQLite)
DATABASE_URL=sqlite:///instance/dev.db

# Production (Supabase)
# DATABASE_URL=postgresql://user:password@host:port/database

# Supabase Configuration (Production)
SUPABASE_URL=your-supabase-url
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key
```

## 🗄️ Database Setup

### 🏠 Local Development (SQLite)

```bash
# Initialize database
flask db init

# Create migration
flask db migrate -m "Initial migration"

# Apply migration
flask db upgrade

# Atau jalankan aplikasi langsung (akan create database otomatis)
uv run python run.py
```

### 🌐 Production (Supabase)

#### 1. Setup Supabase Project

1. Buat account di [Supabase](https://supabase.com/)
2. Buat project baru
3. Copy Database URL dari Settings > Database
4. Copy API Keys dari Settings > API

#### 2. Update Environment Variables

```env
# Production Configuration
FLASK_ENV=production
DATABASE_URL=postgresql://postgres:[password]@[host]:[port]/postgres
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

#### 3. Run Migrations

```bash
# Set environment untuk production
export FLASK_ENV=production

# Run migrations
flask db upgrade
```

### 🔄 Switching Between Databases

```bash
# Development (SQLite)
export DATABASE_URL=sqlite:///instance/dev.db

# Production (Supabase)
export DATABASE_URL=postgresql://postgres:[password]@[host]:[port]/postgres
```

## 📦 Manajemen Dependencies dengan UV

### Menambah Dependencies

```bash
# Add production dependency
uv add flask sqlalchemy

# Add development dependency
uv add --dev pytest black flake8

# Add dependency dari GitHub
uv add git+https://github.com/user/repo.git

# Add dependency dengan versi spesifik
uv add "flask>=2.3.0,<3.0.0"
```

### Update Dependencies

```bash
# Update semua dependencies
uv sync

# Update dependency spesifik
uv add flask@latest

# Lock dependencies
uv lock
```

### Useful UV Commands

```bash
# Show installed packages
uv pip list

# Show dependency tree
uv pip show --tree

# Export ke requirements.txt (jika diperlukan)
uv pip compile pyproject.toml -o requirements.txt

# Run command dalam virtual environment
uv run python script.py
uv run flask run
uv run pytest
```

## 🔐 Authentication

### User Roles

- **Buyer**: Pembeli produk
- **Seller**: Penjual produk
- **Admin**: Administrator sistem

### JWT Token

Setelah login berhasil, Anda akan mendapat JWT token yang harus disertakan dalam header untuk endpoint yang memerlukan autentikasi.

## 📚 API Documentation

### 🔑 Authentication Endpoints

| Method   | Endpoint                    | Description                  | Auth Required |
| -------- | --------------------------- | ---------------------------- | ------------- |
| `POST`   | `/auth/register/buyer`      | Registrasi sebagai buyer     | ❌            |
| `POST`   | `/auth/register/seller`     | Registrasi sebagai seller    | ❌            |
| `POST`   | `/auth/login`               | Login user                   | ❌            |
| `POST`   | `/auth/logout`              | Logout user                  | ✅            |
| `POST`   | `/auth/resend-verification` | Kirim ulang email verifikasi | ❌            |
| `POST`   | `/auth/refresh-token`       | Refresh JWT token            | ❌            |
| `DELETE` | `/auth/delete-account`      | Hapus akun                   | ✅            |

#### Example Request - Register Buyer

```bash
curl -X POST http://localhost:5000/auth/register/buyer \
  -H "Content-Type: application/json" \
  -d '{
    "email": "buyer@example.com",
    "password": "password123",
    "name": "John Doe",
    "phone": "08123456789",
    "address": "Jakarta"
  }'
```

### 👤 User Profile Endpoints

| Method | Endpoint                 | Description          | Auth Required |
| ------ | ------------------------ | -------------------- | ------------- |
| `GET`  | `/users/profile`         | Lihat profil user    | ✅            |
| `PUT`  | `/users/profile/buyer`   | Update profil buyer  | ✅ (Buyer)    |
| `PUT`  | `/users/profile/seller`  | Update profil seller | ✅ (Seller)   |
| `PUT`  | `/users/profile/picture` | Update foto profil   | ✅            |
| `PUT`  | `/users/password`        | Ganti password       | ✅            |

### 🛍️ Product Endpoints

| Method   | Endpoint                           | Description                 | Auth Required |
| -------- | ---------------------------------- | --------------------------- | ------------- |
| `GET`    | `/products`                        | Lihat semua produk          | ❌            |
| `GET`    | `/products/{product_id}`           | Detail produk               | ❌            |
| `POST`   | `/products`                        | Tambah produk               | ✅ (Seller)   |
| `PUT`    | `/products/{product_id}`           | Update produk               | ✅ (Seller)   |
| `DELETE` | `/products/{product_id}`           | Hapus produk                | ✅ (Seller)   |
| `GET`    | `/products/category/{category_id}` | Produk berdasarkan kategori | ❌            |
| `GET`    | `/products/seller/{seller_id}`     | Produk berdasarkan seller   | ❌            |
| `GET`    | `/products/price-range`            | Filter berdasarkan harga    | ❌            |
| `GET`    | `/products/search`                 | Cari produk                 | ❌            |

#### Query Parameters untuk `/products`

- `category_id` - Filter berdasarkan kategori
- `seller_id` - Filter berdasarkan seller
- `price_min` - Harga minimum
- `price_max` - Harga maksimum
- `name` - Cari berdasarkan nama
- `page` - Halaman (default: 1)
- `per_page` - Item per halaman (default: 10)

### 📦 Category Endpoints

| Method   | Endpoint                             | Description            | Auth Required |
| -------- | ------------------------------------ | ---------------------- | ------------- |
| `GET`    | `/categories`                        | Lihat semua kategori   | ❌            |
| `GET`    | `/categories/{category_id}`          | Detail kategori        | ❌            |
| `GET`    | `/categories/{category_id}/products` | Kategori dengan produk | ❌            |
| `POST`   | `/categories`                        | Tambah kategori        | ✅ (Admin)    |
| `PUT`    | `/categories/{category_id}`          | Update kategori        | ✅ (Admin)    |
| `DELETE` | `/categories/{category_id}`          | Hapus kategori         | ✅ (Admin)    |

### 🛒 Order Endpoints

| Method | Endpoint                    | Description         | Auth Required |
| ------ | --------------------------- | ------------------- | ------------- |
| `POST` | `/orders`                   | Buat order          | ✅ (Buyer)    |
| `GET`  | `/orders/buyer`             | Lihat order buyer   | ✅ (Buyer)    |
| `GET`  | `/orders/seller`            | Lihat order seller  | ✅ (Seller)   |
| `GET`  | `/orders/{order_id}`        | Detail order        | ✅            |
| `PUT`  | `/orders/{order_id}/status` | Update status order | ✅            |
| `POST` | `/orders/{order_id}/cancel` | Batalkan order      | ✅ (Buyer)    |

### ⭐ Rating Endpoints

| Method   | Endpoint                        | Description   | Auth Required |
| -------- | ------------------------------- | ------------- | ------------- |
| `POST`   | `/ratings`                      | Buat rating   | ✅ (Buyer)    |
| `GET`    | `/ratings/product/{product_id}` | Rating produk | ❌            |
| `GET`    | `/ratings/user`                 | Rating user   | ✅            |
| `GET`    | `/ratings/{rating_id}`          | Detail rating | ❌            |
| `PUT`    | `/ratings/{rating_id}`          | Update rating | ✅ (Buyer)    |
| `DELETE` | `/ratings/{rating_id}`          | Hapus rating  | ✅            |

## 🧪 Testing

### Run Tests dengan UV

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app

# Run specific test file
uv run pytest tests/test_auth.py

# Install test dependencies jika belum ada
uv add --dev pytest pytest-cov
```

### Manual API Testing

Gunakan tools seperti:

- **Postman**: Import collection dari `/docs/postman/`
- **curl**: Contoh request ada di dokumentasi
- **HTTPie**: `http GET localhost:5000/products`

### Local Development Server

```bash
# Run dengan UV
uv run python run.py

# Atau dengan Flask CLI
uv run flask run

# Run dengan auto-reload untuk development
uv run flask run --reload
```

## 🌐 Deployment

### 🏗️ Production Setup dengan Supabase

#### 1. Database Migration ke Supabase

```bash
# Set environment untuk production
export DATABASE_URL=postgresql://postgres:[password]@[host]:[port]/postgres

# Run migrations
uv run flask db upgrade
```

#### 2. Environment Variables Production

```env
FLASK_ENV=production
DATABASE_URL=postgresql://postgres:[password]@[host]:[port]/postgres
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
SECRET_KEY=your-production-secret-key
JWT_SECRET_KEY=your-production-jwt-key
```

### 🚀 Deploy ke Render

1. Connect repository ke Render
2. Set build command: `uv sync`
3. Set start command: `uv run python run.py`
4. Set environment variables
5. Deploy automatically

### 🐳 Docker Deployment (Optional)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

# Install UV
RUN pip install uv

# Install dependencies
RUN uv sync

# Run application
CMD ["uv", "run", "python", "run.py"]
```

## 🗄️ Database Configuration Details

### 📝 Supabase Setup Guide

#### 1. Create Supabase Project

1. Go to [Supabase Dashboard](https://app.supabase.com/)
2. Click "New Project"
3. Fill project details and wait for setup

#### 2. Get Database Credentials

```bash
# From Supabase Dashboard > Settings > Database
Host: db.your-project.supabase.co
Port: 5432
Database: postgres
Username: postgres
Password: your-password
```

#### 3. Connection String Format

```bash
postgresql://postgres:your-password@db.your-project.supabase.co:5432/postgres
```

### 🔧 Configuration Examples

#### Local Development (.env)

```env
FLASK_ENV=development
DATABASE_URL=sqlite:///instance/dev.db
SECRET_KEY=dev-secret-key
JWT_SECRET_KEY=dev-jwt-key
```

#### Production (.env)

```env
FLASK_ENV=production
DATABASE_URL=postgresql://postgres:password@db.project.supabase.co:5432/postgres
SUPABASE_URL=https://project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
SECRET_KEY=your-production-secret-key
JWT_SECRET_KEY=your-production-jwt-key
```

### 🔄 Migration Commands

#### For SQLite (Local)

```bash
# Initialize migrations
uv run flask db init

# Create migration
uv run flask db migrate -m "Initial migration"

# Apply migration
uv run flask db upgrade
```

#### For Supabase (Production)

```bash
# Set production database URL
export DATABASE_URL=postgresql://postgres:password@db.project.supabase.co:5432/postgres

# Apply migrations to Supabase
uv run flask db upgrade

# Check migration status
uv run flask db current
```

## 🤝 Contributing

### Development Workflow

```bash
# 1. Fork repository dan clone
git clone https://github.com/your-username/sayur-lokal-be.git
cd sayur-lokal-be

# 2. Setup development environment
uv sync
source .venv/bin/activate  # Linux/Mac
# atau .venv\Scripts\activate  # Windows

# 3. Create feature branch
git checkout -b feature/amazing-feature

# 4. Make changes and test
uv run pytest

# 5. Commit and push
git commit -m 'Add amazing feature'
git push origin feature/amazing-feature

# 6. Create Pull Request
```

### Code Standards

- Use Black for code formatting: `uv run black .`
- Use Flake8 for linting: `uv run flake8`
- Write tests for new features
- Update documentation as needed

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact

- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **GitHub**: [@Satriaa11](https://github.com/Satriaa11)
- **Project Link**: [https://github.com/Satriaa11/sayur-lokal-be](https://github.com/Satriaa11/sayur-lokal-be)

---

⭐ **Jika project ini membantu, berikan star ya!** ⭐
