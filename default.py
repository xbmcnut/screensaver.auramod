# -*- coding: utf-8 -*-
import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
import os
import sys

_addon = xbmcaddon.Addon()
_id = _addon.getAddonInfo('id')
_path = _addon.getAddonInfo('path')
_skin = os.path.basename(os.path.normpath(xbmcvfs.translatePath('special://skin/')))
_xml = 'Custom_Screensaver_1166.xml'


class Screensaver(xbmcgui.WindowXMLDialog):
    
    class ExitMonitor(xbmc.Monitor):
        
        def __init__(self, exit_callback):
            super().__init__()
            self.exit_callback = exit_callback
            
        def onScreensaverDeactivated(self):
            log('Screensaver Deactivated')
            self.exit_callback()
            
        def onScreensaverActivated(self):
            log('Screensaver Activated')

    def onInit(self):
        self.monitor = self.ExitMonitor(self.exit)
        
    def exit(self):
        self.close()
        
        
def log(msg, level=xbmc.LOGDEBUG):
    message = '{}: {}'.format(_id, msg)
    xbmc.log(msg=message, level=level)


if __name__ == '__main__':
    screensaver_gui = Screensaver(_xml, _path, 'Default', '1080p')
    screensaver_gui.doModal()
    del screensaver_gui
