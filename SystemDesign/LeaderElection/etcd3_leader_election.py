"""etcd3 Leader election."""
import sys
import time
from threading import Event

import etcd3

LEADER_KEY = '/leader'
LEASE_TTL = 5
SLEEP = 1


def put_not_exist(client, key, value, lease=None):
    status, _ = client.transaction(
        compare=[
            client.transactions.version(key) == 0
        ],
        success=[
            client.transactions.put(key, value, lease)
        ],
        failure=[],
    )
    return status


def leader_election(client, me):
    lease = None
    try:

        lease = client.lease(LEASE_TTL)
        print("election")
        status = put_not_exist(client, LEADER_KEY, me, lease)
    except Exception as err:
        print ("error"+err)
        status = False
    return status, lease


def main(me):
    client = etcd3.client(host="192.168.1.14", port=2379)

    while True:
        print('leader election')
        leader, lease = leader_election(client, me)

        if leader:
            print('leader')
            try:
                while True:
                    # do work
                    lease.refresh()
                    time.sleep(SLEEP)
            except (Exception, KeyboardInterrupt):
                return
            finally:
                lease.revoke()
        else:
            print('follower; standby')

            election_event = Event()
            def watch_cb(event):
                if isinstance(event, etcd3.events.DeleteEvent):
                    election_event.set()
            watch_id = client.add_watch_callback(LEADER_KEY, watch_cb)

            try:
                while not election_event.is_set():
                    time.sleep(SLEEP)
                print('new election')
            except (Exception, KeyboardInterrupt):
                return
            finally:
                client.cancel_watch(watch_id)

if __name__ == '__main__':
    me = sys.argv[1]
    main(me)