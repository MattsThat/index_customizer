drop table if exists constituents;

create table constituents (
    id          integer primary key autoincrement,
    index_id    integer,
    code        text,
    name        text,
    name_jp     text,
    par_value   float,
    

)