# viajes_aventura_poo

Travel agency management system for **Viajes Aventura**. It handles
clients, travel packages, destinations, and reservations, designed with
a robust layered architecture and secure database transactions.

## System Features

-   **Client Management:** Register new clients with secure PBKDF2
    password hashing.
-   **Package Management:** View available travel packages, dates,
    pricing, and available slots.
-   **Reservations:** Book packages for clients, automatically
    generating unique reservation codes and decreasing available slots.
-   **Many-to-Many Relationships:** Assign multiple destinations to a
    single travel package.
-   **Persistence:** Supports SQLite (default) and MySQL, configurable
    via environment variables.
-   **Transactions:** Ensures data integrity (e.g., a reservation is
    only saved if slots can be successfully deducted).

## Prerequisites

-   Python 3.10 or higher.
-   Visual Studio Code (recommended).
-   MySQL 8+ (only required if you use `DB_ENGINE=mysql`).

## Installation

### 1. Clone the repository

``` bash
git clone <url-del-repositorio>
cd viajes_aventura_poo
```

### 2. Create and activate the virtual environment

**Windows:**

``` bash
python -m venv .venv
.venv\\Scripts\\activate
```

**macOS / Linux:**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Duplicate the `.env.example` file and rename it to `.env`. Adjust the
values according to your database engine (SQLite by default).

## Execution

Make sure the virtual environment is activated and run:

``` bash
python main.py
```

## Initial Data (Seed)

On the first run, the system will automatically create the database
tables and populate them with sample data:

-   **Statuses:** Pending, Confirmed, Cancelled.
-   **Transport Types:** Flight, Bus.
-   **Destinations:** Patagonia, Machu Picchu.
-   **Packages:** Adventure in Patagonia, Machu Picchu Express.

## Architecture

The project follows a strict layered architecture to ensure separation
of concerns and scalability:

-   **Domain (`domain/`):** Pure business entities (`Client`, `Package`,
    `Reservation`, etc.) with built-in validation and password hashing
    logic.
-   **Persistence (`persistence/`):** Data Access Objects (DAOs) for
    safe database interaction using parameterized queries to prevent SQL
    injection.
-   **Services (`services/`):** Business logic layer
    (`booking_service.py`) that orchestrates interactions between DAOs
    (e.g., checking availability before saving a reservation).
-   **Presentation (`menus/`):** Console user interfaces with robust
    input validation loops.
-   **Utils (`utils/`):** Helper functions for input validation and UI
    management.

## Author

Juan Pablo Miranda (Adapted for Viajes Aventura)

## License

Academic project - INACAP (TI3021).

## `requirements.txt`

Make sure your `requirements.txt` includes the required libraries so the
project can run in different environments:

``` text
python-dotenv==1.0.1
PyMySQL==1.1.1
```
