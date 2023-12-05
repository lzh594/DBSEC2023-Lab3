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

