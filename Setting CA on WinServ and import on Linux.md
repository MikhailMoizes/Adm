# Setting CA on WinServ and import on Linux
  <p>To setting CA you should follow the next instructions:<p>
  <ol>
   <li>Create DC(Domain Controller)</li>
     <p></p>
   <li>Install cerctificate services</li>
     <p></p>
   <li>Request and install a server certificate.</li>
     <p>Follow these steps to create a server authentication certificate on the VPN server:</p>
       <ol>
         <li>In the Server Manager, in the Service menu, select the Certification Authority item;</li>
         <li>In the Certification Authority window, expand the Certification Authority (Local) node → CA_Name → Certificate Templates, and right-click on the Certificate Templates node and select Manage from the context menu;</li>
         <li>In the Certificate Templates Console, right-click the Web Server template and select Copy template from the context menu;</li>
         <li>The Properties window of the new template will open, in the Compatibility tab, leave the default setting of Windows Server 2003 - in the General tab, name the template, for example, VPN IPSec, specify the validity period no more than the validity period created by the CA;</li>
         <li> In the Request Processing tab, check the Allow private key export box;</li>
         <li> In the Subject Name tab, set the Provided in request radio button;</li>
         <li> In the Extensions tab in the Application Policies, check the presence of the Server Authentication policy:</li>
         <li> Press the OK button, close the certificate templates console and return to the Certification Authority; </li>
         <li> Right-click on the Certificate templates node and in the context menu select create → Issued certificate template</li>
         <li> In the Enable certificate templates window that opens, select the created certificate from the list and click the OK button.</li>
    </ol>
    <li> Issue a certificate through the web interface.</li>
    <li> Through mmc. export the certificate with the key.</li>
    <li> Move the certificate to the linux server.</li>
    <li> Separate the certificate and key using openssl.</li>
    <ol>
      <li>Extracting the public key:</li>
      <pre><code>openssl pkcs12 -in file_name.pfx -clcerts -nokeys -out file_name.crt</code></pre>
      <li>Certificate Extraction:</li>
      <pre><code>openssl pkcs12 -in file_name.pfx -nocerts -out file_name.private.key</code></pre>
      <li>Disabling the private key passphrase:</li>
      <pre><code>openssl rsa -in file_name.private.key -out file_name.key</code></pre>
    </ol>
  </ol>
