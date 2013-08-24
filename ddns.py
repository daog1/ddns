#!/usr/bin/env python
#-*- coding:utf-8 -*-

from dnspod.apicn import *
import time
def getip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666))
    ip = sock.recv(16)
    sock.close()
    return ip
def getrecordip(domain,email,password,sub_domain,record_type):
    record_id =None
    record_ip =None
    api = DomainList(email=email, password=password)
    for d in api().get('domains'):
        if d['name']==domain:
            domain_id=d['id']
    api=RecordList(domain_id,email=email, password=password)
    record_id =None
    for r in api().get('records'):
        if r['name']==sub_domain and \
                        r['type'] == record_type:
            record_id = r['id']
            record_ip = r ['value']
    return record_id,record_ip,domain_id
def main():
    email = "xxxxxxxxx"
    password = "xxxxxxx"
    domain = "uwetech.com"
    sub_domain = "pc"
    record_type = "A"
    record_line='默认'

    record_id = None
    record_ip = None
    domain_id = None
    while True:
        try:
            record_id,record_ip,domain_id = getrecordip(domain,email,password,sub_domain,record_type)
            ip = getip()
            if record_ip == ip:
                print sub_domain,'.',domain,'=',record_ip
                pass
            else:
                api = RecordDdns(record_id,sub_domain,record_line,domain_id=domain_id,email=email, password=password,record_type=record_type)
                print api()
        except Exception,e:
            print 'Exception',e
        time.sleep(1)
    
if __name__ == '__main__':
    main()