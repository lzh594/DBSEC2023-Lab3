create trigger shop
    after delete on shoppingcarts
    for each row
    begin
        insert into shoppinghistory(uid, book_id, date, amount) values(OLD.uid, OLD.book_id, now(), OLD.amount)
    end;