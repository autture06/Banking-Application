import AppKit

class AppDelegate(AppKit.NSObject):
    def applicationSupportsSecureRestorableState(self):
        return True

def enable_secure_restorable_state():
    app = AppKit.NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    app.setDelegate_(delegate)

if __name__ == "__main__":
    enable_secure_restorable_state()
