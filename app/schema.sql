DROP TABLE IF EXISTS things;

CREATE TABLE things (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  thing TEXT UNIQUE NOT NULL,
  nickname TEXT 
);
