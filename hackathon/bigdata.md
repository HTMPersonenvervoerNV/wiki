# Big data

Over the last four years we have collected all our own data published via the [national accesspoint for public transport information](https://ndovloket.nl/). This data is the primary source for our in house business analytics team. Combining the different data sources allows us to do performance analytics on different KPI's.

## Raw data
The raw historic information consists of the KV1 schedules converted to denormalised passing times, KV6 punctuality and KV17 operational changes converted to CSV. The dataset is available from a [public folder](http://bigdata.openebs.nl/). Below the data definition language statement can be found to create a table in a relational database of your choice. We would advise to try your idea on a single operating day, for scaling up we can help you in the right direction. Putting all data in a single table would performance wise not be a smart idea. 

```sql
CREATE TABLE "tt" (
        "operatingday"          DATE          NOT NULL,
        "trip_id"               VARCHAR(16)   NOT NULL,
        "pointorder"            SMALLINT      NOT NULL,
        "passagesequencenumber" SMALLINT      NOT NULL,
        "userstopcode"          VARCHAR(10)   NOT NULL,
        "targetarrivaltime"     VARCHAR(8)    NOT NULL,
        "targetdeparturetime"   VARCHAR(8)    NOT NULL,
        "recordedarrivaltime"   VARCHAR(8),
        "recordeddeparturetime" VARCHAR(8)
);
```
```sql
CREATE TABLE "kv6" (
        "receive"                   TIMESTAMP     NOT NULL,
        "message"                   TIMESTAMP     NOT NULL,
        "vehicle"                   TIMESTAMP     NOT NULL,
        "messagetype"               VARCHAR(10)   NOT NULL,
        "operatingday"              DATE          NOT NULL,
        "dataownercode"             VARCHAR(10)   NOT NULL,
        "lineplanningnumber"        VARCHAR(10),
        "journeynumber"             INTEGER       NOT NULL,
        "reinforcementnumber"       SMALLINT      NOT NULL,
        "userstopcode"              VARCHAR(10),
        "passagesequencenumber"     SMALLINT,
        "distancesincelastuserstop" INTEGER,
        "punctuality"               INTEGER,
        "rd_x"                      VARCHAR(11),
        "rd_y"                      VARCHAR(11),
        "blockcode"                 INTEGER,
        "vehiclenumber"             INTEGER,
        "wheelchairaccessible"      VARCHAR(5),
        "source"                    VARCHAR(10)   NOT NULL,
        "numberofcoaches"           SMALLINT
);
```
```sql
CREATE TABLE "kv17" (
        "message"               TIMESTAMP     NOT NULL,
        "server"                TIMESTAMP     NOT NULL,
        "messagetype"           VARCHAR(17)   NOT NULL,
        "dataownercode"         VARCHAR(10)   NOT NULL,
        "operatingday"          DATE          NOT NULL,
        "lineplanningnumber"    VARCHAR(10)   NOT NULL,
        "journeynumber"         DECIMAL(6)    NOT NULL,
        "reinforcementnumber"   DECIMAL(2)    NOT NULL,
        "reasontype"            DECIMAL(3),
        "subreasontype"         VARCHAR(10),
        "reasoncontent"         VARCHAR(255),
        "subreasoncontent"      VARCHAR(255),
        "userstopcode"          VARCHAR(10),
        "passagesequencenumber" DECIMAL(4),
        "lagtime"               DECIMAL(4),
        "targetarrivaltime"     TIME,
        "targetdeparturetime"   TIME,
        "journeystoptype"       VARCHAR(12),
        "destinationcode"       VARCHAR(10),
        "destinationname50"     VARCHAR(50),
        "destinationname16"     VARCHAR(16),
        "destinationdetail16"   VARCHAR(16),
        "destinationdisplay16"  VARCHAR(16)
);
```

## Departure punctuality

Our transport authority monitors our performance based on predetermined KPI's. These KPI's include measures to prevent early departures. The data is available from a [public folder](http://bigdata.openebs.nl/htm-punctdep/) and consists of the following data definition language statement. 

```sql
CREATE TABLE "punctdep" (
	"receive"              TIMESTAMP,
	"operatingday"         DATE,
	"lineplanningnumber"   VARCHAR(10),
	"journeynumber"        INTEGER,
	"pointorder"           SMALLINT,
	"userstopcode"         VARCHAR(10),
	"punctuality_computed" INTEGER,
	"name"                 VARCHAR(64),
	"vanaf"                VARCHAR(64),
	"richting"             VARCHAR(64),
	"vehiclenumber"        INTEGER,
	"ltmin61"              TINYINT,
	"min60"                TINYINT,
	"pos60"                TINYINT,
	"pos120"               TINYINT,
	"pos180"               TINYINT,
	"pos300"               TINYINT,
	"gt300"                TINYINT,
	"classificatie"        VARCHAR(16),
	"dow"                  TINYINT,
	"hod"                  TINYINT,
	"driverid"             TINYINT,
	"punctuality"          INTEGER
);
```

## General Trip Export
Sometimes all you need is some statistics on the performance of the system. Did we provide realtime data? Was the journey cancelled or was the traveler uninformed. The data is available from a [public folder](http://bigdata.openebs.nl/export/htm/) and consists of the following data definition language statement.

```sql
CREATE TABLE "htm_export" (
	"datum"               DATE,
	"lijn"                CHARACTER LARGE OBJECT,
	"ritnr"               CHARACTER LARGE OBJECT,
	"geplande_vertrek"    VARCHAR(8),
	"geplande_aankomst"   VARCHAR(8),
	"dru_tijd"            INTEGER,
	"eerste_halte"        VARCHAR(255),
	"laatste_halte"       VARCHAR(255),
	"aantal_haltes"       BIGINT,
	"has_kv1"             CHAR(1),
	"has_kv6"             TINYINT,
	"count_arrivals"      BIGINT,
	"vehiclenumber"       INTEGER,
	"werkelijke_vertrek"  TIMESTAMP,
	"werkelijke_aankomst" TIMESTAMP,
	"werkelijke_dru_tijd" BIGINT,
	"count_departures"    BIGINT,
	"has_kv17"            BOOLEAN,
	"reasontype"          DECIMAL(3),
	"reasoncontent"       VARCHAR(255)
);
```
