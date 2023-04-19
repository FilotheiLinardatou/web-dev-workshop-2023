DROP TABLE IF EXISTS task; 
DROP TABLE IF EXISTS dev_takes_task;

CREATE TABLE dev_takes_task
(name varchar(50),
email varchar(30),
primary key (name, email)
);