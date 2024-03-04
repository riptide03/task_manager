create table if not exists tasks (
    id int primary key not null,
    name text not null,
    details text,
    due_datetime char(16),
    priority int,
    completed int not null
);
