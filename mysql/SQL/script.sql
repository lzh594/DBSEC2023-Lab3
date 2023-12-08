create definer = root@`%` trigger shop
    after delete
    on shoppingcarts
    for each row
begin
        insert into shoppinghistory(uid, book_id, date) values(OLD.uid, OLD.book_id, curdate());
    end;


