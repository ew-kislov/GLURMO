insert into user_group(name) values ('default'), ('ski'), ('stuff');
insert into scheduler_partition(name) values ('default'), ('debug'), ('research');

insert into
    user(name, pass_key, is_admin, user_group_id, uid)
values
    ('evgeniykislov', 't75865h43uh', 1, 3, 501),
    ('petya', 'fgn45u8g45n', 0, 2, 100),
    ('vasya', '85y4ug48un', 0, 1, 101);

insert into
    user_field_value(user_id, user_field_id, value)
values
    (1, 1, 12),
    (1, 2, 1),
    (1, 3, 3),
    (1, 4, 2);

insert into
    user_field_value(user_id, user_field_id, value)
values
    (2, 1, 34),
    (2, 2, 0),
    (2, 3, 0),
    (1, 4, 2);

insert into
    limit_item(user_field_id, max_value)
values
    (1, 30),
    (1, 60),
    (2, 6),
    (3, 4),
    (4, 16);

insert into
    bound_limit(limit_id, user_group_id, is_default, is_active)
values 
    (1, 1, 1, 1),
    (1, 2, 1, 1),
    (2, 3, 1, 1),
    (3, null, 1, 1),
    (4, null, 1, 1),
    (5, null, 1, 1);

insert into
    job_rule(soft_priority, soft_priority_period_minutes, hard_priority)
values
    (null, null, 3),
    (null, null, 2),
    (1, 2, 1),
    (null, null, 10);

insert into
    bound_job_rule(job_rule_id, user_id, is_default)
values
    (1, 3, false),
    (2, 2, false),
    (3, 1, false),
    (4, null, true);

insert into
    booster(soft_priority_increase, hard_priority_increase, period_minutes)
values
    (1, null, 20);

insert into
    bound_booster(booster_id, user_id, amount)
values
    (1, 1, 5),
    (1, 2, 1),
    (1, 3, 1);