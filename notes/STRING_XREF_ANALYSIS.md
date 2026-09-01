# ALICE GREENFINGERS - EXHAUSTIVE STRING + XREF ANALYSIS (STEP 6)

*Generated on 2026-09-01 13:13:07*

## METRICS SUMMARY
- **Total Referenced String Literals Extracted:** 874

## STRING CROSS-REFERENCE TABLE

| String Literal | Referencing Function RVA | Function Identifier | Subsystem Classification | Evidence Confidence |
| --- | --- | --- | --- | --- |
| `TaskbarCreated` | `0x00401100` | `FUN_00401100` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `close all` | `0x00401cb0` | `FUN_00401cb0` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `/ErrorStdOut` | `0x00401f20` | `FUN_00401f20` | `Diagnostics & Exception Handling` | **CONFIRMED (Binary String Pointer)** |
| `/AutoIt3ExecuteScript` | `0x00401f20` | `FUN_00401f20` | `Script Engine Host` | **CONFIRMED (Binary String Pointer)** |
| `/AutoIt3ExecuteLine` | `0x00401f20` | `FUN_00401f20` | `Script Engine Host` | **CONFIRMED (Binary String Pointer)** |
| `/AutoIt3OutputDebug` | `0x00401f20` | `FUN_00401f20` | `Script Engine Host` | **CONFIRMED (Binary String Pointer)** |
| `#include depth exceeded.  Make sure there are no recursive includes` | `0x004033c0` | `FUN_004033c0` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `Unterminated string` | `0x004033c0` | `FUN_004033c0` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `Error opening the file` | `0x004033c0` | `FUN_004033c0` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `#include` | `0x004039a0` | `FUN_004039a0` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `#requireadmin` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `#NoAutoIt3Execute` | `0x00403a20` | `FUN_00403a20` | `Script Engine Host` | **CONFIRMED (Binary String Pointer)** |
| `,3), iVar1 == 0)) &&
               (param_1 = (wchar_t *)((int)param_1 + -1), (int)param_1 < 1)) {
              return true;
            }
          }
        }
        if (0 < (int)param_1) {
          FUN_00454014((int)this,(int)param_2,*param_3,L` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `,0xf);
          if ((iVar1 == 0) || (iVar1 = __wcsnicmp(pwVar5,L` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `#notrayicon` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `') {
        pwVar5 = _Str + 1;
        _Str[sVar2 - 1] = L'\0';
        FUN_00444b5f(pwVar5);
        FUN_00444bbb(pwVar5);
      }
      (**(code **)(**(int **)((int)this + 4) + 8))(pwVar5);
      FUN_004111dc(_Str);
      return true;
    }
    iVar1 = __wcsnicmp(param_1,L` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `,0xf);
      if ((iVar1 == 0) || (iVar1 = __wcsnicmp(param_1,L` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `#OnAutoItStartRegister` | `0x00403a20` | `FUN_00403a20` | `Script Engine Host` | **CONFIRMED (Binary String Pointer)** |
| `,0xd);
    if (iVar1 == 0) {
      if (*(int *)((int)this + 0x20) != 0) {
        uVar4 = 0;
        do {
          iVar1 = __wcsicmp((wchar_t *)**(undefined4 **)(*(int *)((int)this + 0x1c) + uVar4 * 4),
                            param_2);
          if (iVar1 == 0) {
            return (bool)(((**(int **)(*(int *)((int)this + 0x2c) + uVar4 * 4) < 2) - 1U & 3) + 1);
          }
          uVar4 = uVar4 + 1;
        } while (uVar4 < *(uint *)((int)this + 0x20));
        return true;
      }
    }
    else {
      iVar1 = __wcsnicmp(param_1,L` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `,3), iVar1 == 0)) {
        param_1 = (wchar_t *)0x1;
        while (uVar3 = FUN_0046fd6c(param_4,pwVar5), (char)uVar3 != '\0') {
          *param_3 = *param_3 + 1;
          FUN_00444bbb(pwVar5);
          FUN_00444b5f(pwVar5);
          iVar1 = __wcsnicmp(pwVar5,L` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `,3), iVar1 == 0)) {
            param_1 = (wchar_t *)((int)param_1 + 1);
          }
          else {
            iVar1 = __wcsnicmp(pwVar5,L` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `,0xd);
            if (((iVar1 == 0) || (iVar1 = __wcsnicmp(pwVar5,L` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `,8);
      if (iVar1 == 0) {
        uVar3 = FUN_00444bfc((int)this,(int)(param_1 + 8),local_2004);
        iVar1 = *param_3;
        if ((char)uVar3 == '\x01') {
          uVar4 = FUN_00410190(param_2,local_2004);
          uVar4 = FUN_004033c0(this,local_2004,uVar4,(int)param_2,param_1,iVar1);
          return (char)uVar4 != '\0';
        }
        FUN_00454014((int)this,(int)param_2,iVar1,L` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `,param_1);
        return false;
      }
      iVar1 = __wcsnicmp(param_1,L` | `0x00403a20` | `FUN_00403a20` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILECREATENTFSLINK` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `WINGETPROCESS` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `ENVSET` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILEFINDFIRSTFILE` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `SHELLEXECUTE` | `0x00404170` | `FUN_00404170` | `Script Engine Host` | **CONFIRMED (Binary String Pointer)** |
| `WINGETHANDLE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `STRINGISINT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `ROUND` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLCREATERADIO` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `GUISETHELP` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `BINARYTOSTRING` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILEGETVERSION` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLCREATECONTEXTMENU` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `STRINGFORMAT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `HOTKEYSET` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `HTTPSETPROXY` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `INIRENAMESECTION` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `ASIN` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `UDPSEND` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLSETDEFBKCOLOR` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `WINGETCLASSLIST` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `STRINGREGEXP` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `PROCESSLIST` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLCREATELISTVIEWITEM` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `CONTROLFOCUS` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILERECYCLEEMPTY` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `CLIPGET` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `WINGETTEXT` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `ENVGET` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `MOUSEGETCURSOR` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `PROCESSWAIT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `SENDKEEPACTIVE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILEOPEN` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `STRINGTRIMRIGHT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLCREATEOBJ` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `WINGETCARETPOS` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLSETGRAPHIC` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `AUTOITWINGETTITLE` | `0x00404170` | `FUN_00404170` | `Script Engine Host` | **CONFIRMED (Binary String Pointer)** |
| `FILESELECTFOLDER` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `WINACTIVATE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUISETSTATE` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `INIREADSECTION` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `CONSOLEWRITE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `DLLCALLBACKFREE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLSENDTODUMMY` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLSETBKCOLOR` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLCREATEICON` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `UBOUND` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLGETHANDLE` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `SHUTDOWN` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLCREATECOMBO` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `TRAYSETTOOLTIP` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `INETGET` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `STRINGFROMASCIIARRAY` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILESETPOS` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `MOUSEGETPOS` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `WINEXISTS` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `BEEP` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `TRAYSETICON` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `DRIVEMAPDEL` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `TRAYCREATEITEM` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `TRAYITEMGETSTATE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `ISPTR` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLRECVMSG` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `TCPACCEPT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `DLLSTRUCTCREATE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLSETSTYLE` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `DLLSTRUCTSETDATA` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `DLLCALLBACKREGISTER` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILEEXISTS` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `ISOBJ` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `CDTRAY` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `DRIVEGETDRIVE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `SPLASHIMAGEON` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `UDPBIND` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `CONTROLSETTEXT` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `STRINGUPPER` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUIGETCURSORINFO` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `GUIREGISTERMSG` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `STRINGLEFT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `STRING` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLCREATELABEL` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `DRIVEGETSERIAL` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `WINWAIT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `STRINGISSPACE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `DIRGETSIZE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILECREATESHORTCUT` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `PLUGINOPEN` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `DRIVESETLABEL` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `WINSETONTOP` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `TRAYITEMGETTEXT` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `DRIVEGETTYPE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `INETGETINFO` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `STRINGSTRIPWS` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `CONTROLGETFOCUS` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILEFLUSH` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLSETLIMIT` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `FILEMOVE` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `FILEGETSHORTNAME` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `DIRMOVE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `BITAND` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `DRIVESPACETOTAL` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLSENDMSG` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `WINWAITACTIVE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `CONSOLEREAD` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `DIRCREATE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `STRINGISXDIGIT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `PROGRESSOFF` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `TOOLTIP` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `INETCLOSE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILERECYCLE` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `GUICTRLCREATEDATE` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `GUIDELETE` | `0x00404170` | `FUN_00404170` | `GUI & User Interface` | **CONFIRMED (Binary String Pointer)** |
| `PIXELSEARCH` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `STRINGISFLOAT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `SHELLEXECUTEWAIT` | `0x00404170` | `FUN_00404170` | `Script Engine Host` | **CONFIRMED (Binary String Pointer)** |
| `CONTROLMOVE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `TCPLISTEN` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `STRINGINSTR` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `FILECHANGEDIR` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `STRINGSPLIT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `BITNOT` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `TCPSHUTDOWN` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `INIREADSECTIONNAMES` | `0x00404170` | `FUN_00404170` | `Save / Storage File I/O` | **CONFIRMED (Binary String Pointer)** |
| `WINGETSTATE` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
| `BITOR` | `0x00404170` | `FUN_00404170` | `System / Engine Internal` | **CONFIRMED (Binary String Pointer)** |
