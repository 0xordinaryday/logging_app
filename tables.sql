BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "collars" (
	"hole_id"	TEXT,
	"easting"	REAL,
	"northing"	REAL,
	"elevation"	REAL,
	"starting_depth"	REAL,
	"ending_depth"	REAL,
	"inclination"	INTEGER,
	"azimuth"	INTEGER,
	"logged_by"	TEXT,
	"date"	TEXT,
	"drill_model"	TEXT,
	"barrel_type"	TEXT,
	"fluid"	TEXT,
	"diameter"	TEXT,
	PRIMARY KEY("hole_id")

);
CREATE TABLE IF NOT EXISTS "project_information" (
	"hole_id"	TEXT,
	"client"	TEXT,
	"job_id"	TEXT,
	"project_name"	TEXT,
	"project_line_2"	TEXT,
	"location"	TEXT
    -- PRIMARY KEY("hole_id")
);
CREATE TABLE IF NOT EXISTS "strata" (
	"hole_id"	TEXT,
	"from"	REAL,
	"to"	REAL,
	"classification_as1726"	TEXT,
	"graphic_log_keyword"	TEXT,
	"description"	TEXT,
	"method"	TEXT,
    PRIMARY KEY("hole_id")
);
CREATE TABLE IF NOT EXISTS "notessamples" (
	"hole_id"	TEXT,
	"from"	REAL,
	"to"	REAL,
	"notes"	TEXT,
    PRIMARY KEY("hole_id")
);
CREATE TABLE IF NOT EXISTS "moistureconsistency" (
	"hole_id"	TEXT,
	"from"	REAL,
	"to"	REAL,
	"moisture"	TEXT,
    "consistency"   TEXT,
    PRIMARY KEY("hole_id")
);
CREATE TABLE IF NOT EXISTS "penetration" (
	"hole_id"	TEXT,
	"from"	REAL,
	"to"	REAL,
	"penetration"	TEXT,
    PRIMARY KEY("hole_id")
);
CREATE TABLE IF NOT EXISTS "structureobs" (
	"hole_id"	TEXT,
	"depth"	REAL,
	"notes"	REAL,
    PRIMARY KEY("hole_id")
);
CREATE TABLE IF NOT EXISTS "waterlevel" (
	"hole_id"	TEXT,
	"depth"	REAL,
	"date"	TEXT,
    PRIMARY KEY("hole_id")
);
CREATE TABLE IF NOT EXISTS "waterflows" (
	"hole_id"	TEXT,
	"depth"	REAL,
	"event"	TEXT,
    PRIMARY KEY("hole_id")
);
CREATE TABLE IF NOT EXISTS "pp" (
	"hole_id"	TEXT,
	"depth"	REAL,
	"pp"	INTEGER,
    PRIMARY KEY("hole_id")
);
CREATE TABLE IF NOT EXISTS "dcp" (
	"hole_id"	TEXT,
	"depth"	REAL,
	"dcp"	INTEGER,
    PRIMARY KEY("hole_id")
);
CREATE TABLE IF NOT EXISTS "eoh" (
	"hole_id"	TEXT,
	"from"	REAL,
	"to"	REAL,
	"eoh_text"	TEXT,
    PRIMARY KEY("hole_id")
);

-- INSERT INTO "collars" ("hole_id","easting","northing","elevation","starting_depth","ending_depth","inclination","azimuth","logged_by","date","drill_model","barrel_type","fluid","diameter") VALUES ('BH1','574747','5285155','50','0','15','-90','0','DG','24 Jan 2023','Hanjin D+B D8','Auger','','150mm');
-- INSERT INTO "project_information" ("hole_id","client","job_id","project_name","project_line_2","location") VALUES ('BH1','Glamorgan Spring Bay Council','TG22202/1','Geotechnical Investigation',NULL,'Rheban Road, Spring Beach');
-- INSERT INTO "project_information" ("hole_id","client","job_id","project_name","project_line_2","location") VALUES ('BH2','West Tamar Council','TG99202/1','Some kind of job',NULL,'123 Fake Street, Gravelly Beach');

COMMIT;
