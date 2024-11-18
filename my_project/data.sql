-- Створення бази даних
DROP DATABASE IF EXISTS GooglePlayStoreDB;
CREATE DATABASE IF NOT EXISTS GooglePlayStoreDB;
USE GooglePlayStoreDB;

-- DROP IF EXISTS statements for each table
DROP TABLE IF EXISTS PurchaseHistory;
DROP TABLE IF EXISTS AppUpdates;
DROP TABLE IF EXISTS Installs;
DROP TABLE IF EXISTS Devices;
DROP TABLE IF EXISTS Ratings;
DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Applications;
DROP TABLE IF EXISTS Developers;
DROP TABLE IF EXISTS AppCategories;


-- Таблиця для розробників додатків
CREATE TABLE IF NOT EXISTS  Developers (
    developer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    website VARCHAR(255),
    contact_email VARCHAR(255),
    INDEX idx_developer_name (name)
);

-- Таблиця для категорій додатків
CREATE TABLE IF NOT EXISTS AppCategories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Таблиця для додатків
CREATE TABLE IF NOT EXISTS Applications (
    app_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category_id INT,
    release_date DATE,
    developer_id INT,
    current_version VARCHAR(50),
    FOREIGN KEY (developer_id) REFERENCES Developers(developer_id),
    FOREIGN KEY (category_id) REFERENCES AppCategories(category_id),
    INDEX idx_app_name (name),
    INDEX idx_release_date (release_date)
);

-- Таблиця для користувачів
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    signup_date DATE,
    INDEX idx_username (username),
    INDEX idx_email (email)
);

-- Таблиця для відгуків
CREATE TABLE IF NOT EXISTS Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    app_id INT,
    user_id INT,
    review_text TEXT,
    review_date DATE,
    FOREIGN KEY (app_id) REFERENCES Applications(app_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    INDEX idx_review_date (review_date)
);

-- Таблиця для оцінок додатків
CREATE TABLE IF NOT EXISTS Ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    app_id INT,
    user_id INT,
    rating_value INT CHECK (rating_value BETWEEN 1 AND 5),
    rating_date DATE,
    FOREIGN KEY (app_id) REFERENCES Applications(app_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    INDEX idx_rating_value (rating_value),
    INDEX idx_rating_date (rating_date)
);

-- Таблиця для пристроїв користувачів
CREATE TABLE IF NOT EXISTS Devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    device_model VARCHAR(255),
    os_version VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    INDEX idx_device_model (device_model)
);

-- Таблиця для встановлень додатків
CREATE TABLE IF NOT EXISTS Installs (
    install_id INT AUTO_INCREMENT PRIMARY KEY,
    app_id INT,
    user_id INT,
    install_date DATE,
    device_id INT,
    FOREIGN KEY (app_id) REFERENCES Applications(app_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (device_id) REFERENCES Devices(device_id),
    INDEX idx_install_date (install_date)
);

-- Таблиця для оновлень додатків
CREATE TABLE IF NOT EXISTS AppUpdates (
    update_id INT AUTO_INCREMENT PRIMARY KEY,
    app_id INT,
    update_version VARCHAR(50),
    update_date DATE,
    FOREIGN KEY (app_id) REFERENCES Applications(app_id),
    INDEX idx_update_date (update_date)
);

-- Таблиця для історії покупок
CREATE TABLE IF NOT EXISTS PurchaseHistory (
    purchase_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    app_id INT,
    purchase_date DATE,
    purchase_amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (app_id) REFERENCES Applications(app_id),
    INDEX idx_purchase_date (purchase_date)
);

-- -- 1. Developers
-- INSERT INTO Developers (name, website, contact_email) VALUES
-- ('Google LLC', 'https://google.com', 'support@google.com'),
-- ('Facebook', 'https://facebook.com', 'support@facebook.com'),
-- ('Twitter Inc.', 'https://twitter.com', 'support@twitter.com'),
-- ('Microsoft', 'https://microsoft.com', 'support@microsoft.com'),
-- ('Apple', 'https://apple.com', 'support@apple.com'),
-- ('Amazon', 'https://amazon.com', 'support@amazon.com'),
-- ('Snapchat', 'https://snapchat.com', 'support@snapchat.com'),
-- ('Spotify', 'https://spotify.com', 'support@spotify.com'),
-- ('Zoom', 'https://zoom.us', 'support@zoom.us'),
-- ('Netflix', 'https://netflix.com', 'support@netflix.com');

-- -- 2. AppCategories
-- INSERT INTO AppCategories (name) VALUES
-- ('Social Media'),
-- ('Productivity'),
-- ('Games'),
-- ('Entertainment'),
-- ('Education'),
-- ('Shopping'),
-- ('Finance'),
-- ('Health & Fitness'),
-- ('Travel'),
-- ('News');

-- -- 3. Users
-- INSERT INTO Users (username, email, password, signup_date) VALUES
-- ('user1', 'user1@example.com', 'password1', '2024-01-01'),
-- ('user2', 'user2@example.com', 'password2', '2024-01-02'),
-- ('user3', 'user3@example.com', 'password3', '2024-01-03'),
-- ('user4', 'user4@example.com', 'password4', '2024-01-04'),
-- ('user5', 'user5@example.com', 'password5', '2024-01-05'),
-- ('user6', 'user6@example.com', 'password6', '2024-01-06'),
-- ('user7', 'user7@example.com', 'password7', '2024-01-07'),
-- ('user8', 'user8@example.com', 'password8', '2024-01-08'),
-- ('user9', 'user9@example.com', 'password9', '2024-01-09'),
-- ('user10', 'user10@example.com', 'password10', '2024-01-10');

-- -- 4. Applications
-- INSERT INTO Applications (name, category_id, release_date, developer_id, current_version) VALUES
-- ('Facebook', 1, '2010-07-01', 2, '1.2.3'),
-- ('Google Drive', 2, '2012-04-24', 1, '3.1.5'),
-- ('Twitter', 1, '2013-10-10', 3, '2.8.9'),
-- ('Microsoft Word', 2, '2015-05-15', 4, '16.0.0'),
-- ('Apple Music', 4, '2018-09-15', 5, '2.2.2'),
-- ('Amazon Shopping', 6, '2011-06-20', 6, '3.0.5'),
-- ('Snapchat', 1, '2014-05-02', 7, '11.4.5'),
-- ('Spotify', 4, '2013-07-01', 8, '8.6.0'),
-- ('Zoom', 2, '2020-03-15', 9, '5.6.3'),
-- ('Netflix', 4, '2016-12-01', 10, '7.1.2');

-- -- 5. Reviews
-- INSERT INTO Reviews (app_id, user_id, review_text, review_date) VALUES
-- (1, 1, 'Great app for connecting with friends!', '2024-01-10'),
-- (2, 2, 'Very useful for storing files.', '2024-01-11'),
-- (3, 3, 'Love the new updates.', '2024-01-12'),
-- (4, 4, 'Excellent tool for document editing.', '2024-01-13'),
-- (5, 5, 'Awesome music collection!', '2024-01-14'),
-- (6, 6, 'Easy to shop with this app.', '2024-01-15'),
-- (7, 7, 'Great for sharing moments with friends.', '2024-01-16'),
-- (8, 8, 'Amazing playlists.', '2024-01-17'),
-- (9, 9, 'Perfect for virtual meetings.', '2024-01-18'),
-- (10, 10, 'Love the variety of shows and movies.', '2024-01-19');

-- -- 6. Ratings
-- INSERT INTO Ratings (app_id, user_id, rating_value, rating_date) VALUES
-- (1, 1, 5, '2024-01-10'),
-- (2, 2, 4, '2024-01-11'),
-- (3, 3, 3, '2024-01-12'),
-- (4, 4, 5, '2024-01-13'),
-- (5, 5, 4, '2024-01-14'),
-- (6, 6, 5, '2024-01-15'),
-- (7, 7, 4, '2024-01-16'),
-- (8, 8, 5, '2024-01-17'),
-- (9, 9, 3, '2024-01-18'),
-- (10, 10, 5, '2024-01-19');

-- -- 7. Devices
-- INSERT INTO Devices (user_id, device_model, os_version) VALUES
-- (1, 'Samsung Galaxy S21', 'Android 11'),
-- (2, 'iPhone 12', 'iOS 14.4'),
-- (3, 'Google Pixel 5', 'Android 12'),
-- (4, 'OnePlus 8', 'Android 11'),
-- (5, 'iPhone SE', 'iOS 14.2'),
-- (6, 'Xiaomi Mi 10', 'Android 11'),
-- (7, 'Huawei P30', 'Android 10'),
-- (8, 'LG G8', 'Android 9'),
-- (9, 'Sony Xperia XZ3', 'Android 10'),
-- (10, 'iPhone 11', 'iOS 13');

-- -- 8. Installs
-- INSERT INTO Installs (app_id, user_id, install_date, device_id) VALUES
-- (1, 1, '2024-01-10', 1),
-- (2, 2, '2024-01-11', 2),
-- (3, 3, '2024-01-12', 3),
-- (4, 4, '2024-01-13', 4),
-- (5, 5, '2024-01-14', 5),
-- (6, 6, '2024-01-15', 6),
-- (7, 7, '2024-01-16', 7),
-- (8, 8, '2024-01-17', 8),
-- (9, 9, '2024-01-18', 9),
-- (10, 10, '2024-01-19', 10);

-- -- 9. AppUpdates
-- INSERT INTO AppUpdates (app_id, update_version, update_date) VALUES
-- (1, '1.2.4', '2024-02-01'),
-- (2, '3.1.6', '2024-02-02'),
-- (3, '2.9.0', '2024-02-03'),
-- (4, '16.1.0', '2024-02-04'),
-- (5, '2.3.0', '2024-02-05'),
-- (6, '3.0.6', '2024-02-06'),
-- (7, '11.5.0', '2024-02-07'),
-- (8, '8.7.0', '2024-02-08'),
-- (9, '5.7.0', '2024-02-09'),
-- (10, '7.2.0', '2024-02-10');

-- -- 10. PurchaseHistory
-- INSERT INTO PurchaseHistory (user_id, app_id, purchase_date, purchase_amount) VALUES
-- (1, 1, '2024-01-10', 0.99),
-- (2, 2, '2024-01-11', 1.99),
-- (3, 3, '2024-01-12', 2.99),
-- (4, 4, '2024-01-13', 0.00),
-- (5, 5, '2024-01-14', 4.99),
-- (6, 6, '2024-01-15', 0.00),
-- (7, 7, '2024-01-16', 3.99),
-- (8, 8, '2024-01-17', 9.99),
-- (9, 9, '2024-01-18', 0.00),
-- (10, 10, '2024-01-19', 5.99);

-- -- 1. Developers
-- -- Індекс для швидкого пошуку за іменем розробника та контактним email
-- CREATE INDEX idx_developers_name ON Developers (name);
-- CREATE INDEX idx_developers_contact_email ON Developers (contact_email);

-- -- 2. AppCategories
-- -- Індекс для швидкого пошуку за назвою категорії
-- CREATE INDEX idx_appcategories_name ON AppCategories (name);

-- -- 3. Users
-- -- Індекси для пошуку користувача за username та email
-- CREATE INDEX idx_users_username ON Users (username);
-- CREATE INDEX idx_users_email ON Users (email);

-- -- 4. Applications
-- -- Індекси для швидкого доступу до додатків за категорією та розробником
-- CREATE INDEX idx_applications_category_id ON Applications (category_id);
-- CREATE INDEX idx_applications_developer_id ON Applications (developer_id);

-- -- 5. Reviews
-- -- Індекси для пошуку відгуків за додатком та датою
-- CREATE INDEX idx_reviews_app_id ON Reviews (app_id);
-- CREATE INDEX idx_reviews_review_date ON Reviews (review_date);

-- -- 6. Ratings
-- -- Індекси для ефективного пошуку рейтингів за додатком та значенням рейтингу
-- CREATE INDEX idx_ratings_app_id ON Ratings (app_id);
-- CREATE INDEX idx_ratings_rating_value ON Ratings (rating_value);

-- -- 7. Devices
-- -- Індекси для пошуку пристроїв за моделлю та версією ОС
-- CREATE INDEX idx_devices_device_model ON Devices (device_model);
-- CREATE INDEX idx_devices_os_version ON Devices (os_version);

-- -- 8. Installs
-- -- Індекси для пошуку установок за додатком і датою установки
-- CREATE INDEX idx_installs_app_id ON Installs (app_id);
-- CREATE INDEX idx_installs_install_date ON Installs (install_date);

-- -- 9. AppUpdates
-- -- Індекси для швидкого доступу до оновлень за версією та датою
-- CREATE INDEX idx_appupdates_update_version ON AppUpdates (update_version);
-- CREATE INDEX idx_appupdates_update_date ON AppUpdates (update_date);

-- -- 10. PurchaseHistory
-- -- Індекси для пошуку покупок за додатком і датою покупки
-- CREATE INDEX idx_purchasehistory_app_id ON PurchaseHistory (app_id);
-- CREATE INDEX idx_purchasehistory_purchase_date ON PurchaseHistory (purchase_date);