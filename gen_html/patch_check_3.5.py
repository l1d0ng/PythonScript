#!/usr/bin/python3.5
# coding:utf-8
import csv
import os
import sys
from datetime import datetime

def get_data(path):
    final = []
    output=os.popen(' cd %s ;git log --author=htc  --pretty=format:"%%scn,%%ae ,%%H, %%cd"'%(path)).read().splitlines()
#    print(output)
    for item in output:
        #print(item)
        temp = []
        item=item.split(',')
#        print(item)
        for n in item:
            temp.append(n)
#            print(n)      
        final.append(temp)
#    print(final)

    return final

	
def write_data_csv(data, name):
    file_name = name+'.csv'
    with open(file_name, 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(['Title','Author','Commit ID','Time'])
            f_csv.writerows(data)

def write_data_html(data, name, path):
    file_name = name+".html"
    f = open(file_name,'w')
    message ="""
             <html>
             <body>
             <font size="10" color="#008000">HTC Patch</font>
             <font size="4" color="#008000">("""+path+""")</font></br></br>
             <table border="1" cellspacing="0">
             <tr bgcolor="#008000">
             <th>Title</th>
             <th>Author</th>
             <th>Commit ID</th>
             <th>Date</th>
             </tr>"""
    print(len(data))
    for n in data:
        message = message+"""<tr>"""
        message = message+"""<td style="padding-right:20px">"""+n[0]+"""</td><td style="padding-right:20px">"""+n[1]+""" """+"""</td>"""
        message = message+"""<td style="padding-right:20px">"""+n[2]+"""</td><td style="padding-right:20px">"""+n[3]+""" """+"""</td>"""
        message = message+"""</tr>"""

    message = message+"""</table>
             </br></br>
             <div style="float:right;">
             <font size="4 style="padding-right:20px" color="#008000">HTC SSD BT</font>
             </div>
             </body>
             </html>"""
    f.write(message)
    f.close()
             
if __name__ == '__main__':
        print("Path:")
        print(sys.argv[1])
        print("Excel Name:")
        print(sys.argv[1].split('/')[-1]+'.csv')
        print("HTML Name:")
        print(sys.argv[1].split('/')[-1]+'.html')
        result = get_data(sys.argv[1])
        write_data_csv(result, sys.argv[1].split('/')[-1])
        write_data_html(result, sys.argv[1].split('/')[-1], sys.argv[1])
