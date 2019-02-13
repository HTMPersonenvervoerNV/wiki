# Schedules

## BISON KV1

At HTM we exchange our schedules foremost in the [BISON KV1](http://bison.connekt.nl/standaarden/) standard. This format consists of a set of CSV files plus header, and is the basis for all travel information we exchange. The most recent KV1 files can be found at the [national accesspoint for public transport information](https://ndovloket.nl/) where the latest schedules for [HTM](http://data.ndovloket.nl/htm/) and [HTMbuzz](http://data.ndovloket.nl/htmbuzz/) are available.

## Daily CSV 

To make life easier for data processing crunching, we have denormalised the schedules of the KV1 file in a CSV file, in a passing time per line. The files can be obtained via our [open data processing portal](http://bigdata.openebs.nl/raw/) and are available since 2014. Below the data definition language statement can be found to create a table in a relational database of your choice. 
```
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

## NeTEx

HTM is a metropolean transport operator leading with the deployment of [Network Timetable Exchange](http://netex-cen.eu). This European standard is exchanged in XML and has a publicly available [XSD](https://github.com/NeTEx-CEN/NeTEx). To process the files several initiatives are available, for the [Java JAXB](https://github.com/entur/netex-java-model/) one we can give support. The latest [HTM NeTEx publication](http://data.ndovloket.nl/netex/htm/) includes many interesting features directly exported from our vehicle and crew optimiser.
