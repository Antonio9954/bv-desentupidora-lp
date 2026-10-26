"""Gera os artigos do blog no mesmo formato do artigo pilar.
Uso (na raiz do repo): python tools/gerar_artigos.py publicar/blog
O conteúdo de cada artigo fica em tools/artigos.py. Topo, rodapé, autor e empresa são copiados do artigo pilar.
"""
import json
import re
import sys
from pathlib import Path

BLOG = Path(sys.argv[1])
SITE = "https://bvdesentupidora.com.br"
DATA = "2026-10-26"
DATA_BR = "26/10/2026"
LINKEDIN = "https://www.linkedin.com/in/bvdesentupidora/"

pilar = (BLOG / "niveis-de-entupimento" / "index.html").read_text(encoding="utf-8")
GTM_HEAD = re.search(r"<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager -->", pilar, re.S).group(0)
GTM_BODY = re.search(r"<!-- Google Tag Manager \(noscript\) -->\n<noscript>.*?</noscript>", pilar, re.S).group(0)
TOPO = re.search(r'<header class="topo">.*?</header>', pilar, re.S).group(0)
RODAPE = re.search(r'<footer class="rodape">.*?</footer>', pilar, re.S).group(0)
SCRIPT = re.search(r"<script>\ndocument\.querySelectorAll\('\.video-facade'\).*?</script>", pilar, re.S).group(0)
SOBRE = re.search(r'<section class="sobre-autor">.*?</section>', pilar, re.S).group(0)
EMPRESA = [n for n in json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', pilar, re.S).group(1))["@graph"]
           if n["@type"] in ("Plumber", "Person")]
for n in EMPRESA:
    if n["@type"] == "Person":
        n.setdefault("url", LINKEDIN)

VIDEOS = {
    "bn_lcqH_SDA": dict(name="Como o cano enche de gordura: caso real", up="2026-09-24T13:00:00-07:00", dur=None, short=True,
                        desc="Lucas Nonato, da BV Desentupidora, mostra como a gordura gruda nas paredes do cano, estreita a passagem da água e causa entupimentos que voltam depois de desobstruídos."),
    "rIHn8FNLqQM": dict(name="Olha o que saiu desse cano nesse desentupimento", up="2026-07-26T04:00:07-07:00", dur="PT6M56S", short=False,
                        desc="Desentupimento da rede pluvial de uma casa em Heitoraí (GO). Lucas Nonato, da BV Desentupidora, mostra o que foi retirado de dentro do cano: chinelo infantil, tampa de garrafa, lata de cerveja, lápis, escova de dente, papel, cabelo e muita terra."),
    "BjAMEKyD2ZQ": dict(name="Dicas para Evitar Entupimentos em Casas de Eventos | BV Desentupidora", up="2026-07-24T14:40:16-07:00", dur="PT1M10S", short=True,
                        desc="Atendimento real em uma casa de eventos em que o vaso sanitário e o ralo do banheiro entupiram juntos durante um evento, com dicas de Lucas Nonato, da BV Desentupidora, para evitar entupimentos em casas de eventos, buffets e salões de festa."),
    "qkuLm06mmnM": dict(name="Serviço de desentupimento residencial na cidade de Itaberaí GO", up="2026-05-31T05:31:29-07:00", dur="PT1M20S", short=True,
                        desc="Desentupimento residencial de pia e esgoto no bairro Beira Rio, em Itaberaí (GO), feito pela BV Desentupidora sem quebrar piso. O vídeo mostra o que costuma entupir a pia e os equipamentos usados no atendimento."),
    "cvyNzEpSA-U": dict(name="Serviço de desentupimento de pia: vídeo real", up="2026-09-07T05:32:05-07:00", dur="PT45S", short=True,
                        desc="Desentupimento de pia feito pela BV Desentupidora em 31/08/2026, em Inhumas (GO), com a retirada de pedras de gordura que obstruíam a tubulação."),
    "FZJdTEZoqXE": dict(name="Antes e depois da pia: serviço real em Goiânia", up="2026-10-20T05:10:04-07:00", dur="PT35S", short=True,
                        desc="Antes e depois de um desentupimento de pia com limpeza de caixa de gordura feito pela BV Desentupidora em Goiânia: a caixa estava com a água totalmente preta e, depois do serviço, a água voltou a ficar transparente e a pia passou a escoar normalmente."),
    "D4aA6c9-8lc": dict(name="Desentupimento de restaurante em Goiânia GO", up="2026-10-17T07:00:24-07:00", dur="PT30S", short=False,
                        desc="Restaurante em Goiânia com a rede de esgoto totalmente parada e sem nenhuma caixa de inspeção. Lucas Nonato, da BV Desentupidora, abriu a fossa e entrou com o hidrojato pelo cano que chega até ela."),
    "cjH3O35wWQI": dict(name="Olha o tanto de gordura no final", up="2026-09-28T07:15:20-07:00", dur="PT1M9S", short=True,
                        desc="Lucas Nonato, da BV Desentupidora, mostra na prática como a gordura se acumula nas paredes internas da tubulação e por que esse acúmulo diminui a passagem da água até provocar o entupimento."),
}

# (texto, url para o "citation" do JSON-LD ou None)
FONTES = {
    "nbr8160": ("ABNT. <em>NBR 8160:1999 — Sistemas prediais de esgoto sanitário: projeto e execução</em>. Define caixa de gordura, caixa de inspeção e caixa sifonada.", None),
    "nbr10844": ("ABNT. <em>NBR 10844:1989 — Instalações prediais de águas pluviais</em>. Trata de calhas, condutores e da rede que leva a água da chuva para fora do imóvel.", None),
    "saneago_oleo": ('Governo de Goiás / Saneago. <a href="https://goias.gov.br/saneago-alerta-para-o-descarte-correto-do-oleo-de-cozinha/" rel="nofollow noopener" target="_blank">Saneago incentiva descarte correto do óleo de cozinha</a>. Estudo da Saneago aponta que 25% dos extravasamentos de esgoto são causados pelo descarte de óleo em pias e ralos.',
                     "https://goias.gov.br/saneago-alerta-para-o-descarte-correto-do-oleo-de-cozinha/"),
    "tribuna": ('Tribuna do Planalto. <a href="https://tribunadoplanalto.com.br/?p=62957" rel="nofollow noopener" target="_blank">Como usar a rede de esgoto corretamente e evitar entupimentos — Dicas da Saneago</a>.', "https://tribunadoplanalto.com.br/?p=62957"),
    "eng360": ('Engenharia 360. <a href="https://engenharia360.com/esgoto-edificios-pela-nbr-8160/" rel="nofollow noopener" target="_blank">Esgoto em edifícios pela NBR 8160</a>.', "https://engenharia360.com/esgoto-edificios-pela-nbr-8160/"),
    "bobvila": ('Bob Vila. <a href="https://www.bobvila.com/articles/how-to-use-a-plunger/" rel="nofollow noopener" target="_blank">How to Use a Plunger</a> (técnica de uso do desentupidor de ventosa).', "https://www.bobvila.com/articles/how-to-use-a-plunger/"),
    "epa": ("EPA (Agência de Proteção Ambiental dos EUA). <em>Stormwater Best Management Practices</em>. Recomenda a manutenção preventiva dos sistemas de drenagem para reduzir obstruções e alagamentos.", None),
    "epa_fog": ("EPA (Agência de Proteção Ambiental dos EUA). Materiais sobre FOG (<em>fats, oils and grease</em>: gorduras, óleos e graxas), apontados como causa importante de bloqueios em sistemas de esgoto.", None),
    "he2011": ("He, X. et al. (2011). <em>Evidence for fat, oil, and grease (FOG) deposit formation mechanisms in sewer lines</em>. Environmental Science &amp; Technology. Mostra que ácidos graxos reagem com cálcio e formam depósitos sólidos parecidos com sabão.", None),
    "fabricantes": ("Tigre e Amanco Wavin. Materiais técnicos sobre sistemas prediais hidráulicos e prevenção de obstruções em tubulações.", None),
    "tigre45": ("Tigre. Ficha técnica dos tubos de esgoto: temperatura máxima de trabalho de 45 °C em regime não contínuo.", None),
    "sanepar": ("Sanepar (Companhia de Saneamento do Paraná). Orientações sobre caixa de gordura: limpeza a cada 3 a 6 meses em residências e com frequência mensal ou quinzenal em cozinhas comerciais.", None),
    "anvisa": ("Anvisa. Orientações sobre produtos de limpeza: usar cada produto sozinho ou diluído em água, sem misturar. Disque-Intoxicação: 0800-722-6001.", None),
    "bf_metodos": ('Benjamin Franklin Plumbing (Ann Arbor). <a href="https://www.benjaminfranklinplumbing.com/ann-arbor/blog/2025/november/which-methods-are-most-effective-for-drain-cleaning/" rel="nofollow noopener" target="_blank">Which Methods Are Most Effective for Drain Cleaning?</a> (2025). Hidrojateamento opera geralmente entre 1.500 e 4.000 PSI.',
                   "https://www.benjaminfranklinplumbing.com/ann-arbor/blog/2025/november/which-methods-are-most-effective-for-drain-cleaning/"),
    "bf_mitos": ('Benjamin Franklin Plumbing (Redmond). <a href="https://www.benjaminfranklinplumbing.com/redmond/blog/2026/january/debunking-common-drain-cleaning-myths-what-options-really-work/" rel="nofollow noopener" target="_blank">Debunking Common Drain Cleaning Myths</a> (2026).',
                 "https://www.benjaminfranklinplumbing.com/redmond/blog/2026/january/debunking-common-drain-cleaning-myths-what-options-really-work/"),
    "wikem": ('WikEM. <a href="https://wikem.org/wiki/Hydrogen_sulfide_toxicity/pt" rel="nofollow noopener" target="_blank">Toxicidade do sulfeto de hidrogênio</a>. Em concentração alta, o gás pode causar perda de consciência em poucas respirações.', "https://wikem.org/wiki/Hydrogen_sulfide_toxicity/pt"),
    "campo": ("Experiência de campo da equipe BV Desentupidora (atendimentos em Goiânia, Itaberaí, Inhumas, Heitoraí e região).", None),
}

ARTIGOS = {
    "niveis-de-entupimento": "Como saber se o entupimento é grave: os 4 níveis",
    "rede-pluvial-entupida": "Rede pluvial entupida: sinais, causas e prevenção antes das chuvas",
    "vaso-sanitario-entupido": "Vaso sanitário entupido: o que fazer passo a passo",
    "precisa-quebrar-piso-para-desentupir": "Precisa quebrar o piso para desentupir?",
    "desentupir-pia-com-gordura": "Como desentupir pia com gordura: o que funciona de verdade",
    "limpeza-caixa-de-gordura": "Caixa de gordura: de quanto em quanto tempo limpar",
    "como-funciona-hidrojateamento": "Como funciona o hidrojateamento",
    "pode-jogar-oleo-na-pia": "Pode jogar óleo na pia? E o que não usar para desentupir",
}


def video(vid, label, alt, legenda):
    cls = "video" if VIDEOS[vid]["short"] else "video video-h"
    return f'''<figure class="{cls}">
      <button class="video-facade" type="button" data-id="{vid}" aria-label="Assistir ao vídeo: {label}">
        <img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="{alt}" width="480" height="360" loading="lazy">
        <span class="play" aria-hidden="true"></span>
      </button>
      <figcaption>{legenda}</figcaption>
    </figure>'''


FOTO_GORDURA = '''<figure class="foto-vertical">
      <img src="../img/nivel-4-cano-de-gordura.webp" alt="Pedaços de gordura endurecida, alguns no formato do cano, retirados de uma caixa de gordura e colocados no chão ao lado da caixa aberta" width="634" height="1378" loading="lazy">
      <figcaption>Gordura endurecida no formato do cano, retirada de uma caixa de gordura.</figcaption>
    </figure>'''


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")


def gerar(a):
    url = f"{SITE}/blog/{a['slug']}/"
    texto = re.sub(r"<[^>]+>", " ", a["corpo"])
    minutos = max(3, round(len(texto.split()) / 200))
    citacoes = [FONTES[f][1] for f in a["fontes"] if FONTES[f][1]] + [a["linkedin"]]
    post = {"@type": "BlogPosting", "@id": url + "#artigo", "headline": a["h1"], "description": a["desc"], "inLanguage": "pt-BR",
            "datePublished": DATA, "dateModified": DATA, "author": {"@id": f"{SITE}/#lucas-nonato"},
            "publisher": {"@id": f"{SITE}/#empresa"}, "mainEntityOfPage": url, "image": a["imagem"], "keywords": a["keywords"],
            "about": [{"@type": "Thing", "name": t} for t in a["sobre"]],
            "isBasedOn": {"@type": "CreativeWork", "url": a["linkedin"], "author": {"@id": f"{SITE}/#lucas-nonato"}},
            "citation": citacoes}
    if a.get("videos"):
        post["video"] = [{"@id": f"{url}#video-{v}"} for v in a["videos"]]
    grafo = list(EMPRESA) + [post,
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": f"{SITE}/blog/"},
            {"@type": "ListItem", "position": 3, "name": a["migalha"], "item": url}]}]
    for vid in a.get("videos", []):
        v = VIDEOS[vid]
        o = {"@type": "VideoObject", "@id": f"{url}#video-{vid}", "name": v["name"], "description": v["desc"],
             "thumbnailUrl": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg", "uploadDate": v["up"]}
        if v["dur"]:
            o["duration"] = v["dur"]
        o.update({"contentUrl": f"https://www.youtube.com/shorts/{vid}" if v["short"] else f"https://www.youtube.com/watch?v={vid}",
                  "embedUrl": f"https://www.youtube-nocookie.com/embed/{vid}", "inLanguage": "pt-BR",
                  "author": {"@id": f"{SITE}/#lucas-nonato"}, "publisher": {"@id": f"{SITE}/#empresa"}})
        grafo.append(o)
    grafo.append({"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in a["faq"]]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False, indent=2)

    faq = "\n".join(f"    <details>\n      <summary>{q}</summary>\n      <p>{r}</p>\n    </details>" for q, r in a["faq"])
    fontes = "\n".join(f"        <li>{FONTES[f][0]}</li>" for f in a["fontes"])
    fontes += f'\n        <li>Lucas Nonato. <a href="{a["linkedin"]}" rel="noopener" target="_blank">Relato original deste atendimento no LinkedIn</a>.</li>'
    leia = "\n".join(f'        <li><a href="../{s}/">{ARTIGOS[s]}</a></li>' for s in a["leia"])

    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

{GTM_HEAD}

<title>{a["title"]}</title>
<meta name="description" content="{esc(a["desc"])}">
<meta name="author" content="Lucas Nonato">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">

<meta property="og:type" content="article">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="BV Desentupidora">
<meta property="og:title" content="{esc(a["h1"])}">
<meta property="og:description" content="{esc(a["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{a["imagem"]}">
<meta property="article:published_time" content="{DATA}">
<meta property="article:modified_time" content="{DATA}">
<meta property="article:author" content="{LINKEDIN}">

<link rel="icon" href="../../assets/favicon-48.png" type="image/png" sizes="48x48">
<link rel="stylesheet" href="../blog.css">

<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{GTM_BODY}

{TOPO}

<main>
  <nav class="migalha" aria-label="Você está em"><a href="../../">Início</a> › <a href="../">Blog</a> › {a["migalha"]}</nav>

  <article>
    <h1>{a["h1"]}</h1>

    <div class="autor-linha">
      <img src="../img/lucas-nonato.webp" alt="Lucas Nonato, fundador da BV Desentupidora" width="48" height="48">
      <div>
        Por <strong>Lucas Nonato</strong>, técnico em desentupimento e hidrojateamento há 10 anos em Goiânia e região<br>
        Publicado em <time datetime="{DATA}">{DATA_BR}</time> · Atualizado em <time datetime="{DATA}">{DATA_BR}</time> · {minutos} min de leitura
      </div>
    </div>

    <div class="resumo">
      <span class="rotulo">Resumo rápido</span>
      <p>{a["resumo"]}</p>
    </div>

{a["corpo"]}

    <h2>Perguntas frequentes</h2>
{faq}

    {SOBRE}

    <section>
      <h2>Fontes</h2>
      <ol class="fontes">
{fontes}
      </ol>
    </section>

    <nav class="leia-tambem" aria-label="Leia também">
      <h2>Leia também</h2>
      <ul>
{leia}
      </ul>
    </nav>
  </article>
</main>

{RODAPE}
{SCRIPT}
</body>
</html>
'''
    destino = BLOG / a["slug"] / "index.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8", newline="\n")
    print(f"{a['slug']}: title {len(a['title'])}c, desc {len(a['desc'])}c, {minutos} min, bv={texto.count('BV')}")


exec(Path(__file__).with_name("artigos.py").read_text(encoding="utf-8"))
