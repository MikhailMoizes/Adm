# Failover Web Server
<ol>
  <li>To create a failover web server, download nginx.</li>
  <li>Add certificate and public key information in /etc/nginx/snippets/snakeoil.</li>
  <li> Completely change the /etc/nginx/sites-available/defaults file.</li>
   <pre><code>upstream backend { 
 server adress:port fail_timeout=25; 
 server adress:port fail_timeout=25; 
} 
server { 
    listen 443 ssl default_server; 
    include snippets/snakeoil.conf;
    server_name site_name; 
 location / { 
  proxy_pass http://backend ;
 } 
}
server { 
   listen 80  default_server; 
  server_name _;
  return 301 https://site_name;
}
</code></pre>
  <li>Download iptables and write the following settings:<li>
   <pre><code>iptables -t nat -A PREROUTING -i `out_interface` -p tcp --dport 80 -j DNAT --to `adress`:`port`
iptables -t nat -A PREROUTING -i `out_interface` -p tcp --dport 443 -j DNAT --to `adress`:`port`
iptables -A FORWARD -i `in` -o `out_interface` -j ACCEPT # allow forwarding from internal port to external
iptables -t nat -A POSTROUTING -o `out_interface` -j MASQUERADE # Creating NAT Rules
iptables -A FORWARD -i `out_interface` -m state --state ESTABLISHED,RELATED -j ACCEPT # Allow external response 
iptables -I INPUT -i `out_interface` -m state --state ESTABLISHED,RELATED -j ACCEPT # Allow external response
iptables -P INPUT DROP # Ban all tricks
iptables -A INPUT -i lo -j ACCEPT 
iptables -A INPUT -i `in` -j ACCEPT 
iptables -A INPUT -i туннель(если есть) -j ACCEPT 
iptables -A INPUT -i `out_interface` -p gre -j ACCEPT
iptables -A INPUT -i `out_interface` -p icmp -j ACCEPT
iptables -A INPUT -i `out_interface` -p 53 -j ACCEPT
iptables -A INPUT -i `out_interface` -p 80 -j ACCEPT
iptables -A INPUT -i `out_interface` -p tcp –dport 443 -j ACCEPT
iptables -A INPUT -i `out_interface` -p 47 -j ACCEPT
iptables -A INPUT -i `out_interface` -p 22 -j ACCEPT
iptables -A INPUT -i `out_interface` -p tcp –dport 2222 -j ACCEPT
iptables -A INPUT -i `out_interface` -p tcp –dport 2244 -j ACCEPT
iptables -A INPUT -i `out_interface` -p esp -j ACCEPT
iptables –A INPUT –i `out_interface` –p 123 ACCEPT
iptables -t nat -A PREROUTING -i `out_interface` -p tcp --dport 2222 -j DNAT --to `adress`:22
iptables -t nat -A PREROUTING -i `out_interface` -p tcp --dport 2244 -j DNAT --to `adress`:22
iptables -t nat -A PREROUTING -i `out_interface` -p tcp --dport 53 -j DNAT --to `adress`:53
iptables -t nat -A PREROUTING -i `out_interface` -p udp --dport 53 -j DNAT --to `adress`:53
</code></pre>

