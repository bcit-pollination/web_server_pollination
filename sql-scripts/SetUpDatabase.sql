DROP DATABASE IF EXISTS voting_system;
CREATE DATABASE voting_system;
USE voting_system;

CREATE TABLE Users (
    user_id 			INT 			NOT NULL 	AUTO_INCREMENT,
    first_name 			VARCHAR(40) 	NOT NULL,
    last_name 			VARCHAR(40) 	NOT NULL,
    email               VARCHAR(40)     NOT NULL	UNIQUE,
    dob                 DATE            NOT NULL,
    password	        VARBINARY(200)  NOT NULL,
    voting_token		VARCHAR(36) 	NOT NULL	UNIQUE,
    deactivated			BOOLEAN			NOT NULL	DEFAULT(FALSE),
    PRIMARY KEY (user_id)
);

CREATE TABLE Vote (
    vote_id 		INT 		NOT NULL 	AUTO_INCREMENT,
    user_id 		INT 		NOT NULL,
    time_stamp 		TIMESTAMP 	NOT NULL 	DEFAULT(CURRENT_TIMESTAMP),
    PRIMARY KEY (vote_id),
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE Organization (
    org_id 				INT 			NOT NULL 	AUTO_INCREMENT,
    org_name 			VARCHAR(40) 	NOT NULL 	UNIQUE				DEFAULT('Unknown'),
    verifier_password   VARBINARY(200)     NOT NULL,
    disabled			BOOLEAN			NOT NULL    DEFAULT(FALSE),
    PRIMARY KEY (org_id)
);

CREATE TABLE Enrollment (
    enrollment_id 		INT 			NOT NULL 	AUTO_INCREMENT,
    user_id 			INT 			NOT NULL,
    org_id 				INT 			NOT NULL,
    privilege 	        INT 			NOT NULL 	DEFAULT(0), /* 0 to 4 = Removed, Invited, Member, Admin, Owner */
    user_org_id 		VARCHAR(40)     NOT NULL,
    PRIMARY KEY (enrollment_id),
    FOREIGN KEY (user_id)
        REFERENCES Users (user_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (org_id)
        REFERENCES Organization (org_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE KEY (user_id, org_id),
    CHECK (privilege BETWEEN 0 AND 4)
);

CREATE TABLE Election (
    election_id 	            INT 			NOT NULL 	AUTO_INCREMENT,
    org_id 			            INT 			NOT NULL,
    election_description		VARCHAR(400)	NOT NULL,
    start_time 		            VARCHAR(40) 	NOT NULL,
    end_time 		            VARCHAR(40) 	NOT NULL,
    anonymous 	                BOOLEAN 		NOT NULL 	DEFAULT(TRUE),
    public_results              BOOLEAN     	NOT NULL    DEFAULT(FALSE),
    verified                    BOOLEAN     	NOT NULL	DEFAULT(FALSE),
    PRIMARY KEY (election_id),
    FOREIGN KEY (org_id)
        REFERENCES Organization (org_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Question (
    question_id                 INT             NOT NULL    AUTO_INCREMENT,
    election_id                 INT             NOT NULL,
    question_description        VARCHAR(400)     NOT NULL,
    min_selection_count         INT             NOT NULL    DEFAULT 1,
    max_selection_count         INT             NOT NULL    DEFAULT 1,
    priority_selections         BOOLEAN	        NOT NULL    DEFAULT FALSE,
    PRIMARY KEY (question_id),
    FOREIGN KEY (election_id)
        REFERENCES Election (election_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CHECK (min_selection_count > 0),
    CHECK (max_selection_count > 0),
    CHECK (max_selection_count >= min_selection_count)
);

CREATE TABLE Opt (
    option_id 		        INT 			NOT NULL 	AUTO_INCREMENT,
    question_id 	        INT 			NOT NULL,
    option_description      VARCHAR(400) 	NOT NULL,
    total_votes_for         INT				NOT NULL	DEFAULT 0,
    PRIMARY KEY (option_id),
    FOREIGN KEY (question_id)
        REFERENCES Question (question_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Choice (
    choice_id 	INT 	NOT NULL 	AUTO_INCREMENT,
    vote_id     INT 	NOT NULL,
    option_id 	INT 	NOT NULL,
    priority	INT		NOT NULL	DEFAULT 0, /* 0 is a non-priority vote, 1 is the highest priority, 2 is lower, etc. */
    PRIMARY KEY (choice_id),
    FOREIGN KEY (vote_id)
        REFERENCES Vote (vote_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (option_id)
        REFERENCES Opt (option_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE KEY (vote_id, option_id),
    CHECK (priority >= 0)
);

