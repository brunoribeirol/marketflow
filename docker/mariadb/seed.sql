-- ======================================
-- 🚫 Optional: Clean Tables (if needed)
-- ======================================
-- DELETE FROM orders;
-- DELETE FROM products;
-- DELETE FROM categories;
-- DELETE FROM clients;

-- ======================================
-- 👤 Clients
-- ======================================
INSERT INTO clients (name, email) VALUES
('Alice Johnson', 'alice.johnson@example.com'),
('Bob Smith', 'bob.smith@example.com'),
('Clara Davis', 'clara.davis@example.com'),
('Daniel Lee', 'daniel.lee@example.com'),
('Eva Moore', 'eva.moore@example.com'),
('Frank Brown', 'frank.brown@example.com');

-- ======================================
-- 📂 Categories
-- ======================================
INSERT INTO categories (name) VALUES
('Meat & Fish'),
('Fruits'),
('Cleaning Products'),
('Beverages'),
('Snacks'),
('Bakery');

-- ======================================
-- 🛒 Products (category_id in sequence)
-- ======================================
INSERT INTO products (name, price, category_id) VALUES
('Salmon Fillet', 45.00, 1),
('Beef Steak', 60.00, 1),
('Apple', 3.50, 2),
('Banana', 2.99, 2),
('Detergent', 8.50, 3),
('Disinfectant', 12.00, 3),
('Cola', 5.00, 4),
('Orange Juice', 7.50, 4),
('Potato Chips', 6.00, 5),
('Chocolate Bar', 4.00, 5),
('Bread Loaf', 4.50, 6),
('Croissant', 3.75, 6);

-- ======================================
-- 📦 Orders (client_id, product_id)
-- ======================================
INSERT INTO orders (client_id, product_id) VALUES
(1, 1),
(2, 4),
(3, 7),
(4, 10),
(5, 3),
(6, 12);
