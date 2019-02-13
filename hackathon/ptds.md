# PTDS.json

For the client side exchange of scheduled and real time travel information we designed a light weight normalised data format serialised in JSON. The object names and properties are closely modelled after Transmodel terminology. Typical public transport data consists of:

 - network; such as stops, their locations, the route link between two stops
 - service; lines, which stops follow in what order, distances
 - timetables; passing times
 - operational; vehicles executing journeys, drivers operating vehicles
 - realtime; real time passing times for points along the route
 - passenger usage; boarding, alighting passengers, and derivatives such as crowdedness

Historic files can be browsed through via [index.json](http://ptds.htmwiki.nl/index.json). [Sourcecode in Javascript](https://github.com/plannerstack/PTDS.js) for [PTDS](http://ptds.htmwiki.nl).

## Network

### ScheduledStopPoints

```json
{
  "scheduledStopPoints": {
    "HTM:9137": {
      "name": "Martinus Nijhofflaan",
      "stopAreaRef": "HTM:9136",
      "x": 83834,
      "y": 445852
    }
  }
}
```

A scheduled stop point is a location where a traveller can board or alight a vehicle. The **key value** is unique and referenced to from a JourneyPattern, and not intended to be presented to the user. The **name** is the full name of the stop, presented to the user. **StopAreaRef** refers to the StopArea object, which is currently not provided in this format, but the property facilitates aggregation of multiple stops into a single location for example two stops in an opposite direction, or a station with multiple tracks.

## Service

### JourneyPatterns

```json
{
  "journeyPatterns": {
    "HTM:15:160": {
      "lineRef": "HTM:15",
      "direction": 2,
      "pointsInSequence": [
        "HTM:2602",
        "HTM:2812",
        "HTM:2805",
        "HTM:2834",
        "HTM:2851",
        "HTM:2705",
        "HTM:3802",
        "HTM:3813",
        "HTM:3828",
        "HTM:3838",
        "HTM:5104",
        "HTM:5107",
        "HTM:5934",
        "HTM:5936",
        "HTM:5938",
        "HTM:5940",
        "HTM:9810",
        "HTM:9812",
        "HTM:9816"
      ],
      "distances": [
        0,
        561,
        1068,
        1470,
        1924,
        2488,
        2953,
        3342,
        3687,
        4079,
        4442,
        4774,
        5443,
        5997,
        6760,
        7350,
        8234,
        8841,
        9759
      ]
	}
  }
}
```

A journey pattern is a container that groups shared properties of journeys, for example which stop follows another. It is the normalisation step between the more generic Line and can be differentiated by a direction. Multiple patterns with the same line and direction may exists, for example a trip starting or ending at a different location. In this object we introduce the first column store. Column stores contain list of a primary type having same length which can be observed as a normal table when iterating over all the list using the same pivot. Opposed to row stores, where all attributes are adjacent but require more memory to read the entire object. Additional features such as compression capabilities are easy to observe.

The **key value** is unique and referenced to from a vehicleJourney, and not intended to be presented to the user. **lineRef** references towards a future Line object, which is not available in the current dataset, together with **direction** the client can aggregate all journeys for the same line in the same direction. In **pointsInSequence** we store the stops which are operated in sequence, **distances** tells us the distance travelled since start of the journey. Using these two lists as boilerplate we are able to represent realtime information in exactly the same fashion.


## Timetable

### VehicleJourneys

```json
{
  "vehicleJourneys": {
    "HTM:15:150012:2018-11-08": {
        "journeyPatternRef": "HTM:15:160",
		"times": [
			21600,
			21600,
			21706,
			21706,
			21796,
			21796,
			21902,
			21902,
			22001,
			22001,
			22134,
			22134,
			22221,
			22221,
			22297,
			22297,
			22349,
			22349,
			22413,
			22413,
			22488,
			22488,
			22545,
			22545,
			22660,
			22660,
			22780,
			22780,
			22879,
			22879,
			22962,
			22962,
			23090,
			23090,
			23179,
			23179,
			23527,
			23527
		]
	}
}
```
A VehicleJourney is modelled using the same concepts as the JourneyPattern, which it refers to using **journeyPatternRef**. Carefully observed may be noticed that the length of the **times** list is twice the length as the **pointsInSequence** attribute from the JourneyPattern. It is doubled to facilitate arrival and departure time, this allows to model wait time on the stop. The time is taken in seconds since the start of the day.

When the journey is operated additional properties may appear. For example **cancelled** which will be true after a KV17 CANCEL has been sent, **shortened** informs if any stops in the JourneyPattern are skipped. Additionally the **realtime** dictionary appears, which **key value** is equal to the **vehicleNumber** operating the trip. The **blockNumber** refers to the block the journey is part of in operational context, at this moment available for presentation only. To model the intermediate data points **times** and **distances** are used, for each data point received, the time since the start of the day is taken in combination with the distance travelled since the last stop plus the distance of the stop since the beginning of the trip. Using this method, realtime and scheduled information can be drawn in the same domain.

```json
{
  "vehicleJourneys": {
	"HTM:15:150012:2018-11-08": {
      "cancelled": false,
      "shortened": [],
      "realtime": {
        "5017": {
          "vehicleNumber": 5017,
          "blockNumber": 1502,
          "times": [
            21591,
            21613,
            21634,
            21654,
            ...
            23330,
            23346
          ],
          "distances": [
            0,
            0,
            110,
            241,
            ...,
            9722,
            9759
          ]
        }
      }
    }
  }
}
```
