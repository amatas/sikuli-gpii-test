import unittest
import shutil
from sikuli.Sikuli import *

# We need to enable OCR
Settings.OcrTextRead = True
Settings.OcrTextSearch = True

# Remove the logs, only need the unittest output
Settings.ActionLogs = False
Settings.InfoLogs = False
Settings.DebugLogs = False

class SikuliGPIITestResult(unittest.TextTestResult):

    # This method captures the entire screen and saves a screenshot
    def captureScreen(self, test_name):
        screen = Screen()
        file = screen.capture(screen.getBounds())
        shutil.move(file, os.path.join(r'C:\Screenshots', test_name + '-' + os.path.basename(file)))

    # Method overloaded to make a screenshot when a test fails
    def addFailure(self, test, err):
        self.captureScreen(str(test))
        super(SikuliGPIITestResult, self).addFailure(test, err)

    # Method overloaded to make a screenshot when a test fails
    def addError(self, test, err):
        self.captureScreen(str(test))
        super(SikuliGPIITestResult, self).addError(test, err)

# The methods can be found at
# http://sikulix-2014.readthedocs.io/en/latest/genindex.html
class TestInstallation(unittest.TestCase):
    def test_01_init_install_gpii(self):
        doubleClick("installer-icon.png")
        click("next-button.png")
        click("accept-terms.png")
        click("next-button.png")
        assert exists("location-label.png")

    def test_02_check_default_installation_path(self):
        startLocPath = find(Pattern("location-label.png"))
        PathText = Region(startLocPath.getX() + 80, startLocPath.getY(), 170, 19).text()
        # The OCR is not so accurate, and sometimes the spaces between letters
        # are missing. In this case it doesn't recognizes the space between
        # 'Program' and 'Files'.
        assert PathText == 'C:\\ProgramFiles (x86)\\GPII\\'

    def test_03_finish_installation(self):
        click("next-button.png")
        click("install-button.png")
        wait("completed-label.png",45)
        click("finish-button.png")

    def test_04_check_desktop_launcher_shortcut(self):
        assert exists("start-shortcut.png")

    def test_05_check_desktop_usb_shortcut(self):
        assert exists("RFID-shortcut.png")

    def test_06_check_desktop_nfc_shortcut(self):
        assert exists("USB-shortcut.png")

    def test_07_uninstall(self):
        doubleClick("installer-icon.png")
        click("next-button.png")
        click("remove-button.png")
        wait("remove-gpii-label.png")
        click("remove-button.png")
        wait("completed-label.png",60)
        click("finish-button.png")
        assert not (exists("start-shortcut.png") or exists("RFID-shortcut.png") or exists("USB-shortcut.png"))

suite = unittest.TestLoader().loadTestsFromTestCase(TestInstallation)
unittest.TextTestRunner(resultclass=SikuliGPIITestResult,verbosity=2).run(suite)
