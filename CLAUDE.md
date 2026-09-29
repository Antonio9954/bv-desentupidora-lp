# BV Desentupidora — Landing Page

Contexto do projeto para qualquer sessão do Claude Code que abrir este repositório.
Leia este arquivo inteiro antes de fazer qualquer alteração.

## O negócio

- Empresa: BV Desentupidora, desentupidora em Goiânia/GO (Antonio é o dono)
- Site ao vivo: **https://bvdesentupidora.com.br/** (produção real, hospedado na Hostinger)
- WhatsApp/telefone: (62) 99605-1575
- Antonio quer ter domínio total da operação (site, Ads, Analytics) no próprio nome, sem depender de agência

## Onde as coisas ficam

- **Repositório**: antonio9954/bv-desentupidora-lp (GitHub)
  - branch `pages-preview` = branch principal de trabalho, publicada também no GitHub Pages como pré-visualização (`noindex`)
  - `index.html` na raiz = versão de pré-visualização (GitHub Pages)
  - `publicar/index.html` = deveria espelhar o que está no ar na Hostinger, **mas está desatualizado** (ver auditoria abaixo — não usar como fonte de verdade até ser sincronizado)
- **Site de produção real**: Hostinger, pasta `public_html`, editado hoje via Gerenciador de Arquivos (File Browser) direto no servidor
- **A fonte de verdade real hoje é o `index.html` da raiz do repo** (branch `pages-preview`), não o `publicar/`

## Como publicar mudanças no site ao vivo

O site da Hostinger **não atualiza sozinho a partir do GitHub** — é preciso subir manualmente:
1. Editar o código (aqui no repo, branch `pages-preview`)
2. Commitar e dar push
3. Publicar no Hostinger: painel hPanel → Gerenciador de Arquivos (abre em nova aba, só funciona com clique humano real, não com automação) → `public_html` → abrir `index.html` no editor → usar busca/substituição (Ctrl+F no editor) para aplicar as mesmas mudanças, ou subir arquivo novo
4. Login da Hostinger é via "Entrar com o Google" (conta antoniovie3057@gmail.com) — a sessão fica salva no navegador do Claude Desktop depois do primeiro login manual

Quando o Antonio disser **"mudar o site"**, o entendimento é: pegar o que já está commitado no repo e aplicar no Hostinger, sem precisar reexplicar o processo.

## Rastreamento (não mexer sem avisar)

- Google Tag Manager: `GTM-KB5H87LR`
- Google Analytics 4: `G-VZ9G7BWF7R` (propriedade "Site BV Desentupidora")
- Google Ads: conta 711-632-3884, campanha de Pesquisa ativa ("pesquisa venda bv desentupidora")
- Eventos customizados via dataLayer: `whatsapp_click`, `phone_click` (listener central no JS do site, não usa mais `onclick` individual)
- Confirmado funcionando ao vivo em 28/09/2026 (GTM carrega, dataLayer populado, sem erro no console)

## O que já foi feito

- Site completo construído mobile-first, com seção de antes/depois com fotos reais dos serviços (sem qualquer edição que "limpe" resultado que não aconteceu — regra explícita do Antonio)
- GTM, GA4, Search Console configurados e vinculados ao Google Ads
- Domínio bvdesentupidora.com.br registrado, hospedagem Hostinger contratada, site publicado
- Campanha de Google Ads (Pesquisa) criada e publicada, com sitelinks, frases de destaque e extensão de mensagem WhatsApp

## Sessão de hoje (28/09/2026)

1. Trocou o texto de 5 H2 da landing page pra incluir palavras-chave da campanha de Ads (mantendo texto natural, sem mudar estrutura/CSS/JS):
   - Serviços → "Desentupidora de Esgoto em Goiânia e Região"
   - Tipos de imóvel → "Desentupidora Perto de Mim para Todo Tipo de Imóvel"
   - Diferenciais → "Por que escolher nossa Empresa de Desentupimento?"
   - Banner Goiânia → "Desentupidora em Goiânia 24h"
   - CTA final → "Esgoto entupido? Peça um Orçamento Grátis agora"
   - Essas mudanças já estão commitadas **e já estão no ar** (aplicadas direto no Hostinger via editor do File Manager)
2. Fez uma **auditoria técnica completa** do site ao vivo (Lighthouse/PageSpeed real, mobile, 4G lento) — **auditoria só, nada foi corrigido ainda, aguardando autorização do Antonio**. Resultado:
   - Nota Desempenho: 74/100 · Acessibilidade 94 · Boas práticas 100 · SEO 100
   - LCP 3,3s · TBT 530ms (alto) · CLS 0,01 (ótimo) · FCP 2,8s

   **🔴 Crítico (pendente de autorização):**
   - Fonte do Google Fonts bloqueia renderização inicial (~1.640ms perdidos) — precisa carregar assíncrono
   - 3 sitelinks do Google Ads (`#como-funciona`, `#avaliacoes`, `#perguntas-frequentes`) apontam pra âncoras que **não existem mais no HTML ao vivo** — os `id` sumiram das seções, sitelinks quebrados
   - Botão vermelho "Ligar Agora" (`.btn-ligar`, `#E53935`) reprovado no teste de contraste de acessibilidade do Lighthouse

   **🟠 Importante (pendente de autorização):**
   - Logo do cabeçalho (`logo-bv-desentupidora.webp`, 240×255px/25,5KB) ~24KB maior do que precisa pro tamanho exibido (54-76px)
   - Foto do hero pode perder ~17KB só com melhor compressão WebP
   - Animação de pulso do WhatsApp (`wa-pulse-strong`/`wa-pulse-soft`) usa `box-shadow`+`filter` em 10 botões da página — não é "composto" pela GPU, contribui pro TBT alto. Reescrever usando só `transform`/`opacity` mantendo o mesmo efeito visual
   - `publicar/index.html` está desatualizado em relação ao `index.html` da raiz (que é o que está realmente no ar) — precisa sincronizar pra não causar regressão na próxima publicação

   **🟢 Opcional:**
   - Selos do Hero repetem quase literalmente na seção "Por que escolher" (conteúdo, não é bug técnico)
   - Falta tag `<main>` no HTML (acessibilidade)

   Análise de conversão (hipóteses, sem dado de comportamento real): 10 elementos pulsando ao mesmo tempo pode diluir a sensação de urgência; pop-up de desconto por tempo fixo (10-20s) pode interromper alguém já convertendo.

## Regras que o Antonio já deixou explícitas (seguir sempre)

- **Nunca "limpar"/embelezar artificialmente fotos de antes/depois** — só fotos reais, sem alterar o resultado do serviço (questão de propaganda enganosa/CDC)
- **Nunca aplicar mudança de código sem mostrar antes e pedir autorização**, especialmente mudanças de performance/técnicas — sempre explicar: problema, onde está, impacto, como pretende corrigir, se altera visual/conversão/funcionamento
- Preservar identidade visual (logo, cores, fotos reais) — evolução, não redesign
- Não remover nem duplicar código de rastreamento sem avisar antes
- Login/senha nunca são digitados pelo Claude nem guardados em memória — sessões de navegador persistem sozinhas depois do primeiro login manual
