import os
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"]="C:/apps/anaconda3/envs/blockus/Library/lib/qt6/plugins/platforms"

from blokus_game import Blokus
import sys
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
   app = QApplication(sys.argv)

   game = Blokus()
   game.ui.show()

   sys.exit(app.exec())