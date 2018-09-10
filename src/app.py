import redis
import sys
# import argparse

def main():
    host = sys.argv[1]
    port = sys.argv[2]
    keys = sys.argv[3]
    print('host: ', host)
    print('port: ', port)
    print('keys: ', keys)
    try: 
        r = redis.StrictRedis(host=host, port=port, db=0)
        print(r.set('WEB1', 'hello'))
        print(r.set('WEB_1', 'hello1'))
        print(r.set('WEB_1_2', 'hello12'))
        print(r.set('WEB1_1_2_3', 'hello123'))
    except Exception as err:
        print(err)
        return
    else:
        for key in r.scan_iter(keys):
            print('DEL {}: {}'.format(key, r.delete(key)))

if __name__ == "__main__":
    main()