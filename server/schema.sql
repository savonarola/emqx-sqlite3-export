CREATE TABLE IF NOT EXISTS measurements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id STRING NOT NULL,
    temperature REAL NOT NULL,
    -- unix timestamp in seconds
    created_at INTEGER NOT NULL
);