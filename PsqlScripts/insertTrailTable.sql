--username from sign-in page, Name from Register page
insert into Users values ('nparaj14', 'Niraj');
insert into Users values ('vstadn14', 'Vitalii');
insert into Users values ('ltnguyen14', 'Lam');
insert into Users values ('ssudhe13', 'Sidd');
insert into Users values ('ptran14', 'James');
insert into Users values ('aadhik14', 'Adhish');

--hardcoded-Location Data (No changes required excpt CVPA)
insert into Locations values ('Barrett Lobby', 39.822893, -84.912441);
insert into Locations values ('Bundy Lobby', 39.823430, -84.911988);
insert into Locations values ('Hoerner Lobby', 39.823536, -84.911288);
insert into Locations values ('EH Lobby', 39.822666, -84.913309);
insert into Locations values ('OA Lobby', 39.822977, -84.914155);
insert into Locations values ('Mills Lobby', 39.821505, -84.910859);
insert into Locations values ('Warren Lobby', 39.821697, -84.911264);
insert into Locations values ('Wilson Lobby', 39.821307, -84.911296);
insert into Locations values ('Wellness Lobby', 39.822498, -84.912145);
insert into Locations values ('Lilly Front Door', 39.823404, -84.914808);
insert into Locations values ('Carpenter Main Entrance', 39.8241181, -84.914537);
insert into Locations values ('LBC Main Entrance', 39.824230, -84.913694);
insert into Locations values ('CST Main Entrance', 39.824562, -84.912835);
insert into Locations values ('Dennis Main Entrance', 39.824234, -84.912037);
insert into Locations values ('Noyes Hall EPIC Colab', 39.824627, -84.912094);
--need arts building co-ordinates

--As soon as user presses FINISH button in create games page,
--insert game name, creator_id to this table
insert into Games (game_name, creator_id) values ('Freshman Tour', 'nparaj14');
insert into Games (game_name, creator_id) values ('Class Day', 'vstadn14');
 
--To get the game_id, query using game_name and creator_id
--second integer in values is simply a counter
--insertion should occur right after insert into Games
insert into GamesLocation 
	values (1, 1, 'Barrett Lobby', 'Nexflix and Chill with a Freshman');
insert into GamesLocation 
	values (1, 2, 'Bundy Lobby', 'It is kinda hot here');
insert into GamesLocation
	values (1, 3, 'Hoerner Lobby', 'Welcome to Prison');
insert into GamesLocation
	values (1, 4, 'OA Lobby', 'This is a new Freshman dorm. Kinda stinks though.');
insert into GamesLocation
	values (2, 1, 'Mills Lobby', 'Time to stop procrastinating');
insert into GamesLocation 
	values (2, 2, 'CST Main Entrance', 'Say Hi to Dave');
insert into GamesLocation 
	values (2, 3, 'LBC Main Entrance', 'SLAP RAJA AND RUN MOFO');

--A creator is added to Invites automatically
--the combination of game_id and invitee_id must be unique!
insert into Invites values (1, 'aadhik14');
insert into Invites values (1, 'ltnguyen14');
insert into Invites values (1, 'vstadn14');
insert into Invites values (2, 'ssudhe13');
insert into Invites values (2, 'ptran14');
	