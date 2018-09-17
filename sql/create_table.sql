SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS accounts;
SET FOREIGN_KEY_CHECKS=1;


CREATE TABLE accounts(
	username VARCHAR(50) PRIMARY KEY,
	password VARCHAR(256),
	firstName VARCHAR(50),
	lastName VARCHAR(50),
	balance FLOAT(21) NOT NULL
);


