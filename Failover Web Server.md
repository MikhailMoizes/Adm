# Failover Web Server
<ol>
  <li>To create a failover web server, download nginx.</li>
  <li>Add certificate and public key information in /etc/nginx/snippets/snakeoil.</li>
  <li> Completely change the /etc/nginx/sites-available/defaults file.</li>
   <pre><code>upstream backend { 
 server адрес:порт fail_timeout=25; 
 server адрес:порт fail_timeout=25; 
} 
server { 
    listen 443 ssl default_server; 
    include snippets/snakeoil.conf;
    server_name имя_сайтаr; 
 location / { 
  proxy_pass http://backend ;
 } 
}
server { 
   listen 80  default_server; 
  server_name _;
  return 301 https://имя_сайта;
}
</code></pre>
