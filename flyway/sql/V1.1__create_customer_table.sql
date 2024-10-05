CREATE TABLE customer (
    id int NOT NULL,
    first_name  varchar(35) NOT NULL,
    last_name   varchar(35) NOT NULL,
    middle_initial varchar(1),
    city        varchar(50),
    state       varchar(2),
    zip         INT,
    PRIMARY KEY (id)
);