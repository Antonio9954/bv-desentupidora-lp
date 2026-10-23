# Padrão de Artigos — Blog BV Desentupidora

Este arquivo é a regra fixa para **todo** artigo do blog (bvdesentupidora.com.br/blog/).
Se usar o Claude Code para criar um artigo novo, peça: "crie um artigo seguindo o PADRAO-BLOG.md".

Arquivos: o modelo de artigo fica em `blog-modelo/index.html` (fora de `publicar/`, não vai para o site). Cada artigo novo é uma cópia dele em `publicar/blog/<slug>/index.html`. Fotos: `python tools/converter-webp.py pasta-com-fotos/ publicar/blog/img/`. Os links internos são relativos (`../`, `../../`) para a página funcionar no site e na prévia do GitHub Pages.

---

## 1. Antes de escrever

- [ ] **1 artigo = 1 pergunta = 1 palavra-chave principal.**
- [ ] A palavra-chave **não** pode ser "desentupidora em Goiânia", "desentupidora 24h" ou o nome de uma cidade sozinha. Essas são da landing page, das páginas de serviço e do site de 90 páginas.
- [ ] Conferir se nenhum artigo já publicado responde à mesma pergunta (evitar canibalização).
- [ ] Separar a **prova real**: foto, vídeo ou caso atendido pela BV.

## 2. Estrutura obrigatória (nesta ordem)

1. **Título (H1)** com a palavra-chave no começo, como a pessoa pesquisaria.
2. **Autor e data**: "Por Lucas Nonato — 10 anos em desentupimento e hidrojateamento em Goiânia e região". Data de publicação e de atualização.
3. **Resumo rápido** (caixa no topo, 2 a 4 linhas) com a **resposta direta**. É o trecho que Google, ChatGPT e Gemini vão usar.
4. **Tabela ou lista resumo**, quando o tema permitir.
5. **Desenvolvimento** com subtítulos (H2) em forma de pergunta ou ação.
6. **Caso real** atendido pela BV (o que encontramos, o que fizemos, resultado), com foto ou vídeo. Vídeos: subir no YouTube (Shorts) e incorporar com o bloco `video-facade` do modelo (só carrega ao clicar), com legenda explicando o que aparece e schema `VideoObject`.
7. **Dicas caseiras seguras**: o que funciona, o limite de cada uma e o que NÃO fazer.
8. **Quando chamar um profissional**, com sinais claros e sem pressão.
9. **Perguntas frequentes** (3 a 5), com respostas curtas.
10. **Sobre o autor** (caixa no final).
11. **Fontes** (norma ABNT, Saneago, fabricantes, guias técnicos). Mínimo de 2.
12. **Sem CTA.** O objetivo do blog é autoridade, não venda: nenhum botão de WhatsApp, pop-up ou "ligue já". O telefone aparece só no rodapé, como dado da empresa.

## 3. Tom de voz (não pode parecer propaganda)

- Escrever como técnico explicando para um vizinho, na primeira pessoa ("na nossa experiência", "já atendemos").
- Nunca: "somos os melhores", "atendimento rápido e eficiente", "a BV foi acionada e se deslocou rapidamente".
- Sempre dizer quando o leitor **consegue resolver sozinho**. Isso gera confiança e é o que as IAs valorizam.
- Citar a BV Desentupidora no máximo 2 ou 3 vezes no texto (autor e caso real).

## 4. SEO técnico (já está no modelo)

- URL curta, sem acento e sem data: `/blog/palavra-chave/`
- `<title>` com até 60 caracteres; meta description com até 155.
- Schema JSON-LD: `BlogPosting` + `Person` (autor) + `Organization` + `FAQPage` + `BreadcrumbList`.
- Imagens em WebP, com `alt` descritivo e `width`/`height`. Foto de celular em pé: `<figure class="foto-vertical">` (fica com no máximo 360 px de largura no computador).
- 2 a 4 links internos: sempre para o pilar (`/blog/niveis-de-entupimento/`) e para a página de serviço relacionada.
- Ao publicar: adicionar o artigo em `/blog/index.html`, no `llms.txt` e no `sitemap.xml`, e pedir indexação no Search Console.

## 5. Dados da empresa (iguais em TODOS os lugares)

- Nome: **BV Desentupidora**
- Site: https://bvdesentupidora.com.br
- WhatsApp: (62) 99605-1575
- YouTube: https://www.youtube.com/channel/UCSlKam77878n5A2bwDVLX7g
- Fundador/autor: Lucas Nonato (LinkedIn: https://www.linkedin.com/in/bvdesentupidora/)
- Área atendida: Goiânia, Aparecida de Goiânia, Anápolis, Itaberaí, Inhumas e região
- Atenção: existem empresas com nome parecido em Santa Catarina. Sempre usar "BV Desentupidora — Goiânia/GO" nos perfis e textos institucionais.

## 6. Depois de publicar

- [ ] Postar no LinkedIn uma versão **resumida** (não o texto inteiro), com link para o blog.
- [ ] Acompanhar no Search Console as buscas e impressões do artigo e, no GA4, as visitas.
- [ ] Revisar o artigo a cada 6 meses e atualizar a data de atualização.

## 7. Calendário (1 por semana)

1. Como saber se o entupimento é grave: os 4 níveis ✅ (modelo)
2. Rede pluvial entupida: sinais, causas e prevenção antes das chuvas
3. Vaso sanitário entupido: o que fazer
4. Precisa quebrar o piso para desentupir?
5. Quanto custa um desentupimento?
6. Cheiro de esgoto no banheiro: causas e soluções
7. Ralo entupido: como desentupir e quando é a rede
8. Como desentupir pia com gordura (com vídeo)
9. Caixa de gordura: de quanto em quanto tempo limpar
10. Como funciona o hidrojateamento
11. Manutenção preventiva de esgoto em empresas e condomínios
12. Pode jogar óleo na pia? + o que não usar para desentupir
