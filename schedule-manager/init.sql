SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

CREATE TABLE IF NOT EXISTS schedules (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME,
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

INSERT INTO schedule_db.schedules
(title, description, start_datetime)
VALUES
('파이썬', 'vod 완독', 20251125090000);

INSERT INTO schedule_db.schedules
(title, description, start_datetime)
VALUES
('플라스', 'vod 완독', 20251130090000);

INSERT INTO schedule_db.schedules
(title, description, start_datetime)
VALUES
('페아피', 'vod 완독', 20251205090000);

INSERT INTO schedule_db.schedules
(title, start_datetime)
VALUES
('꿀잠자기', 20251125245959);

INSERT INTO schedule_db.schedules
(title, start_datetime)
VALUES
('밥먹기', 20251226103000);

INSERT INTO schedule_db.schedules
(title, start_datetime)
VALUES
('숨쉬기', 20251225000000);
