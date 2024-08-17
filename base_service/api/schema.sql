DROP TABLE IF EXISTS service_registration;
DROP TABLE IF EXISTS service_status;

CREATE TABLE service_registration (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  service_name TEXT NOT NULL,
  host_name TEXT NOT NULL,
  port INTEGER NOT NULL,
  alive_path TEXT NOT NULL,
  health_check_path TEXT NOT NULL,
  unique (service_name),
  unique (host_name, port)
);

CREATE TABLE service_status (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  alive BOOLEAN NOT NULL,
  health_check BOOLEAN NOT NULL,
  last_check TEXT NOT NULL,
  service_id INTEGER NOT NULL,
  FOREIGN KEY (service_id) REFERENCES service_registration (id)
);