"""Monta a pasta de conteúdo do JupyterLite.

Copia o notebook e os dados para `destino` e insere no início do notebook
uma célula que instala o ipywidgets, que não vem incluído no Pyodide.
O notebook original do repositório não é alterado.
"""
import json
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
NOTEBOOK = "TP_Matheus_de_Sousa.ipynb"
DADOS = ["SN_m_tot_V2.0.txt", "SN_d_tot_V2.0.txt"]

CELULA_SETUP = {
    "cell_type": "code",
    "execution_count": None,
    "metadata": {},
    "outputs": [],
    "source": [
        "# Versão web (JupyterLite): o Python roda no navegador.\n",
        "# Para usar, vá em Run > Run All Cells e role até a interface no fim da seção 3.\n",
        "%pip install -q ipywidgets",
    ],
}


def main(destino: Path) -> None:
    destino.mkdir(parents=True, exist_ok=True)
    for nome in DADOS:
        shutil.copy(RAIZ / nome, destino / nome)

    nb = json.loads((RAIZ / NOTEBOOK).read_text(encoding="utf-8"))
    nb["cells"].insert(0, CELULA_SETUP)
    nb["metadata"]["kernelspec"] = {
        "display_name": "Python (Pyodide)",
        "language": "python",
        "name": "python",
    }
    (destino / NOTEBOOK).write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
