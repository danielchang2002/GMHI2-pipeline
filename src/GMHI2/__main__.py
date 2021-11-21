from . import prerun


def main():
    up_to_date = prerun.check_versions()
    # if not up_to_date:
    #     return
    prerun.check_and_install_databases()


if __name__ == "__main__":
    main()
