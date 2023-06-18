# How to make DNS on debian 11 and forward it to another DNS?
<ol>
  <li> The question is complex, but the answer is simple!</li>
  <li> Download bind*</li>
  <li> Let's use the files /etc/bind/db.local (for network), /etc/bind/named.conf.default-zones (for zones), /etc/bind/named.conf.options (for forward).</li> 
  <li> The first file looks something like this: </li>
