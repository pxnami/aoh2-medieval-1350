"""Add Medieval 1350 assets to a local AoH2 DE APK; output requires signing."""
import argparse
import copy
import shutil
import tempfile
import zipfile
from pathlib import Path


def replacements(apk, payload, version):
    updates = {}
    versions = ("4k", "14k") if version == "both" else (version,)
    for selected in versions:
        root = payload / selected
        if not root.is_dir():
            raise ValueError(f"Missing payload: {root}")
        for file in root.rglob("*"):
            if not file.is_file():
                continue
            name = "assets/" + file.relative_to(root).as_posix()
            data = file.read_bytes()
            if file.name == "Age_of_Civilizations":
                original = apk.read(name).decode("utf-8-sig")
                tokens = [token for token in original.strip().split(";") if token]
                for token in data.decode("utf-8").strip().split(";"):
                    if token and token not in tokens:
                        tokens.append(token)
                data = (";".join(tokens) + ";").encode("utf-8")
            elif file.suffix == ".properties":
                original = apk.read(name).decode("utf-8-sig")
                additions = data.decode("utf-8").splitlines()
                keys = {line.split("=", 1)[0].strip() for line in additions if "=" in line}
                lines = [line for line in original.splitlines()
                         if line.split("=", 1)[0].strip() not in keys]
                data = ("\n".join(lines + additions) + "\n").encode("utf-8")
            updates[name] = data
    return updates


def patch(source, destination, payload, version):
    if source.resolve() == destination.resolve():
        raise ValueError("Choose an output different from the input APK.")
    if destination.exists():
        raise ValueError("Output already exists; choose a new filename.")
    with zipfile.ZipFile(source) as apk:
        if "AndroidManifest.xml" not in apk.namelist() or "classes.dex" not in apk.namelist():
            raise ValueError("Input is not a standalone APK.")
        updates = replacements(apk, payload, version)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=destination.parent) as temp:
            staging = Path(temp) / "unsigned.apk"
            with zipfile.ZipFile(staging, "w", allowZip64=True) as output:
                for entry in apk.infolist():
                    name = entry.filename
                    signature = name.upper().startswith("META-INF/") and (
                        name.upper().endswith((".RSA", ".DSA", ".EC", ".SF"))
                        or name.upper() == "META-INF/MANIFEST.MF")
                    if signature or name in updates:
                        continue
                    info = copy.copy(entry)
                    with apk.open(entry) as incoming, output.open(info, "w") as outgoing:
                        shutil.copyfileobj(incoming, outgoing)
                for name, data in sorted(updates.items()):
                    output.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)
            with zipfile.ZipFile(staging) as result:
                for name, data in updates.items():
                    if result.read(name) != data:
                        raise ValueError(f"Asset verification failed: {name}")
                for entry in apk.infolist():
                    if entry.filename not in updates and not entry.filename.upper().startswith("META-INF/"):
                        saved = result.getinfo(entry.filename)
                        if (saved.CRC, saved.file_size) != (entry.CRC, entry.file_size):
                            raise ValueError(f"Unrelated file changed: {entry.filename}")
            staging.rename(destination)
    print(f"Added/merged {len(updates)} assets: {destination}")
    print("UNSIGNED: align and sign before installation. Phone gameplay remains untested.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("apk", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--version", choices=("4k", "14k", "both"), default="both")
    args = parser.parse_args()
    try:
        patch(args.apk, args.output, Path(__file__).parent / "payload", args.version)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        parser.exit(1, f"Error: {error}\n")


if __name__ == "__main__":
    main()
