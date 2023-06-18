# How to make DNS on debian 11 and forward it to another DNS?
<ol>
  <li> The question is complex, but the answer is simple!</li>
  <li> Download <pre><code>bind*</pre></code></li>
  <li> Let's use the files <br>for network<pre><code>/etc/bind/db.local</pre></code> for zones<pre><code>/etc/bind/named.conf.default-zones</pre></code> for forward<pre><code>/etc/bind/named.conf.options</pre></code></li> 
  <li> The first file looks something like this: </li>
