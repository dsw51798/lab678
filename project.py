import argparse
import json
import yaml
import xmltodict


def load_json(path):
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError as error:
        print("Składnia pliku nie jest poprawna: " + error)
        return
    except Exception as error:
        print("Wystąpił błąd: " + error)
        return
    except FileNotFoundError as error:
        print("Nie znaleziono danego pliku: " + error)
        return


def save_json(data, path):
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
            print(f"Dane pomyślnie zapisane do {path}.")
    except Exception as error:
        print("Wystąpił bład: " + error)


def load_yaml(path):
    try:
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
            return data
    except yaml.YAMLError as error:
        print("Składnia pliku nie jest poprawna: " + error)
        return
    except Exception as error:
        print("Wystąpił błąd: " + error)
        return
    except FileNotFoundError as error:
        print("Nie znaleziono danego pliku: " + error)
        return


def save_yaml(data, path):
    try:
        with open(path, 'w') as f:
            yaml.safe_dump(data, f, default_flow_style=False)
            print(f"Dane pomyślnie zapisane do {path}.")
    except Exception as error:
        print("Wystąpił bład: " + error)


def load_xml(path):
    try:
        with open(path, 'r') as f:
            data = xmltodict.parse(f.read())
            return data
    except xmltodict.expat.ExpatError as error:
        print("Składnia pliku nie jest poprawna: " + error)
        return
    except Exception as error:
        print("Wystąpił błąd: " + error)
        return
    except FileNotFoundError as error:
        print("Nie znaleziono danego pliku: " + error)
        return


def save_xml(data, path):
    try:
        with open(path, 'w') as f:
            xml_data = xmltodict.unparse(data, pretty=True)
            print(f"Dane pomyślnie zapisane do {path}.")
    except Exception as error:
        print("Wystąpił bład: " + error)


def main():
    parser = argparse.ArgumentParser(prog="Konwersja plików",
                                     description="Skrypt do konwersji plików .xml .json i .yml pomiędzy formatami")
    parser.add_argument('input_file', type=str, help='Ścieżka pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka pliku wyjściowego')

    args = parser.parse_args()

    if args.input_file.endswith('.json'):
        data = load_json(args.input_file)
    elif args.input_file.endswith(('.yml', '.yaml')):
        data = load_yaml(args.input_file)
    elif args.input_file.endswith('.xml'):
        data = load_xml(args.input_file)
    else:
        print("Podany format pliku wejścia nie jest obsługiwany.")

    if data:
        if args.output_file.endswith('.json'):
            save_json(data, args.output_file)
        elif args.output_file.endswith(('.yml', '.yaml')):
            save_yaml(data, args.output_file)
        elif args.output_file.endswith('.xml'):
            save_xml(data, args.output_file)
        else:
            print("Podany format pliku wejścia nie jest obsługiwany.")
    else:
        print("Operacja zakończona niepowodzeniem.")


if __name__ == "__main__":
    main()
