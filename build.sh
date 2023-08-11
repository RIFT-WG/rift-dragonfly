#!/bin/bash

D=draft-przygienda-rift-dragonfly++

# xml2rfc $D.xml

echo -- df++


xml2rfc $D.xml

nl -ba $D.txt > $D.nl.txt

