[app]
# (str) Title of your application
title = Kivy Calculator

# (str) Package name
package.name = kivycalculator

# (str) Package domain (e.g., org.kivy)
package.domain = org.example

# (str) Source code directory (where your main.py is located)
source.dir = .

# (str) Main Python file (e.g., main.py)
source.main = main.py

# (str) Version of your application
version = 1.0

# (list) Supported screen orientations
orientation = portrait

# (list) Permissions needed by your app
permissions = INTERNET

# (list) List of external Python modules your app needs
requirements = python3, kivy

# (bool) Enable fullscreen mode
fullscreen = 1

# (list) Supported platforms
# Example: android, ios
android.arch = armeabi-v7a

# (str) Android NDK version
android.ndk = 21b

# (str) Android SDK version
android.sdk = 31

# (bool) Enable compiling .py files into .pyo (optimized) files
android.compile_pyo = 1

# (str) Android log level (default: INFO)
android.log_level = INFO

# (str) Minimum Android API level
android.minapi = 21

# (str) Target Android API level
android.targetapi = 30

# (str) Android build type (debug or release)
android.build_type = debug
