create table authors
(
    author_id int          not null
        primary key,
    aname     varchar(255) not null
);

create table category
(
    category_id   int          not null
        primary key,
    category_name varchar(255) not null
);

create table publishers
(
    pub_id int          not null
        primary key,
    pname  varchar(255) not null
);

create table books
(
    book_id     int            not null
        primary key,
    bname       varchar(255)   not null,
    author_id   int            not null,
    pub_id      int            not null,
    category_id int            not null,
    price       decimal(10, 2) not null,
    pub_year    int            not null,
    url         varchar(255)   not null,
    isbn        char(10)       not null,
    sales       int default 0  null,
    rate        decimal(2, 1)  not null,
    constraint books_ibfk_1
        foreign key (author_id) references authors (author_id)
            on update cascade on delete cascade,
    constraint books_ibfk_2
        foreign key (pub_id) references publishers (pub_id)
            on update cascade on delete cascade,
    constraint books_ibfk_3
        foreign key (category_id) references category (category_id)
            on update cascade on delete cascade
);

create table users
(
    uid     int          not null
        primary key,
    uname   varchar(100) not null,
    email   varchar(100) null,
    tel     char(11)     null,
    pwdhash varchar(255) not null
);

create table collections
(
    uid     int not null,
    book_id int not null,
    primary key (uid, book_id),
    constraint collections_ibfk_1
        foreign key (uid) references users (uid)
            on update cascade on delete cascade,
    constraint collections_ibfk_2
        foreign key (book_id) references books (book_id)
            on update cascade on delete cascade
);

create index book_id
    on collections (book_id);

create table shoppingcarts
(
    uid     int not null,
    book_id int not null,
    amount  int not null,
    primary key (uid, book_id),
    constraint shoppingcarts_ibfk_1
        foreign key (uid) references users (uid)
            on update cascade on delete cascade,
    constraint shoppingcarts_ibfk_2
        foreign key (book_id) references books (book_id)
            on update cascade on delete cascade,
    check (`amount` > 0)
);

create index book_id
    on shoppingcarts (book_id);

create table shoppinghistory
(
    id      int auto_increment
        primary key,
    uid     int      not null,
    book_id int      not null,
    date    datetime not null,
    amount  int      not null,
    constraint shoppinghistory_ibfk_1
        foreign key (uid) references users (uid)
            on update cascade on delete cascade,
    constraint shoppinghistory_ibfk_2
        foreign key (book_id) references books (book_id)
            on update cascade on delete cascade
);

create index book_id
    on shoppinghistory (book_id);

create index uid
    on shoppinghistory (uid);