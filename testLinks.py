from functionalityPackage import monitor_links

links_to_track = ["https://www.facebook.com", "https://in.linkedin.com/", "https://www.python.org/"]

#Tracking the above Links and send mail if link is down.
monitor_links.monitor(links_to_track)
