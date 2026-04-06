# SQL Introduction (MySQL)

This folder contains a progressive set of MySQL scripts designed to practice core SQL fundamentals: database and table management (DDL), inserting and querying data (DML), filtering and sorting results, and basic aggregation.

The scripts follow the typical Holberton/ALX style: each task is implemented as a standalone `.sql` file you can execute with the MySQL client.

---

## Learning Objectives

By the end of this folder, you should be comfortable with:

- Connecting to a MySQL server and selecting databases
- **DDL** (Data Definition Language): creating/dropping databases and tables
- **DML** (Data Manipulation Language): inserting rows
- Reading table definitions and metadata
- Querying data with `SELECT`, `WHERE`, `ORDER BY`
- Simple aggregates: `COUNT()`, `AVG()`
- Grouping results with `GROUP BY`

---

## Requirements / Environment

- MySQL installed locally **or** access to a MySQL server (e.g. Docker, VM, remote sandbox)
- `mysql` client available in your terminal

Check version:

```bash
mysql --version
```

---

## How to Run a Script

General pattern:

```bash
cat <script.sql> | mysql -hlocalhost -uroot -p
```

Or from inside the MySQL prompt:

```sql
SOURCE path/to/script.sql;
```

### Using a specific database

If a script expects a database, you can provide it on the command line:

```bash
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p my_database
```

---

## Files and What They Teach

Below is a course-style walkthrough of each script.

### 0. List databases

**File:** `0-list_databases.sql`

- Introduces the MySQL server catalog.
- Uses `SHOW DATABASES;` to list all databases on the server.

Key idea: a MySQL server can host multiple databases; SQL commands often apply within a selected database.

---

### 1. Create a database (if missing)

**File:** `1-create_database_if_missing.sql`

- Introduces `CREATE DATABASE`.
- Uses `IF NOT EXISTS` to make the script **idempotent** (safe to re-run).

Idempotency is a good practice for provisioning scripts.

---

### 2. Remove a database

**File:** `2-remove_database.sql`

- Introduces `DROP DATABASE`.
- Uses `IF EXISTS` to avoid errors if the database is already gone.

Be careful: `DROP DATABASE` deletes **all tables and data** in that database.

---

### 3. List tables in a database

**File:** `3-list_tables.sql`

- Introduces `SHOW TABLES;`.
- Demonstrates the difference between server-wide metadata (`SHOW DATABASES`) and database-scoped metadata (`SHOW TABLES`).

---

### 4. Create a first table

**File:** `4-first_table.sql`

- Introduces basic `CREATE TABLE` syntax.
- Reinforces the concept of column definitions and table schema.

Common elements you should recognize:
- Column name
- Data type (e.g. `INT`, `VARCHAR`)
- Optional constraints (`NOT NULL`, `DEFAULT`, `PRIMARY KEY`, etc.)

---

### 5. Show full table description

**File:** `5-full_table.sql`

- Teaches how to inspect a table definition.
- Depending on the task, this is commonly done with:
  - `SHOW CREATE TABLE table_name;` (best for the exact DDL)
  - or `DESCRIBE table_name;` / `EXPLAIN table_name;` (quick schema view)

---

### 6. List all rows

**File:** `6-list_values.sql`

- Introduces the simplest form of querying:

```sql
SELECT * FROM table_name;
```

Concept: `*` means “all columns”. In production code, prefer explicit columns for clarity and performance.

---

### 7. Insert a row

**File:** `7-insert_value.sql`

- Introduces inserting data with `INSERT INTO`.

Typical pattern:

```sql
INSERT INTO table_name (col1, col2) VALUES (val1, val2);
```

---

### 8. Count records matching a condition

**File:** `8-count_89.sql`

- Introduces `COUNT()`.  
- Reinforces filtering with `WHERE`.

Typical pattern:

```sql
SELECT COUNT(*) FROM table_name WHERE condition;
```

---

### 9. Create a table with a full schema

**File:** `9-full_creation.sql`

- Applies everything learned in DDL:
  - multiple columns
  - constraints
  - default values
  - keys

This kind of script is a stepping stone toward schema migrations.

---

### 10. Order results by score

**File:** `10-top_score.sql`

- Introduces ordering results using `ORDER BY`.

Typical pattern:

```sql
SELECT score, name FROM second_table ORDER BY score DESC;
```

`DESC` sorts from highest to lowest.

---

### 11. Filter results and order them

**File:** `11-best_score.sql`

This script demonstrates two fundamental query concepts together:

- **Filtering** with `WHERE score >= 10`
- **Sorting** with `ORDER BY score DESC`

```sql
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
```

Read it as: “Give me the score and name for rows with score at least 10, sorted by highest score first.”

---

### 12. Update rows

**File:** `12-no_cheating.sql`

- Introduces `UPDATE`.

Typical pattern:

```sql
UPDATE table_name
SET col = new_value
WHERE condition;
```

Important: without a `WHERE`, you update **every row**.

---

### 13. Update using a condition

**File:** `13-change_class.sql`

- Reinforces `UPDATE ... WHERE ...`.
- Introduces the idea of “targeting” rows using a predicate.

---

### 14. Compute an average

**File:** `14-average.sql`

- Introduces `AVG()` for numeric columns.

Typical pattern:

```sql
SELECT AVG(score) FROM second_table;
```

---

### 15. Group and aggregate

**File:** `15-groups.sql`

- Introduces `GROUP BY`.
- Often combined with aggregates (`COUNT`, `AVG`, `MAX`, `MIN`).

Typical pattern:

```sql
SELECT name, COUNT(*)
FROM table_name
GROUP BY name;
```

Concept: `GROUP BY` partitions rows into groups that share the same value(s) in the grouped column(s).

---

### 16. Select rows with missing links

**File:** `16-no_link.sql`

- Often used to practice `IS NULL` checks.

Typical pattern:

```sql
SELECT *
FROM table_name
WHERE some_column IS NULL;
```

`NULL` means “unknown / missing”. It is **not** equal to `0` or an empty string.

---

## Useful SQL Notes

### `WHERE` vs `HAVING`

- Use `WHERE` to filter **rows before grouping**.
- Use `HAVING` to filter **groups after aggregation**.

### Safe re-runs

For scripts that create or drop objects, prefer:

- `CREATE ... IF NOT EXISTS`
- `DROP ... IF EXISTS`

---

## Next Steps

After mastering this folder, a natural progression is:

- Joins (`INNER JOIN`, `LEFT JOIN`)
- Subqueries
- Indexes and query performance
- Normalization and schema design
- Transactions (`BEGIN`, `COMMIT`, `ROLLBACK`)
