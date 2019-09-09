# Realtime

## BISON KV6 and KV17
All realtime information for HTM journeys are exchanged in the [BISON KV6 and KV17](http://bison.connekt.nl/standaarden/) standards. This datastream is delivered by the [national accesspoint for public transport information](https://ndovloket.nl/) where it can be received on [best effort basis](http://data.ndovloket.nl/REALTIME.TXT) or via a [service level agreement](https://ndovloket.nl/aanmelden/). Both [KV6](https://github.com/BISONNL/KV6) as [KV17](https://github.com/BISONNL/KV17) are XML based and have XSD schema's to easy parsing. For Java JAXB a [KV6 model](https://github.com/bliksemlabs/kv6-java-model) and [KV17 model](https://github.com/bliksemlabs/kv17-java-model) exists. We have also created [a minimal boilerplate to receive the realtime data in Java](https://github.com/HTMPersonenvervoerNV/java-rt-bison). But it is no challenge to do it in any other language such as Python2.

```python
from gzip import GzipFile
from cStringIO import StringIO
import zmq

context = zmq.Context()

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://pubsub.besteffort.ndovloket.nl:7658")
subscriber.setsockopt(zmq.SUBSCRIBE, "/RIG/KV6posinfo")
subscriber.setsockopt(zmq.SUBSCRIBE, "/RIG/KV17cvlinfo")

while True:
    multipart = subscriber.recv_multipart()
    address = multipart[0]
    contents = ''.join(multipart[1:])
    try:
        contents = GzipFile('','r',0,StringIO(contents)).read()
        print('GZIP', address, contents)
    except:
        raise
        print('NOT ', address, contents)

subscriber.close()
context.term()
```
