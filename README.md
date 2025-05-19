# 🛒 MarketFlow

**MarketFlow** is a minimalist and professional supermarket management system built with **Python**, **Docker**, and **MariaDB**. It simulates a basic retail environment, managing CRUD operations for **clients**, **categories**, **products**, and **orders**, following clean architecture principles with a modular service layer and testing strategy.

---

## 📦 Technologies

- **Python 3.11**
- **MariaDB 10.11**
- **Docker & Docker Compose**
- **Pytest** for unit testing
- **dotenv** for environment management
- **Flake8** (Linting)
- **Black** (Code Formatting)

---

## 📁 Project Structure

```
marketflow/
├── app/                          # Source code
│   ├── config/                   # Env loader
│   ├── db/                       # Database connection logic
│   ├── models/                   # Domain entities
│   ├── services/                 # Business logic
│   ├── repositories/             # DB interaction layer
│   ├── queries/                  # Raw SQL queries
│   ├── controllers/              # REST-like interface (entrypoints)
│   ├── utils/                    # Utility functions
│   └── smoke_test.py             # Simple DB connectivity test
│   └── main.py                   # Entry point
│
├── docker/
│   ├── Dockerfile                # Python container config
│   └── mariadb/
│       ├── schema.sql            # Table structure
│       └── seed.sql              # Initial data
│
├── tests/                        # Unit tests (pytest)
├── docker-compose.yml            # Service orchestration
├── .env                          # Environment variables
├── .flake8                       # Flake8 linting configuration
├── .gitignore                    # Ignore rules
├── requirements.txt              # Python dependencies
├── Makefile
├── README.md
└── LICENSE

```

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/brunoribeirol/marketflow.git
cd marketflow
```

### 2. Create the `.env` file

```dotenv
DB_HOST=db
DB_PORT=3306
DB_USER=user
DB_PASSWORD=pass
DB_NAME=marketflow_db
DB_ROOT_PASSWORD=
```

---

## 🐳 Running with Docker

### 1. Build and Start

```bash
make build
make up
```

### 2. Run the App

```bash
make run
```

---

## 🧪 Testing

Run all tests using:

```bash
make test
```

---

## 🧰 Utilities

### Linting with flake8

```bash
make lint
```

### Auto-formatting with black

```bash
make format
```

### Open DB Shell

```bash
make db
```

---

## 🛠️ Useful Makefile Commands

| Command        | Description                                |
| -------------- | ------------------------------------------ |
| `make build`   | Build Docker containers                    |
| `make up`      | Start containers in detached mode          |
| `make down`    | Stop and remove containers and volumes     |
| `make bash`    | Open shell in app container                |
| `make logs`    | Show app container logs                    |
| `make run`     | Run the application manually               |
| `make test`    | Run all tests with pytest                  |
| `make lint`    | Lint code using flake8                     |
| `make format`  | Format code using black                    |
| `make mariadb` | Open MariaDB terminal inside the container |

---

## ✅ Project Highlights

- ✔️ Modular clean architecture
- ✔️ Dockerized local development
- ✔️ Linting & formatting setup
- ✔️ Full unit test coverage
- ✔️ Easy setup with Makefile automation

---

## 📝 License

[LICENSE](LICENSE)
