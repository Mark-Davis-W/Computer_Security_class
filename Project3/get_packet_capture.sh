#!/usr/bin/bash

FILENAME=proj3.pcap

if ! command -v wget &> /dev/null
then
	echo "install the wget package (sudo apt install wget)"
	exit

elif test -f "$FILENAME"; then
	echo "$FILENAME exists."
	exit
else
	wget 'https://file.ecen4133.org/proj3.pcap'
fi
