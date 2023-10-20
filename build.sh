#!/bin/bash

if [ `which xmlstarlet` -a `which xml2rfc` -a `which svgcheck` ]
then

  for f in svg/*.svg
  do
    cp $f $f.orig
#    rm $f.prep
#
#    xmlstarlet ed -d "//sodipodi:namedview" $f | xmlstarlet ed -d "//svg:metadata" | \
#    xmlstarlet ed -d "//@inkscape:version" | xmlstarlet ed -d "//@sodipodi:docname" | \
#    xmlstarlet ed -d "//svg:g/@inkscape:label" | xmlstarlet ed -d "//svg:g/@inkscape:groupmode" | \
#    # xmlstarlet ed -d "//svg:rect/@style" | \
#    xmlstarlet ed -d "//svg:path/@style" | \
#    xmlstarlet ed -d "//svg:text/@style" | \
#    xmlstarlet ed -d "//svg:text/svg:tspan"  > $f.prep
    svgcheck -a -r $f | xmlstarlet ed -d "//svg:text/@stroke" > prep/$f
    # rm $f.1
    done

  D=draft-przygienda-rift-dragonfly++

  # xml2rfc $D.xml

  echo -- df++

  echo -- to text
#  xml2rfc $D.xml
  echo -- to pdf
  xml2rfc --pdf $D.xml

  nl -ba $D.txt > $D.nl.txt
  exit
fi

echo install xml2rfc/xmlstarlet/svgcheck to run ...


