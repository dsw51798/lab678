import argparse


def main():
    parser = argparse.ArgumentParser(prog="Konwersja plików",
                                     description="Skrypt do konwersji plików .xml .json i .yml pomiędzy formatami")
    parser.add_argument('input_file', type=str, help='Ścieżka pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka pliku wyjściowego')

    args = parser.parse_args()


if __name__ == "__main__":
    main()
