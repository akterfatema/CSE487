$TTL 1h
@       IN      SOA     verysecureserver.com. admin.verysecureserver.com. (
                 2023001701   ; serial
                 3600         ; refresh (1 hour)
                 900          ; retry (15 minutes)
                 1209600      ; expire (2 weeks)
                 3600         ; minimum (1 hour)
                 )

@       IN      NS      verysecureserver.com.
@       IN      A       192.168.0.154
www     IN      A       192.168.0.154
