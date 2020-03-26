CREATE DATABASE democrance;
CREATE USER democranceuser WITH PASSWORD 'user123';
ALTER ROLE democranceuser SET client_encoding TO 'utf8';
ALTER ROLE democranceuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE democranceuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE democrance TO democranceuser;
