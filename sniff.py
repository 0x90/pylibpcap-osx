#!/usr/bin/python.debug

import sys
import pcap
import string
import time

# convert string to list of ascii octets
def dumphex(s):
    bytes = map(lambda x: '%.2x' % x, map(ord, s))
    if len(s)>16:
      for i in range((len(s)+16)/16*16, 15, -16):
        bytes.insert(i,'\n')
    #return string.join(bytes, ' ')
    return bytes

def print_packet(pkt):
  eth_dst = pkt[:6]
  eth_src = pkt[6:12]
  print time.asctime(time.localtime(time.time()))
  print "%s -> %s" % (string.join(dumphex(eth_src),':'),
                      string.join(dumphex(eth_dst),':'))
  data = pkt[12:]
  print ' %s' % string.join(dumphex(data),' ')


def packet_callback (plen, pkt):
  print_packet(pkt)


if __name__=='__main__':

  if len(sys.argv) < 3:
    print 'usage: sniff.py <interface> <expr>'
    sys.exit(0)
  p = pcap.pcapObject()
  #dev = pcap.lookupdev()
  dev = sys.argv[1]
  net, mask = pcap.lookupnet(dev)
  # note:  to_ms does nothing on linux
  p.open_live(dev, 1500, 0, 100)
  #p.dump_open('dumpfile')
  p.setfilter(string.join(sys.argv[2:],' '), 0, 0)

  # try-except block to catch keyboard interrupt.  Failure to shut
  # down cleanly can result in the interface not being taken out of promisc.
  # mode
  try:
    while 1:
      p.dispatch(1, packet_callback)

    # specify 'None' to dump to dumpfile, assuming you have called
    # the dump_open method
    #  p.dispatch(0, None)

    # the loop method is another way of doing things
    #  p.loop(0, packet_callback)

    # as is the next() method
    #  pkt, hdr = p.next()
    #  if pkt:
    #    print_packet(pkt)
  except KeyboardInterrupt:
    print '%s' % sys.exc_type
    print 'shutting down'
    print '%d packets received, %d packets dropped, %d packets dropped by interface' % p.stats()
  


