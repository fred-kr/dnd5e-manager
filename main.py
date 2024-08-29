if __name__ == "__main__":
    import sys
    import argparse

    from src.dnd_app.app import EquipmentManager

    parser = argparse.ArgumentParser()
    parser.add_argument("--clean-config", action="store_true")

    args = parser.parse_args()

    clean_config = bool(args.clean_config)
    app = EquipmentManager(clean_config, sys.argv)
    app.mw.show()
    sys.exit(app.exec())
