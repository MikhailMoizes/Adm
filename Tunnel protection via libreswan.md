# Tunnel protection via libreswan
<ol>
	<li> Download <b>libreswan</b>;</li>
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
	right=`REMOTE_NETWORK`
	rightprotoport=gre
  </pre></code>
	<li> Second file format:</li>
	<pre><code>our_network far_network : PSK “Super secret key”</pre></code>
	<li> From the second side it is similar. <b>We live and enjoy.</b></li>
	<li> If you want to start up dynamics in the network, then download <b>frr</b> from the link: https://deb.frrouting.org/ </li>


