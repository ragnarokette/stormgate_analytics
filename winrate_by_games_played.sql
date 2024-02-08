drop table if exists retained;

create temp table retained as
select distinct
    player_id,
    race,
    mmr,
    matches,
    win_rate
from
    players
where
    matches > 10;
    
create temp table lost as
select distinct
    player_id,
    race,
    mmr,
    matches,
    win_rate
from
    players
where
    matches <= 10;
    
select distinct
    race,
    avg(win_rate)
from retained
group by 1;

select distinct
    race,
    avg(win_rate)
from lost
group by 1;

select distinct
    matches,
    race,
    avg(win_rate)
from players
where matches > 0
group by 1,2
order by 1;