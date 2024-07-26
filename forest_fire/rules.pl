% Rules to determine fire spread area based on wind direction
fire_spread_area(CurrentArea, SpreadArea) :-
    wind_direction(north), north_adjacent(CurrentArea, SpreadArea).
fire_spread_area(CurrentArea, SpreadArea) :-
    wind_direction(east), east_adjacent(CurrentArea, SpreadArea).
fire_spread_area(CurrentArea, SpreadArea) :-
    wind_direction(south), south_adjacent(CurrentArea, SpreadArea).
fire_spread_area(CurrentArea, SpreadArea) :-
    wind_direction(west), west_adjacent(CurrentArea, SpreadArea).


% Rules to determine fire size based on weather
fire_size(small) :- weather(rain).
fire_size(large) :- weather(dry).

% Determine action based on fire area and size
take_action(FireArea) :-
    fire_spread_area(FireArea, SpreadArea),
    (FireArea = village;
     FireArea = forest;
     SpreadArea = village),
    write('Take immediate fire fighting action.').

take_action(FireArea) :-
    fire_spread_area(FireArea, SpreadArea),
    fire_size(large),
    (SpreadArea = lake;
     SpreadArea = river),
    write('Monitor fire situation and check firebreak.').

take_action(FireArea) :-
    fire_spread_area(FireArea, SpreadArea),
    fire_size(small),
    (SpreadArea = lake;
     SpreadArea = river),
    write('Monitor fire situation.').