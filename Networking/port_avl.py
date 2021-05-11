#FInd out a port is already in use

'''
$ lsof -i -P -n
$ lsof -i -P -n | grep LISTEN
'''

import logging
import socket

logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

#Check one port
def check_port(ip, port, timeout):
    ret = False
    logging.debug(f'Checking {ip}:{port}')

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.setdefaulttimeout(timeout)
        s.settimeout(timeout)
        conn = s.connect_ex((ip, port))
        logging.debug(f'Connection {ip}:{port} = {conn}')
        s.close()

        if conn == 0:
            ret = False
            logging.debug(f'In Use {ip}:{port}')

        else:
            ret = True
            logging.debug(f'Usable {ip}:{port}')

    except Exception as ex:
        ret = False
        logging.debug(f'Error {ip}:{port} = {ex.msg}')
    finally:
        logging.debug(f'Returning {ip}:{port} = {ret}')
        return ret

#Check Range of ports
def check_range(ip, scope):
    ret = {}
    for p in scope:
        r = check_port(ip, p, 1.0)
        ret[p] = r
    return ret


def main():
    my_port = 135
    p = check_port('localhost', my_port, 2.0)
    logging.info(f'Port {my_port} Usable = {p} \n')

    #RAnge of ports
    ports = check_range('localhost', range(3306,3309))
    for k,v in ports.items():
        logging.info(f'Port {k} usable {v}')

if __name__ == '__main__':
    main()
    