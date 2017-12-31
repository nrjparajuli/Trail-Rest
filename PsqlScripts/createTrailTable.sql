-- noinspection SqlNoDataSourceInspectionForFile

DROP TABLE IF EXISTS Users CASCADE;
CREATE TABLE Users (
	user_id			VARCHAR(10),  --Earlham Username
	first_name		VARCHAR(100),
	PRIMARY KEY (user_id)
);

DROP TABLE IF EXISTS Games CASCADE;
CREATE TABLE Games (
	game_id			SERIAL,
	game_name		VARCHAR(30),
	creator_id		VARCHAR(10),
	PRIMARY KEY (game_id),
	FOREIGN KEY (creator_id) REFERENCES Users(user_id),
	UNIQUE (game_name)
);

DROP TABLE IF EXISTS Locations CASCADE;
CREATE TABLE Locations (
	location_id		VARCHAR(50),
	latitude		REAL,
	longitude		REAL,
	PRIMARY KEY (location_id)
);

DROP TABLE IF EXISTS GamesLocation;
CREATE TABLE GamesLocation (
	game_id			INTEGER,
	location_num	INTEGER,
	location 		VARCHAR(50),
	message			VARCHAR(140), 	--Same as Twitter
	FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS Invites;
CREATE TABLE Invites (
	game_id			INTEGER,
	invitee			VARCHAR(10),
	completed		BOOLEAN DEFAULT null,
	duration_min	DECIMAL(5,2) DEFAULT null,
	FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE,
	UNIQUE (game_id, invitee)
);

DROP FUNCTION IF EXISTS insertintoInvites( );
CREATE FUNCTION insertintoInvites( ) RETURNS TRIGGER AS
$$
BEGIN
    INSERT INTO Invites (game_id, invitee) VALUES (new.game_id, new.creator_id);
    RETURN new;
END
$$
  LANGUAGE 'plpgsql';

CREATE TRIGGER Invite_creator
AFTER INSERT ON Games
FOR EACH ROW
EXECUTE PROCEDURE insertintoInvites( );
