# Conteúdo dos artigos. Executado por gerar_artigos.py (usa video(), FOTO_GORDURA, gerar()).

# Publicação: 1 por semana. Para publicar o próximo, mova o primeiro slug de FILA para PUB,
# coloque a data em DATAS e rode `python tools/gerar_artigos.py publicar/blog`.
PUB = ["niveis-de-entupimento", "rede-pluvial-entupida"]
DATAS = {"niveis-de-entupimento": "2026-10-26", "rede-pluvial-entupida": "2026-10-26"}
FILA = ["vaso-sanitario-entupido", "precisa-quebrar-piso-para-desentupir", "desentupir-pia-com-gordura",
        "limpeza-caixa-de-gordura", "como-funciona-hidrojateamento", "pode-jogar-oleo-na-pia"]

# slug: (título na lista, frase do índice do blog, frase do llms.txt)
LISTA = {
    "niveis-de-entupimento": ("Como saber se o entupimento é grave: os 4 níveis e o que fazer em cada um",
                              "Um guia para identificar o nível do entupimento, o que dá para resolver em casa e quando chamar um profissional.",
                              "como identificar se o entupimento é simples ou está na rede, o que resolver em casa, o que não fazer e quando chamar um profissional."),
    "rede-pluvial-entupida": ("Rede pluvial entupida: sinais, causas e prevenção antes das chuvas",
                              "Como saber se a rede pluvial está entupida, o que mais entope e o que fazer antes das chuvas.",
                              "sinais de rede pluvial entupida, o que mais entope (caso real em Heitoraí, GO, com vídeo) e como prevenir antes das chuvas."),
    "vaso-sanitario-entupido": ("Vaso sanitário entupido: o que fazer passo a passo",
                                "Como usar a ventosa certa, o que nunca jogar no vaso e o sinal de que o problema está na rede.",
                                "passo a passo com ventosa, o que não jogar no vaso e por que vaso e ralo entopem juntos (caso real em casa de eventos)."),
    "precisa-quebrar-piso-para-desentupir": ("Precisa quebrar o piso para desentupir?",
                                             "Por onde o profissional entra na tubulação sem quebrar e quando a quebra é inevitável.",
                                             "na maioria dos casos não: acessos usados, sonda rotativa x hidrojato e quando a quebra é inevitável (caso real em Itaberaí, GO)."),
    "desentupir-pia-com-gordura": ("Como desentupir pia com gordura: o que funciona de verdade",
                                   "Sifão, ventosa, o limite da água quente e quando a gordura já virou placa no cano.",
                                   "como a gordura vira placa no cano, passo a passo com sifão e ventosa e o que não fazer (caso real em Inhumas, GO)."),
    "limpeza-caixa-de-gordura": ("Caixa de gordura: de quanto em quanto tempo limpar",
                                 "Frequência de limpeza em casa e em restaurante, sinais de caixa cheia e o descarte da gordura.",
                                 "frequência de limpeza (3 a 6 meses em casa; mensal ou quinzenal em restaurante), sinais de caixa cheia e como limpar."),
    "como-funciona-hidrojateamento": ("Como funciona o hidrojateamento",
                                      "O que é, por que resolve entupimento de gordura que volta e por que a técnica importa.",
                                      "o que é (1.500 a 4.000 PSI), quando usar, riscos para o cano e segurança em fossas (caso real em restaurante de Goiânia)."),
    "pode-jogar-oleo-na-pia": ("Pode jogar óleo na pia? E o que não usar para desentupir",
                               "Por que o óleo entope, como descartar e o que nunca usar para desentupir.",
                               "por que óleo na pia entope, como descartar e o que não usar para desentupir: misturas de produtos, soda, água fervendo e arame."),
}

LI = "https://www.linkedin.com/pulse/"

# ---------------------------------------------------------------------------
# 2. Rede pluvial
# ---------------------------------------------------------------------------
REDE = dict(
    slug="rede-pluvial-entupida",
    title="Rede pluvial entupida: sinais, causas e prevenção",
    h1="Rede pluvial entupida: sinais, causas e prevenção antes das chuvas",
    desc="Como saber se a rede pluvial está entupida, o que costuma causar o problema e o que fazer antes das chuvas para o quintal e a calha não alagarem.",
    migalha="Rede pluvial entupida",
    keywords="rede pluvial entupida, ralo do quintal entupido, calha transbordando, água da chuva não escoa, desentupimento de rede pluvial",
    sobre=["Rede pluvial", "Drenagem de águas pluviais", "Desentupimento"],
    imagem="https://i.ytimg.com/vi/rIHn8FNLqQM/maxresdefault.jpg",
    videos=["rIHn8FNLqQM"],
    linkedin=LI + "o-que-encontramos-dentro-de-uma-rede-pluvial-em-heitora%C3%AD-vieira-ujdif/",
    resumo="A rede pluvial é a tubulação que leva a água da chuva das calhas, ralos do quintal e grelhas até a rua. Ela está entupida quando, na chuva, a água empoça no quintal ou na garagem, a calha transborda ou o ralo externo devolve água. Na maioria dos casos a causa é terra, folhas e pequenos objetos arrastados para dentro do cano ao longo de meses. Limpar calhas e ralos antes da época de chuvas evita boa parte dos problemas; quando a água já não escoa, a rede precisa ser desobstruída com equipamento, quase sempre sem quebrar piso.",
    corpo='''    <p>Todo ano, quando as chuvas voltam a Goiás, recebemos chamados com a mesma história: o quintal virou piscina, a água da garagem entrou em casa ou a calha transbordou pela parede. Quase sempre a rede pluvial já estava parcialmente fechada havia meses, e ninguém percebeu porque não chovia. Neste guia explico como reconhecer o problema cedo e o que dá para fazer antes de precisar de equipamento.</p>

    <h2>Resumo: sinais de rede pluvial entupida</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Sinal</th><th>O que costuma indicar</th><th>O que fazer</th></tr></thead>
        <tbody>
          <tr><td>Calha transbordando pela borda</td><td>Calha ou condutor (cano que desce da calha) com folhas</td><td>Limpar a calha e testar o condutor com mangueira</td></tr>
          <tr><td>Água empoçando perto de um ralo do quintal</td><td>Grelha ou caixa daquele ralo cheia de terra</td><td>Tirar a grelha e retirar a terra (com luva)</td></tr>
          <tr><td>Ralo externo devolvendo água na chuva</td><td>Trecho da rede depois do ralo obstruído</td><td>Chamar profissional</td></tr>
          <tr><td>Quintal ou garagem alagando em toda chuva</td><td>Rede principal do imóvel fechada</td><td>Chamar profissional antes da próxima chuva forte</td></tr>
        </tbody>
      </table>
    </div>

    <h2>O que é a rede pluvial?</h2>
    <p>A rede pluvial é o sistema que leva a água da chuva para longe do imóvel. Ela começa nas calhas, nos ralos externos e nas áreas cimentadas do quintal, passa por caixas de passagem e termina na sarjeta ou na galeria da rua. É ela que evita alagamentos, infiltrações e danos à estrutura da casa.</p>
    <p>A rede pluvial não é a rede de esgoto. A casa tem duas redes separadas, e a norma de águas pluviais (ABNT NBR 10844) trata da rede de chuva à parte. Quando a água da chuva entra no esgoto, o esgoto transborda nos dias de chuva forte; quando o esgoto entra na rede pluvial, ele vai direto para a rua e para os córregos.</p>

    <h2>O que mais entope a rede pluvial?</h2>
    <p>Na minha experiência, quase nunca é uma coisa só. É o acúmulo, ao longo de meses, de:</p>
    <ul>
      <li><strong>Terra e areia</strong> levadas pela enxurrada, principalmente em quintal sem piso ou com jardim perto do ralo.</li>
      <li><strong>Folhas e galhos</strong> de árvores próximas, que entram pela calha.</li>
      <li><strong>Restos de obra</strong>: cimento, areia e pedaços de reboco varridos para o ralo.</li>
      <li><strong>Objetos pequenos</strong>: brinquedos, chinelos, tampas, garrafas e embalagens plásticas.</li>
      <li><strong>Raízes</strong> que entram por juntas e trincas do cano.</li>
    </ul>
    <p>Mesmo sem lixo, a rede pode fechar: terra, sedimentos e raízes vão reduzindo o diâmetro do cano até a água não passar.</p>

    <div class="caso">
      <p><span class="rotulo">Caso real (Heitoraí, GO):</span> o proprietário contou que, sempre que chovia, a água acumulava no quintal e demorava muito para sumir. Na inspeção, a rede pluvial estava completamente fechada. De dentro do cano tiramos chinelo infantil, tampa de garrafa, lata de cerveja, lápis, escova de dente, papel, cabelo e muita terra. Cada objeto sozinho parece inofensivo, mas juntos formaram uma barreira que segurava mais sujeira a cada chuva. Desobstruímos com sonda rotativa e um desengordurante alcalino para soltar o que estava grudado na parede do cano, sem quebrar piso nem parede.</p>
    </div>

    ''' + video("rIHn8FNLqQM", "o que saiu da rede pluvial em Heitoraí", "Vídeo do desentupimento da rede pluvial de uma casa em Heitoraí (GO)",
                "Vídeo (caso real, 7 min): Lucas Nonato mostra a desobstrução da rede pluvial em Heitoraí (GO) e os objetos que saíram de dentro do cano, junto com a terra acumulada.") + '''

    <h2>O que dá para fazer em casa?</h2>
    <ul>
      <li><strong>Limpar a calha:</strong> com escada firme e luva, retire folhas e terra da calha e da boca do condutor. Depois jogue água com a mangueira e veja se ela desce sem transbordar.</li>
      <li><strong>Limpar os ralos do quintal:</strong> tire a grelha e retire com a mão (de luva) ou com uma pá pequena a terra e as folhas da caixa logo abaixo.</li>
      <li><strong>Testar com mangueira:</strong> com tudo limpo, deixe a mangueira correndo em cada ralo por alguns minutos. Se a água desce bem, a rede está livre. Se sobe, o problema está mais adiante no cano.</li>
    </ul>
    <p>Esses cuidados resolvem quando a sujeira está na entrada. Se a água continua subindo depois da limpeza, o entupimento está dentro da tubulação, onde a mão não alcança.</p>

    <h2>O que não fazer</h2>
    <ul class="nao">
      <li>Usar produto químico. Terra, folhas e objetos não se dissolvem, e o produto vai parar na rua.</li>
      <li>Ligar a rede pluvial no esgoto para "dar vazão". Além de proibido, faz o esgoto transbordar na chuva.</li>
      <li>Usar o ralo do quintal como lixeira ou varrer terra, cimento e restos de obra para dentro dele.</li>
      <li>Tirar a grelha do ralo e deixar sem. É ela que segura os objetos maiores.</li>
    </ul>

    <h2>Como prevenir antes das chuvas?</h2>
    <ul>
      <li>Limpe calhas e ralos do quintal <strong>antes da época de chuvas</strong>. Com árvore perto do telhado, limpe também no meio da estação.</li>
      <li>Coloque <strong>tela ou grelha</strong> na boca dos condutores e dos ralos externos.</li>
      <li>Não deixe brinquedos e objetos pequenos perto dos ralos.</li>
      <li>Em obra ou reforma, proteja os ralos para não entrar areia e cimento.</li>
      <li>Ao perceber a água escoando mais devagar, peça uma inspeção. Um trecho parcialmente fechado aparece no teste com mangueira, antes de virar alagamento.</li>
    </ul>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>A água sobe no ralo mesmo depois de limpar a grelha e a caixa.</li>
      <li>O quintal ou a garagem alagam em toda chuva, mesmo nas fracas.</li>
      <li>Há retorno de água ou mau cheiro nos ralos externos.</li>
      <li>Aparecem infiltrações perto da tubulação.</li>
    </ul>
    <p>Na maioria dos casos dá para desobstruir pelos próprios ralos e caixas, sem quebrar nada. Veja também <a href="../precisa-quebrar-piso-para-desentupir/">quando é preciso quebrar o piso</a> e <a href="../niveis-de-entupimento/">os 4 níveis de entupimento</a>.</p>''',
    faq=[
        ("Como saber se a rede pluvial está entupida?", "Os sinais mais comuns são água empoçando no quintal ou na garagem durante a chuva, calha transbordando e ralo externo devolvendo água. Se a água sobe no ralo mesmo depois de limpar a grelha, o entupimento está dentro da tubulação."),
        ("A rede pluvial pode entupir mesmo sem lixo?", "Pode. Terra, areia, sedimentos e raízes vão reduzindo aos poucos o diâmetro do cano até a água não conseguir passar."),
        ("A rede pluvial pode ser ligada no esgoto?", "Não. As duas redes devem ser separadas. A água da chuva no esgoto faz a rede de esgoto transbordar, e o esgoto na rede pluvial vai direto para a rua e para os córregos."),
        ("Produto químico desentope rede pluvial?", "Não. O que entope a rede pluvial costuma ser terra, folhas e objetos, que não se dissolvem com produto. É preciso retirar a sujeira ou desobstruir o cano com equipamento."),
        ("É possível desentupir a rede pluvial sem quebrar o piso?", "Na maioria dos casos, sim. Com sonda rotativa ou hidrojateamento, a obstrução é removida pelos próprios ralos e caixas da rede."),
    ],
    fontes=["nbr10844", "epa", "fabricantes", "campo"],
    leia=["niveis-de-entupimento", "precisa-quebrar-piso-para-desentupir", "como-funciona-hidrojateamento"],
)

# ---------------------------------------------------------------------------
# 3. Vaso sanitário
# ---------------------------------------------------------------------------
VASO = dict(
    slug="vaso-sanitario-entupido",
    title="Vaso sanitário entupido: o que fazer passo a passo",
    h1="Vaso sanitário entupido: o que fazer passo a passo",
    desc="O que fazer quando o vaso entope: como usar a ventosa certa, o que nunca jogar no vaso e o sinal de que o problema está na rede, não no vaso.",
    migalha="Vaso sanitário entupido",
    keywords="vaso sanitário entupido, como desentupir vaso, ventosa para vaso, vaso e ralo entupidos, o que não jogar no vaso",
    sobre=["Vaso sanitário", "Desentupimento", "Rede de esgoto"],
    imagem="https://i.ytimg.com/vi/BjAMEKyD2ZQ/maxresdefault.jpg",
    videos=["BjAMEKyD2ZQ"],
    linkedin=LI + "desentupimento-de-vaso-sanit%C3%A1rio-e-ralo-em-casa-eventos-vieira-j1abf/",
    resumo="Na maioria das vezes, vaso sanitário entupido se resolve com um desentupidor de ventosa próprio para vaso (o que tem uma \"saia\" de borracha), usado com água cobrindo a borracha. A primeira regra é não dar descarga de novo. Se o ralo do banheiro entope junto, se o vaso borbulha quando outro ponto escoa ou se a água sobe em outro lugar, o problema não está no vaso: está na tubulação que os dois compartilham, e precisa de equipamento profissional.",
    corpo='''    <p>Vaso entupido é um dos chamados mais comuns que atendemos, e também um dos que mais dá para resolver em casa. O que complica é insistir na descarga, jogar produto químico ou empurrar um arame. Abaixo está o passo a passo que eu mesmo faria antes de chamar alguém.</p>

    <h2>Resumo: o que o vaso está te dizendo</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>O que acontece</th><th>Onde costuma estar o problema</th><th>Resolve em casa?</th></tr></thead>
        <tbody>
          <tr><td>Água desce devagar, mas desce</td><td>Excesso de papel ou começo de obstrução na curva do vaso</td><td>Sim, quase sempre</td></tr>
          <tr><td>Água sobe e não desce</td><td>Obstrução na curva do vaso ou logo depois</td><td>Na maioria das vezes, com ventosa</td></tr>
          <tr><td>Caiu um objeto (celular, brinquedo, frasco)</td><td>Objeto preso na curva do vaso</td><td>Só se der para tirar com a mão; não empurre</td></tr>
          <tr><td>Vaso e ralo do banheiro entupidos juntos</td><td>Tubulação que recebe os dois pontos</td><td>Não, precisa de profissional</td></tr>
        </tbody>
      </table>
    </div>

    <h2>O que fazer quando o vaso entope?</h2>
    <ol>
      <li><strong>Pare de dar descarga.</strong> Cada descarga é mais água num vaso que não escoa. Se a caixa acoplada estiver enchendo, feche o registro atrás do vaso.</li>
      <li><strong>Proteja o chão</strong> com pano ou jornal e use luva.</li>
      <li><strong>Use a ventosa certa.</strong> A ventosa de vaso tem uma saia de borracha que encaixa na saída do vaso. A ventosa reta, de pia, não veda direito e perde força.</li>
      <li><strong>Deixe água cobrindo a borracha.</strong> Sem água, a ventosa não faz pressão. Se o vaso estiver vazio, coloque um balde de água.</li>
      <li><strong>Encaixe e bombeie.</strong> Empurre devagar na primeira vez, para tirar o ar, e depois faça movimentos firmes para cima e para baixo, sem tirar a ventosa do lugar, por 20 a 30 segundos. Repita algumas vezes.</li>
      <li><strong>Teste com um balde, não com a descarga.</strong> Jogue um balde de água no vaso. Se descer bem, aí sim dê a descarga.</li>
    </ol>
    <p>Se depois de três ou quatro tentativas nada mudou, pare. Insistir com força pode deslocar o entupimento para dentro da tubulação, onde fica mais difícil de resolver.</p>

    <h2>E se caiu um objeto no vaso?</h2>
    <p>Celular, brinquedo, frasco ou tampa não se dissolvem. Se o objeto ainda está visível, tente tirar com a mão, de luva. Se já desceu, <strong>não use a ventosa nem dê descarga</strong>: a pressão empurra o objeto para a curva do vaso ou para o cano, e às vezes é preciso tirar o vaso do lugar para retirar.</p>

    <h2>Por que o vaso e o ralo entopem juntos?</h2>
    <p>Porque eles costumam dividir o mesmo trecho de tubulação até a caixa de inspeção. Quando os dois param ao mesmo tempo, ou quando o vaso borbulha na hora em que a máquina de lavar esvazia, o problema está nesse trecho comum ou numa caixa de inspeção já cheia. A ventosa no vaso não alcança esse ponto.</p>

    <div class="caso">
      <p><span class="rotulo">Caso real (casa de eventos):</span> fomos chamados com o evento acontecendo. O vaso sanitário e o ralo do banheiro tinham parado juntos. Do lado de dentro parecia um problema no vaso, mas, como os dois pontos travaram ao mesmo tempo, o entupimento estava na rede que recebe os dois. Desobstruímos a tubulação pela caixa, sem quebrar nada, e o banheiro voltou a funcionar sem interromper o evento.</p>
    </div>

    ''' + video("BjAMEKyD2ZQ", "vaso e ralo entupidos juntos em uma casa de eventos", "Vídeo do atendimento em uma casa de eventos com o vaso sanitário e o ralo do banheiro entupidos juntos",
                "Vídeo (caso real, 1 min): atendimento na casa de eventos em que o vaso e o ralo do banheiro entupiram juntos durante um evento.") + '''

    <h2>O que nunca jogar no vaso?</h2>
    <ul>
      <li>Lenço umedecido, mesmo os que dizem "pode descartar no vaso".</li>
      <li>Absorvente, fralda, preservativo e cotonete.</li>
      <li>Fio dental e cabelo, que se enrolam e prendem o resto.</li>
      <li>Papel-toalha, guardanapo, copos e plásticos, que não se desfazem na água como o papel higiênico.</li>
      <li>Restos de comida, óleo e gordura.</li>
    </ul>

    <h2>Como evitar entupimento em casa de eventos e comércio?</h2>
    <p>Banheiro de uso intenso entope mais. O que mais ajuda, na nossa experiência:</p>
    <ul>
      <li>Lixeira com tampa em cada cabine e aviso para não descartar nada no vaso.</li>
      <li>Grelha ou proteção nos ralos, contra cabelo e resíduos.</li>
      <li>Inspeção dos ralos, vasos e caixas de inspeção antes de eventos grandes.</li>
      <li>Em local com cozinha, caixa de gordura limpa em dia.</li>
      <li>Atenção aos primeiros sinais: água descendo devagar, mau cheiro ou retorno de água.</li>
    </ul>

    <h2>O que não fazer</h2>
    <ul class="nao">
      <li>Usar soda cáustica ou misturar produtos. São corrosivos, podem espirrar e não resolvem objeto nem excesso de papel.</li>
      <li>Usar a ventosa depois de colocar produto químico. O produto pode espirrar no rosto e nos olhos.</li>
      <li>Empurrar arame ou cabide. Risca a louça e pode prender ainda mais o entupimento.</li>
      <li>Jogar água fervendo. A louça pode trincar com a diferença de temperatura.</li>
    </ul>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>A ventosa não resolveu depois de algumas tentativas.</li>
      <li>Caiu um objeto e já não dá para alcançar.</li>
      <li>O vaso entope de novo em poucos dias.</li>
      <li>O ralo do banheiro entope junto, ou a água sobe em outro ponto da casa.</li>
    </ul>
    <p>Para entender a gravidade do seu caso, veja também <a href="../niveis-de-entupimento/">os 4 níveis de entupimento</a>.</p>''',
    faq=[
        ("Pode usar soda cáustica no vaso entupido?", "Não é recomendado. A soda é corrosiva, perigosa para quem manuseia e não resolve objeto preso nem excesso de papel. Se não funcionar, ainda deixa o vaso cheio de produto para quem for fazer o serviço."),
        ("Qual desentupidor usar no vaso sanitário?", "O de ventosa com saia de borracha, próprio para vaso. A saia encaixa na saída do vaso e veda melhor que a ventosa reta de pia."),
        ("Por que o vaso e o ralo entopem juntos?", "Porque costumam dividir o mesmo trecho de tubulação. Quando os dois param ao mesmo tempo, o entupimento está nesse trecho comum ou numa caixa de inspeção cheia, e não no vaso. A ventosa não resolve; é preciso equipamento profissional."),
        ("Por que o vaso entope toda hora?", "Os motivos mais comuns são objeto preso na curva do vaso, descarte de lenço umedecido ou papel-toalha e acúmulo na tubulação. Se entope de novo em poucos dias, vale chamar um profissional para ver o que está preso."),
    ],
    fontes=["nbr8160", "bobvila", "tribuna", "campo"],
    leia=["niveis-de-entupimento", "precisa-quebrar-piso-para-desentupir", "rede-pluvial-entupida"],
)

# ---------------------------------------------------------------------------
# 4. Precisa quebrar o piso?
# ---------------------------------------------------------------------------
PISO = dict(
    slug="precisa-quebrar-piso-para-desentupir",
    title="Precisa quebrar o piso para desentupir? Quase nunca",
    h1="Precisa quebrar o piso para desentupir?",
    desc="Na maioria dos casos, não. Veja por onde o profissional entra na tubulação, quando quebrar é inevitável e como evitar obra para resolver um entupimento.",
    migalha="Quebrar o piso para desentupir",
    keywords="precisa quebrar piso para desentupir, desentupir sem quebrar, desentupimento sem quebra-quebra, caixa de inspeção, sonda rotativa",
    sobre=["Desentupimento", "Caixa de inspeção", "Sonda rotativa", "Hidrojateamento"],
    imagem="https://i.ytimg.com/vi/qkuLm06mmnM/hqdefault.jpg",
    videos=["qkuLm06mmnM"],
    linkedin=LI + "atendimento-real-de-desentupimento-em-itabera%C3%AD-go-como-vieira-nyjqf/",
    resumo="Na maioria dos casos, não é preciso quebrar o piso para desentupir. O profissional entra na tubulação pelos pontos de acesso que já existem (caixa de inspeção, caixa de gordura, ralo, sifão ou a saída do vaso) e remove a obstrução com sonda rotativa ou hidrojateamento. Quebrar só costuma ser inevitável quando o cano está rompido, amassado ou afundado, ou quando a rede não tem nenhum ponto de acesso. Ter caixas de inspeção no imóvel é o que mais evita obra.",
    corpo='''    <p>"Vai precisar quebrar?" é uma das primeiras perguntas que ouço em todo atendimento. É um medo justo: piso quebrado é sujeira, obra e gasto. A boa notícia é que, com o equipamento certo, quase sempre dá para resolver sem tocar no piso. Abaixo explico por onde entramos na tubulação e em quais situações a quebra realmente é necessária.</p>

    <h2>Resumo: quando precisa e quando não precisa quebrar</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Situação</th><th>Precisa quebrar?</th><th>Como costuma ser resolvido</th></tr></thead>
        <tbody>
          <tr><td>Gordura, cabelo, papel ou resíduos no cano</td><td>Não</td><td>Sonda rotativa ou hidrojateamento pelos acessos existentes</td></tr>
          <tr><td>Objeto preso na tubulação</td><td>Normalmente não</td><td>Sonda rotativa ou retirada pela caixa mais próxima</td></tr>
          <tr><td>Raízes dentro do cano</td><td>Às vezes não</td><td>Sonda rotativa; se a raiz rompeu o cano, reparo no trecho</td></tr>
          <tr><td>Cano quebrado, amassado ou afundado</td><td>Sim, no trecho danificado</td><td>Abertura localizada e troca do trecho</td></tr>
          <tr><td>Rede sem nenhum ponto de acesso</td><td>Às vezes</td><td>Buscar outro acesso antes de quebrar (veja o caso do restaurante)</td></tr>
        </tbody>
      </table>
    </div>

    <h2>Por onde o profissional entra na tubulação sem quebrar?</h2>
    <p>Toda rede de esgoto tem pontos por onde dá para chegar ao cano: <strong>caixas de inspeção</strong> (as tampas no quintal ou na garagem), a <strong>caixa de gordura</strong>, os <strong>ralos</strong>, o <strong>sifão</strong> da pia e a saída do <strong>vaso</strong>. A norma de esgoto predial (ABNT NBR 8160) prevê caixas de inspeção justamente para permitir manutenção e desobstrução sem obra.</p>
    <p>O primeiro passo não é "forçar" o desentupimento: é entender onde está a obstrução e o que a causou. Antes de ligar qualquer máquina, avalio o tipo de instalação, o diâmetro do cano, o ponto provável da obstrução, os acessos disponíveis e o material que está entupindo.</p>

    <h2>Quais equipamentos permitem desentupir sem quebrar?</h2>
    <ul>
      <li><strong>Sonda rotativa:</strong> um cabo de aço flexível que gira dentro do cano e rompe ou puxa a obstrução. É eficiente contra bloqueios compactados, raízes, gordura endurecida e objetos.</li>
      <li><strong>Hidrojato (hidrojateamento):</strong> água em alta pressão que limpa a parede interna do cano por inteiro. É o mais indicado para gordura, lodo, areia e incrustações. Veja <a href="../como-funciona-hidrojateamento/">como funciona o hidrojateamento</a>.</li>
    </ul>
    <p>A escolha entre os dois depende da avaliação no local. O objetivo é devolver o fluxo completo do cano, e não só abrir um furinho para a água voltar a descer.</p>

    <div class="caso">
      <p><span class="rotulo">Caso real (Itaberaí, GO):</span> em uma casa no bairro Beira Rio, a pia e o esgoto tinham parado. Localizamos o ponto da obstrução e trabalhamos pelos acessos que a própria instalação já tinha, com equipamento profissional. O serviço foi feito sem quebrar piso e sem sujar a casa, e o vídeo mostra o que costuma entupir a pia e o maquinário usado.</p>
    </div>

    ''' + video("qkuLm06mmnM", "desentupimento residencial sem quebrar em Itaberaí", "Vídeo de desentupimento residencial de pia e esgoto sem quebrar piso em Itaberaí (GO)",
                "Vídeo (caso real, 1 min): desentupimento residencial de pia e esgoto em Itaberaí (GO), feito pelos acessos da própria instalação, sem quebrar piso.") + '''

    <p>Quando a rede não tem caixa de inspeção, ainda dá para procurar outro acesso antes de pensar em quebrar. Em um restaurante em Goiânia sem nenhuma caixa, entramos com o hidrojato pelo cano que chega até a fossa. O caso está contado no artigo sobre <a href="../como-funciona-hidrojateamento/">hidrojateamento</a>.</p>

    <h2>Quando quebrar o piso é inevitável?</h2>
    <ul>
      <li><strong>Cano rompido ou amassado:</strong> nenhum equipamento conserta cano quebrado; o trecho precisa ser trocado.</li>
      <li><strong>Trecho afundado ("barriga"):</strong> a água fica parada naquele ponto e o entupimento sempre volta.</li>
      <li><strong>Raiz que rompeu o cano:</strong> a sonda retira a raiz, mas a trinca continua deixando outra entrar.</li>
      <li><strong>Rede sem nenhum acesso possível:</strong> quando não há caixa, ralo nem outro ponto por onde entrar.</li>
    </ul>
    <p>Mesmo nesses casos, a quebra deve ser localizada, só no trecho do problema, e não um "quebra-quebra" à procura do entupimento.</p>

    <h2>O que dá para fazer em casa antes de chamar alguém?</h2>
    <ul>
      <li>Se o entupimento é só na pia, desmonte e lave o sifão. Resolve boa parte dos casos.</li>
      <li>Em pia ou vaso, use o desentupidor de ventosa certo, com água cobrindo a borracha.</li>
      <li>Descubra onde ficam as caixas de inspeção e a caixa de gordura do imóvel e deixe as tampas acessíveis (sem piso ou vaso de planta em cima).</li>
    </ul>

    <h2>O que não fazer</h2>
    <ul class="nao">
      <li>Quebrar o piso por conta própria "para achar o entupimento".</li>
      <li>Usar soda cáustica ou misturar produtos. Além do risco de queimadura, o produto fica parado no cano.</li>
      <li>Empurrar arame ou cabo de vassoura. Pode furar o cano ou soltar conexões.</li>
      <li>Cobrir caixas de inspeção com piso na reforma. É isso que, mais tarde, obriga a quebrar.</li>
    </ul>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>A água demora para escoar em mais de um ponto, há mau cheiro constante ou o vaso borbulha.</li>
      <li>A água volta pelos ralos.</li>
      <li>O entupimento se repete e você precisa usar produto químico com frequência.</li>
    </ul>
    <p>Para entender a gravidade do seu caso, veja <a href="../niveis-de-entupimento/">os 4 níveis de entupimento</a>.</p>''',
    faq=[
        ("Desentupidora sempre precisa quebrar o piso?", "Não. Na maioria dos casos o profissional entra pelos acessos que já existem, como caixa de inspeção, caixa de gordura, ralos e sifão, e remove a obstrução com sonda rotativa ou hidrojateamento."),
        ("Quando é preciso quebrar o piso para desentupir?", "Quando o cano está rompido, amassado ou afundado, quando uma raiz rompeu a tubulação ou quando a rede não tem nenhum ponto de acesso. Mesmo assim, a abertura deve ser só no trecho com problema."),
        ("Qual a diferença entre sonda rotativa e hidrojato?", "A sonda rotativa atua mecanicamente, girando dentro do cano para romper ou puxar a obstrução. O hidrojato usa água em alta pressão para limpar a parede interna do cano por inteiro. A escolha depende da avaliação no local."),
        ("Como evitar ter que quebrar o piso no futuro?", "Ter caixas de inspeção no imóvel e mantê-las acessíveis, sem piso por cima. São elas que permitem desobstruir e fazer manutenção sem obra."),
    ],
    fontes=["nbr8160", "bf_metodos", "campo"],
    leia=["niveis-de-entupimento", "como-funciona-hidrojateamento", "vaso-sanitario-entupido"],
)

# ---------------------------------------------------------------------------
# 8. Pia com gordura
# ---------------------------------------------------------------------------
PIA = dict(
    slug="desentupir-pia-com-gordura",
    title="Como desentupir pia com gordura: o que funciona",
    h1="Como desentupir pia com gordura: o que funciona de verdade",
    desc="Passo a passo para desentupir pia de cozinha com gordura: limpar o sifão, ventosa, o limite da água quente e quando a gordura já virou placa na rede.",
    migalha="Desentupir pia com gordura",
    keywords="desentupir pia com gordura, pia da cozinha entupida, sifão entupido, gordura no cano, placa de gordura",
    sobre=["Pia de cozinha", "Gordura na tubulação", "Desentupimento"],
    imagem="https://i.ytimg.com/vi/cvyNzEpSA-U/hqdefault.jpg",
    videos=["cvyNzEpSA-U"],
    linkedin=LI + "gordura-na-tubula%C3%A7%C3%A3o-da-pia-por-que-ela-vira-barras-causa-vieira-eua7f/",
    resumo="Pia de cozinha entope quase sempre por gordura misturada com restos de comida: o óleo esfria dentro do cano, gruda na parede e vai prendendo arroz, farinha e borra de café até a água não passar. Comece desmontando e lavando o sifão, que resolve boa parte dos casos; depois use o desentupidor de ventosa. Água quente só desloca a gordura para mais adiante. Se a pia volta a entupir em pouco tempo, a gordura já virou placa na tubulação e precisa ser removida com equipamento.",
    corpo='''    <p>A pia da cozinha é o ponto da casa que mais entope, e quase sempre pelo mesmo motivo: gordura. Ninguém joga uma panela de óleo de uma vez, mas um pouco de cada louça, todo dia, vai formando uma camada dentro do cano. Em 10 anos de serviço, já encontrei tubulações praticamente fechadas por essa mistura. Abaixo mostro como ela se forma e o que fazer em casa antes de chamar alguém.</p>

    <h2>Resumo: o que fazer em cada situação</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Situação</th><th>Onde costuma estar a gordura</th><th>O que fazer</th></tr></thead>
        <tbody>
          <tr><td>Pia lenta, mas escoando</td><td>Sifão e começo do cano</td><td>Limpar o sifão</td></tr>
          <tr><td>Pia parada, só ela</td><td>Sifão ou ramal da pia</td><td>Sifão e depois ventosa</td></tr>
          <tr><td>Pia volta a entupir em pouco tempo</td><td>Placas de gordura na parede do cano</td><td>Remoção com equipamento (sonda ou hidrojato)</td></tr>
          <tr><td>Caixa de gordura cheia ou outros pontos ruins</td><td>Caixa de gordura ou rede depois dela</td><td>Limpar a caixa e chamar profissional</td></tr>
        </tbody>
      </table>
    </div>

    <h2>Como a gordura entope o cano da pia?</h2>
    <p>Óleo, manteiga, molhos e gordura de carne descem quentes e líquidos, mas esfriam no caminho. Ao esfriar, ficam pegajosos e grudam na parede do cano, principalmente em curvas, conexões e trechos com pouca inclinação. Essa camada vira uma superfície onde arroz, farinha, borra de café e fibras de alimentos se prendem. O processo se repete todo dia e a passagem da água vai fechando.</p>
    <p>Com o tempo, a camada endurece. Pesquisas sobre depósitos de gordura em redes de esgoto mostram que os ácidos graxos reagem com o cálcio e formam um material sólido parecido com sabão. Por isso, muitas obstruções não são uma gordura mole: são placas, "pedras" ou barras rígidas que só saem com remoção mecânica.</p>

    <div class="caso">
      <p><span class="rotulo">Caso real (Inhumas, GO, 31/08/2026):</span> a pia de uma residência estava parada. Ao abrir a tubulação, encontramos pedras de gordura que obstruíam a passagem da água. Removemos as placas da parede do cano, e não só um furo no meio delas. É isso que impede o entupimento de voltar em poucos dias.</p>
    </div>

    ''' + video("cvyNzEpSA-U", "pedras de gordura retiradas da pia", "Vídeo de desentupimento de pia com retirada de pedras de gordura em Inhumas (GO)",
                "Vídeo (caso real, 45 s): pedras de gordura retiradas da tubulação de uma pia em Inhumas (GO), em 31/08/2026.") + '''

    <h2>Passo a passo para desentupir a pia</h2>
    <ol>
      <li><strong>Limpe o sifão.</strong> É a peça em curva embaixo da pia. Coloque um balde por baixo, desrosqueie com a mão, lave por dentro e monte de novo, conferindo a borracha de vedação. Resolve boa parte dos casos.</li>
      <li><strong>Use o desentupidor de ventosa.</strong> Deixe água cobrindo a borracha e tampe o ladrão da pia (o furinho de cima) com um pano molhado. Em cuba dupla, tampe também o ralo da outra cuba. Faça movimentos firmes por 20 a 30 segundos e repita.</li>
      <li><strong>Água quente da torneira com detergente, só como apoio.</strong> Ajuda em gordura recente perto do ralo, mas não é solução: a gordura derrete, avança alguns metros, esfria de novo e endurece num trecho mais difícil.</li>
      <li><strong>Olhe a caixa de gordura.</strong> Se ela estiver cheia até a saída, o problema não é mais a pia. Veja <a href="../limpeza-caixa-de-gordura/">de quanto em quanto tempo limpar a caixa de gordura</a>.</li>
    </ol>

    <h2>Quais alimentos mais entopem a pia?</h2>
    <ul>
      <li>Óleo de fritura, gordura de carnes e aves, manteiga e margarina.</li>
      <li>Molhos gordurosos, queijos, maionese e caldos de cozimento.</li>
      <li>Arroz, massas e farinha, que incham com a água e grudam na gordura.</li>
      <li>Borra de café, que vira sedimento no sifão.</li>
    </ul>
    <p>Detergente ajuda a tirar gordura do prato, mas não mantém a gordura dissolvida pelo cano todo: ela se separa da água e gruda mais adiante. Usar bastante detergente não torna seguro jogar óleo na pia.</p>

    <h2>O que não fazer</h2>
    <ul class="nao">
      <li>Usar soda cáustica. Ela é corrosiva e, com a gordura, pode formar uma massa ainda mais dura.</li>
      <li>Jogar água fervendo em cano de PVC. O cano de esgoto não foi feito para essa temperatura.</li>
      <li>Usar ventosa depois de colocar produto químico. O produto pode espirrar no rosto e nos olhos.</li>
      <li>Empurrar arame ou cabide. Pode furar o cano, soltar o sifão ou quebrar e ficar preso lá dentro.</li>
    </ul>
    <p>Para a lista completa do que não usar, veja <a href="../pode-jogar-oleo-na-pia/">pode jogar óleo na pia?</a>.</p>

    <h2>Como evitar que a pia entupa de novo?</h2>
    <ul>
      <li><strong>Óleo nunca na pia.</strong> Guarde em garrafa PET com tampa e entregue num ponto de coleta. Em Goiás, a Saneago tem o programa Olho no Óleo, que dá desconto na conta de água para quem entrega o óleo usado.</li>
      <li><strong>Raspe pratos e panelas</strong> no lixo e passe papel-toalha na gordura antes de lavar.</li>
      <li><strong>Use peneira no ralo</strong> e esvazie todo dia.</li>
      <li><strong>Mantenha a caixa de gordura limpa</strong>, para a gordura não seguir para a rede.</li>
    </ul>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>Sifão limpo e ventosa não resolveram.</li>
      <li>A pia volta a entupir em poucos dias ou semanas.</li>
      <li>Há barulho no ralo, bolhas, mau cheiro ou retorno de água.</li>
      <li>A caixa de gordura está transbordando.</li>
    </ul>
    <p>Quando a gordura já virou placa, a solução é limpar a parede do cano inteira, normalmente com <a href="../como-funciona-hidrojateamento/">hidrojateamento</a>.</p>''',
    faq=[
        ("Água quente desentope pia com gordura?", "Não de verdade. Ela derrete a gordura perto do ralo, mas a gordura avança alguns metros, esfria e endurece de novo num trecho mais difícil. Água fervendo ainda pode danificar cano de PVC."),
        ("Bicarbonato com vinagre desentope pia com gordura?", "Faz espuma e ajuda na limpeza e no cheiro, mas não remove placas de gordura endurecida nem entupimento total."),
        ("Por que a pia da cozinha volta a entupir?", "Porque, quando só se abre uma passagem, a placa de gordura continua grudada na parede do cano e volta a prender restos de comida. A solução é remover a gordura da parede inteira."),
        ("Borra de café pode ir na pia?", "Não é recomendado. A borra não se dissolve, fica presa na gordura do cano e aumenta a obstrução."),
        ("Detergente impede a gordura de grudar no cano?", "Não garante. O detergente ajuda a tirar gordura da louça, mas a gordura pode se separar da água no caminho e grudar mais adiante na tubulação."),
    ],
    fontes=["he2011", "saneago_oleo", "nbr8160", "campo"],
    leia=["limpeza-caixa-de-gordura", "pode-jogar-oleo-na-pia", "como-funciona-hidrojateamento"],
)

# ---------------------------------------------------------------------------
# 9. Caixa de gordura
# ---------------------------------------------------------------------------
CAIXA = dict(
    slug="limpeza-caixa-de-gordura",
    title="Caixa de gordura: de quanto em quanto tempo limpar",
    h1="Caixa de gordura: de quanto em quanto tempo limpar",
    desc="Com que frequência limpar a caixa de gordura em casa e em restaurante, os sinais de que ela está cheia e o que fazer com a gordura retirada.",
    migalha="Limpeza de caixa de gordura",
    keywords="limpeza de caixa de gordura, caixa de gordura cheia, de quanto em quanto tempo limpar caixa de gordura, caixa de gordura com mau cheiro",
    sobre=["Caixa de gordura", "Manutenção preventiva", "Rede de esgoto"],
    imagem=f"{SITE}/blog/img/nivel-4-cano-de-gordura.webp",
    videos=["FZJdTEZoqXE"],
    linkedin=LI + "tiramos-um-cano-de-gordura-dentro-uma-caixa-veja-o-que-vieira-nk1sf/",
    resumo="Depende de quanta gordura desce pela pia. Como referência, a Sanepar orienta limpar a caixa de gordura a cada 3 a 6 meses em residências, e com frequência mensal ou até quinzenal em restaurantes e cozinhas comerciais. O sinal mais seguro é olhar dentro: quando a camada de gordura chega perto da saída da caixa, já passou da hora. Caixa cheia deixa a gordura seguir para a rede, onde ela endurece e entope.",
    corpo='''    <p>A caixa de gordura é uma das peças mais esquecidas da casa. Ninguém lembra dela até a pia parar ou o quintal começar a cheirar mal. E quando ela fica cheia por muito tempo, a gordura passa para a rede de esgoto, onde o problema fica bem maior. Abaixo explico como ela funciona, como saber se está na hora de limpar e o que dá para fazer sem chamar ninguém.</p>

    <h2>De quanto em quanto tempo limpar a caixa de gordura?</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Tipo de imóvel</th><th>Referência de limpeza</th><th>Limpe antes se...</th></tr></thead>
        <tbody>
          <tr><td>Casa</td><td>A cada 3 a 6 meses</td><td>Cozinha muito com óleo ou fritura</td></tr>
          <tr><td>Condomínio (caixa coletiva)</td><td>Rotina fixa, definida pela administração</td><td>Algum morador reclama de pia lenta ou cheiro</td></tr>
          <tr><td>Restaurante, lanchonete, buffet</td><td>Mensal ou até quinzenal</td><td>Antes de eventos grandes ou temporadas de movimento</td></tr>
        </tbody>
      </table>
    </div>
    <p>Esses prazos são referência (a Sanepar, companhia de saneamento do Paraná, orienta nessa faixa). A forma mais confiável de definir a frequência do seu imóvel é abrir a caixa algumas vezes e ver em quanto tempo a camada de gordura se forma.</p>

    <h2>Como a caixa de gordura funciona?</h2>
    <p>A água da pia da cozinha não vai direto para a rede: passa antes pela caixa de gordura. Lá dentro, a água desacelera, a gordura (mais leve) sobe e fica presa na superfície, e a água segue por uma saída mais baixa. A norma de esgoto predial (ABNT NBR 8160) prevê a caixa de gordura justamente para reter a gordura antes que ela chegue à tubulação.</p>
    <p>O problema é que a caixa só retém, não elimina. A gordura vai acumulando e, quando a camada chega à saída, começa a passar junto com a água para a rede. Uma caixa cheia deixa de proteger o sistema e vira parte do problema.</p>

    <h2>Quais os sinais de caixa de gordura cheia?</h2>
    <ul>
      <li>Mau cheiro forte perto da caixa ou no quintal.</li>
      <li>Água escura ou preta dentro da caixa.</li>
      <li>Pia da cozinha escoando devagar, mesmo com o sifão limpo.</li>
      <li>Camada grossa de gordura na superfície, perto da altura da saída.</li>
      <li>Caixa transbordando ou água saindo pela tampa.</li>
    </ul>

    <div class="caso">
      <p><span class="rotulo">Caso real (Goiânia):</span> a pia da cozinha não escoava e a caixa de gordura estava com a água totalmente preta. Depois do desentupimento da pia e da limpeza da caixa, a água voltou a ficar transparente e a pia passou a escoar normalmente.</p>
    </div>

    ''' + video("FZJdTEZoqXE", "antes e depois da caixa de gordura em Goiânia", "Vídeo de antes e depois da limpeza de uma caixa de gordura com água preta em Goiânia",
                "Vídeo (caso real, 35 s): antes e depois da caixa de gordura. A água estava preta e voltou a ficar transparente depois do serviço.") + '''

    <div class="caso">
      <p><span class="rotulo">Caso real (o "cano de gordura"):</span> em outro atendimento, abrimos a caixa de gordura e, junto com a placa da superfície, saiu um bloco sólido, branco-amarelado, no formato exato do cano, com a marca da curva da conexão. É o que acontece quando a caixa fica cheia: a gordura passa para o cano seguinte, esfria e se molda lá dentro.</p>
    </div>

    ''' + FOTO_GORDURA + '''

    <h2>Dá para limpar a caixa de gordura sozinho?</h2>
    <p>Em casa, com caixa pequena e gordura ainda mole, dá:</p>
    <ol>
      <li>Use luva, máscara e roupa que possa sujar. O cheiro é forte.</li>
      <li>Abra a tampa e retire a camada de gordura da superfície com uma pá pequena ou um pote, colocando num balde.</li>
      <li>Coloque a gordura retirada em saco plástico resistente, bem fechado, e descarte no lixo comum. <strong>Nunca jogue de volta no vaso, no ralo ou na rua.</strong></li>
      <li>Raspe as paredes da caixa, feche bem a tampa e jogue água da torneira na pia para ver se escoa.</li>
    </ol>
    <p>Quando a gordura já endureceu, a caixa é grande (condomínio, restaurante) ou a rede depois dela também está lenta, o serviço precisa de equipamento e de descarte adequado do resíduo.</p>

    <h2>O que não fazer</h2>
    <ul class="nao">
      <li>Jogar soda cáustica ou produto para "derreter" a gordura. Ela amolece, segue para a rede e endurece de novo lá.</li>
      <li>Descartar a gordura retirada no vaso, no ralo ou no bueiro.</li>
      <li>Deixar a caixa sem tampa ou com tampa quebrada.</li>
      <li>Ligar ralo de quintal ou água de chuva na caixa de gordura. Ela enche de água, perde a função e transborda.</li>
    </ul>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>A gordura está dura, em blocos, e não sai com a pá.</li>
      <li>Mesmo com a caixa limpa, a pia continua lenta: a gordura já passou para a rede.</li>
      <li>A caixa transborda logo depois de limpa.</li>
      <li>É restaurante ou condomínio, com caixa grande e volume alto.</li>
    </ul>
    <p>Se a pia é o que está te incomodando, veja também <a href="../desentupir-pia-com-gordura/">como desentupir pia com gordura</a>.</p>''',
    faq=[
        ("De quanto em quanto tempo limpar a caixa de gordura em casa?", "Como referência, a cada 3 a 6 meses, mas depende de quanto óleo desce pela pia. O mais seguro é abrir a caixa e limpar quando a camada de gordura se aproxima da saída."),
        ("E em restaurante?", "Com frequência mensal ou até quinzenal, porque o volume de gordura é bem maior. Vale definir uma rotina fixa e limpar antes de eventos ou períodos de muito movimento."),
        ("Por que a água da caixa de gordura fica preta?", "Porque a caixa está cheia de gordura e matéria orgânica em decomposição. É sinal de que passou da hora de limpar."),
        ("Produto biológico ou enzimático substitui a limpeza?", "Não. Esses produtos ajudam na manutenção e no cheiro depois de uma limpeza, mas a gordura acumulada continua precisando ser retirada da caixa."),
        ("O que fazer com a gordura retirada da caixa?", "Colocar em saco plástico resistente, bem fechado, e descartar no lixo comum. Nunca jogar de volta no vaso, no ralo ou na rua."),
    ],
    fontes=["nbr8160", "sanepar", "eng360", "campo"],
    leia=["desentupir-pia-com-gordura", "pode-jogar-oleo-na-pia", "niveis-de-entupimento"],
)

# ---------------------------------------------------------------------------
# 10. Hidrojateamento
# ---------------------------------------------------------------------------
HIDRO = dict(
    slug="como-funciona-hidrojateamento",
    title="Como funciona o hidrojateamento (e quando usar)",
    h1="Como funciona o hidrojateamento",
    desc="O que é hidrojateamento, por que ele resolve entupimento de gordura que volta, quais os riscos para o cano e por que a técnica de quem opera importa.",
    migalha="Como funciona o hidrojateamento",
    keywords="hidrojateamento, hidrojato, como funciona hidrojateamento, desentupimento com hidrojato, hidrojateamento restaurante",
    sobre=["Hidrojateamento", "Desentupimento", "Gordura na tubulação"],
    imagem="https://i.ytimg.com/vi/D4aA6c9-8lc/maxresdefault.jpg",
    videos=["D4aA6c9-8lc"],
    linkedin=LI + "hidrojato-na-fossa-por-que-t%C3%A9cnica-importa-tanto-quanto-vieira-rz3zf/",
    resumo="Hidrojateamento é a limpeza do cano por dentro com água em alta pressão, geralmente entre 1.500 e 4.000 PSI em encanamentos. Uma mangueira com bico especial percorre a tubulação e os jatos raspam a gordura, o lodo e os resíduos grudados na parede. Diferente de produto químico ou arame, que só abrem um furo, o hidrojato limpa o cano inteiro, por isso é o mais indicado para gordura e entupimento que volta. A mesma pressão que limpa pode trincar cano velho, então o resultado depende de quem opera.",
    corpo='''    <p>Quando um cliente me diz "já desentupiu três vezes este ano", quase sempre o cano foi aberto, mas nunca foi limpo. É aí que entra o hidrojateamento. Neste guia explico como ele funciona, quando é a melhor opção e por que a técnica de quem opera importa tanto quanto a máquina.</p>

    <h2>Resumo: hidrojato x outros métodos</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Método</th><th>O que faz</th><th>Melhor para</th><th>Limite</th></tr></thead>
        <tbody>
          <tr><td>Produto químico / soda</td><td>Tenta dissolver</td><td>Nada que recomendemos</td><td>Corrosivo e não remove gordura endurecida</td></tr>
          <tr><td>Arame / cabo</td><td>Fura a obstrução</td><td>Cabelo na entrada do ralo</td><td>Abre um furo; o cano continua sujo</td></tr>
          <tr><td>Sonda rotativa</td><td>Rompe ou puxa mecanicamente</td><td>Objetos, raízes, bloqueios compactados</td><td>Não lava a parede do cano inteira</td></tr>
          <tr><td>Hidrojateamento</td><td>Lava a parede do cano com alta pressão</td><td>Gordura, lodo, areia, incrustações</td><td>Exige avaliação do cano antes</td></tr>
        </tbody>
      </table>
    </div>

    <h2>O que é hidrojateamento?</h2>
    <p>É a desobstrução e limpeza de tubulações com água em alta pressão. A máquina bombeia água por uma mangueira até um bico com saídas direcionadas: jatos para frente rompem a obstrução e jatos para trás impulsionam a mangueira e lavam a parede do cano enquanto ela avança. Em encanamentos, a pressão costuma ficar entre 1.500 e 4.000 PSI.</p>

    <h2>Por que o hidrojato resolve onde outros métodos falham?</h2>
    <p>Em cozinhas, o grande inimigo é a gordura. Ela desce quente pela pia, esfria no caminho, gruda na parede do cano e vai fechando a passagem camada por camada. Desentupidor químico e arame costumam só abrir um furo nessa massa: a água volta a descer, mas o cano continua sujo e entope de novo. Como o hidrojato raspa a parede inteira, ele desobstrui e, ao mesmo tempo, funciona como prevenção contra novos entupimentos.</p>

    <div class="caso">
      <p><span class="rotulo">Caso real (restaurante em Goiânia):</span> a rede de um restaurante simplesmente não descia; não era escoamento lento, a água parava. O primeiro passo em qualquer atendimento é achar um ponto de acesso, normalmente uma caixa de inspeção. Ali não havia nenhuma, e sem caixa não há por onde entrar sem quebrar piso. A solução foi abrir a fossa: o cano que chega até ela estava acessível por dentro, e foi por ali que introduzi a mangueira do hidrojato, trabalhando em direção à obstrução. Havia muita gordura e resíduo em toda a tubulação. Depois do serviço, a rede voltou a escoar.</p>
    </div>

    ''' + video("D4aA6c9-8lc", "hidrojato entrando pela fossa de um restaurante", "Vídeo do hidrojato operando pelo cano dentro da fossa de um restaurante em Goiânia",
                "Vídeo (caso real, 30 s): restaurante em Goiânia sem caixas de inspeção. O hidrojato entra pelo cano que chega à fossa para desobstruir a rede tomada por gordura.") + '''

    <h2>Hidrojato pode danificar o cano?</h2>
    <p>Pode, se for usado sem avaliação. O jato que limpa é o mesmo que pode trincar cano antigo, quebradiço ou corroído. Por isso, saber usar significa:</p>
    <ul>
      <li><strong>Ler a rede antes de ligar a máquina:</strong> material do cano, idade, trajeto e onde provavelmente está a obstrução.</li>
      <li><strong>Escolher o ponto de entrada certo.</strong> No restaurante, sem caixas de inspeção, foi a fossa. A escolha errada significa quebrar piso ou forçar o cano no lugar errado.</li>
      <li><strong>Dosar a pressão e escolher o bico</strong> conforme o tipo de resíduo e a resistência da tubulação.</li>
      <li><strong>Saber quando parar.</strong> Insistir com pressão num cano comprometido transforma um entupimento em obra.</li>
    </ul>

    <h2>Abrir uma fossa é perigoso?</h2>
    <p>É. A decomposição do esgoto gera gases como sulfeto de hidrogênio, metano, amônia e gás carbônico. O sulfeto de hidrogênio é extremamente tóxico: em concentração alta, pode causar perda de consciência em poucas respirações. O metano traz risco de explosão, e o gás carbônico, de asfixia. Esses gases são invisíveis e se acumulam rápido em tanques fechados. A regra que sigo e recomendo: nunca entre numa fossa, nunca se debruce sobre a abertura e deixe o local ventilar antes de qualquer trabalho.</p>

    <h2>Quando o hidrojateamento é indicado?</h2>
    <ul>
      <li>Entupimento de gordura que volta em poucas semanas.</li>
      <li>Cozinha de restaurante, lanchonete ou condomínio com histórico de entupimento.</li>
      <li>Rede pluvial com terra e areia acumuladas.</li>
      <li>Manutenção preventiva, antes que a cozinha pare em pleno expediente.</li>
    </ul>

    <h2>O que todo dono de restaurante pode fazer</h2>
    <ul>
      <li><strong>Instalar caixas de inspeção.</strong> É a principal lição do caso acima: sem elas, qualquer manutenção fica mais difícil, demorada e cara.</li>
      <li><strong>Manter a caixa de gordura limpa no prazo.</strong> Quando ela satura, a gordura segue direto para a rede.</li>
      <li><strong>Raspar pratos e panelas no lixo</strong> antes de lavar e usar peneira nos ralos da cozinha.</li>
      <li><strong>Fazer hidrojateamento preventivo</strong> em vez de esperar a rede parar.</li>
    </ul>

    <h2>O que não fazer</h2>
    <ul class="nao">
      <li>Usar soda cáustica ou desentupidor químico. O calor da reação pode amolecer cano de PVC e degradar vedações.</li>
      <li>Confiar em água fervente. Despejar grandes volumes repetidamente pode deformar o cano e comprometer as juntas.</li>
      <li>Usar lavadora de alta pressão doméstica no cano. Pressão sem controle e sem o bico certo pode soltar emendas.</li>
      <li>Abrir a fossa por conta própria.</li>
    </ul>
    <p>Veja também <a href="../precisa-quebrar-piso-para-desentupir/">quando é preciso quebrar o piso</a> e <a href="../limpeza-caixa-de-gordura/">de quanto em quanto tempo limpar a caixa de gordura</a>.</p>''',
    faq=[
        ("O que é hidrojateamento?", "É a desobstrução e limpeza de tubulações com água em alta pressão, geralmente entre 1.500 e 4.000 PSI em encanamentos. Os jatos rompem a obstrução e lavam a parede interna do cano."),
        ("Hidrojato pode danificar o encanamento?", "Pode, se aplicado sem avaliação ou com pressão inadequada, principalmente em canos antigos ou corroídos. Feito com técnica, avaliando o cano antes, é seguro."),
        ("Dá para fazer hidrojateamento sem caixa de inspeção?", "Sim, mas exige encontrar outro ponto de acesso, como um ralo, a caixa de gordura ou, em alguns casos, o cano que chega à fossa. Isso pede experiência para não quebrar piso nem danificar a rede."),
        ("Por que restaurantes entopem com tanta frequência?", "Por causa da gordura, que endurece ao esfriar e se acumula na parede do cano. Caixa de gordura sem limpeza no prazo faz o problema chegar mais rápido à rede."),
        ("É seguro abrir a fossa por conta própria?", "Não é recomendável, por causa dos gases tóxicos e inflamáveis que se acumulam ali, como sulfeto de hidrogênio e metano."),
    ],
    fontes=["bf_metodos", "bf_mitos", "wikem", "campo"],
    leia=["precisa-quebrar-piso-para-desentupir", "desentupir-pia-com-gordura", "limpeza-caixa-de-gordura"],
)

# ---------------------------------------------------------------------------
# 12. Óleo na pia + o que não usar
# ---------------------------------------------------------------------------
OLEO = dict(
    slug="pode-jogar-oleo-na-pia",
    title="Pode jogar óleo na pia? E o que não usar para desentupir",
    h1="Pode jogar óleo na pia? E o que não usar para desentupir",
    desc="Por que óleo na pia entope o cano, como descartar certo e o que nunca usar para desentupir: misturas de produtos, soda cáustica, água fervendo e arame.",
    migalha="Pode jogar óleo na pia?",
    keywords="pode jogar óleo na pia, óleo na pia entope, como descartar óleo de cozinha, soda cáustica desentupir, misturar água sanitária e vinagre",
    sobre=["Óleo de cozinha", "Descarte de óleo", "Produtos de limpeza", "Desentupimento"],
    imagem=f"{SITE}/blog/img/nivel-4-cano-de-gordura.webp",
    videos=["cjH3O35wWQI"],
    linkedin=LI + "saiba-como-gordura-para-dentro-do-seu-encanamento-caso-vieira-bnbif/",
    resumo="Não. Óleo de cozinha jogado na pia esfria dentro do cano, gruda na parede e, somado a restos de comida, fecha a passagem com o tempo; em Goiás, a Saneago aponta o óleo como causa de 25% dos extravasamentos de esgoto. O certo é esperar esfriar, guardar em garrafa PET fechada e levar a um ponto de coleta. Para desentupir, nunca misture produtos de limpeza (pode liberar gás tóxico) e evite soda cáustica, água fervendo e arame: o que resolve é sifão, ventosa e, se a gordura já endureceu, remoção mecânica.",
    corpo='''    <p>Você joga um pouco de óleo na pia, abre a torneira e, aparentemente, tudo vai embora. Só que a gordura sumir da sua frente não é o mesmo que ela sair do sistema de esgoto. Em 10 anos de serviço, já tirei de caixas de gordura blocos sólidos no formato exato do cano. Neste guia explico por que o óleo entope, como descartar e o que nunca usar na hora de desentupir.</p>

    <h2>Resumo: o que não usar para desentupir</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>O que as pessoas usam</th><th>Risco</th><th>Por quê</th></tr></thead>
        <tbody>
          <tr><td>Mistura de produtos de limpeza</td><td><strong>Grave</strong></td><td>Pode liberar gás tóxico (cloro, cloraminas)</td></tr>
          <tr><td>Soda cáustica e desentupidor químico</td><td><strong>Grave</strong></td><td>Queimaduras na pele e nos olhos; com gordura, pode endurecer a massa</td></tr>
          <tr><td>Água fervendo</td><td>Moderado</td><td>Deforma cano de PVC e só empurra a gordura para frente</td></tr>
          <tr><td>Arame, cabide, cabo de vassoura</td><td>Moderado</td><td>Fura o cano, solta conexões ou fica preso dentro</td></tr>
          <tr><td>Ar comprimido e "bombinhas"</td><td>Moderado</td><td>Pressão sem controle pode soltar emendas</td></tr>
          <tr><td>Refrigerante, sal grosso, bicarbonato com vinagre</td><td>Leve</td><td>Não fazem mal, mas raramente resolvem gordura endurecida</td></tr>
        </tbody>
      </table>
    </div>

    <h2>Por que não pode jogar óleo na pia?</h2>
    <p>O óleo desce quente e líquido, encontra o cano frio e começa a endurecer na parede. Camada após camada, o diâmetro útil do cano vai fechando e restos de comida se prendem nele, até que um dia a água para de descer. No setor de saneamento, esse material é chamado de FOG (gorduras, óleos e graxas), e a agência ambiental dos EUA (EPA) o reconhece como uma das causas importantes de bloqueio em redes de esgoto. Em Goiás, um estudo da Saneago aponta que 25% dos extravasamentos de esgoto são causados pelo descarte de óleo em pias e ralos.</p>

    ''' + video("cjH3O35wWQI", "como a gordura se acumula dentro do cano", "Vídeo de Lucas Nonato mostrando o acúmulo de gordura dentro da tubulação",
                "Vídeo (caso real, 1 min): Lucas Nonato mostra como a gordura se prende às paredes internas do cano e reduz a passagem da água.") + '''

    <div class="caso">
      <p><span class="rotulo">Caso real (o "cano de gordura"):</span> abrimos a caixa de gordura de um cliente e, junto com a placa da superfície, saiu um bloco sólido, branco-amarelado, no formato exato do cano, redondo, comprido e com a marca da curva da conexão. A caixa existe para separar a gordura da água; quando não é limpa, enche, e a gordura passa para o cano seguinte e se solidifica lá dentro.</p>
    </div>

    ''' + FOTO_GORDURA + '''

    <h2>Como descartar o óleo de cozinha usado?</h2>
    <ol>
      <li>Espere o óleo esfriar.</li>
      <li>Coloque em garrafa PET limpa, com tampa.</li>
      <li>Leve a um ponto de coleta ou programa de reciclagem. Em Goiás, a Saneago tem o programa Olho no Óleo, que dá desconto na conta de água para quem entrega o óleo usado.</li>
    </ol>
    <p>O óleo recolhido vira sabão, biodiesel e outros produtos. Nunca descarte na pia, no vaso, no quintal ou no solo.</p>

    <h2>O que não usar para desentupir (do mais grave ao mais leve)</h2>

    <h3>1. Misturar produtos de limpeza</h3>
    <p>É o erro que mais me assusta, porque é feito por quem quer "reforçar" a limpeza. Água sanitária com vinagre ou qualquer ácido pode liberar gás cloro; com produtos à base de amônia forma cloraminas, que irritam os olhos e as vias respiratórias; com álcool pode formar clorofórmio. A orientação da Anvisa é usar cada produto sozinho ou diluído só em água. Se acontecer, saia do ambiente, procure um lugar ventilado e ligue para o Disque-Intoxicação: 0800-722-6001.</p>
    <p>Detalhe que pouca gente sabe: muita pia entupida já tem soda ou desentupidor químico parado dentro. Jogar outro produto por cima é misturar química às cegas.</p>

    <h3>2. Soda cáustica e desentupidor químico</h3>
    <p>A soda (hidróxido de sódio) causa queimaduras graves na pele e nos olhos e libera calor ao entrar em contato com a água. Com o cano totalmente entupido, o produto fica parado ali: se você usar a ventosa depois, pode respingar no rosto. E com a gordura a soda forma uma espécie de sabão que, em vez de sumir, pode deixar a massa ainda mais dura.</p>

    <h3>3. Água fervendo</h3>
    <p>O tubo de esgoto de PVC comum tem temperatura máxima de trabalho bem abaixo da fervura: a Tigre informa 45 °C em regime não contínuo, e água fervendo chega a 100 °C. O calor pode deformar o cano e desgastar juntas e vedações, causando vazamento escondido. E a gordura derretida volta a endurecer alguns metros à frente, num trecho mais difícil de alcançar.</p>

    <h3>4. Arame, cabide e cabo de vassoura</h3>
    <p>Raspam ou furam o PVC, principalmente nas curvas, podem desencaixar o sifão e, às vezes, quebram e ficam presos dentro, virando um segundo entupimento.</p>

    <h3>5. Ar comprimido e "bombinhas"</h3>
    <p>Pressionar o cano sem controle pode soltar emendas que estavam só encaixadas. O hidrojateamento profissional é diferente: pressão regulada, bico certo para o diâmetro e direção controlada.</p>

    <h3>6. Refrigerante, sal grosso, bicarbonato com vinagre</h3>
    <p>Não oferecem perigo, mas raramente resolvem gordura endurecida. Bicarbonato com vinagre faz espuma, mas um neutraliza o outro e sobra pouco poder de limpeza.</p>

    <h2>O que funciona de verdade?</h2>
    <ul>
      <li><strong>Sifão primeiro:</strong> desmonte com um balde embaixo e lave. Boa parte dos entupimentos de pia está ali.</li>
      <li><strong>Ventosa, nunca química:</strong> tampe o ladrão (e o ralo da outra cuba, se for dupla) antes de bombear.</li>
      <li><strong>Água quente da torneira com detergente</strong> só como manutenção leve, não como desentupidor.</li>
      <li><strong>Produtos enzimáticos</strong> ajudam na manutenção depois de uma limpeza, mas não desentopem cano fechado.</li>
      <li>Se a gordura já endureceu, a solução é <a href="../como-funciona-hidrojateamento/">remoção mecânica ou hidrojateamento</a>.</li>
    </ul>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>Sifão e ventosa não resolveram.</li>
      <li>Já foi colocado produto químico e o cano continua entupido.</li>
      <li>A pia volta a entupir em pouco tempo ou a caixa de gordura transborda.</li>
    </ul>
    <p>Veja também <a href="../desentupir-pia-com-gordura/">como desentupir pia com gordura</a> e <a href="../limpeza-caixa-de-gordura/">de quanto em quanto tempo limpar a caixa de gordura</a>.</p>''',
    faq=[
        ("Pode jogar óleo de cozinha na pia?", "Não. O óleo esfria dentro do cano, gruda na parede e, com restos de comida, fecha a passagem com o tempo. Em Goiás, a Saneago aponta o óleo como causa de 25% dos extravasamentos de esgoto."),
        ("Pouco óleo na pia também entope?", "Sim. Mesmo pequenas quantidades formam camadas quando o descarte se repete todo dia. O entupimento costuma ser resultado desse acúmulo."),
        ("Como descartar óleo de cozinha usado?", "Espere esfriar, coloque em garrafa PET com tampa e leve a um ponto de coleta. Em Goiás, o programa Olho no Óleo, da Saneago, dá desconto na conta de água para quem entrega o óleo."),
        ("Pode misturar água sanitária e vinagre para desentupir?", "Não. Água sanitária com vinagre ou qualquer ácido pode liberar gás cloro, que é tóxico. A Anvisa orienta usar cada produto sozinho ou diluído só em água."),
        ("Soda cáustica desentope gordura?", "Não é recomendado. A soda causa queimaduras graves e, com a gordura, pode formar uma massa ainda mais dura dentro do cano."),
    ],
    fontes=["saneago_oleo", "epa_fog", "anvisa", "tigre45", "campo"],
    leia=["desentupir-pia-com-gordura", "limpeza-caixa-de-gordura", "como-funciona-hidrojateamento"],
)

for a in (REDE, VASO, PISO, PIA, CAIXA, HIDRO, OLEO):
    gerar(a)

atualizar_listas()
