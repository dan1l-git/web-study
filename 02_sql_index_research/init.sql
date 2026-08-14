CREATE TABLE IF NOT EXISTS clients (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    phone VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    rating NUMERIC DEFAULT 5.0 CHECK (rating >= 1.0 AND rating <= 5.0)
);

CREATE TABLE IF NOT EXISTS drivers (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    license_number VARCHAR UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    status VARCHAR NOT NULL CHECK (status IN ('active', 'blocked', 'on_vacation'))
);

CREATE TABLE IF NOT EXISTS rides (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    client_id INT NOT NULL,
    driver_id INT NOT NULL,
    ride_date TIMESTAMP NOT NULL,
    status VARCHAR NOT NULL CHECK (status IN ('requested', 'ongoing', 'completed', 'cancelled')),
    price NUMERIC NOT NULL CHECK (price > 0),

    CONSTRAINT fk_client
        FOREIGN KEY (client_id)
        REFERENCES clients(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_driver
        FOREIGN KEY (driver_id)
        REFERENCES drivers(id)
        ON DELETE RESTRICT
);