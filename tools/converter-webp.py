"""
Converte fotos (JPG, PNG, HEIC já convertido etc.) para WebP leve, para o blog.

Uso:
    python tools/converter-webp.py pasta-com-fotos/ blog/img/

- Redimensiona para no máximo 1200 px de largura (mantém a proporção).
- Corrige a rotação das fotos de celular.
- Remove dados de localização (EXIF/GPS) por segurança.
- Qualidade 80 (boa imagem com arquivo pequeno).
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

LARGURA_MAX = 1200
QUALIDADE = 80
EXTENSOES = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}


def converter(origem: Path, destino_dir: Path) -> None:
    with Image.open(origem) as img:
        img = ImageOps.exif_transpose(img)
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")
        if img.width > LARGURA_MAX:
            altura = round(img.height * LARGURA_MAX / img.width)
            img = img.resize((LARGURA_MAX, altura), Image.LANCZOS)
        destino = destino_dir / (origem.stem.lower().replace(" ", "-") + ".webp")
        img.save(destino, "WEBP", quality=QUALIDADE, method=6)
    antes = origem.stat().st_size / 1024
    depois = destino.stat().st_size / 1024
    print(f"{origem.name}: {antes:,.0f} KB -> {destino.name}: {depois:,.0f} KB ({img.width}x{img.height})")


def main() -> None:
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    origem_dir, destino_dir = Path(sys.argv[1]), Path(sys.argv[2])
    destino_dir.mkdir(parents=True, exist_ok=True)
    arquivos = [p for p in sorted(origem_dir.iterdir()) if p.suffix.lower() in EXTENSOES]
    if not arquivos:
        print("Nenhuma imagem encontrada.")
    for p in arquivos:
        converter(p, destino_dir)


if __name__ == "__main__":
    main()
