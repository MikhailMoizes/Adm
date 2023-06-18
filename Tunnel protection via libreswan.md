# Tunnel protection via libreswan
<ol>
  <li> Download libreswan;</li>
  <li> Open the <pre><code>/etc/ipsec.d/ipsec.conf</pre></code> files, and then <pre><code>/etc/ipsec.d/your_name.secrets</pre></code></li>
  <li> First file format: </li>
  <pre><code>conn `YOUR_NAME`
	auto=start
	authby=secret
	type=tunnel
	ike=aes256-sha1
	phase2=esp
	phase2alg=aes256-sha2
	left=`YOUR_NETWORK`  
	leftprotoport=gre
	right=далекая_сеть
	rightprotoport=gre
  </pre></code>


