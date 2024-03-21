import sys
import time
import libtorrent as lt

#Create torrent
fs = lt.file_storage()
lt.add_files(fs, "/app/traffic_generator/torrent/test.mp4")
t = lt.create_torrent(fs)
t.add_tracker("udp://tracker.openbittorrent.com:80/announce", 0)
t.set_creator('libtorrent %s' % lt.version)
t.set_comment("Test")
lt.set_piece_hashes(t, "/app/traffic_generator/torrent/")
torrent = t.generate()
f = open("/app/traffic_generator/torrent/test.torrent", "wb")
f.write(lt.bencode(torrent))
f.close()

# Seed torrent
ses = lt.session()
ses.listen_on(6881, 6891)
h = ses.add_torrent({'ti': lt.torrent_info('/app/traffic_generator/torrent/test.torrent'), 'save_path': '/app/traffic_generator/torrent/'}) 
print("Total size: " + str(h.status().total_wanted))
print("Name: " + h.name())
while True:
  s = h.status()
  state_str = ['queued', 'checking', 'downloading metadata', \
    'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
  print('\r%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
    (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
  sys.stdout.flush()
  time.sleep(10)
  break