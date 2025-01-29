from cx_Freeze import setup, Executable
import sys

# Definir as opções para cx_Freeze
build_exe_options = {
    "packages": ["pandas", "tkinter"],  # Inclua aqui quaisquer outros pacotes necessários
    "include_files": [],  # Se você precisar incluir arquivos adicionais, liste-os aqui
    "excludes": [],  # Exclua pacotes que não são necessários
}

# Ajuste o executável
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use "Console" para aplicativos de linha de comando

# Configuração
setup(
    name="Agrupador de linhas",
    version="1.0",
    description="Este código é uma aplicação gráfica em Python que utiliza tkinter e pandas para processar arquivos CSV. A aplicação permite ao usuário selecionar um arquivo CSV, processá-lo para agrupar dados, e salvar o resultado em um novo arquivo CSV.",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base=base, icon="path/to/icon.ico")]
)
