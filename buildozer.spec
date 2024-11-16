[app]
# (str) Title of your application
title = Kivy Calculator

# (str) Package name
package.name = kivycalculator

# (str) Package domain (should be a domain you own)
package.domain = com.yourdomain

# (str) Source code file name (main Python file)
source.include_exts = py,png,jpg,kv,atlas
source.main = main.py

# (list) List of directories to be included (comma-separated)
source.include_dirs = data

# (str) Application version
version = 1.0

# (str) Application description
description = A simple calculator app built using Kivy

# (str) Author name
author = Your Name

# (str) Package identifier
package.identifier = com.yourdomain.kivycalculator

# (int) Minimum API level required (21 = Android 5.0)
android.api = 21

# (int) Target API level (auto will pick the latest)
android.minapi = 21
android.sdk = 31
android.ndk = 25b

# (str) Full screen mode (True for fullscreen)
fullscreen = 1

# (list) Permissions required by the app
android.permissions = INTERNET

# (list) Additional modules to be included (comma-separated)
requirements = python3,kivy

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash image
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Orientation: one of 'landscape', 'portrait' or 'sensor'
orientation = portrait

# (bool) If True, presplash animation using Gif images is enabled
presplash_animation = False

# (list) Additional jars to be included (comma-separated)
# android.add_jars =

# (str) The filename of the main script
entrypoint = main.py

# (bool) Copy the `.apk` to the directory specified below when the build finishes
# copy_to_bin = True
