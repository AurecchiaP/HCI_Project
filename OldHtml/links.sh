#!/bin/bash

for i in $(find . -type f -name '*.html'); do
	sed -i '' 's/eco\_society\///g' "$i"
done


#linkchecker $(find . -type f -name '*.html') | grep "URL" | grep -v "Real URL"