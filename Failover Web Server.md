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
  <li>Download iptables and write the following settings:</li>
<pre><code>iptables -t nat -A PREROUTING -i `out_interface` -p tcp --dport 80 -j DNAT --to `adress`:`port`</code></pre>
<pre><code>iptables -t nat -A PREROUTING -i `out_interface` -p tcp --dport 443 -j DNAT --to `adress`:`port`</code></pre>
<pre><code>iptables -A FORWARD -i `in` -o `out_interface` -j ACCEPT # allow forwarding from internal port to external</code></pre>
<pre><code>iptables -t nat -A POSTROUTING -o `out_interface` -j MASQUERADE # Creating NAT Rules</code></pre>
<pre><code>iptables -A FORWARD -i `out_interface` -m state --state ESTABLISHED,RELATED -j ACCEPT # Allow external response </code></pre>
<pre><code>iptables -I INPUT -i `out_interface` -m state --state ESTABLISHED,RELATED -j ACCEPT # Allow external response</code></pre>
<pre><code>iptables -P INPUT DROP # Ban all tricks</code></pre>
<pre><code>iptables -A INPUT -i lo -j ACCEPT </code></pre>
<pre><code>iptables -A INPUT -i `in` -j ACCEPT </code></pre>
<pre><code>iptables -A INPUT -i tunnel (if any) -j ACCEPT </code></pre>
<pre><code>iptables -A INPUT -i `out_interface` -p gre -j ACCEPT</code></pre>
<pre><code>iptables -A INPUT -i `out_interface` -p icmp -j ACCEPT</code></pre>
<pre><code>iptables -A INPUT -i `out_interface` -p 53 -j ACCEPT</code></pre>
<pre><code>iptables -A INPUT -i `out_interface` -p 80 -j ACCEPT</code></pre>
<pre><code>iptables -A INPUT -i `out_interface` -p tcp –dport 443 -j ACCEPT</code></pre>
<pre><code>iptables -A INPUT -i `out_interface` -p 47 -j ACCEPT</code></pre>
<pre><code>iptables -A INPUT -i `out_interface` -p 22 -j ACCEPT</code></pre>
<pre><code>iptables -A INPUT -i `out_interface` -p tcp –dport 2222 -j ACCEPT</code></pre>
<pre><code>iptables -A INPUT -i `out_interface` -p tcp –dport 2244 -j ACCEPT</code></pre>
<pre><code>iptables -A INPUT -i `out_interface` -p esp -j ACCEPT</code></pre>
<pre><code>iptables –A INPUT –i `out_interface` –p 123 ACCEPT</code></pre>
<pre><code>iptables -t nat -A PREROUTING -i `out_interface` -p tcp --dport 2222 -j DNAT --to `adress`:22</code></pre>
<pre><code>iptables -t nat -A PREROUTING -i `out_interface` -p tcp --dport 2244 -j DNAT --to `adress`:22</code></pre>
<pre><code>iptables -t nat -A PREROUTING -i `out_interface` -p tcp --dport 53 -j DNAT --to `adress`:53</code></pre>
<pre><code>iptables -t nat -A PREROUTING -i `out_interface` -p udp --dport 53 -j DNAT --to `adress`:53</code></pre>


