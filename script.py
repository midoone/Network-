#!/usr/bin/env python3


# import the module os to interact with the file system. #
import os

#execute the command touch to create file named networkinfo+currnet date. #
os.system("touch networkinfo$(date '+%m-%d-%y')")


#print the dnss
# execute the command cat to see server name and then copie the result to the networkinfo file.#
os.system("cat /etc/resolv.conf | sed -E -n '/nameserver/p' >> networkinfo$(date '+%m-%d-%y')") 


#print the ipv4 of the network#
# execute the command ifconfig and use sed to print the second line, then use awk to print the first and the second filed after that copie to result to the file networkinfo.#
os.system("ifconfig | sed -E -n '2p'| awk '{print$1,$2}'  >> networkinfo$(date '+%m-%d-%y')")


#print the brodcast of the network
# execute the command ifconfig and use the sed to print the second line, then use awk to print the third and the fourth filed after that copie the result to the networkinfo file. #
os.system("ifconfig | sed -E -n '2p' | awk '{print$3,$4}'  >> networkinf$(date '+%m-%d-%y')")


#print the network mask
# execute the command ifconfig and use the sed to print the second line, then use awk to print the fifth and the sixth filed, copie the result to the networkinfo. #
os.system("ifconfig | sed -E -n '2p' | awk '{print$5,$6}'   >> networkinfo$(date '+%m-%d-%y')")


#print the open ports
#execute the command netstat -lntu and then use the sed command to print all lines that have the word " LISTEN", after that copie the result to the networkinfo file. #
os.system("netstat -lntu | sed -E -n '/LISTEN/p'  >> networkinfo$(date '+%m-%d-%y')")





