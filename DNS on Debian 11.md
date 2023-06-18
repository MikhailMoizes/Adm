# How to make DNS on Debian 11 and forward it to another DNS?
<ol>
  <li> The question is complex, but the answer is simple!</li>
  <li> Download <pre><code>bind*</pre></code></li>
  <li> Let's use the files: <br>for network<pre><code>/etc/bind/db.local</pre></code> for zones<pre><code>/etc/bind/named.conf.default-zones</pre></code> for forward<pre><code>/etc/bind/named.conf.options</pre></code></li> 
  <li> The first file looks something like this: </li>
  <pre><code>
  $TTL    604800
@       IN      SOA     `CHANGE_ME`. root.`CHANGE_ME`. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      localhost.      
@       IN      A       127.0.0.1       
@       IN      AAAA    ::1    
`CHANGE_ME` 	CNAME	  `CHANGE_ME`
`CHANGE_ME`.	IN	NS	`CHANGE_ME`.
`CHANGE_ME`	IN	A	`CHANGE_ME`. ; glue record
</pre></code>
  <li> The second file is more attractive:</li>
  <pre><code>
  zone ‘`CHANGE_ME`’ {
	type master;
	allow-transfer { any; };
	file “/etc/bind/db.local”;
</pre></code>
  <li> The last one is the bomb: </li>
    <pre><code>
forwarders { `CHANGE_ME`; };
dnssec-validation no;
allow-query { any; }
listen-on { any; }
  </pre></code>

