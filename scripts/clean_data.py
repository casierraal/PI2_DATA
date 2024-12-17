import pandas as pd

# Cargar datos
def load_data(file_path):
    return pd.read_excel(file_path)

# Limpiar datos
def clean_data(df):
    df.dropna(inplace=True)  # Eliminar filas con valores nulos
    df.drop_duplicates(inplace=True)  # Eliminar duplicados
    return df

# Guardar datos limpios
def save_data(df, output_path):
    df.to_excel(output_path, index=False)

if __name__ == "__main__":
    # Ejemplo con archivo Internet.xlsx
    input_file = "../data/Internet.xlsx"
    output_file = "../data/Internet_cleaned.xlsx"
    
    data = load_data(input_file)
    cleaned_data = clean_data(data)
    save_data(cleaned_data, output_file)
    print("Datos limpiados y guardados exitosamente.")
