CREATE TABLE metadata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    processed_at DATETIME NOT NULL,
    status VARCHAR(50) NOT NULL,
    source VARCHAR(100)
);
