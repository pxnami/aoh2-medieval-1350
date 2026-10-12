# Android port — experimental

Mod-only payload and local APK patcher for both **4K (4,269 provinces)** and **14K (13,892 provinces)**. The scenarios, English events and custom 14K countries are the same as the desktop packages. No APK, game executable, signing key or full map is distributed here.

## Status

Asset repacking was checked against a supplied Android APK named version `2.01957652812950`. Its Earth 1440 and Earth14K 1354 province-owner files match the desktop foundations byte for byte, and its map configurations have the expected province counts. The filename is not proof of the APK's authenticity or its manifest version.

A combined unsigned APK was built locally. All 61 added/merged assets were read back; CRCs and sizes of unrelated non-signature entries were preserved. Android installation, Java deserialization and gameplay have **not** been tested on a device. This release is experimental, not a confirmed working Android release.

## Build your local copy

Requires Python 3.9 or newer, a standalone APK from your own game installation, a JDK with `keytool`, and Android SDK Build Tools (`zipalign` and `apksigner`). Split APK sets are not supported by this script.

1. Download and extract the Android mod ZIP.
2. Run from its extracted `android` directory:

```text
python patch_apk.py original.apk medieval1350-unsigned.apk --version both
```

Use `--version 4k` or `--version 14k` to include only one map's scenario. The input APK is retained. An existing output is refused. The patcher merges scenario indexes and custom country translations with the APK's existing assets, preserving its other scenarios and translations. It does not alter DEX code, the manifest, permissions, package ID, payment/licensing logic or native libraries. Original signatures are invalidated by repacking and removed from the output.

3. Create your own local signing key (passwords are requested interactively):

```text
keytool -genkeypair -keystore medieval1350-local.jks -alias medieval1350 -keyalg RSA -keysize 2048 -validity 3650
zipalign -P 16 -f 4 medieval1350-unsigned.apk medieval1350-aligned.apk
apksigner sign --ks medieval1350-local.jks --out medieval1350-signed.apk medieval1350-aligned.apk
apksigner verify --verbose medieval1350-signed.apk
```

Use recent SDK Build Tools supporting `zipalign -P 16`. Alignment must happen before signing. Keep the private signing key local; do not upload it. See the official [apksigner documentation](https://developer.android.com/tools/apksigner) and [zipalign documentation](https://developer.android.com/tools/zipalign).

4. Back up/export your saves before changing the installed app. A copy signed with your key cannot update an installation signed by a different key. Do not uninstall until your saves are backed up; uninstallation can erase app data. Installation may also be constrained by the original game's licensing or delivery setup, which this patcher does not bypass.
5. Install your signed local APK through Android's package installer, then select Earth or Earth 14K and the corresponding 1350 scenario. Start a new campaign.
6. Check the starting date and country borders, advance a turn and check the English plague event. Please report your Android version, game version and any loading error.

The payload is not a desktop `mods` folder and cannot simply be copied to Downloads or an assumed `Android/data` directory. Normal Android app storage permissions do not guarantee access to the game's private files.

The patched APK is for local use. GitHub distributes only the mod and patching tool; obtain the game separately. Existing historical limitations and complete feature documentation are in the repository's main README.
