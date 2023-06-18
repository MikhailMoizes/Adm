# Extract Docker-Image from ISO file on LINUX
**Here we have an ISO file with a docker image, but we don't know how to download it at all.
**
<ol>
  <li>We audit: apt-cdrom add, and after lsblk.</li>
  <li>We find the desired, unidentified object, and remember it.</li>
  <li>Turn on the brain and create a separate directory: mkdir /mnt/docker, then mount mount /dev/unidentified_object /mnt/docker</li>
  <li>Download the image: docker load < /mnt/docker/image</li>
  <li>And finally, we launch the native into the world: docker images, docker run -P -d -p 8080:80 -image_name, docker ps.</li>
</ol>
