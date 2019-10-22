drop table if exists index

create table index (
    id          integer primary key autoincrement,
    name        text,
    bbg_name    text,
    jp_name     text,
)