create table bookstoredb.authors
(
    author_id int          not null
        primary key,
    aname     varchar(255) not null
);

create table bookstoredb.category
(
    category_id   int          not null
        primary key,
    category_name varchar(255) not null
);

create table bookstoredb.publishers
(
    pub_id int          not null
        primary key,
    pname  varchar(255) not null
);

create table bookstoredb.books
(
    book_id     int          not null
        primary key,
    bname       varchar(255) not null,
    author_id   int          not null,
    pub_id      int          not null,
    category_id int          not null,
    price       varchar(255) not null,
    pub_year    int          not null,
    constraint books_ibfk_1
        foreign key (author_id) references bookstoredb.authors (author_id)
            on update cascade on delete cascade,
    constraint books_ibfk_2
        foreign key (pub_id) references bookstoredb.publishers (pub_id)
            on update cascade on delete cascade,
    constraint books_ibfk_3
        foreign key (category_id) references bookstoredb.category (category_id)
            on update cascade on delete cascade
);

create index author_id
    on bookstoredb.books (author_id);

create index category_id
    on bookstoredb.books (category_id);

create index pub_id
    on bookstoredb.books (pub_id);

create table bookstoredb.users
(
    uid    int          not null
        primary key,
    uname  varchar(100) not null,
    passwd varchar(100) not null,
    email  varchar(100) null,
    tel    char(11)     null
);

create table bookstoredb.collections
(
    uid     int not null,
    book_id int not null,
    primary key (uid, book_id),
    constraint collections_ibfk_1
        foreign key (uid) references bookstoredb.users (uid)
            on update cascade on delete cascade,
    constraint collections_ibfk_2
        foreign key (book_id) references bookstoredb.books (book_id)
            on update cascade on delete cascade
);

create index book_id
    on bookstoredb.collections (book_id);

create table bookstoredb.shoppingcarts
(
    uid     int not null,
    book_id int not null,
    amount  int not null,
    primary key (uid, book_id),
    constraint shoppingcarts_ibfk_1
        foreign key (uid) references bookstoredb.users (uid)
            on update cascade on delete cascade,
    constraint shoppingcarts_ibfk_2
        foreign key (book_id) references bookstoredb.books (book_id)
            on update cascade on delete cascade,
    check (`amount` > 0)
);

create index book_id
    on bookstoredb.shoppingcarts (book_id);

create table bookstoredb.shoppinghistory
(
    uid     int  not null,
    book_id int  not null,
    date    date null,
    primary key (uid, book_id),
    constraint shoppinghistory_ibfk_1
        foreign key (uid) references bookstoredb.users (uid)
            on update cascade on delete cascade,
    constraint shoppinghistory_ibfk_2
        foreign key (book_id) references bookstoredb.books (book_id)
            on update cascade on delete cascade
);

create index book_id
    on bookstoredb.shoppinghistory (book_id);

