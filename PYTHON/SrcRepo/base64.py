#!/usr/bin/python
import sys

str = ""
if len(sys.argv)>1:
    str = sys.argv[1];
else:
    str = "abc";

print "raw string: " + str;

str = "this is string example....wow!!!";
str = str.encode('base64','strict');

print "Encoded String: " + str;
print "Decoded String: " + str.decode('base64','strict')
