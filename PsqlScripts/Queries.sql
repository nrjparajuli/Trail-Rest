-- noinspection SqlNoDataSourceInspectionForFile

--Which games have I been invited to?
SELECT g.game_id, game_name
FROM Games AS g, Invites AS i
WHERE g.game_id=i.game_id AND invitee='ssudhe13';

--Which games did I create?
SELECT game_id, game_name
FROM Games
WHERE creator_id='nparaj14';

--Which users are invited to play a particular game?
SELECT invitee
FROM Invites
WHERE game_id=1;

--Create a new game
INSERT INTO Games (game_name, creator_id) VALUES ('Ganja Run', 'ssudhe13');

--What are all the available locations;
SELECT location_id
FROM Locations;

--Get the locations and messages for a game
SELECT location_num, location, message
FROM GamesLocation
WHERE game_id=1
ORDER BY location_num;

--Mark a player's game as complete and save time
--doesn't work as of yet
UPDATE Invites
SET completed='t', duration_min=13
WHERE game_id=1 AND invitee='ltnguyen14';
