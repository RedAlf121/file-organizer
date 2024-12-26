import argparse
import file_organizer
import importlib

def main(path,strategy):
    try:
        if not path or not strategy:
            raise Exception("Los parametros del comando son obligatorios, usar -h o --help para más información")
        strategy = importlib.import_module(f"organize_strategies.{strategy}")
        file_organizer.organize_directory(path,strategy)
    except ModuleNotFoundError:
        print("Estrategia no definida, revise con -h o --help para ver las estrategias disponibles")
    except Exception as e:
        e.with_traceback()

if __name__ == "__main__":
# Crear el parser
    parser = argparse.ArgumentParser(description="Organizador de archivos, requiere de dos parámetros. Path para la ruta y Strategy para las estrategias")
    
    # Añadir argumentos
    parser.add_argument("path", type=str, help="Ruta del directorio a organizar")
    parser.add_argument("strategy", type=str, help="Comando para la estrategia de organizacion, de momento solo esta anime")
    
    # Parsear los argumentos
    args = parser.parse_args()
    
    # Llamar a la función principal con los parámetros
    main(args.path, args.strategy)
