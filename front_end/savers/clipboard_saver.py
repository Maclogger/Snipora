from PIL import Image
import io
import platform
import subprocess
from front_end.savers.i_saver import ISaver


class ClipboardSaver(ISaver):
    def save(self, screenshot_path: str) -> bool:
        try:
            # Načítanie obrázka
            img = Image.open(screenshot_path)

            # Uloženie obrázka do pamäťového bufferu vo formáte PNG
            output = io.BytesIO()
            img.save(output, format="PNG")
            image_data = output.getvalue()
            output.close()

            # Rozlíšenie platformy
            current_platform = platform.system().lower()

            if "windows" in current_platform:
                self._copy_to_clipboard_windows(image_data)
            elif "darwin" in current_platform:  # macOS
                self._copy_to_clipboard_macos(image_data)
            elif "linux" in current_platform:
                self._copy_to_clipboard_linux(image_data)
            else:
                raise NotImplementedError(f"Unsupported platform: {current_platform}")

            return True
        except Exception as e:
            print(f"Error copying image to clipboard: {e}")
            return False

    @staticmethod
    def _copy_to_clipboard_windows(image_data: bytes):
        import win32clipboard  # pywin32 library is required
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, image_data[14:])  # Skip BMP header
        win32clipboard.CloseClipboard()

    @staticmethod
    def _copy_to_clipboard_macos(image_data: bytes):
        process = subprocess.Popen(
            ['osascript', '-e', 'set the clipboard to (read (POSIX file "/dev/stdin") as PNG picture)'],
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        process.communicate(input=image_data)

    @staticmethod
    def _copy_to_clipboard_linux(image_data: bytes):
        # Requires xclip installed
        try:
            process = subprocess.Popen(
                ['xclip', '-selection', 'clipboard', '-t', 'image/png'],
                stdin=subprocess.PIPE,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            process.stdin.write(image_data)  # Priamo zapisujeme dáta
            process.stdin.close()           # Uzatvoríme stdin, aby proces pokračoval
            process.wait()                  # Počkáme, kým sa proces ukončí
        except FileNotFoundError:
            raise RuntimeError("xclip is required for clipboard functionality on Linux.")


if __name__ == "__main__":
    saver = ClipboardSaver()
    success = saver.save("test.png")
    print(success)
