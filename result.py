yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose logs
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose down
[+] Running 2/2
 ✔ Container avatar-avatar-app-1  Removed                                                                                                                               0.0s 
 ✔ Network avatar_default         Removed                                                                                                                               0.2s 
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ docker compose up -d 
[+] Running 1/2
 ✔ Network avatar_default         Created                                                                                                                               0.1s 
 ⠧ Container avatar-avatar-app-1  Starting                                                                                                                              0.7s 
Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint avatar-avatar-app-1 (8b6f4f72722cb85a521a4f9773d63a6a7857c5d6dac214e8369c92b1e8b98ef7): failed to bind host port for 0.0.0.0:9036:172.25.0.2:8000/tcp: address already in use
yaz@gpu:~/tak/GP/AVATAR/Wav2Lip/models$ 
