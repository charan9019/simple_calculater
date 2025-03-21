[app]

title = Basic Kivy App
package.name = basicapp
package.domain = net.aesencryptornl
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy
version = 0.1
orientation = portrait

[buildozer]

log_level = 2
warn_on_root = 1

[buildozer.android]

fullscreen = 0
android.api = 30
android.minapi = 21
android.ndk = 19b
android.sdk = 24
android.entrypoint = org.kivy.android.PythonActivity
android.manifest.theme = @android:style/Theme.NoTitleBar
android.update_sdk = True
android.javac_target = 1.8
