import storage

storage.remount("/", readonly=False)

m = storage.getmount("/")
m.label = "KLOTZ_R"

storage.remount("/", readonly=True)

storage.enable_usb_drive()
