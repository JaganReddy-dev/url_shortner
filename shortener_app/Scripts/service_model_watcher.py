import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


SERVICES_DIR = Path("shortener_app/Services")
MODELS_BASE = Path("shortener_app/Models/V1")
REQUEST_DIR = MODELS_BASE / "Request"
RESPONSE_DIR = MODELS_BASE / "Response"


def to_pascal_case(name: str) -> str:
    return "".join(word.capitalize() for word in name.split("_"))


def write_model(path: Path, class_name: str):
    path.parent.mkdir(parents=True, exist_ok=True)

    content = f"""# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY
from pydantic import BaseModel


class {class_name}(BaseModel):
    pass
"""

    if not path.exists():
        path.write_text(content)
        print(f"✅ Created {path}")


def delete_model(path: Path):
    if path.exists():
        path.unlink()
        print(f"🗑️  Deleted {path}")


def rename_model(old_path: Path, new_path: Path, old_class: str, new_class: str):
    if not old_path.exists():
        return

    content = old_path.read_text()
    content = content.replace(old_class, new_class)

    new_path.parent.mkdir(parents=True, exist_ok=True)
    new_path.write_text(content)
    old_path.unlink()

    print(f"🔁 Renamed {old_path} → {new_path}")


def sync_models(service_name: str):
    pascal = to_pascal_case(service_name)

    req_file = REQUEST_DIR / f"{service_name}.py"
    res_file = RESPONSE_DIR / f"{service_name}.py"

    # Response always exists
    write_model(res_file, f"{pascal}Response")

    # Request depends on GET
    if service_name.startswith("get"):
        delete_model(req_file)
    else:
        write_model(req_file, f"{pascal}Request")


class ServiceWatcher(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith(".py"):
            return

        service_name = Path(event.src_path).stem
        sync_models(service_name)

    def on_moved(self, event):
        if not event.src_path.endswith(".py") or not event.dest_path.endswith(".py"):
            return

        old_name = Path(event.src_path).stem
        new_name = Path(event.dest_path).stem

        old_pascal = to_pascal_case(old_name)
        new_pascal = to_pascal_case(new_name)

        # Rename response
        rename_model(
            RESPONSE_DIR / f"{old_name}.py",
            RESPONSE_DIR / f"{new_name}.py",
            f"{old_pascal}Response",
            f"{new_pascal}Response",
        )

        # Rename or delete request
        if new_name.startswith("get"):
            delete_model(REQUEST_DIR / f"{old_name}.py")
        else:
            rename_model(
                REQUEST_DIR / f"{old_name}.py",
                REQUEST_DIR / f"{new_name}.py",
                f"{old_pascal}Request",
                f"{new_pascal}Request",
            )

        sync_models(new_name)


def main():
    observer = Observer()
    observer.schedule(ServiceWatcher(), str(SERVICES_DIR), recursive=True)
    observer.start()

    print("👀 Watching Services directory...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
