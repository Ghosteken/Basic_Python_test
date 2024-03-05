CREATE TABLE color_statistics (
    id SERIAL PRIMARY KEY,
    mean_color VARCHAR(50) NOT NULL,
    mode_color VARCHAR(50) NOT NULL,
    median_color VARCHAR(50) NOT NULL,
    variance FLOAT NOT NULL,
    red_probability FLOAT NOT NULL
);
