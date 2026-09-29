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
  - `publicar/index.html` = versão de produção para a Hostinger: igual ao `index.html` da raiz, só troca `<meta name="robots">` de `noindex, follow` para `index, follow, max-image-preview:large`. Sincronizado em 28/09/2026 (commit do pacote de velocidade); ao mudar a raiz, regenerar com esse mesmo sed
- **Site de produção real**: Hostinger, pasta `public_html`, editado hoje via Gerenciador de Arquivos (File Browser) direto no servidor
- **A fonte de verdade real hoje é o `index.html` da raiz do repo** (branch `pages-preview`), não o `publicar/`

## Como publicar mudanças no site ao vivo

O site da Hostinger **não atualiza sozinho a partir do GitHub** — é preciso subir manualmente:
1. Editar o código (aqui no repo, branch `pages-preview`)
2. Commitar e dar push
3. Publicar no Hostinger: painel hPanel → Gerenciador de Arquivos (abre em nova aba, só funciona com clique humano real, não com automação) → `public_html` → abrir `index.html` no editor → usar busca/substituição (Ctrl+F no editor) para aplicar as mesmas mudanças, ou subir arquivo novo
4. Login da Hostinger é via "Entrar com o Google" com a conta que hospeda o site — **NÃO é a antoniovie3057@gmail.com** (é outra conta do Antonio). O Antonio faz o login manualmente no navegador do Claude Desktop; a sessão pode expirar
5. Caminho que funcionou em 28/09/2026: hPanel → Sites → bvdesentupidora.com.br → Gerenciador de Arquivos "Abrir" (o clique do Claude funcionou, abre na mesma aba o File Browser em `srv880-files.hstgr.io/<id>/files/`). Para subir arquivos (inclusive binários) o Claude usou a API do próprio File Browser com a sessão logada (`POST /api/resources/public_html/<caminho>?override=true`, header `X-Auth` = `localStorage.jwt`), baixando cada arquivo do GitHub Pages (`/publicar/...`) e conferindo SHA-256 antes e depois. Subir primeiro os assets novos, conferir que o domínio os serve, e só então o `index.html`
6. A página é servida como `x-hcdn-cache-status: DYNAMIC` (sem cache de HTML no CDN) — não precisa "Limpar cache" depois de trocar o index.html
7. `curl` do PC do Antonio costuma levar 403 "Checking your browser" (proteção anti-robô da Hostinger); para conferir o site ao vivo, usar o navegador

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
2. Primeira auditoria técnica (PageSpeed mobile: 74, LCP 3,3s, TBT 530ms). Foi **refeita do zero na mesma noite** — ver item 3; algumas conclusões dela estavam erradas (ex.: o pulso NÃO causava o TBT).
3. **Auditoria refeita + pacote de velocidade aplicado** (commit `0f34dd5` no `pages-preview`, autorizado pelo Antonio: itens 1, 2, 5, 6, 7, 9).
   - Medição antes (site ao vivo, PageSpeed mobile, 2 rodadas): nota 71 e 91 · FCP 2,8/2,7s · LCP 5,2/2,7s · TBT 230/80ms. A nota oscila muito por carga do servidor do Google; o constante era a fonte travando a 1ª pintura.
   - Medição depois (GitHub Pages, 2 rodadas): **nota 97 e 100 · FCP 1,0/0,9s · LCP 1,5s · TBT 200/90ms · CLS 0,005/0** · zero recurso bloqueante · zero animação não composta.
   - Feito: (1) Inter hospedada no site (`assets/fonts/inter-latin.woff2` + preload + @font-face inline, sem Google Fonts); (2) carrossel de avaliações travava para sempre na 3ª avaliação ~6s após abrir — corrigido, pausa fora da tela, pointercancel não avança card, realinha ao girar; (5) pulso do WhatsApp agora é anel em `::after` com transform/opacity (mesmo visual); (6) logo `logo-bv-desentupidora-sm.webp` 152×162 10,6KB (antes 26KB) e favicon `favicon-48.png` 4,5KB (antes 34–40KB); (7) `scroll-margin-top` nas seções com id (título não fica sob o cabeçalho nos sitelinks); (9) seção logo abaixo do hero não fica mais invisível na 1ª dobra (só seções abaixo da tela animam).
   - `publicar/index.html` agora = versão de produção (igual à raiz, mas com `robots` index).
   - **PUBLICADO na Hostinger em 28/09/2026 ~23:10** (pedido do Antonio): `assets/fonts/inter-latin.woff2`, `assets/logo-bv-desentupidora-sm.webp`, `assets/favicon-48.png` e `index.html` (commit `6d0d2aa`). Backup do index.html anterior: `backup-hostinger-index-antes-2026-09-28.html` (fora do git, na pasta do projeto).
   - Correção feita depois da 1ª publicação (commit `6d0d2aa`): o script de entrada das seções media a posição com getBoundingClientRect ao carregar → "reflow forçado" de 239 ms que atrasava a foto do hero. Agora usa só IntersectionObserver; carrossel mede ao aparecer.
   - PageSpeed mobile no site ao vivo depois (23:01–23:13): 82, 78 (antes da correção do reflow), 83 e 60 (esta com o servidor do PageSpeed sobrecarregado: gtag levou 3.364 ms). **FCP ≈ 1,0 s em todas** (antes 2,7–2,8 s). LCP de laboratório 4,4–4,5 s nesse horário — o GitHub Pages com o MESMO código deu 97/100 (LCP 1,5 s) às 22:51 e 78 (LCP 4,6 s) às 23:04, então é oscilação do PageSpeed; quando a foto demora a ser pintada lá, o simulador passa a contar o GTM (121 KB) disputando banda com ela. Aprovados agora: sem recurso bloqueante, sem reflow forçado, sem animação não composta. Sem dados de campo (CrUX) ainda.

4. **Pacote "site liso"** (Antonio pediu "o que você recomenda para ficar totalmente liso, faça"; testes SÓ no site ao vivo, nunca no GitHub Pages). Publicado na Hostinger ~23:30, commits `4144c3a` + `6e458f2`:
   - GTM/GA4 só baixa no evento `load` ou no 1º toque/tecla/rolagem (antes: no início do `<head>`). TBT caiu para 70 ms na 1ª medição ao vivo
   - Antes/depois com `<picture>`: até 640px sempre a versão 768px
   - Pop-up: brilho do contador em `::after` (opacity), barra com `scaleX`, contador só roda com o pop-up aberto
   - Área de toque 44px no telefone do cabeçalho (padding 12 + margin −12, visual igual) e no X do pop-up (`.popup-close::before`)
   - button_text do WhatsApp do cabeçalho = aria-label; clique em CTA marca `converted` também em memória
   - Removido o `<link rel="preload">` da fonte (hipótese de que segurava a 1ª pintura) — **hipótese NÃO confirmada**: sem ele a espera continuou (~1,1 s). Mantido sem preload (texto aparece na hora com font-display: swap)
   - **Em aberto:** no PageSpeed ao vivo os 3 primeiros quadros ficam brancos e a página inteira (com a foto) aparece junto ~1–1,4 s (observado) com CPU ociosa (site 105 ms de CPU) → LCP simulado 4,4–4,5 s, nota 78–84. O mesmo código deu 97/100 no início da noite. Causa não identificada; suspeita de ambiente do PageSpeed. Depois de ~23:35 o PageSpeed parou de concluir análises (inclusive da 404.html). Refazer a medição em outro horário; ideal medir usuários reais (Core Web Vitals no GA4/Search Console)

   **Pendente (achados da auditoria, não autorizados ainda):**
   - (3) Fotos de antes/depois no iPhone — FEITO no item 4 (<picture>)
   - (4) Todas as fotos .webp têm metadado C2PA "Claude forneceu este arquivo e pode ter criado ou modificado" (5,7KB cada) — reexportar das fotos ORIGINAIS sem metadados (precisa das originais do Antonio). Ruim principalmente nas fotos de antes/depois
   - (8) GTM + GA4 = 311KB e 100% do TBT — FEITO no item 4 (carrega depois do load). Container só tem GA4 (tag Google + eventos whatsapp_click/phone_click); sem tag de conversão do Ads
   - (10) Ícone de telefone do cabeçalho com área de toque 19×19px; X do pop-up 28×28px; clique no WhatsApp do cabeçalho vai pro GA4 com button_text vazio; contraste do "Ligar Agora"/"Ligar"/© rodapé; falta `<main>`; contador do pop-up roda a cada 1s mesmo sem pop-up
   - Contador "Oferta termina em 20:00" reinicia a cada nova visita — pergunta em aberto pro Antonio (CDC)
   - Hostinger CDN responde 403 "Checking your browser" para clientes sem navegador após poucas requisições (curl etc.); navegador real e PageSpeed passam. Conferir prévia do link no WhatsApp e status da página de destino no Ads

## Regras que o Antonio já deixou explícitas (seguir sempre)

- **Nunca "limpar"/embelezar artificialmente fotos de antes/depois** — só fotos reais, sem alterar o resultado do serviço (questão de propaganda enganosa/CDC)
- **Nunca aplicar mudança de código sem mostrar antes e pedir autorização**, especialmente mudanças de performance/técnicas — sempre explicar: problema, onde está, impacto, como pretende corrigir, se altera visual/conversão/funcionamento
- Preservar identidade visual (logo, cores, fotos reais) — evolução, não redesign
- Não remover nem duplicar código de rastreamento sem avisar antes
- Login/senha nunca são digitados pelo Claude nem guardados em memória — sessões de navegador persistem sozinhas depois do primeiro login manual
