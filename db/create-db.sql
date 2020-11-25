create table user_group (
    id integer not null primary key autoincrement,
    name nvarchar(20) not null,
    creation_date datetime not null default current_timestamp
);

create table user (
    id integer not null primary key autoincrement,
    name nvarchar(20) not null,
    is_admin boolean default false,
    user_group_id integer,
    creation_date datetime not null default current_timestamp,
    foreign key(user_group_id) references user_group(id)
);

create table scheduler_partition (
    id integer not null primary key autoincrement,
    name nvarchar(20) not null
);

create table user_field (
    id integer not null primary key autoincrement,
    name nvarchar(50) not null,
    creation_date datetime not null default current_timestamp
);

create table user_field_value (
    id integer not null primary key autoincrement,
    user_id integer not null,
    user_field_id integer not null,
    value integer not null default 0,
    foreign key(user_id) references user(id),
    foreign key(user_field_id) references user_field(id)
);

create table limit_item (
    id integer not null primary key autoincrement,
    user_field_id integer not null,
    max_value integer not null,
    foreign key(user_field_id) references user_field(id)
);

create table user_limit (
    id integer not null primary key autoincrement,
    creation_date datetime not null default current_timestamp
);

create table limit_item_limit_join (
    limit_id integer not null,
    limit_item_id integer not null,
    foreign key(limit_id) references user_limit(id),
    foreign key(limit_item_id) references limit_item(id)
);

create table bounded_limit (
    id integer not null primary key autoincrement,
    limit_id integer not null,
    user_id integer,
    user_group_id integer,
    scheduler_partition_id integer,
    refresh_period_days integer,
    last_refreshed datetime,
    priority integer,
    is_default boolean,
    is_active boolean not null,
    creation_date datetime not null default current_timestamp,
    foreign key(limit_id) references user_limit(id),
    foreign key(user_id) references user(id),
    foreign key(user_group_id) references user_group(id),
    foreign key(scheduler_partition_id) references scheduler_partition(id)
);

create table job_rule (
    id integer not null primary key autoincrement,
    soft_priority integer,
    soft_priority_period_days integer,
    hard_priority,
    creation_date datetime not null default current_timestamp
);

create table bounded_job_rule (
    id integer not null primary key autoincrement,
    job_rule_id integer not null,
    user_id integer,
    user_group_id integer,
    scheduler_partition_id integer,
    priority integer,
    is_default integer,
    is_active boolean not null,
    creation_date datetime not null default current_timestamp,
    foreign key(job_rule_id) references job_rule(id),
    foreign key(user_id) references user(id),
    foreign key(user_group_id) references user_group(id),
    foreign key(scheduler_partition_id) references scheduler_partition(id)
);

create table booster (
    id integer not null primary key autoincrement,
    soft_priority_increase integer,
    hard_priority_increase integer,
    creation_date datetime not null default current_timestamp
);

create table user_field_booster_join (
    booster_id integer not null,
    user_field_id integer not null,
    foreign key(booster_id) references booster(id)
    foreign key(user_field_id) references user_field(id)
);

create table bounded_booster (
    id integer not null primary key autoincrement,
    booster_id integer not null,
    user_id integer,
    user_group_id integer,
    scheduler_partition_id integer,
    amount integer not null,
    creation_date datetime not null default current_timestamp,
    foreign key(booster_id) references booster(id),
    foreign key(user_id) references user(id),
    foreign key(user_group_id) references user_group(id),
    foreign key(scheduler_partition_id) references scheduler_partition(id)
);

insert into
    user_field(name)
values 
    ('total_node_hours'),
    ('current_node_hours'),
    ('running_jobs'),
    ('current_nodes');