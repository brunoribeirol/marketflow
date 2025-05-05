# 🛒 MarketFlow

MarketFlow is a simple and professional containerized CRUD system built with **Python**, **MariaDB**, and **Docker**.  
It simulates a basic retail environment, managing clients, products, and orders through a command-line menu and a structured database schema.

---

## 📦 Technologies

- **Python 3.11**
- **MariaDB 10.11**
- **Docker & Docker Compose**
- **Pytest** for unit testing
- **dotenv** for environment management

---

## 📁 Project Structure

```
marketflow/
├── app/                          # Source code
│   ├── config/                   # Env loader
│   ├── db/                       # DB connection & raw SQL
│   ├── models/                   # Domain entities
│   ├── services/                 # Business logic (CRUD)
│   ├── utils/                    # CLI menu & helpers
│   └── main.py                   # Entry point
│
├── docker/
│   ├── Dockerfile                # Python container config
│   └── mariadb/
│       ├── schema.sql            # Table structure
│       └── seed.sql              # Initial data
│
├── scripts/
│   └── start.sh                  # Project runner
│
├── tests/                        # Unit tests (pytest)
├── .env                          # DB credentials
├── .gitignore                    # Ignore rules
├── .dockerignore                 # Docker ignore list
├── docker-compose.yml            # Service orchestration
├── requirements.txt              # Python dependencies
├── LICENSE
└── README.md

```

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-user/marketflow.git
cd marketflow
```

### 2. Create the `.env` file

```dotenv
DB_HOST=db
DB_PORT=3306
DB_NAME=marketflow
DB_USER=user
DB_PASSWORD=pass
```

### 3. Start the services using Docker Compose

```bash
bash scripts/start.sh
```

Or manually:

```bash
docker-compose up --build
```

---

## 🧪 Running Tests

Make sure the containers are running, then execute:

```bash
docker exec -it marketflow_app pytest tests/
```

Or locally (if dependencies are installed):

```bash
pytest tests/
```

---

## 🧱 Database Overview

The system uses three relational tables:

- `clients`: Stores customer data
- `products`: Stores product data
- `orders`: Connects clients and products via foreign keys

SQL scripts are located in `docker/mariadb/`.

---

## 📚 Features

- Create, list, update, and delete:
  - Clients
  - Products
  - Orders
- View orders with client/product JOINs
- CLI menu interaction
- Modular architecture (services, models, db)
- Containerized with Docker
- Auto database setup on first run

---

## 📝 License

[LICENSE](LICENSE)

---

## 👨‍💻 Author

Bruno Ribeiro
