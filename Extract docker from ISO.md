# Extract Docker-Image from ISO file on LINUX
<h3>**Here we have an ISO file with a docker image, but we don't know how to download it at all.**</h3>
<ol>
  <li>We audit:<pre><code> apt-cdrom add</pre></code>, and after <pre><code>lsblk</pre></code></li>
  <li>We find the desired, unidentified object, and remember it.</li>
  <li>Turn on the brain and create a separate directory: <pre><code>mkdir /mnt/docker</pre></code> then mount <pre><code>mount /dev/unidentified_object /mnt/docker</pre></code></li>
  <li>Download the image: <pre><code>docker load < /mnt/docker/image</pre></code></li>
  <li>And finally, we launch the native into the world: <pre><code>docker images</pre></code> <pre><code>docker run -P -d -p 8080:80 -image_name</pre></code> <pre><code>docker ps</pre></code></li>
</ol>
