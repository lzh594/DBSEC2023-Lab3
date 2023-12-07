create table shoppinghistory
(
    uid     int  not null,
    book_id int  not null,
    date    date not null,
    primary key (uid, book_id, date),
    constraint shoppinghistory_ibfk_1
        foreign key (uid) references users (uid)
            on update cascade on delete cascade,
    constraint shoppinghistory_ibfk_2
        foreign key (book_id) references books (book_id)
            on update cascade on delete cascade
);

create index book_id
    on shoppinghistory (book_id);

