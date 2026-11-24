# Conteúdo dos artigos. Executado por gerar_artigos.py (usa video(), FOTO_GORDURA, gerar()).

# Publicação: 2 por semana. Para publicar o próximo, mova o primeiro slug de FILA para PUB,
# coloque a data em DATAS e rode `python tools/gerar_artigos.py publicar/blog`.
PUB = ["niveis-de-entupimento", "rede-pluvial-entupida", "vaso-sanitario-entupido",
       "precisa-quebrar-piso-para-desentupir", "desentupir-pia-com-gordura", "raizes-na-rede-pluvial",
       "limpeza-caixa-de-gordura", "como-funciona-hidrojateamento", "cimento-no-encanamento",
       "pode-jogar-oleo-na-pia", "caixa-cega-esgoto", "desentupimento-hospitais-e-clinicas",
       "gordura-endurecida-no-cano", "entupimento-recorrente"]
DATAS = {"niveis-de-entupimento": "2026-10-26", "rede-pluvial-entupida": "2026-10-26",
         "vaso-sanitario-entupido": "2026-10-27", "historia-bv-desentupidora": "2026-11-02",
         "precisa-quebrar-piso-para-desentupir": "2026-11-02", "desentupir-pia-com-gordura": "2026-11-02",
         "raizes-na-rede-pluvial": "2026-11-07",
         "limpeza-caixa-de-gordura": "2026-11-09", "como-funciona-hidrojateamento": "2026-11-09",
         "cimento-no-encanamento": "2026-11-10", "pode-jogar-oleo-na-pia": "2026-11-10",
         "caixa-cega-esgoto": "2026-11-14", "desentupimento-hospitais-e-clinicas": "2026-11-19",
         "gordura-endurecida-no-cano": "2026-11-24",
         "entupimento-recorrente": "2026-11-24"}
FILA = []
# Artigos escritos à mão (não gerados aqui): entram no índice, llms.txt e sitemap, mas não no "Leia também".
EXTRAS = ["historia-bv-desentupidora"]

# slug: (título na lista, frase do índice do blog, frase do llms.txt)
LISTA = {
    "historia-bv-desentupidora": ("A história da BV Desentupidora: de Goiânia a Itaberaí e de volta à capital",
                                  "Como a BV começou em Goiânia em 2016, nasceu em Itaberaí em 2017 e voltou à capital.",
                                  "como a BV Desentupidora começou em Goiânia (2016), nasceu em Itaberaí (GO) em 2017 com Benedito Nonato Vieira Filho e voltou a Goiânia; quem é quem, as duas empresas, telefones e canais oficiais."),
    "niveis-de-entupimento": ("Entupimento em Goiânia: como saber se é grave pelos 4 níveis e o que fazer em cada um",
                              "Um guia para identificar o nível do entupimento, o que dá para resolver em casa e quando chamar um profissional.",
                              "como identificar se o entupimento é simples ou está na rede, o que resolver em casa, o que não fazer e quando chamar um profissional."),
    "rede-pluvial-entupida": ("Rede pluvial entupida em Goiânia: sinais, causas e prevenção antes das chuvas",
                              "Como saber se a rede pluvial está entupida, o que mais entope e o que fazer antes das chuvas.",
                              "sinais de rede pluvial entupida, o que mais entope (caso real em Heitoraí, GO, com vídeo) e como prevenir antes das chuvas."),
    "vaso-sanitario-entupido": ("Vaso sanitário entupido em Goiânia: o que fazer passo a passo",
                                "Como usar a ventosa certa, o que nunca jogar no vaso e o sinal de que o problema está na rede.",
                                "passo a passo com ventosa, o que não jogar no vaso e por que vaso e ralo entopem juntos (caso real em casa de eventos)."),
    "precisa-quebrar-piso-para-desentupir": ("Precisa quebrar o piso para desentupir em Goiânia?",
                                             "Por onde o profissional entra na tubulação sem quebrar e quando a quebra é inevitável.",
                                             "na maioria dos casos não: acessos usados, sonda rotativa x hidrojato e quando a quebra é inevitável (caso real em Itaberaí, GO)."),
    "desentupir-pia-com-gordura": ("Como desentupir pia com gordura em Goiânia: o que funciona de verdade",
                                   "Sifão, ventosa, o limite da água quente e quando a gordura já virou placa no cano.",
                                   "como a gordura vira placa no cano, passo a passo com sifão e ventosa e o que não fazer (caso real em Inhumas, GO)."),
    "raizes-na-rede-pluvial": ("Raízes na rede pluvial em Goiânia: o alerta que canteiros perto da tubulação escondem",
                               "Como a raiz entra no cano, os sinais, a distância segura do canteiro e se é preciso quebrar o piso.",
                               "como a raiz de um canteiro entra na rede pluvial, sinais, distância segura, cimento no cano e caso real com 2 metros de raiz retirados sem quebrar o piso."),
    "limpeza-caixa-de-gordura": ("Caixa de gordura em Goiânia: de quanto em quanto tempo limpar",
                                 "Frequência de limpeza em casa e em restaurante, sinais de caixa cheia e o descarte da gordura.",
                                 "frequência de limpeza (3 a 6 meses em casa; mensal ou quinzenal em restaurante), sinais de caixa cheia e como limpar."),
    "como-funciona-hidrojateamento": ("Como funciona o hidrojateamento em Goiânia",
                                      "O que é, por que resolve entupimento de gordura que volta e por que a técnica importa.",
                                      "o que é (1.500 a 4.000 PSI), quando usar, riscos para o cano e segurança em fossas (caso real em restaurante de Goiânia)."),
    "cimento-no-encanamento": ("Cimento no encanamento em Goiânia: por que vira pedra dentro do cano e o que fazer se cair no ralo",
                               "Por que lavar ferramenta de obra no ralo entope, onde lavar e o que fazer nas primeiras horas.",
                               "por que o cimento endurece mesmo dentro do cano cheio d'água, onde lavar ferramentas de obra, o que fazer se cair cimento no ralo (hidrojato no mesmo dia) e mitos e verdades; caso real em Goiânia com vídeo comparando trecho limpo e trecho sujo."),
    "pode-jogar-oleo-na-pia": ("Pode jogar óleo na pia? Como descartar em Goiânia e o que não usar para desentupir",
                               "Por que o óleo entope, como descartar e o que nunca usar para desentupir.",
                               "por que óleo na pia entope, como descartar e o que não usar para desentupir: misturas de produtos, soda, água fervendo e arame."),
    "caixa-cega-esgoto": ("Caixa cega no esgoto em Goiânia: o que é e por que encarece o desentupimento",
                          "A caixa de passagem lacrada debaixo do piso: por que o serviço fica mais caro, o mau cheiro e como evitar.",
                          "o que é caixa cega (caixa de passagem lacrada com contrapiso e piso), por que encarece o desentupimento, mau cheiro e infiltração, como se localiza a caixa (inclusive pelo som, com martelo de borracha) e caso real em uma jantinha no interior de Goiás, resolvido em 4 horas, com vídeos."),
    "desentupimento-hospitais-e-clinicas": ("Desentupimento especializado em hospitais e clínicas de Goiânia: riscos e como fazer a manutenção certa",
                                            "Por que ralo entupido ou com cheiro é risco para pacientes, as áreas críticas e como a manutenção deve ser feita.",
                                            "por que ralos, pias e sifões entupidos ou com mau cheiro são risco em hospitais e clínicas (estudos de surtos em UTI), pacientes e áreas que exigem cuidado, frequência de manutenção preventiva e como executar o serviço com autorização da CCIH, isolamento, EPI e registro."),
    "gordura-endurecida-no-cano": ("Gordura endurecida no cano em Goiânia: por que vira pedra e como remover sem danificar o encanamento",
                                   "Gordura comum x saponificada, o papel da soda cáustica, sonda rotativa x hidrojato e quando trocar o cano.",
                                   "por que a gordura vira pedra no cano (saponificação: ácidos graxos + cálcio formam sabão duro), como a soda cáustica contribui, se desentupidores de mercado como o Diabo Verde funcionam, qual método usar em cada nível (desengordurante no nível 1, sonda rotativa nos níveis 2 e 3, hidrojateamento no nível 4) e quando o cano pode ser recuperado ou precisa ser trocado."),
    "entupimento-recorrente": ("Entupimento recorrente em Goiânia: como saber se é gordura, cano sem caimento ou cano deformado",
                               "Como diferenciar gordura, contrapendente e cano amassado, e quando a sonda rotativa não basta.",
                               "como diferenciar as 3 causas do entupimento que volta (gordura acumulada, pouco caimento ou contrapendente e cano deformado), por que o desentupimento resolve só por um tempo, declividade mínima da NBR 8160 (2% até 75 mm, 1% a partir de 100 mm), quando a sonda rotativa resolve e quando é preciso corrigir o trecho; caso real de rede pluvial achatada em Itaberaí (GO) com vídeo."),
}

LI = "https://www.linkedin.com/pulse/"

# ---------------------------------------------------------------------------
# 2. Rede pluvial
# ---------------------------------------------------------------------------
REDE = dict(
    slug="rede-pluvial-entupida",
    title="Rede pluvial entupida em Goiânia: sinais, causas e prevenção",
    h1="Rede pluvial entupida em Goiânia: sinais, causas e prevenção antes das chuvas",
    desc="Como saber se a rede pluvial está entupida, o que costuma causar o problema e o que fazer antes das chuvas para o quintal e a calha não alagarem.",
    migalha="Rede pluvial entupida",
    keywords="rede pluvial entupida, ralo do quintal entupido, calha transbordando, água da chuva não escoa, desentupimento de rede pluvial",
    sobre=["Rede pluvial", "Drenagem de águas pluviais", "Desentupimento"],
    imagem="https://i.ytimg.com/vi/rIHn8FNLqQM/maxresdefault.jpg",
    videos=["rIHn8FNLqQM", "lk54797N6pM"],
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

    <h2>E quando o cano está achatado e cheio de terra?</h2>
    <p>Nem toda rede pluvial entupida se resolve do mesmo jeito. Quando um trecho do cano está achatado, o espaço interno fica menor, a água perde força ali e a terra assenta justamente nesse ponto. Com o tempo, a terra compactada fecha o que sobrou da passagem.</p>
    <div class="caso">
      <p><span class="rotulo">Caso real (Itaberaí, GO, novembro de 2026):</span> a rede pluvial de um sobradinho estava obstruída havia meses. O cano tinha um trecho achatado e estava tomado por terra. O hidrojato, que costuma ser a primeira escolha em rede pluvial, não tinha passagem: o bico não avançava e a água voltava. Insistir com mais pressão num cano já deformado seria arriscar romper o tubo. Trocamos para a sonda rotativa e fomos devagar, avançando, recuando para tirar a terra solta e avançando de novo, sem forçar o trecho achatado. Foram muitas horas de serviço, com as equipes da BV de Itaberaí e de Goiânia, e muita terra retirada até a água voltar a correr.</p>
      <p>Desentupir devolve a passagem, mas não desamassa o cano. Esse trecho continua sendo o primeiro lugar onde a terra volta a acumular; se a rede fechar de novo, vale avaliar a troca só daquele pedaço.</p>
    </div>

    ''' + video("lk54797N6pM", "sonda rotativa em rede pluvial com cano achatado", "Sonda rotativa trabalhando na rede pluvial de um sobradinho em Itaberaí (GO)",
                "Vídeo (caso real, 41 s): a sonda rotativa abrindo a passagem no cano achatado e a água voltando a escorrer depois de meses de rede parada.") + '''

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
    fontes=["nbr10844", "epa", "fabricantes", "li_sonda", "campo"],
    leia=["niveis-de-entupimento", "precisa-quebrar-piso-para-desentupir", "como-funciona-hidrojateamento"],
)

# ---------------------------------------------------------------------------
# 3. Vaso sanitário
# ---------------------------------------------------------------------------
VASO = dict(
    slug="vaso-sanitario-entupido",
    title="Vaso sanitário entupido em Goiânia: o que fazer passo a passo",
    h1="Vaso sanitário entupido em Goiânia: o que fazer passo a passo",
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
    title="Precisa quebrar o piso para desentupir em Goiânia? Quase nunca",
    h1="Precisa quebrar o piso para desentupir em Goiânia?",
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
      <li>Cobrir caixas de inspeção com piso na reforma. É isso que, mais tarde, obriga a quebrar: veja o que é uma <a href="../caixa-cega-esgoto/">caixa cega</a>.</li>
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
    title="Como desentupir pia com gordura em Goiânia: o que funciona",
    h1="Como desentupir pia com gordura em Goiânia: o que funciona de verdade",
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
    leia=["limpeza-caixa-de-gordura", "pode-jogar-oleo-na-pia", "como-funciona-hidrojateamento", "niveis-de-entupimento"],
)

# ---------------------------------------------------------------------------
# 9. Caixa de gordura
# ---------------------------------------------------------------------------
CAIXA = dict(
    slug="limpeza-caixa-de-gordura",
    title="Caixa de gordura em Goiânia: de quanto em quanto tempo limpar",
    h1="Caixa de gordura em Goiânia: de quanto em quanto tempo limpar",
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
    title="Como funciona o hidrojateamento em Goiânia (e quando usar)",
    h1="Como funciona o hidrojateamento em Goiânia",
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
    title="Pode jogar óleo na pia? Como descartar em Goiânia",
    h1="Pode jogar óleo na pia? Como descartar em Goiânia e o que não usar para desentupir",
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
    <p>O óleo usado não vai para a pia, o vaso, o ralo, o bueiro nem o quintal. O bueiro é rede pluvial: o que entra nele vai direto para córregos e rios, sem tratamento. O caminho certo é simples:</p>
    <ol>
      <li><strong>Espere esfriar.</strong> Óleo quente queima e amolece a garrafa PET.</li>
      <li><strong>Coe os restos de comida</strong> com uma peneira ou um pano fino.</li>
      <li><strong>Guarde em garrafa PET limpa e seca, com tampa de rosca.</strong> Um funil evita que escorra. Dá para juntar o óleo de várias frituras na mesma garrafa até encher; mantenha bem fechada, longe do sol e do fogão.</li>
      <li><strong>Leve a um ponto de coleta.</strong> Em Goiás, a Saneago recebe o óleo pelo programa Olho no Óleo em postos de coleta como as unidades do Vapt Vupt, em Goiânia, Anápolis e outras cidades, e transforma cada litro entregue em crédito na conta de água (em 2023, R$ 0,50 por litro). Bares, restaurantes, supermercados e condomínios podem se cadastrar para a Saneago buscar o óleo no local. Alguns supermercados e cooperativas de reciclagem também recebem; pergunte antes de levar.</li>
    </ol>

    <h3>E a gordura que fica na panela e no prato?</h3>
    <p>É ela que vai para a pia todo dia sem ninguém perceber. Antes de lavar, passe papel-toalha na panela, na frigideira e nos pratos e jogue o papel no lixo comum. Gordura que endureceu na assadeira, como a de carne ou bacon, sai melhor raspada com uma espátula, direto para o lixo. Só depois leve a louça para a pia, com água e detergente.</p>
    <p>O óleo recolhido vira biodiesel, sabão e outros produtos. Jogado na pia, ele vira o bloco de gordura da foto acima.</p>

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
        ("Como descartar óleo de cozinha usado?", "Espere esfriar, coe os restos de comida, guarde em garrafa PET com tampa de rosca e leve a um ponto de coleta. Em Goiás, o programa Olho no Óleo, da Saneago, recebe o óleo em postos como o Vapt Vupt e dá crédito na conta de água por litro entregue."),
        ("Pode misturar água sanitária e vinagre para desentupir?", "Não. Água sanitária com vinagre ou qualquer ácido pode liberar gás cloro, que é tóxico. A Anvisa orienta usar cada produto sozinho ou diluído só em água."),
        ("Soda cáustica desentope gordura?", "Não é recomendado. A soda causa queimaduras graves e, com a gordura, pode formar uma massa ainda mais dura dentro do cano."),
    ],
    fontes=["saneago_oleo", "epa_fog", "anvisa", "tigre45", "campo"],
    leia=["desentupir-pia-com-gordura", "limpeza-caixa-de-gordura", "como-funciona-hidrojateamento"],
)

# ---------------------------------------------------------------------------
# Raízes na rede pluvial (texto do Antonio, 07/11/2026)
# ---------------------------------------------------------------------------
RAIZES = dict(
    slug="raizes-na-rede-pluvial",
    title="Raízes na rede pluvial em Goiânia: o risco dos canteiros",
    h1="Raízes na rede pluvial em Goiânia: o alerta que canteiros perto da tubulação escondem",
    desc="Raízes de um canteiro entraram na rede pluvial e causaram 2 anos de alagamento. Veja os sinais, a distância segura e se é preciso quebrar o piso.",
    migalha="Raízes na rede pluvial",
    keywords="raízes na rede pluvial, raiz dentro do cano, canteiro perto da tubulação, quintal alagando quando chove, precisa quebrar para tirar raiz do cano",
    sobre=["Rede pluvial", "Raízes em tubulações", "Hidrojateamento"],
    imagem=f"{SITE}/blog/img/raiz-2-metros-capa.webp",
    videos=["MWbG7DCMUyo", "hQdNCBS5Q6M"],
    resumo="Raízes de plantas procuram umidade e entram na rede pluvial por juntas mal vedadas, trincas ou caixas sem tampa. Dentro do cano, elas crescem, prendem terra, folhas e objetos, e a água da chuva para de escoar. Em um atendimento recente, retiramos cerca de 2 metros de raiz de dentro de uma tubulação pluvial que alagava a casa havia 2 anos. Na maioria dos casos dá para desobstruir sem quebrar o piso, mas o canteiro precisa ser tratado, ou a raiz volta.",
    corpo='''    <h2>Resumo: raízes na rede pluvial em 6 respostas</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Pergunta</th><th>Resposta curta</th></tr></thead>
        <tbody>
          <tr><td>Por que a raiz entra no cano?</td><td>Busca água e encontra juntas, trincas ou caixas abertas</td></tr>
          <tr><td>Qual o sinal mais comum?</td><td>Quintal ou garagem que alaga a cada chuva forte</td></tr>
          <tr><td>Produto químico resolve?</td><td>Não. Raiz é material vivo e fibroso</td></tr>
          <tr><td>Precisa quebrar e trocar os canos?</td><td>Quase sempre não; avalie a desobstrução antes</td></tr>
          <tr><td>Como evitar que volte?</td><td>Afastar o canteiro, vedar juntas e revisar antes das chuvas</td></tr>
          <tr><td>Melhor época para revisar em Goiás</td><td>Setembro e início de outubro, antes do período chuvoso</td></tr>
        </tbody>
      </table>
    </div>

    <h2>Como a raiz de um canteiro entra na rede pluvial?</h2>
    <p>A raiz não fura um cano inteiro. Ela entra por onde já existe uma abertura: junta de PVC mal colada, trinca causada por recalque do solo, tubo de concreto antigo ou caixa de passagem sem tampa e coberta de terra.</p>
    <p>A rede pluvial é um alvo fácil por três motivos:</p>
    <ul>
      <li>Fica úmida por dias depois de cada chuva, e a raiz cresce na direção da água.</li>
      <li>Costuma ser rasa e passar rente a muros, jardins e canteiros.</li>
      <li>Carrega terra e matéria orgânica, que alimentam a raiz dentro do tubo.</li>
    </ul>
    <p>Uma vez dentro, a raiz engrossa e se ramifica no sentido do fluxo. Ela vira uma peneira: segura folhas, areia e objetos, e o cano fecha aos poucos. Por isso o problema costuma piorar ano a ano, e não de uma vez.</p>

    <h2>Caso real: 2 anos de alagamento e 2 metros de raiz dentro do cano</h2>
    <p>Este atendimento mostra, na prática, o que explico no guia sobre <a href="../rede-pluvial-entupida/">rede pluvial entupida</a>.</p>
    <div class="caso">
      <p>Fomos chamados para desentupir a rede de esgoto de uma residência. Durante o serviço, encontramos a rede pluvial do imóvel com as caixas cobertas de terra. Alertamos a cliente sobre o risco de alagamento com as chuvas de fim de ano.</p>
      <p>A resposta dela mostrou o tamanho do problema: a casa já alagava havia 2 anos. Ela tentou desobstruir por conta própria várias vezes, sem resultado, e estava desistindo. Um pedreiro tinha recomendado quebrar o piso e trocar toda a tubulação.</p>
      <p>Propusemos tentar a desobstrução antes de qualquer quebra. Dentro da rede, encontramos:</p>
      <ul>
        <li>Bolas de tênis e bolinhas de cachorro</li>
        <li>Tampas de garrafa</li>
        <li>Terra compactada e restos de cimento endurecidos na parede do cano</li>
        <li>Raízes do canteiro ao lado, com cerca de 2 metros de comprimento</li>
      </ul>
      <p>Os objetos explicam parte do entupimento. Bolinhas rolam pelo quintal e entram por ralos sem grelha ou caixas abertas. Mas foram as raízes que transformaram a rede em uma barreira: elas prenderam cada objeto e cada punhado de terra que passava.</p>
      <p>Usamos <a href="../como-funciona-hidrojateamento/">hidrojateamento</a>: o jato de alta pressão cortou as raízes, soltou o cimento e arrastou os objetos até a caixa, onde foram retirados. Depois, testamos o escoamento com água e a rede voltou a funcionar sem quebrar o piso. A cliente foi orientada sobre o canteiro, porque a raiz que ficou no solo continua procurando água.</p>
    </div>

    <figure class="foto-vertical">
      <img src="../img/raiz-2-metros-retirada-rede-pluvial.webp" alt="Técnico da BV Desentupidora segura raiz de cerca de 2 metros retirada de rede pluvial residencial" width="873" height="1200" loading="lazy">
      <figcaption>Raiz de cerca de 2 metros retirada de dentro da rede pluvial.</figcaption>
    </figure>

    <figure class="foto-vertical">
      <img src="../img/raiz-saindo-caixa-pluvial-canteiro.webp" alt="Raiz do canteiro retirada da caixa de passagem da rede pluvial, ao lado das plantas" width="931" height="1200" loading="lazy">
      <figcaption>A raiz saindo da caixa de passagem, rente ao canteiro de onde veio.</figcaption>
    </figure>

    ''' + video("MWbG7DCMUyo", "raiz de 2 metros dentro da rede pluvial", "Técnico segura a raiz de cerca de 2 metros retirada da rede pluvial, no quintal da casa",
                "Vídeo (caso real, 1 min): a rede pluvial que alagava a casa havia 2 anos, resolvida com desobstrução, sem quebrar o piso.") + '''

    <h2>Cimento na rede pluvial: o perigo de lavar ferramentas no ralo durante obra ou reforma</h2>
    <p>No mesmo desentupimento, encontramos cimento endurecido dentro da tubulação. Ele vem de um hábito comum em obra e reforma: lavar baldes, colher de pedreiro, betoneira e desempenadeira no ralo do quintal.</p>
    <p>O cimento não se dissolve na água. Ele assenta no fundo do cano, endurece e fica preso à parede. Com isso:</p>
    <ul>
      <li>O diâmetro útil do cano diminui a cada lavagem</li>
      <li>A superfície fica áspera e passa a segurar terra, folhas e raízes</li>
      <li>Na próxima chuva forte, a água não tem por onde passar</li>
    </ul>
    <p>No vídeo deste caso, mostro como o cimento fica dentro da tubulação e comparo dois trechos da mesma rede: um já desobstruído e limpo e outro ainda sujo, antes da passagem do hidrojato. Explico o assunto em detalhe no artigo sobre <a href="../cimento-no-encanamento/">cimento no encanamento</a>.</p>

    ''' + video("hQdNCBS5Q6M", "cimento na rede pluvial, antes e depois", "Vídeo comparando dois trechos da mesma rede pluvial, um limpo e outro ainda sujo",
                "Vídeo (caso real, 47 s): à esquerda, a tubulação já limpa; à direita, a que ainda estava suja.") + '''

    <p>Como evitar durante uma obra ou reforma:</p>
    <ul>
      <li>Lave ferramentas dentro de um balde ou tambor, nunca no ralo</li>
      <li>Deixe a água descansar até o material assentar no fundo</li>
      <li>Descarte o resíduo sólido junto com o entulho da obra</li>
      <li>Tampe ralos e caixas de passagem enquanto a obra durar</li>
      <li>Combine essa regra com o pedreiro antes do início do serviço</li>
    </ul>

    <h2>Quais sinais indicam raiz dentro da rede pluvial?</h2>
    <ul>
      <li>Quintal, garagem ou área externa que alaga em toda chuva forte, mesmo com ralos limpos</li>
      <li>Água que escoa devagar e volta pelo ralo durante a chuva</li>
      <li>Caixa de passagem com terra, lodo ou raízes finas aparecendo</li>
      <li>Entupimento que volta pouco tempo depois de uma limpeza</li>
      <li>Canteiro, árvore ou arbusto a menos de 1 ou 2 metros da linha do cano</li>
      <li>Piso cedendo ou trincando em cima do trajeto da tubulação</li>
    </ul>
    <p>Quando dois ou mais desses sinais aparecem juntos e há plantas perto, a raiz deve ser a primeira suspeita.</p>

    <h2>Qual a distância segura entre canteiro e rede pluvial?</h2>
    <p>Não existe uma medida única, porque depende da planta. A regra prática citada por paisagistas é manter a planta a uma distância equivalente, no mínimo, à metade da largura da copa adulta. Para árvores de raiz agressiva, como o fícus, a recomendação vai de 10 a 15 metros de qualquer construção ou tubulação.</p>
    <p>Na minha experiência com canteiros residenciais, o que mais causa problema é:</p>
    <ul>
      <li>Canteiro plantado em cima ou rente à linha do cano</li>
      <li>Arbustos e árvores de raiz superficial perto de caixas de passagem</li>
      <li>Canteiro sem fundo, sobre solo raso, que força a raiz a correr para os lados</li>
    </ul>
    <p>Antes de plantar, descubra por onde passa a rede pluvial. Prefira espécies de raiz profunda ou de pequeno porte perto de tubulações, como ipê ou pitangueira, e mantenha as caixas de inspeção livres e com tampa.</p>

    <h2>Dicas caseiras que ajudam (e as que não funcionam)</h2>
    <p>O que você pode fazer em casa, com segurança:</p>
    <ul>
      <li><strong>Teste da mangueira:</strong> jogue água em cada ralo externo em dia seco e veja se ela some rápido. Água parada indica obstrução.</li>
      <li>Abra as caixas de passagem e retire terra e folhas acumuladas na superfície.</li>
      <li>Coloque grelha em ralos externos. Bolinhas de cachorro e bolas de tênis entram por ralos abertos.</li>
      <li>Recolha brinquedos e objetos do quintal antes das chuvas.</li>
      <li>Pode as raízes visíveis do canteiro no lado da tubulação, sem cavar perto do cano.</li>
    </ul>
    <p>Dicas que circulam em fóruns e redes sociais, mas que não recomendo:</p>
    <ul class="nao">
      <li><strong>Soda cáustica ou ácido:</strong> não dissolvem raiz grossa e podem danificar o PVC e a vedação das juntas.</li>
      <li><strong>"Matador de raiz" em pó:</strong> é feito para esgoto e não deve ir para rede que despeja em solo, jardim ou galeria pública.</li>
      <li><strong>Arame ou vergalhão empurrado na marra:</strong> pode furar o cano ou empurrar a raiz e os objetos ainda mais para dentro.</li>
      <li><strong>Despejar água em alta pressão sem saber onde está a obstrução:</strong> alivia por dias e não tira a raiz.</li>
    </ul>
    <p>Em fóruns americanos de manutenção e na central de dúvidas da Roto-Rooter, os técnicos repetem o mesmo ponto: a raiz que já está no cano precisa ser cortada, e o produto, quando usado, só ajuda a atrasar o crescimento. O tipo de cano define a ferramenta. Cano fino ou corrugado pode ser rompido por máquina inadequada.</p>

    <h2>Precisa quebrar o piso e trocar os canos?</h2>
    <p>Na maioria dos casos, não. No caso deste artigo, o primeiro orçamento era quebrar tudo. A desobstrução resolveu sem quebra.</p>
    <p>A quebra só se justifica quando:</p>
    <ul>
      <li>O cano está rompido, amassado ou deslocado</li>
      <li>A raiz entra sempre pelo mesmo ponto, e ele não tem como ser vedado</li>
      <li>A rede não tem caixas de inspeção e não há acesso por nenhum ponto</li>
    </ul>
    <p>Quem decide isso deve ser quem viu a rede por dentro. Trocar canos antes de desobstruir é pagar por uma obra que, muitas vezes, não era necessária. Veja também <a href="../precisa-quebrar-piso-para-desentupir/">quando é preciso quebrar o piso para desentupir</a>.</p>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>O quintal já alagou mais de uma vez</li>
      <li>A limpeza caseira não resolveu ou o entupimento volta</li>
      <li>Há raízes visíveis na caixa de passagem</li>
      <li>Alguém recomendou quebrar o piso e você quer uma segunda avaliação</li>
      <li>O período de chuvas está chegando. Em Goiânia, ele vai de outubro a abril, e revisar a rede antes é mais barato que limpar depois do alagamento.</li>
    </ul>
    <p>Para avaliar a gravidade do problema, veja <a href="../niveis-de-entupimento/">os 4 níveis de entupimento</a>.</p>''',
    faq=[
        ("Raiz de canteiro pequeno consegue entupir a rede pluvial?", "Sim. No caso deste artigo, as raízes vinham de um canteiro, não de uma árvore grande, e chegaram a cerca de 2 metros dentro do cano."),
        ("Depois de tirar a raiz, ela volta?", "Pode voltar, porque a planta continua viva e a abertura no cano continua lá. Afastar o canteiro, vedar o ponto de entrada e revisar a rede antes das chuvas reduzem muito o risco."),
        ("De quanto em quanto tempo revisar a rede pluvial?", "Pelo menos uma vez por ano, antes do período chuvoso. Imóveis com canteiros ou árvores perto da tubulação merecem atenção maior."),
        ("Como saber por onde passa a rede pluvial do meu terreno?", "Siga o caminho entre os ralos externos, as caixas de passagem e a saída para a rua. Se o imóvel tiver projeto hidráulico, ele mostra o trajeto."),
        ("Posso lavar ferramentas de obra no ralo do quintal?", "Não. Cimento e argamassa endurecem dentro do cano e não saem com água. Lave em um balde, deixe assentar e descarte o resíduo com o entulho."),
    ],
    fontes=["target10844", "trf6", "rotorooter", "uai_distancia", "uai_ficus", "em_arvores", "ueg_chuvas", "maisgoias", "campo"],
    leia=["rede-pluvial-entupida", "niveis-de-entupimento", "precisa-quebrar-piso-para-desentupir"],
)

# ---------------------------------------------------------------------------
# Cimento no encanamento (10/11/2026; vídeo sIpndvlOzd8 e relato no LinkedIn)
# ---------------------------------------------------------------------------
CIMENTO = dict(
    slug="cimento-no-encanamento",
    title="Cimento no encanamento em Goiânia: por que vira pedra e o que fazer",
    h1="Cimento no encanamento em Goiânia: por que vira pedra dentro do cano e o que fazer se cair no ralo",
    desc="Lavar ferramenta de obra no ralo deixa cimento endurecido no cano. Veja por que a água não resolve, onde lavar e o que fazer se cair cimento na rede.",
    migalha="Cimento no encanamento",
    keywords="cimento no encanamento, cimento entupiu o cano, lavar ferramenta de obra no ralo, cimento no ralo o que fazer, como tirar cimento do cano, argamassa na tubulação",
    sobre=["Cimento Portland", "Entupimento de tubulação", "Hidrojateamento", "Obra e reforma"],
    imagem="https://i.ytimg.com/vi/sIpndvlOzd8/hqdefault.jpg",
    linkedin=LI + "cimento-na-tubula%C3%A7%C3%A3o-caso-real-goiania-go-lucas-nonato-vieira-u8uuf/",
    videos=["sIpndvlOzd8"],
    resumo="Lavar colher de pedreiro, balde, desempenadeira ou betoneira na pia, no tanque ou no ralo do quintal leva cimento para dentro da tubulação. O cimento endurece por reação química com a água, inclusive debaixo d'água, então jogar mais água não dissolve nada. Quando o fluxo para, os grãos assentam nas curvas, emendas e caixas e viram uma crosta de pedra presa à parede do cano, que segura terra, gordura e resíduos até travar a passagem. Lave as ferramentas em um balde, longe dos ralos. Se cair cimento no cano por acidente, o hidrojato deve entrar no mesmo dia, enquanto o material ainda está mole.",
    corpo='''    <h2>Resumo: cimento no cano em 3 situações</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Situação</th><th>O que acontece no cano</th><th>O que fazer</th></tr></thead>
        <tbody>
          <tr><td>Ferramenta lavada na pia, no tanque ou no ralo</td><td>Os grãos assentam nas curvas e endurecem ali</td><td>Lavar em balde, fora da rede</td></tr>
          <tr><td>Cimento caiu no ralo e ainda está mole</td><td>Ainda sai sem quebrar nada</td><td>Hidrojato no mesmo dia</td></tr>
          <tr><td>Cimento já endureceu no cano</td><td>Vira uma crosta de pedra grudada no tubo</td><td>Avaliar com hidrojato ou trocar o trecho</td></tr>
        </tbody>
      </table>
    </div>

    <h2>Por que o cimento entope o cano, se a água deveria levar tudo embora?</h2>
    <p>Essa é a dúvida que mais escuto em obra. A lógica parece boa: abre a torneira, a água corre, o cimento vai embora. O problema é que o cimento não depende do ar para endurecer. Ele é um aglomerante hidráulico: endurece por uma reação química com a própria água, a hidratação, e continua firme mesmo submerso. Por isso dá para concretar pilar de ponte dentro de rio.</p>
    <p>Dentro do encanamento, o que acontece é isto:</p>
    <ul>
      <li>Enquanto a torneira está aberta, a água arrasta os grãos de cimento e areia.</li>
      <li>Quando o fluxo para, a água perde velocidade e os grãos assentam onde ela fica mais lenta: joelhos, emendas, caixas sifonadas e trechos com pouca queda.</li>
      <li>Ali eles endurecem e formam uma lombada áspera, grudada na parede do cano.</li>
      <li>Essa lombada passa a segurar terra, cabelo, papel e gordura. Cada nova lavagem deixa outra camada.</li>
    </ul>
    <p>O entupimento por cimento quase nunca aparece no dia. Ele cresce por camadas, e por isso costuma ser confundido com um entupimento comum até alguém olhar o cano por dentro.</p>
    <p>Não é um problema só do Brasil. A Thames Water, que cuida do esgoto de Londres, gasta cerca de 1,6 milhão de libras por ano retirando concreto endurecido das redes, quase sempre jogado por obras. A técnica usada lá é a mesma que usamos aqui: jato de água de alta pressão para quebrar a crosta em pedaços e retirá-los sem danificar o tubo.</p>

    <h2>Caso real: a diferença entre o trecho que recebeu hidrojato e o que ainda não recebeu</h2>
    <div class="caso">
      <p>Em um atendimento de rede pluvial em Goiânia, encontramos cimento endurecido dentro da tubulação, junto com terra e raízes. Era resíduo de obra: durante anos, baldes e ferramentas foram lavados no ralo do quintal.</p>
      <p>Com um trecho da tubulação exposto, deu para comparar os dois lados da mesma rede:</p>
      <ul>
        <li><strong>Lado onde o hidrojato já passou:</strong> parede lisa, diâmetro livre, a água correndo sem barreira.</li>
        <li><strong>Lado onde o hidrojato ainda não tinha passado:</strong> parede coberta por uma crosta de cimento e terra, tão dura que nem raspando com uma chave ela soltava com facilidade. É essa crosta que reduz o espaço da água e segura tudo o que vem depois.</li>
      </ul>
      <p>Depois da passagem do hidrojato no trecho sujo, a crosta saiu em pedaços e a rede voltou a escoar. O mesmo serviço está descrito no artigo sobre <a href="../raizes-na-rede-pluvial/">raízes na rede pluvial</a>, porque cimento e raiz estavam juntos no mesmo cano.</p>
    </div>

    ''' + video("sIpndvlOzd8", "cimento dentro da tubulação, trecho limpo e trecho sujo", "Trecho exposto de rede pluvial com crosta de cimento e terra na parede do cano",
                "Vídeo (caso real, 47 s): o mesmo cano com um lado já limpo pelo hidrojato e o outro ainda com crosta de cimento.") + '''

    <h2>Onde e como lavar as ferramentas de obra?</h2>
    <p>A regra é simples: a água com cimento não pode ir para nenhum ralo, nem de esgoto nem de água da chuva. O jeito de lavar que recomendamos:</p>
    <ul>
      <li><strong>Raspe antes de molhar.</strong> Tire o grosso da massa com a própria colher ou uma espátula. Quanto menos sobra, menos resíduo vai para a água.</li>
      <li><strong>Use dois baldes.</strong> Um para tirar a massa mais pesada, outro para o enxágue final.</li>
      <li><strong>Deixe a água descansar.</strong> Em algumas horas o cimento assenta no fundo. A água clara de cima pode ir para uma área de terra ou brita da própria obra, longe de ralos e bocas de lobo.</li>
      <li><strong>Descarte a borra como entulho.</strong> Espere endurecer no fundo do balde e jogue junto com o restante do entulho.</li>
      <li><strong>Em obra maior, monte uma área de lavagem.</strong> Uma caixa de madeira forrada com lona já resolve. É o mesmo princípio que a agência ambiental dos EUA (EPA) recomenda para canteiros de obra, com a área afastada de ralos e da drenagem.</li>
    </ul>
    <p>Dicas que pedreiros e encanadores trocam em fóruns como o Reddit, e que funcionam:</p>
    <ul>
      <li>Deixe um balde com água ao lado durante o serviço e mergulhe a ferramenta logo depois de usar, antes da massa secar nela.</li>
      <li>Passe um pouco de óleo na colher e na desempenadeira antes de começar. A massa gruda menos e sai fácil.</li>
      <li>Esfregue com escova de aço ou esponja dura dentro do balde, nunca debaixo da torneira.</li>
      <li>Betoneira se lava no fim do dia com água e brita girando dentro dela, e essa água vai para o balde ou para a área de lavagem.</li>
    </ul>

    <h2>Como proteger o encanamento durante a obra ou reforma?</h2>
    <ul>
      <li>Tampe ralos, caixas sifonadas e pontos de esgoto abertos com tampão, plástico e fita antes de começar.</li>
      <li>Combine com o pedreiro, antes do primeiro dia, onde as ferramentas serão lavadas.</li>
      <li>Não deixe preparar massa em cima de grelha de ralo ou ao lado de caixa de passagem.</li>
      <li>Cuide da área externa também: massa que escorre para a calha ou para a boca de lobo endurece do mesmo jeito.</li>
      <li>Depois da obra, observe as primeiras semanas. Ralo lento ou gorgolejando é sinal de alerta, não espere piorar.</li>
    </ul>

    <h2>Caiu cimento no ralo por acidente: o que fazer?</h2>
    <p>Aqui o relógio manda. Cimento ainda fluido ou recém-assentado sai com o jato de água. Depois de endurecido, vira pedra grudada no tubo, e a remoção fica mais demorada, mais cara e às vezes exige trocar o trecho.</p>
    <ol>
      <li><strong>Pare de usar aquele ponto.</strong> Nada de despejar mais massa ou água suja de obra ali.</li>
      <li><strong>Retire o que estiver ao alcance</strong>, de luva: o que ficou na grelha, no ralo ou na caixa sifonada.</li>
      <li><strong>Chame o hidrojateamento no mesmo dia.</strong> O jato de alta pressão empurra e quebra o material enquanto ele ainda está mole. Veja <a href="../como-funciona-hidrojateamento/">como funciona o hidrojateamento</a>.</li>
      <li><strong>Se foi pouca quantidade e ainda está líquida</strong>, deixe água corrente enquanto o técnico não chega, para os grãos não assentarem. Com volume grande isso não funciona: você só empurra o problema para mais longe.</li>
      <li><strong>Depois da limpeza, confirme o resultado</strong> com teste de escoamento ou inspeção com câmera, para ter certeza de que não sobrou crosta.</li>
    </ol>

    <h2>Mitos e verdades sobre cimento no cano</h2>
    <ul class="nao">
      <li><strong>"Jogando bastante água, o cimento vai embora."</strong> Mito. A água leva uma parte, e o resto assenta no primeiro ponto onde ela fica mais lenta.</li>
      <li><strong>"Cimento só endurece quando seca."</strong> Mito. Ele endurece por reação com a água, por isso endurece dentro do cano cheio.</li>
      <li><strong>"Soda cáustica dissolve cimento."</strong> Mito. A soda age em gordura e matéria orgânica, não em cimento endurecido.</li>
      <li><strong>"Ácido muriático resolve."</strong> Mito perigoso. Solta gases tóxicos em ambiente fechado, pode atacar tubos metálicos e vedações e não alcança uma crosta que está metros para dentro.</li>
      <li><strong>"Um pouquinho de massa não faz mal."</strong> Mito. O entupimento por cimento é cumulativo: cada lavagem deixa uma camada nova.</li>
    </ul>
    <ul>
      <li><strong>"Quanto antes chamar, mais simples a solução."</strong> Verdade. Cimento mole sai com hidrojato; cimento duro pode exigir a troca do trecho.</li>
      <li><strong>"Cimento na rede pluvial também entope."</strong> Verdade. E o problema aparece justamente na primeira chuva forte, quando a água não tem por onde passar. Veja os sinais em <a href="../rede-pluvial-entupida/">rede pluvial entupida</a>.</li>
    </ul>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>Cimento ou argamassa caiu no ralo, mesmo que pareça pouco: quanto mais cedo, mais fácil.</li>
      <li>Depois de uma obra ou reforma, o ralo ficou lento ou o entupimento volta.</li>
      <li>Você já sabe que ferramentas foram lavadas na pia, no tanque ou no ralo do quintal.</li>
      <li>Alguém recomendou quebrar o piso e você quer uma avaliação antes. Na maioria dos casos isso não é necessário: veja <a href="../precisa-quebrar-piso-para-desentupir/">quando é preciso quebrar o piso</a>.</li>
    </ul>
    <p>Para entender a gravidade do que está acontecendo na sua casa, veja <a href="../niveis-de-entupimento/">os 4 níveis de entupimento</a>.</p>''',
    faq=[
        ("Cimento entope cano de PVC?", "Sim. Ele não reage com o PVC, mas gruda nas paredes e conexões e diminui o espaço da água até travar o fluxo."),
        ("Dá para tirar cimento endurecido do cano?", "Em muitos casos sim, com hidrojateamento de alta pressão e bicos próprios. Quando a crosta é grande e o trecho é curto e acessível, às vezes é mais seguro trocar o pedaço do cano."),
        ("Quanto tempo o cimento leva para endurecer dentro do cano?", "A pega começa em poucas horas, conforme o tipo de cimento e a temperatura. Por isso a orientação é agir no mesmo dia."),
        ("Posso lavar a ferramenta no tanque se passar bastante água depois?", "Não. A água extra não dissolve o cimento, só leva o problema para um ponto mais distante e mais difícil de alcançar."),
        ("Onde jogo a água de lavar ferramenta de obra?", "Deixe descansar no balde até o cimento assentar. A água clara vai para uma área de terra ou brita da obra, longe de ralos, e a borra do fundo vai com o entulho."),
    ],
    fontes=["dlubal", "thames", "epa_washout", "mpca", "nbr8160", "nbr10844", "campo"],
    leia=["raizes-na-rede-pluvial", "como-funciona-hidrojateamento", "rede-pluvial-entupida"],
)

# ---------------------------------------------------------------------------
# Caixa cega (caso real: jantinha no interior de Goiás; a cidade NÃO vai no texto, decisão do Antonio)
# ---------------------------------------------------------------------------
CAIXA_CEGA = dict(
    slug="caixa-cega-esgoto",
    title="Caixa cega no esgoto em Goiânia: por que encarece o serviço",
    h1="Caixa cega no esgoto em Goiânia: o que é e por que encarece o desentupimento",
    desc="Caixa cega é a caixa de esgoto lacrada debaixo do piso. Veja por que ela encarece o desentupimento, causa mau cheiro e como evitar.",
    migalha="Caixa cega no esgoto",
    keywords="caixa cega, caixa cega esgoto, caixa de passagem lacrada, caixa de inspeção debaixo do piso, caixa de esgoto escondida, como achar caixa de esgoto",
    sobre=["Caixa de inspeção", "Caixa de passagem", "Desentupimento", "Esgoto sanitário"],
    imagem="https://bvdesentupidora.com.br/blog/img/tampa-caixa-cega-capa.webp",
    videos=["fvLFIs4SRYg", "L69sYPQ8uSc"],
    resumo="Caixa cega é uma caixa de passagem ou de inspeção do esgoto que ficou sem acesso: alguém fechou a tampa com contrapiso e piso, normalmente numa reforma. Ela continua recebendo o esgoto, mas ninguém sabe onde está e ninguém consegue limpá-la. Quando entope, o desentupimento vira três serviços: achar a caixa, quebrar o piso para abrir e só então desobstruir. Por isso fica mais demorado e mais caro. E, como passa anos sem limpeza, a caixa enche de resíduos e pode transbordar sem ninguém ver, com o esgoto infiltrando por dentro do piso e causando mau cheiro. A solução é simples: toda caixa precisa de uma tampa que abra.",
    corpo='''    <p>No nosso dia a dia, "caixa cega" é o nome que damos para a caixa de esgoto que existe, funciona, mas desapareceu do piso. Não é um defeito raro: em reforma de quintal, garagem ou salão comercial, é comum o pedreiro passar o contrapiso por cima da tampa para o piso ficar "bonito". O problema só aparece anos depois, quando o esgoto entope justamente ali.</p>

    <h2>Resumo: caixa com tampa x caixa cega</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th></th><th>Caixa com tampa</th><th>Caixa cega</th></tr></thead>
        <tbody>
          <tr><td>Achar a caixa</td><td>Está à vista</td><td>Precisa localizar debaixo do piso</td></tr>
          <tr><td>Abrir</td><td>Basta tirar a tampa</td><td>Precisa quebrar piso e contrapiso</td></tr>
          <tr><td>Limpeza preventiva</td><td>Possível a qualquer hora</td><td>Na prática, nunca acontece</td></tr>
          <tr><td>Tempo do desentupimento</td><td>Menor</td><td>Maior: achar, quebrar, desentupir e fechar</td></tr>
          <tr><td>Custo</td><td>Só o desentupimento</td><td>Desentupimento + localização + quebra + recomposição do piso</td></tr>
        </tbody>
      </table>
    </div>

    <h2>O que é uma caixa cega e por que ela existe?</h2>
    <p>A rede de esgoto de uma casa ou de um comércio tem caixas no caminho: caixa de inspeção, caixa de passagem, caixa de gordura. Elas ficam nas mudanças de direção e nas emendas da tubulação e existem para uma coisa: dar acesso ao cano. O próprio fabricante descreve a caixa de inspeção como o ponto que permite inspeção, limpeza e desobstrução da rede.</p>
    <p>A caixa vira "cega" quando perde a tampa visível. Os motivos mais comuns que encontramos:</p>
    <ul>
      <li><strong>Reforma:</strong> o piso novo foi assentado por cima da tampa antiga.</li>
      <li><strong>Estética:</strong> o dono não queria uma tampa no meio do quintal ou do salão.</li>
      <li><strong>Obra sem projeto:</strong> a caixa foi feita, fechada com laje ou cimento e ninguém marcou onde ficou.</li>
      <li><strong>Troca de dono:</strong> quem construiu sabia onde estava a caixa; quem comprou o imóvel não sabe.</li>
    </ul>

    <h2>Por que a caixa cega deixa o desentupimento mais caro?</h2>
    <p>Com a caixa aberta, desentupir é colocar a máquina ou o hidrojato direto no ponto certo. Com a caixa cega, antes disso vêm etapas que levam tempo e mão de obra:</p>
    <ol>
      <li><strong>Perceber que existe uma caixa no caminho.</strong> Normalmente o sinal é a mola da máquina, o cabo de aço em espiral, que para sempre no mesmo ponto e começa a enrolar dentro do cano.</li>
      <li><strong>Localizar a caixa debaixo do piso.</strong> Muitas vezes com sonda localizadora, um pequeno transmissor que entra no cano e é seguido por um aparelho na superfície.</li>
      <li><strong>Quebrar o piso e o contrapiso</strong> exatamente em cima da caixa.</li>
      <li><strong>Desentupir e limpar a caixa</strong>, que geralmente está cheia.</li>
      <li><strong>Fechar de novo</strong>, de preferência com tampa de acesso, e recompor o piso em volta.</li>
    </ol>
    <p>Cada etapa a mais é tempo de equipe, equipamento e material. É por isso que o mesmo entupimento custa mais quando a caixa está escondida. Quando não se consegue achar a caixa, o risco é pior: quebrar em vários pontos "procurando" ou, como quase aconteceu no caso abaixo, alguém sugerir refazer a rede inteira.</p>

    <h2>Caixa cega causa mau cheiro e infiltração?</h2>
    <p>Pode causar, e o motivo é a falta de limpeza. Uma caixa que ninguém abre há anos vai acumulando tudo o que desce pelo esgoto: gordura, lodo, areia e, em comércio, até objetos. Na nossa experiência, os sinais que aparecem são:</p>
    <ul>
      <li><strong>Mau cheiro</strong> em um ponto do piso onde "não tem nada", principalmente em dia quente ou depois de chuva. A caixa cheia e mal vedada solta gás pelas juntas do piso.</li>
      <li><strong>Transbordamento que ninguém vê.</strong> Numa caixa com tampa, quando ela enche, o esgoto aparece na tampa e alguém percebe. Na caixa cega, a tampa está debaixo do piso: o esgoto que transborda não tem por onde aparecer e infiltra por dentro do piso, espalhando-se pelo contrapiso e pela base embaixo dele. Pode passar meses assim, sem ninguém ver, até surgir como mancha de umidade, cheiro forte ou piso cedendo.</li>
      <li><strong>Entupimento que sempre volta</strong> no mesmo trecho, mesmo depois de desentupido pelos ralos.</li>
      <li><strong>Esgoto lento em vários pontos ao mesmo tempo</strong>, porque a caixa fica antes de vários ramais.</li>
    </ul>

    <h2>Caso real: a caixa cega da jantinha, achada pelo som</h2>
    <div class="caso">
      <p>Fomos chamados para desentupir o esgoto de uma jantinha no interior de Goiás. Ao passar a máquina, percebi que a mola estava enrolando dentro da tubulação: ela batia sempre no mesmo lugar e não avançava. Esse comportamento indica que a mola está parando dentro de uma caixa de passagem, e não havia nenhuma tampa à vista. Era uma caixa cega, coberta por piso e contrapiso.</p>
      <p>O caminho normal seria passar a sonda localizadora para descobrir onde estava a caixa. Fizemos de outro jeito, com a experiência de muitos anos de desentupimento:</p>
      <ul>
        <li>Medimos quanto da mola entrava até parar na caixa.</li>
        <li>Seguimos a direção da tubulação a partir do ponto de entrada.</li>
        <li>Na área indicada pela medida, fui batendo no piso com um martelinho de borracha. Em cima da caixa, o som muda: fica oco, com eco, porque embaixo há um vazio e não terra compactada.</li>
      </ul>
      <p>Quebramos só naquele ponto. Dentro da caixa havia tampas de garrafa, latas de cerveja, palitos de espetinho, plásticos e muito mais: resíduos que estavam ali havia quase 7 anos, sem nenhuma limpeza. Deu para encher dois baldes e uma bacia. Limpamos a caixa, desentupimos a rede e fechamos deixando uma tampa de acesso, para que o próximo cuidado seja só abrir e limpar.</p>
      <p>O dono já estava pensando em quebrar e refazer toda a tubulação, o que obrigaria a fechar o estabelecimento por 4 a 6 dias. O serviço completo levou 4 horas, e a jantinha não precisou fechar.</p>
    </div>

    <figure class="foto-vertical">
      <img src="../img/residuos-retirados-caixa-cega.webp" alt="Dois baldes e uma bacia cheios de resíduos de esgoto retirados da caixa cega, ao lado da abertura feita no piso" width="634" height="1122" loading="lazy">
      <figcaption>Dois baldes e uma bacia de resíduos retirados da caixa cega, acumulados por quase 7 anos. À esquerda, a abertura feita no piso.</figcaption>
    </figure>

    ''' + video("fvLFIs4SRYg", "caixa cega aberta e limpa", "Caixa cega de esgoto aberta no piso, com água escura e resíduos sendo retirados para um balde",
                "Vídeo 1 (caso real, 16 s): a caixa cega já aberta, com o esgoto parado e os resíduos sendo retirados.") + '''

    ''' + video("L69sYPQ8uSc", "caixa cega fechada com tampa de acesso", "Tampa redonda de concreto encaixada no piso no lugar onde estava a caixa cega",
                "Vídeo 2 (caso real, 12 s): a mesma caixa depois do serviço, agora com tampa de acesso.") + '''

    <h2>Como se acha uma caixa escondida debaixo do piso?</h2>
    <ul>
      <li><strong>Pela mola da máquina:</strong> a distância que a mola entra até parar indica a que distância do ponto de entrada está a caixa.</li>
      <li><strong>Pela sonda localizadora:</strong> o transmissor vai dentro do cano e o aparelho na superfície mostra o trajeto e o ponto onde ele para. Profundidade grande e ferragem no concreto podem atrapalhar a leitura.</li>
      <li><strong>Pela câmera de inspeção:</strong> mostra o cano por dentro, a caixa e o que está entupindo, mas precisa de um ponto de entrada.</li>
      <li><strong>Pelo som:</strong> o método do martelo de borracha do caso acima. Funciona bem nas mãos de quem já fez isso muitas vezes, porque é preciso distinguir o som de uma caixa do som de um piso mal assentado.</li>
      <li><strong>Pela lógica da rede:</strong> caixas costumam ficar onde a tubulação muda de direção e perto da saída para a rua.</li>
    </ul>

    <h2>O que a norma diz sobre as caixas de inspeção?</h2>
    <p>A norma brasileira de esgoto predial (ABNT NBR 8160) trata as caixas de inspeção como parte obrigatória da rede, justamente para permitir manutenção. Entre os pontos principais:</p>
    <ul>
      <li>No máximo <strong>25 m</strong> entre dois dispositivos de inspeção, medidos pelo caminho do cano.</li>
      <li>No máximo <strong>15 m</strong> entre a ligação com a rede pública e o dispositivo de inspeção mais próximo.</li>
      <li>No máximo <strong>10 m</strong> entre o vaso, a caixa de gordura ou a caixa sifonada e um dispositivo de inspeção.</li>
      <li>Tampa de <strong>fácil remoção e com vedação</strong>: ela segura o cheiro, mas precisa abrir.</li>
    </ul>
    <p>Uma caixa cimentada por baixo do piso continua existindo, mas deixa de cumprir a função para a qual a norma pede que ela exista.</p>

    <h2>Como evitar ter uma caixa cega em casa ou no comércio?</h2>
    <ul>
      <li><strong>Antes de qualquer reforma,</strong> marque onde ficam as caixas de inspeção, de passagem e de gordura. Tire foto com uma trena aparecendo e guarde.</li>
      <li><strong>Se o piso vai passar por cima,</strong> use tampa com porta-tampa que recebe o mesmo revestimento. A tampa some no visual, mas continua abrindo. Os próprios fabricantes vendem caixas com tampa preparada para receber piso cerâmico ou cimentado.</li>
      <li><strong>Combine com o pedreiro</strong> que nenhuma tampa será fechada com cimento.</li>
      <li><strong>Ao comprar ou alugar um imóvel,</strong> pergunte onde ficam as caixas. Se ninguém souber e não houver nenhuma tampa à vista, é provável que exista caixa cega.</li>
      <li><strong>Limpe as caixas periodicamente</strong>, principalmente em restaurante, bar e lanchonete. Veja <a href="../limpeza-caixa-de-gordura/">de quanto em quanto tempo limpar a caixa de gordura</a>.</li>
    </ul>

    <h2>O que não fazer</h2>
    <ul class="nao">
      <li>Quebrar o piso por conta própria "procurando a caixa". Sem saber a direção e a distância, o mais comum é quebrar no lugar errado.</li>
      <li>Fechar de novo a caixa com cimento depois do desentupimento. O problema volta, e da próxima vez vai ser preciso quebrar outra vez.</li>
      <li>Jogar soda cáustica ou outros produtos para "dissolver" o entupimento. Eles não dissolvem plástico, lata nem tampa de garrafa, e ficam parados na caixa.</li>
      <li>Aceitar a ideia de refazer toda a rede antes de alguém localizar e abrir a caixa. Na maioria das vezes, o problema está nela.</li>
    </ul>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>O esgoto entope sempre no mesmo trecho e não há nenhuma tampa de caixa à vista.</li>
      <li>Há mau cheiro ou umidade em um ponto fixo do piso.</li>
      <li>Você vai reformar e quer descobrir onde estão as caixas antes de fechar o piso.</li>
      <li>Alguém recomendou quebrar o piso inteiro ou refazer a rede e você quer uma segunda avaliação. Veja <a href="../precisa-quebrar-piso-para-desentupir/">quando é preciso quebrar o piso</a>.</li>
    </ul>
    <p>Para entender a gravidade do que está acontecendo, veja <a href="../niveis-de-entupimento/">os 4 níveis de entupimento</a>.</p>''',
    faq=[
        ("O que é caixa cega no esgoto?", "É uma caixa de passagem ou de inspeção da rede de esgoto que ficou sem acesso, normalmente porque foi coberta com contrapiso e piso. Ela continua recebendo o esgoto, mas não dá para abrir nem limpar."),
        ("Como saber se a minha casa tem caixa cega?", "Os sinais são: nenhuma tampa de caixa à vista no quintal, na garagem ou no salão; entupimento que volta sempre no mesmo trecho; e mau cheiro ou umidade em um ponto fixo do piso."),
        ("Por que o desentupimento fica mais caro com caixa cega?", "Porque antes de desentupir é preciso localizar a caixa debaixo do piso, quebrar o piso e o contrapiso para abrir e, no final, fechar e recompor. São etapas a mais de tempo, equipe e material."),
        ("Pode colocar piso em cima da caixa de inspeção?", "Pode, desde que a caixa tenha tampa com porta-tampa que recebe o revestimento. O piso disfarça a tampa, mas ela continua abrindo. O que não pode é fechar a caixa com cimento."),
        ("Precisa refazer toda a rede quando há caixa cega?", "Normalmente não. Na maioria dos casos basta localizar a caixa, abrir só naquele ponto, limpar, desentupir e deixar uma tampa de acesso."),
    ],
    fontes=["nbr8160", "projetista8160", "tigre_cx", "campo"],
    leia=["precisa-quebrar-piso-para-desentupir", "limpeza-caixa-de-gordura", "como-funciona-hidrojateamento"],
)

COMMONS = "https://commons.wikimedia.org/wiki/File:"
CCBYSA = '<a href="https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br" rel="nofollow noopener" target="_blank">CC BY-SA 4.0</a>'

# Sem atendimento em hospital para mostrar: as fotos de hospitais de Goiânia são ilustrativas (Wikimedia Commons,
# CC BY-SA 4.0, com crédito) e a legenda diz que eles não têm relação com os casos citados (pedido do Antonio, 19/11/2026).
HOSPITAL = dict(
    slug="desentupimento-hospitais-e-clinicas",
    title="Desentupimento em hospitais e clínicas de Goiânia: cuidados",
    h1="Desentupimento especializado em hospitais e clínicas de Goiânia: riscos e como fazer a manutenção certa",
    desc="Por que ralo entupido ou com cheiro é risco em hospitais e clínicas, quais áreas exigem cuidado e como fazer a manutenção sem expor pacientes.",
    migalha="Desentupimento em hospitais e clínicas",
    keywords="desentupimento em hospitais, desentupimento em clínicas, entupimento em hospital, mau cheiro em ralo de hospital, sifão de pia hospitalar, manutenção preventiva hidrossanitária hospitalar, controle de infecção e esgoto",
    sobre=["Controle de infecção hospitalar", "Manutenção predial", "Esgoto sanitário", "Desentupimento"],
    imagem="https://bvdesentupidora.com.br/blog/img/hospital-das-clinicas-ufg-goiania.webp",
    videos=["D4aA6c9-8lc"],
    resumo="Em hospitais e clínicas, ralo entupido ou com cheiro de esgoto não é só desconforto: pias, ralos e sifões já foram a origem de surtos de bactérias resistentes a antibióticos em UTIs, com mortes. O mau cheiro indica que a barreira entre o esgoto e o ambiente falhou (sifão seco, vedação rompida ou resíduo parado). Os mais vulneráveis são pacientes de UTI, prematuros, imunossuprimidos, transplantados, queimados e em hemodiálise. A manutenção precisa ser preventiva e programada, com intervalo menor nas áreas críticas, e todo serviço deve ter autorização da CCIH, isolamento da área, EPI e registro. Trocar peças ou jogar produto químico, sozinhos, não resolvem.",
    corpo='''    <p>Quando foi a última vez que alguém olhou o sifão da pia da UTI, da sala de procedimentos ou do expurgo? Se ninguém sabe responder, este texto é para você. Ele mostra por que o ponto mais contaminado de um quarto de hospital pode estar debaixo da pia, e como o desentupimento e a manutenção devem ser feitos num lugar onde há pacientes graves.</p>

    <figure>
      <img src="../img/hospital-das-clinicas-ufg-goiania.webp" alt="Fachada do Hospital das Clínicas da UFG, em Goiânia, prédio alto de cor bege com árvores e carros estacionados na rua" width="960" height="720" fetchpriority="high">
      <figcaption>Hospital das Clínicas da UFG, em Goiânia. Foto ilustrativa: o hospital não tem relação com os casos e estudos citados neste artigo. Foto: Fronteira / <a href="''' + COMMONS + '''Hospital_das_Cl%C3%ADnicas_da_UFG,_Goi%C3%A2nia,_dezembro_de_2022_(3).jpg" rel="nofollow noopener" target="_blank">Wikimedia Commons</a>, licença ''' + CCBYSA + ''' (imagem reduzida).</figcaption>
    </figure>

    <h2>Resumo: áreas, riscos e manutenção</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Área</th><th>Principal risco</th><th>Ponto de partida para a manutenção*</th></tr></thead>
        <tbody>
          <tr><td>UTI, centro cirúrgico, hemodiálise, CME</td><td>Bactérias resistentes nos sifões; gotículas perto do paciente</td><td>Inspeção mensal; limpeza técnica trimestral</td></tr>
          <tr><td>Cozinha, lactário, banco de leite</td><td>Gordura na rede; contaminação de alimentos</td><td>Caixa de gordura mensal (quinzenal com alto volume)</td></tr>
          <tr><td>Internação, ambulatório e consultórios</td><td>Sifão seco, refluxo, mau cheiro</td><td>Inspeção trimestral; limpeza semestral</td></tr>
          <tr><td>Rede geral de esgoto e caixas de inspeção</td><td>Entupimento e transbordamento</td><td>Semestral, com vídeo-inspeção anual</td></tr>
        </tbody>
      </table>
    </div>
    <p>*Não é norma: é um ponto de partida. A rotina de cada hospital ou clínica é definida pela CCIH (Comissão de Controle de Infecção Hospitalar) junto com a engenharia de manutenção.</p>

    <h2>Por que um ralo entupido ou com cheiro é um risco sério num hospital?</h2>
    <p>Em 10 anos trabalhando com desentupimento e hidrojateamento, aprendi que cheiro de esgoto quase nunca é "só cheiro". Na maioria das vezes ele aparece porque a água que fica parada no sifão secou, a vedação do vaso se rompeu ou há resíduo acumulado na tubulação. Essa água parada no sifão é o que separa o ambiente do esgoto. Quando ela falha, o ar da rede entra no ambiente.</p>
    <p>Em uma casa, isso incomoda. Em um hospital ou numa clínica, o problema é outro: as pessoas ali estão com a imunidade baixa, com cortes cirúrgicos, cateteres e sondas. Um entupimento que causa refluxo ou transbordamento pode contaminar o piso e interditar um leito ou até uma sala cirúrgica.</p>
    <p>Os gases do esgoto, como o sulfeto de hidrogênio (o cheiro de ovo podre), também irritam as vias respiratórias, o que pesa para quem já respira com dificuldade.</p>

    <h2>O que os estudos mostram sobre pias e sifões de hospital?</h2>
    <p>Esse alerta não é só nosso. A ciência vem documentando o problema há anos:</p>
    <ul>
      <li><strong>Revisão de 2017 (<em>Clinical Infectious Diseases</em>):</strong> reuniu 32 relatos, em 20 anos, de bactérias resistentes aos carbapenêmicos (antibióticos de último recurso) encontradas no sistema de água e esgoto de hospitais. A maioria estava ligada a surtos em UTI, com pacientes graves e imunossuprimidos. Ralos, pias e torneiras foram os pontos mais colonizados, e a <em>Pseudomonas aeruginosa</em> foi a bactéria mais encontrada.</li>
      <li><strong>Surto numa UTI em Israel (2016–2017):</strong> 32 casos e 3 mortes. A investigação encontrou a mesma bactéria em duas saídas de pia e em 16 sifões da UTI.</li>
      <li><strong>Carga de bactérias no ralo:</strong> um estudo de um hospital universitário da Bélgica lembra que o ralo debaixo da pia de hospital pode concentrar de 1 milhão a 10 bilhões de bactérias por mililitro. Na UTI estudada, 7 das 8 pias dos quartos de isolamento estavam contaminadas.</li>
      <li><strong>A troca de ralos nos EUA:</strong> o Hospital da Universidade da Virgínia trocou ralos e sifões de uma UTI e tratou as pias com produto químico para conter a transmissão de bactérias resistentes. O tratamento químico foi abandonado porque as pias voltavam a ser colonizadas, e depois da troca surgiu um surto de outra bactéria, a <em>Serratia marcescens</em>.</li>
    </ul>
    <p>A lição que tiro disso: não existe solução mágica. A própria revisão de 2017 conclui que o que mais funciona é a combinação de medidas, com reforço da rotina de controle de infecção. Manutenção bem feita e hábito da equipe andam juntos.</p>

    <h2>Quais pacientes não podem ficar expostos a mau cheiro ou esgoto?</h2>
    <ul>
      <li>Pacientes de UTI (adulto, pediátrica e neonatal)</li>
      <li>Recém-nascidos, principalmente prematuros</li>
      <li>Pacientes em quimioterapia ou com a imunidade muito baixa</li>
      <li>Transplantados (de medula e de órgãos)</li>
      <li>Grandes queimados</li>
      <li>Pacientes em pós-operatório, com feridas abertas, cateteres ou sondas</li>
      <li>Pacientes em hemodiálise</li>
      <li>Pacientes com DPOC, asma grave ou outras doenças respiratórias</li>
      <li>Gestantes e idosos frágeis</li>
    </ul>

    <h2>Quais microrganismos exigem atenção?</h2>
    <ul>
      <li><strong>Bactérias resistentes a antibióticos:</strong> <em>Klebsiella pneumoniae</em> (KPC), <em>Acinetobacter baumannii</em>, <em>Pseudomonas aeruginosa</em>, <em>Serratia marcescens</em> e <em>Enterobacter</em>. Podem causar pneumonia, infecção no sangue, infecção urinária e infecção no local da cirurgia.</li>
      <li><strong><em>Legionella</em>:</strong> vive em sistemas de água mal cuidados e é transmitida pela inalação de gotículas (chuveiros, torneiras, torres de resfriamento). Pode causar pneumonia grave.</li>
      <li><strong>Agentes de diarreia ligados ao esgoto:</strong> <em>E. coli</em>, norovírus e <em>Clostridioides difficile</em>, principalmente quando há refluxo.</li>
      <li><strong>Fungos como o <em>Aspergillus</em>:</strong> se espalham com a poeira de obras e quebras. Por isso a própria manutenção precisa de controle em áreas com pacientes imunossuprimidos.</li>
    </ul>

    <figure>
      <img src="../img/hospital-de-doencas-tropicais-goiania.webp" alt="Entrada do Hospital de Doenças Tropicais de Goiânia, prédio baixo com fachada verde, palmeiras e estacionamento" width="960" height="720" loading="lazy">
      <figcaption>Hospital de Doenças Tropicais (HDT), em Goiânia. Foto ilustrativa: o hospital não tem relação com os casos e estudos citados neste artigo. Foto: Fronteira / <a href="''' + COMMONS + '''Hospital_de_Doen%C3%A7as_Tropicais,_Jardim_Bela_Vista,_Goi%C3%A2nia,_julho_de_2024_(1).jpg" rel="nofollow noopener" target="_blank">Wikimedia Commons</a>, licença ''' + CCBYSA + ''' (imagem reduzida).</figcaption>
    </figure>

    <h2>Quais áreas do hospital pedem cuidado redobrado?</h2>
    <ul>
      <li>UTI adulto, pediátrica e neonatal</li>
      <li>Centro cirúrgico e sala de recuperação</li>
      <li>Oncologia, hematologia e unidades de transplante</li>
      <li>Hemodiálise</li>
      <li>Central de Material e Esterilização (CME)</li>
      <li>Cozinha, lactário e banco de leite</li>
      <li>Pronto-socorro</li>
      <li>Laboratório, expurgos e lavanderia</li>
      <li>Quartos de isolamento</li>
    </ul>
    <p><strong>E nas clínicas?</strong> As áreas críticas são menores, mas a lógica é a mesma: sala de procedimentos, clínica de hemodiálise, posto de coleta de laboratório, expurgo e copa. Uma clínica pequena costuma ter poucos pontos de esgoto, e por isso um único sifão seco ou um ralo entupido já afeta todo o atendimento.</p>

    <h2>Como deve ser a limpeza de ralos, pias e vasos sanitários?</h2>
    <ul>
      <li><strong>Pias de lavar as mãos:</strong> usar só para lavar as mãos. Restos de soro, medicação, comida ou café alimentam as bactérias que vivem no sifão.</li>
      <li><strong>Nada guardado do lado da pia:</strong> materiais, medicamentos e insumos ficam fora da área de respingo.</li>
      <li><strong>Torneiras:</strong> de preferência acionadas sem as mãos, com o jato que não caia direto dentro do ralo (isso espalha gotículas).</li>
      <li><strong>Ralos:</strong> sifonados e com tampa. Em áreas críticas, o ideal é ter o mínimo possível de ralos no piso.</li>
      <li><strong>Vasos sanitários:</strong> descarga com a tampa fechada e desinfecção diária com produto aprovado pela CCIH.</li>
      <li><strong>Sifões:</strong> desinfecção periódica conforme o protocolo da instituição, sabendo que o produto químico, sozinho, tem efeito temporário.</li>
      <li><strong>Registro:</strong> cada limpeza técnica e cada manutenção anotadas, com data, local e responsável.</li>
    </ul>

    <h2>Com que frequência fazer a manutenção preventiva?</h2>
    <p>Não existe um número único na lei. A RDC 63/2011 da Anvisa exige que o serviço de saúde mantenha suas instalações em condições adequadas e seguras, o que na prática pede um plano de manutenção predial documentado (a ABNT NBR 5674 é a base para esse plano).</p>
    <p>A tabela do início do artigo traz um ponto de partida. A lógica é simples: quanto mais grave o paciente e mais uso o ponto tem, menor o intervalo. Entupimento em área crítica é tratado como urgência, não entra em fila. Na cozinha, a frequência segue a de qualquer cozinha comercial: veja <a href="../limpeza-caixa-de-gordura/">de quanto em quanto tempo limpar a caixa de gordura</a>.</p>

    <h2>Como a manutenção deve ser feita sem colocar pacientes em risco?</h2>
    <p><strong>Antes do serviço</strong></p>
    <ul>
      <li>Autorização da CCIH e do enfermeiro responsável pelo setor</li>
      <li>Avaliação de risco: quanto mais crítica a área, mais controle</li>
      <li>Isolamento físico e sinalização da área</li>
      <li>Pacientes próximos remanejados ou serviço feito em horário de menor movimento</li>
    </ul>
    <p><strong>Durante o serviço</strong></p>
    <ul>
      <li>EPI completo: luvas, avental impermeável, máscara PFF2, óculos e botas</li>
      <li>Controle de respingos e gotículas: <a href="../como-funciona-hidrojateamento/">hidrojateamento</a> em área assistencial só com contenção</li>
      <li>Tubulação nunca deixada aberta, para o ar do esgoto não entrar no ambiente</li>
      <li>Ferramentas, mangueiras e equipamentos limpos e desinfetados, sem trazer sujeira de outro serviço</li>
    </ul>
    <p><strong>Depois do serviço</strong></p>
    <ul>
      <li>Limpeza terminal da área pela equipe de higienização</li>
      <li>Resíduos descartados conforme o plano de resíduos da instituição (RDC 222/2018)</li>
      <li>Relatório técnico com fotos, local, data e o que foi feito</li>
    </ul>
    <p>A equipe que entra num hospital precisa ter treinamento em biossegurança e vacinação em dia, principalmente contra hepatite B e tétano.</p>

    <h2>O que a cozinha de um restaurante ensina sobre a do hospital?</h2>
    <p>A cozinha de um hospital funciona como a de um restaurante grande: muita gordura, uso o dia inteiro e nenhum horário bom para parar. É o tipo de rede que mais atendemos em comércios, e o caso abaixo mostra por que o acesso à tubulação faz tanta diferença.</p>
    <div class="caso">
      <p><span class="rotulo">Caso real (restaurante em Goiânia):</span> a rede de esgoto do restaurante estava totalmente parada e não havia nenhuma caixa de inspeção para entrar na tubulação. Sem caixa, o caminho comum seria quebrar o piso. A solução foi abrir a fossa e entrar com a mangueira do hidrojato pelo cano que chega até ela, trabalhando em direção à obstrução, tomada por gordura e resíduos. Depois do serviço, a rede voltou a escoar.</p>
      <p>Num hospital, o mesmo problema teria um peso maior: a cozinha não pode parar e uma quebra de piso levanta poeira perto de pacientes. Por isso caixas de inspeção acessíveis e mapeadas fazem parte de um bom plano de manutenção.</p>
    </div>

    ''' + video("D4aA6c9-8lc", "hidrojato entrando pela fossa de um restaurante", "Vídeo do hidrojato operando pelo cano dentro da fossa de um restaurante em Goiânia",
                "Vídeo (caso real, 30 s): restaurante em Goiânia sem caixas de inspeção. O hidrojato entra pelo cano que chega à fossa para desobstruir a rede tomada por gordura.") + '''

    <h2>O que a equipe pode fazer no dia a dia</h2>
    <ul>
      <li><strong>Ralo de quarto ou consultório vazio:</strong> jogar um pouco de água uma vez por semana. Isso repõe a água do sifão, que seca quando o ponto fica sem uso, e evita o cheiro.</li>
      <li><strong>Ralinho ou grelha na pia da copa e da cozinha:</strong> segura os resíduos antes de chegarem ao cano.</li>
      <li><strong>Avisar logo:</strong> escoamento lento, barulho de "gorgolejo" ou cheiro são os primeiros sinais. Quanto antes a manutenção for chamada, mais simples o serviço.</li>
    </ul>

    <h2>O que nunca fazer</h2>
    <ul class="nao">
      <li><strong>Misturar água sanitária com outros produtos</strong> (como amoníaco ou ácidos): a mistura libera gases tóxicos. Em ambiente fechado, com pacientes, é ainda mais perigoso.</li>
      <li><strong>Usar soda cáustica:</strong> respinga, queima a pele e pode danificar a tubulação.</li>
      <li><strong>Jogar água fervendo em cano de PVC:</strong> pode deformar as conexões.</li>
      <li><strong>Descartar óleo, gordura ou restos de comida na pia:</strong> é a principal causa de entupimento nas cozinhas que atendemos. Veja <a href="../pode-jogar-oleo-na-pia/">como descartar o óleo</a>.</li>
      <li><strong>Desmontar o sifão sem proteção:</strong> o resíduo de dentro é altamente contaminado.</li>
    </ul>

    <h2>Quando chamar uma equipe especializada?</h2>
    <ul>
      <li>Quando o cheiro volta mesmo com o ralo limpo e com água</li>
      <li>Quando há refluxo, transbordamento ou escoamento lento em mais de um ponto</li>
      <li>Quando o entupimento está em área crítica (UTI, centro cirúrgico, hemodiálise, CME)</li>
      <li>Quando a caixa de gordura ou a rede geral precisam de hidrojateamento</li>
      <li>Quando o hospital ou a clínica precisa montar ou revisar o plano de manutenção preventiva</li>
    </ul>
    <p>Para entender a gravidade de um entupimento, veja <a href="../niveis-de-entupimento/">os 4 níveis de entupimento</a>.</p>''',
    faq=[
        ("Ralo com cheiro em hospital é perigoso?", "Sim. Além de indicar falha na vedação do esgoto, pias e ralos hospitalares já foram identificados como reservatórios de bactérias resistentes a antibióticos em surtos de UTI."),
        ("Com que frequência limpar a rede de esgoto de um hospital ou clínica?", "Como ponto de partida, áreas críticas recebem inspeção mensal e limpeza técnica trimestral, e a rede geral é revisada a cada seis meses. A rotina final é definida pela CCIH com a engenharia de manutenção."),
        ("Trocar o sifão resolve a contaminação?", "Não sozinho. A troca pode ser necessária, mas estudos mostram que, sem protocolo e sem mudar a rotina da equipe, as pias voltam a ser colonizadas, e houve caso de surto de outra bactéria depois da troca."),
        ("Quais áreas precisam de mais cuidado com a tubulação?", "UTIs, centro cirúrgico, hemodiálise, oncologia e transplante, CME, cozinha, lactário e quartos de isolamento. Em clínicas: sala de procedimentos, hemodiálise, coleta de laboratório, expurgo e copa."),
        ("Pode fazer hidrojateamento dentro de um hospital?", "Pode, com autorização da CCIH, isolamento da área, contenção de respingos, EPI completo e limpeza terminal depois."),
    ],
    fontes=["kizny", "sheba", "degeyter", "uva", "anvisa_saude", "nbr5674", "sanepar", "campo"],
    leia=["niveis-de-entupimento", "como-funciona-hidrojateamento", "limpeza-caixa-de-gordura"],
)

# ---------------------------------------------------------------------------
# Gordura endurecida / saponificada (pauta do Lucas, 24/11/2026)
# ---------------------------------------------------------------------------
GORDURA_PEDRA = dict(
    slug="gordura-endurecida-no-cano",
    title="Gordura endurecida no cano em Goiânia: por que vira pedra",
    h1="Gordura endurecida no cano em Goiânia: por que vira pedra e como remover sem danificar o encanamento",
    desc="Por que a gordura vira pedra no cano, o papel da soda cáustica, quando usar sonda rotativa ou hidrojateamento e quando o cano precisa ser trocado.",
    migalha="Gordura endurecida no cano",
    keywords="gordura endurecida no cano, gordura saponificada, pedra de gordura no encanamento, incrustação de gordura, soda cáustica e gordura, sonda rotativa ou hidrojateamento, Diabo Verde funciona",
    sobre=["Saponificação", "Gordura na tubulação", "Soda cáustica", "Hidrojateamento", "Sonda rotativa"],
    imagem=SITE + "/blog/img/nivel-4-cano-de-gordura.webp",
    linkedin="https://www.linkedin.com/pulse/como-gordura-entope-tubula%C3%A7%C3%B5es-caso-real-em-lucas-nonato-vieira-palhf",
    videos=["bn_lcqH_SDA"],
    resumo="A gordura vira pedra no cano por uma reação química chamada saponificação: com o tempo, a gordura se quebra em ácidos graxos, que se juntam ao cálcio da água e do esgoto e formam um tipo de sabão duro, insolúvel e grudado na parede do tubo. A soda cáustica acelera essa quebra e pode deixar a massa ainda mais dura. Desentupidores de mercado só ajudam em casos leves; com o cano estreitado (níveis 2 e 3) a sonda rotativa costuma resolver, e com a rede comprometida (nível 4) o caminho mais seguro é o hidrojateamento feito por técnico experiente. Curvas, diâmetro e estado do cano decidem o método, e isso só se confirma no local.",
    corpo='''    <p>Quem já abriu um cano de cozinha antigo conhece a cena: em vez de uma gordura mole, sai uma crosta dura, cinza ou amarelada, que parece pedra e às vezes tem o formato do próprio cano. Em 10 anos de serviço, retirei muito disso de pias, caixas de gordura e redes de esgoto. Neste artigo explico, em palavras simples, por que a gordura endurece, qual é o papel da soda cáustica e como escolher o método de remoção sem estragar o encanamento.</p>

    <h2>Resumo: qual método para cada nível de entupimento</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Nível</th><th>Como está o cano</th><th>O que costuma resolver</th></tr></thead>
        <tbody>
          <tr><td>Nível 1</td><td>Água descendo devagar, camada fina de gordura</td><td>Desengordurante aplicado com alta pressão; limpeza do sifão</td></tr>
          <tr><td>Nível 2</td><td>Um ponto parou, gordura já endurecendo no ramal</td><td>Sonda rotativa</td></tr>
          <tr><td>Nível 3</td><td>Vários pontos ruins, placas de gordura no caminho</td><td>Sonda rotativa (às vezes com hidrojato para acabamento)</td></tr>
          <tr><td>Nível 4</td><td>Rede comprometida, crosta de gordura saponificada</td><td>Hidrojateamento com técnico experiente</td></tr>
        </tbody>
      </table>
    </div>
    <p>A tabela é um ponto de partida. Comprimento do trecho, quantidade de curvas, diâmetro e material do cano mudam a escolha. Se você ainda não sabe em que nível está o seu caso, veja <a href="../niveis-de-entupimento/">como identificar os 4 níveis de entupimento</a>.</p>

    <h2>Por que a gordura vira pedra dentro do cano?</h2>
    <p>Durante muito tempo se achou que a gordura só esfriava e grudava. Ela esfria, sim, mas isso explica apenas a gordura mole, aquela que derrete com água quente. A "pedra" é outra coisa. Pesquisadores da Universidade Estadual da Carolina do Norte, com apoio da agência ambiental dos EUA (EPA), analisaram depósitos tirados de redes de esgoto e concluíram que eles são, basicamente, sabão de cálcio. Um estudo com depósitos de redes do Reino Unido chegou à mesma conclusão.</p>
    <p>Em palavras simples, o processo acontece em três etapas:</p>
    <ol>
      <li><strong>A gordura se quebra.</strong> Óleo e gordura são formados por ácidos graxos presos a uma molécula de glicerina. Com o tempo, a água, o calor e as bactérias do esgoto soltam esses ácidos graxos.</li>
      <li><strong>Os ácidos graxos encontram o cálcio.</strong> O cálcio vem da própria água, de restos de alimentos e até do concreto das caixas e da rede.</li>
      <li><strong>Forma-se um sabão duro.</strong> Ácido graxo + cálcio vira um sal que não se dissolve em água. É a saponificação, a mesma reação do sabão caseiro, só que com cálcio no lugar do sódio. O resultado é uma crosta granulada, parecida com arenito, que gruda na parede do cano e vai crescendo em camadas.</li>
    </ol>
    <p>Esse sabão de cálcio não derrete com água quente e não sai com detergente. Os próprios pesquisadores apontam que ele exige limpeza mecânica pesada, como o hidrojateamento.</p>

    ''' + FOTO_GORDURA + '''

    <h2>Qual a diferença entre gordura comum e gordura saponificada?</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th></th><th>Gordura comum</th><th>Gordura saponificada</th></tr></thead>
        <tbody>
          <tr><td>Textura</td><td>Pastosa, pegajosa, parece manteiga</td><td>Dura, granulada, parece pedra ou arenito</td></tr>
          <tr><td>Com água quente</td><td>Amolece e avança no cano</td><td>Não muda</td></tr>
          <tr><td>Onde aparece</td><td>Sifão, começo do ramal, caixa de gordura</td><td>Parede do cano, curvas, trechos com pouca queda, rede depois da caixa</td></tr>
          <tr><td>Como sai</td><td>Limpeza do sifão, ventosa, desengordurante</td><td>Sonda rotativa ou hidrojateamento</td></tr>
          <tr><td>Sinal típico</td><td>Pia lenta que melhora depois de limpar</td><td>Entupimento que volta pouco tempo depois de desentupido</td></tr>
        </tbody>
      </table>
    </div>

    <h2>A soda cáustica ajuda ou piora a gordura endurecida?</h2>
    <p>Na maioria dos casos, piora. A soda cáustica é hidróxido de sódio, um produto muito alcalino. Ela quebra a gordura muito rápido: é a mesma reação usada para fazer sabão em casa. Perto do ralo, isso pode até abrir uma passagem por algumas horas. O problema é o que acontece depois:</p>
    <ul>
      <li><strong>Acelera a quebra da gordura.</strong> Em laboratório, a quebra da gordura em meio alcalino também gerou os sais de cálcio que formam os depósitos. A soda entrega ao cano exatamente esse ambiente.</li>
      <li><strong>Esquenta e empurra o problema.</strong> A reação da soda com a água libera calor. A gordura amolece, anda alguns metros, esfria num trecho mais difícil e endurece de novo lá.</li>
      <li><strong>Vira uma massa empedrada.</strong> Um trabalho de conclusão de curso de Engenharia Civil do UniCEUB, sobre a rede de esgoto do Distrito Federal, descreve justamente isso: a soda usada para desentupir pia transforma a gordura em uma composição empedrada que adere às paredes da tubulação. O mesmo trabalho liga o problema à falta de caixa de gordura ou à falta de limpeza dela.</li>
      <li><strong>Fica parada no cano.</strong> Com o cano totalmente fechado, o produto fica ali, corrosivo, esperando quem for abrir o sifão ou usar a ventosa.</li>
    </ul>
    <p>Na prática de campo, quando a pessoa conta que já jogou soda várias vezes, quase sempre encontramos a gordura mais dura e mais espalhada pela rede do que nos casos em que nada foi usado.</p>

    <h2>Diabo Verde e outros desentupidores de mercado funcionam?</h2>
    <p>Existem vários desentupidores e desengordurantes vendidos em mercado, como o Diabo Verde e outras marcas. Boa parte deles tem hidróxido de sódio na fórmula, a própria embalagem avisa que causam queimaduras graves e que servem para material orgânico, como gordura, cabelo e papel.</p>
    <ul>
      <li><strong>Onde podem ajudar:</strong> gordura recente, mole, perto do ralo, com a água ainda descendo (nível 1).</li>
      <li><strong>Onde não resolvem:</strong> no nível 4, com a rede comprometida por crosta de gordura saponificada, dificilmente um produto de mercado resolve. Ele não alcança metros de cano e não dissolve sabão de cálcio. O risco é ficar parado no trecho entupido e piorar o endurecimento.</li>
    </ul>
    <p>Se for usar, siga a embalagem, use luva e óculos, nunca misture com outro produto e não use ventosa logo depois. Mais detalhes em <a href="../pode-jogar-oleo-na-pia/">o que não usar para desentupir</a>.</p>

    <h2>Como remover a incrustação sem danificar o encanamento?</h2>
    <p>A regra é tirar a gordura da parede do cano inteira, não só abrir um furo no meio dela, e escolher a ferramenta pelo nível e pelo tipo de tubulação.</p>
    <h3>Nível 1: desengordurante com alta pressão</h3>
    <p>Com a água ainda descendo e a camada de gordura fina, o desengordurante de alta pressão que usamos na BV Desentupidora já resolve: ele solta a gordura da parede enquanto a pressão leva o resíduo embora. Junto, vale limpar o sifão e a caixa de gordura.</p>
    <h3>Níveis 2 e 3: sonda rotativa</h3>
    <p>A sonda rotativa é um cabo de aço com uma ponteira que gira dentro do cano e raspa a parede. Ela resolve bem quando a gordura já endureceu em placas no ramal ou em alguns pontos da rede. Funciona bem em trechos com várias curvas, onde o cabo consegue acompanhar o caminho, e também em cano amassado ou com terra, onde o jato não passa. A ponteira e a velocidade precisam combinar com o diâmetro: ponteira grande demais num cano fino de PVC pode arranhar ou forçar as conexões.</p>
    <h3>Nível 4: hidrojateamento</h3>
    <p>Quando a gordura saponificada tomou a rede, o hidrojateamento é a opção mais segura. O jato de água em alta pressão sai por um bico com furos para trás e para os lados, quebra a crosta e lava a parede do cano em toda a volta, sem raspar com metal. Veja <a href="../como-funciona-hidrojateamento/">como funciona o hidrojateamento</a>.</p>
    <p>Aqui a experiência do técnico conta muito. A pressão, o bico e a velocidade de avanço precisam ser escolhidos para cada cano: pressão alta demais num PVC antigo ou numa emenda mal feita pode causar estrago, e pressão baixa demais só faz um furo na crosta. Também é o técnico que percebe, pelo retorno da água e pelo que sai do cano, se a gordura acabou ou se ainda há trecho sujo.</p>
    <h3>O que conta além do nível</h3>
    <ul>
      <li><strong>Curvas:</strong> cada joelho é um ponto onde a gordura acumula e onde a ferramenta precisa passar.</li>
      <li><strong>Diâmetro:</strong> ramal de pia de 40 ou 50 mm pede ferramenta diferente de uma rede de 100 mm.</li>
      <li><strong>Material e idade:</strong> PVC novo, PVC antigo, ferro fundido e manilha de barro aguentam esforços diferentes.</li>
      <li><strong>Acesso:</strong> sifão, caixa de gordura e caixas de inspeção definem por onde entrar sem quebrar.</li>
    </ul>
    <p>Por isso essa escolha é feita no local, depois de olhar a tubulação, e não por telefone.</p>

    <h2>Caso real: como a gordura para no encanamento</h2>
    <div class="caso">
      <p>No vídeo abaixo eu mostro, na prática, como a gordura vai grudando nas paredes do cano e estreitando a passagem da água até o entupimento voltar mesmo depois de desobstruído. É o mesmo processo que encontramos em um atendimento em Inhumas (GO), contado em detalhes no artigo <a href="https://www.linkedin.com/pulse/como-gordura-entope-tubula%C3%A7%C3%B5es-caso-real-em-lucas-nonato-vieira-palhf" rel="noopener" target="_blank">Como a gordura entope tubulações: caso real em Inhumas-GO</a>: a pia estava parada e, ao abrir a tubulação, o que travava a água eram pedras de gordura grudadas na parede do cano.</p>
      <p>Nesses casos, abrir só um furo no meio da crosta resolve por poucos dias. O que impede a volta é remover a gordura da parede inteira.</p>
    </div>

    ''' + video("bn_lcqH_SDA", "como o cano enche de gordura", "Lucas Nonato mostra um cano com gordura grudada nas paredes internas",
                "Vídeo (caso real): como a gordura gruda nas paredes do cano e estreita a passagem da água.") + '''

    <p>A classificação dos níveis usada neste artigo é a mesma que expliquei no LinkedIn em <a href="https://www.linkedin.com/pulse/os-4-n%C3%ADveis-de-entupimento-como-identificar-o-que-fazer-vieira-ixbuf" rel="noopener" target="_blank">Os 4 níveis de entupimento: como identificar e o que fazer</a> e no <a href="../niveis-de-entupimento/">guia completo aqui do blog</a>.</p>

    <h2>Como saber se a tubulação pode ser recuperada ou precisa ser trocada?</h2>
    <p>Na maioria dos casos de gordura, o cano é recuperado: a gordura sai e o tubo continua bom. A troca entra em cena quando o problema não é mais só a gordura.</p>
    <p><strong>Sinais de que dá para recuperar:</strong></p>
    <ul>
      <li>Depois da limpeza, a água volta a correr com vazão normal.</li>
      <li>O cano não tem vazamento, trinca nem infiltração em volta.</li>
      <li>O entupimento não volta em poucas semanas com o uso normal.</li>
    </ul>
    <p><strong>Sinais de que o trecho pode precisar ser trocado:</strong></p>
    <ul class="nao">
      <li>Cano de PVC amolecido, deformado ou achatado, comum depois de muita soda ou água fervendo.</li>
      <li>Ferro fundido muito corroído por dentro, que solta lascas e volta a segurar gordura logo.</li>
      <li>Trinca, emenda solta ou infiltração de esgoto no piso ou na parede.</li>
      <li>"Barriga" no cano (trecho afundado sem queda), onde a água para e a gordura volta a acumular mesmo depois de limpo.</li>
      <li>Crosta tão aderida que só sairia forçando o tubo, num trecho curto e fácil de trocar.</li>
    </ul>
    <p>Quando há dúvida, a inspeção com câmera depois da limpeza mostra o estado real da parede. Trocar o cano sem antes limpar e olhar por dentro costuma ser gasto desnecessário. Veja também <a href="../precisa-quebrar-piso-para-desentupir/">se é preciso quebrar o piso para desentupir</a>.</p>

    <h2>Dicas caseiras: o que funciona e o que não fazer</h2>
    <p>Algumas dicas que encanadores e moradores trocam em fóruns como o Reddit, e que fazem sentido para prevenção:</p>
    <ul>
      <li>Passe papel-toalha em panelas e pratos antes de lavar e jogue no lixo.</li>
      <li>Guarde o óleo usado em garrafa PET e entregue num ponto de coleta.</li>
      <li>Use peneira no ralo da pia e esvazie todo dia.</li>
      <li>Uma vez por semana, deixe correr água quente da torneira com detergente por alguns minutos. É prevenção para gordura recente, não remove pedra de gordura.</li>
      <li>Produtos com enzimas ou bactérias para manutenção de ralo são citados por muitos profissionais como uso preventivo, não para desentupir.</li>
      <li>Limpe a caixa de gordura com frequência: veja <a href="../limpeza-caixa-de-gordura/">de quanto em quanto tempo limpar</a>.</li>
    </ul>
    <ul class="nao">
      <li>Jogar soda cáustica repetidas vezes para "derreter" a pedra.</li>
      <li>Jogar água fervendo em cano de PVC.</li>
      <li>Misturar produtos de limpeza: pode liberar gás tóxico.</li>
      <li>Empurrar arame, cabide ou vergalhão: fura o cano ou fica preso.</li>
      <li>Usar ventosa logo depois de colocar produto químico.</li>
    </ul>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>O entupimento volta pouco tempo depois de desentupido.</li>
      <li>Sifão limpo e ventosa não resolveram.</li>
      <li>Já foi usada soda ou desentupidor químico e a água continua parada.</li>
      <li>Mais de um ponto da casa está ruim, ou a caixa de gordura transborda.</li>
      <li>Há mau cheiro, barulho de bolhas ou retorno de água.</li>
    </ul>
    <p>Se já colocou produto químico no cano, avise o técnico antes de ele abrir o sifão: isso muda a forma de trabalhar com segurança.</p>''',
    faq=[
        ("O que é gordura saponificada?", "É a gordura que reagiu com o cálcio da água e do esgoto e virou um tipo de sabão duro, que não se dissolve em água. É ela que forma as pedras grudadas na parede do cano."),
        ("Soda cáustica dissolve pedra de gordura?", "Não. A soda pode abrir uma passagem em gordura recente perto do ralo, mas acelera a quebra da gordura e pode deixar a massa ainda mais dura e espalhada pela rede."),
        ("Diabo Verde resolve entupimento de gordura?", "Pode ajudar em gordura recente e leve, com a água ainda descendo. Quando a rede já está comprometida por crosta de gordura (nível 4), dificilmente um produto de mercado resolve."),
        ("Sonda rotativa ou hidrojateamento: qual é melhor para gordura?", "Depende do nível e do cano. A sonda rotativa resolve bem nos níveis 2 e 3 e em trechos com curvas ou cano amassado; no nível 4, com a rede tomada pela gordura, o hidrojateamento é o mais indicado."),
        ("Hidrojateamento estraga o cano?", "Feito com pressão e bico adequados ao tipo de cano, não. O risco aparece com pressão errada em tubo antigo ou emenda frágil, por isso a experiência do técnico importa."),
    ],
    fontes=["uniceub", "ncsu", "williams2012", "epa_ducoste", "diabo_verde", "nbr8160", "li_niveis", "campo"],
    leia=["niveis-de-entupimento", "como-funciona-hidrojateamento", "desentupir-pia-com-gordura"],
)

# ---------------------------------------------------------------------------
# Entupimento recorrente: gordura x caimento x cano deformado (pauta do Lucas, 24/11/2026; publicar 25/11)
# O "exemplo ilustrativo" NÃO é caso real e está marcado assim no texto (decisão do Claude: não inventar caso real).
# ---------------------------------------------------------------------------
RECORRENTE = dict(
    slug="entupimento-recorrente",
    title="Entupimento recorrente em Goiânia: gordura, caimento ou cano?",
    h1="Entupimento recorrente em Goiânia: como saber se é gordura, cano sem caimento ou cano deformado",
    desc="Desentope e volta? Veja como diferenciar gordura, cano com pouca inclinação (contrapendente) e cano deformado, e quando corrigir a tubulação.",
    migalha="Entupimento recorrente",
    keywords="entupimento recorrente, entupimento que volta, cano sem caimento, contrapendente esgoto, declividade do esgoto, barriga no cano, cano amassado, sonda rotativa",
    sobre=["Entupimento recorrente", "Declividade de tubulação de esgoto", "Gordura na tubulação", "Sonda rotativa", "NBR 8160"],
    imagem=SITE + "/blog/img/declividade-cano-esgoto-certo-e-contrapendente.webp",
    videos=["cjH3O35wWQI", "lk54797N6pM"],
    resumo="Quando o entupimento volta, o desentupimento tratou o sintoma e a causa continuou no cano. As três causas mais comuns deixam sinais diferentes. Gordura: atinge pia e cozinha, volta em semanas e sai do cano em placas amareladas. Pouco caimento ou contrapendente (a “barriga”): a caixa de inspeção fica sempre com água parada, o ralo borbulha e o entupimento aparece sempre no mesmo ponto. Cano deformado: a ferramenta trava sempre na mesma distância, às vezes sai terra, e o trecho costuma passar sob garagem ou área com peso. Gordura sai com sonda rotativa ou hidrojato; pouco caimento e cano deformado só se resolvem de vez corrigindo ou trocando o trecho.",
    corpo='''    <p>"Desentupiu e voltou" é a reclamação que mais escuto em 10 anos de serviço. Quase sempre a pessoa já gastou com produto, já chamou alguém, e o problema retornou em semanas. Isso não quer dizer que o serviço anterior foi mal feito: quer dizer que a causa não era só a sujeira. Abaixo explico como diferenciar as três causas mais comuns e o que resolve cada uma.</p>

    <h2>Resumo: as 3 causas lado a lado</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Causa</th><th>Sinais típicos</th><th>O que sai do cano</th><th>O que resolve</th></tr></thead>
        <tbody>
          <tr><td>Gordura acumulada</td><td>Pia e cozinha; volta em semanas; cheiro de gordura velha</td><td>Placas e pedaços amarelados ou acinzentados</td><td>Sonda rotativa ou hidrojato, e caixa de gordura em dia</td></tr>
          <tr><td>Pouco caimento ou contrapendente</td><td>Caixa sempre com água parada; ralo borbulha; entope sempre no mesmo lugar</td><td>Lama, areia e sujeira assentada</td><td>Limpeza dá alívio; corrigir o caimento resolve</td></tr>
          <tr><td>Cano deformado ou quebrado</td><td>Ferramenta trava sempre na mesma distância; trecho sob garagem ou árvore</td><td>Terra, pedaços de cano, raiz</td><td>Sonda rotativa abre passagem; trocar o trecho resolve</td></tr>
        </tbody>
      </table>
    </div>
    <p>As causas também se somam. Um cano com barriga acumula gordura justamente no ponto baixo, e um cano amassado segura gordura e terra no estreitamento.</p>

    <figure>
      <img src="../img/causas-entupimento-recorrente-corte-do-cano.webp" alt="Ilustração em corte de três canos: um com crosta de gordura na parede, um com água parada e sujeira no fundo por falta de caimento e um achatado com terra dentro" width="1200" height="600" loading="lazy">
      <figcaption>Ilustração: como cada causa aparece dentro do cano.</figcaption>
    </figure>

    <h2>Por que o desentupimento resolve, mas o problema volta?</h2>
    <p>Desentupir é abrir passagem. Se o motivo do acúmulo continua lá, a sujeira volta a parar no mesmo ponto:</p>
    <ul>
      <li><strong>Com gordura</strong>, abrir só um furo no meio da crosta deixa a parede do cano áspera e estreita. O resto de comida prende ali de novo.</li>
      <li><strong>Com pouco caimento</strong>, a água não tem velocidade para levar os sólidos. Eles assentam no trecho plano ou na barriga, entupimento após entupimento.</li>
      <li><strong>Com cano deformado</strong>, o estreitamento é físico. A ferramenta passa, mas o cano continua amassado.</li>
    </ul>
    <p>Por isso, num entupimento que se repete, a pergunta não é só "o que entupiu", e sim "por que entupiu aqui de novo".</p>

    <h2>Como saber se a causa é gordura?</h2>
    <ul>
      <li>O problema começa na pia da cozinha, no tanque ou na caixa de gordura.</li>
      <li>Volta em semanas ou poucos meses, de forma gradual: primeiro a água desce devagar, depois para.</li>
      <li>Quando o cano é aberto, saem placas, "pedras" ou pedaços de gordura grudados na parede.</li>
      <li>A caixa de gordura fica cheia rápido ou está sem limpeza há muito tempo.</li>
      <li>Já foi usada soda cáustica várias vezes. Ela tende a deixar a gordura mais dura, como explico em <a href="../gordura-endurecida-no-cano/">por que a gordura vira pedra no cano</a>.</li>
    </ul>
    <p>Gordura pura costuma ser a causa mais simples de resolver: com a parede do cano limpa por inteiro e a caixa de gordura em dia, o problema para de voltar. Se volta mesmo assim, desconfie também do caimento.</p>

    ''' + video("cjH3O35wWQI", "o tanto de gordura no final do cano", "Gordura acumulada nas paredes internas de uma tubulação",
                "Vídeo (caso real, 1 min 9 s): como a gordura se acumula nas paredes internas do cano até diminuir a passagem da água.") + '''

    <h2>Como identificar uma tubulação com pouco caimento ou contrapendente?</h2>
    <p>Esgoto funciona por gravidade. Para a água levar os sólidos, o cano precisa descer o tempo todo na direção da saída. A NBR 8160 recomenda declividade mínima de 2% para canos de até 75 mm e de 1% para canos de 100 mm ou mais. Na prática, isso é 2 cm de queda a cada metro nos canos finos e 1 cm por metro nos de 100 mm.</p>
    <p><strong>Contrapendente</strong> é quando o cano sobe em algum trecho antes da saída. O caso mais comum é a "barriga": um pedaço que afundou e ficou mais baixo que o resto. Ali a água fica parada o tempo todo e a sujeira assenta.</p>

    <figure>
      <img src="../img/declividade-cano-esgoto-certo-e-contrapendente.webp" alt="Ilustração de três canos enterrados: um com caimento correto, um com barriga (contrapendente) acumulando água e sujeira e um com inclinação exagerada deixando sólidos para trás" width="1200" height="630" loading="lazy">
      <figcaption>Ilustração: caimento correto, contrapendente (barriga) e inclinação exagerada.</figcaption>
    </figure>

    <p>Sinais que apontam para caimento errado:</p>
    <ul>
      <li><strong>Caixa de inspeção sempre com água parada</strong>, mesmo horas depois de ninguém usar nada. Numa rede com bom caimento, a caixa esvazia.</li>
      <li><strong>Entope sempre no mesmo ponto.</strong> O técnico mede quanto a mola entrou e a obstrução está sempre na mesma distância.</li>
      <li><strong>Ralo e vaso borbulham</strong> ou fazem barulho quando outro ponto da casa escoa.</li>
      <li><strong>Sai muita lama e areia</strong> no desentupimento, e pouca gordura ou objeto.</li>
      <li><strong>O problema começou depois de uma obra</strong>, de piso que afundou ou de um trecho de cano refeito.</li>
      <li><strong>O imóvel é novo e entope desde a entrega.</strong> Caimento errado e <a href="../cimento-no-encanamento/">resto de obra no cano</a> são suspeitos fortes.</li>
    </ul>
    <p>Inclinação demais também atrapalha. Em trechos muito íngremes, a água corre na frente e os sólidos ficam para trás, colados no fundo do cano. Na nossa experiência, isso aparece em emendas improvisadas e em reformas que mudaram a altura da saída.</p>
    <p>A confirmação vem com medição: nível de mangueira ou nível a laser entre duas caixas, ou inspeção com câmera, que mostra a lâmina de água parada no trecho baixo.</p>
    <p>Esse não é um problema raro em Goiânia. Um trabalho de conclusão de curso de Engenharia Civil da UFG analisou as instalações de esgoto de três empreendimentos residenciais de uma construtora da cidade e concluiu que foram poucos os casos com a declividade correta. Em alguns trechos, os pesquisadores encontraram até contradeclividade: o cano saía da caixa sifonada a 12 cm do teto e chegava ao tubo de queda a 10 cm, ou seja, subia no caminho em vez de descer. O engenheiro da obra relatou que, na entrega, a água às vezes só escoa mais devagar, ninguém percebe na vistoria, e pouco depois a tubulação entope. Entre as causas listadas estão declividade errada e entulho de obra dentro do cano. Os próprios autores avisam que o estudo olhou uma única construtora, mas o padrão é o mesmo que vemos em campo.</p>
    <p>Outros trabalhos da UFG reforçam o quadro: um TCC sobre obras de redes coletoras na Região Metropolitana de Goiânia registrou práticas que dificultam o controle da declividade, e um artigo da revista de engenharia civil da universidade alerta que, com menos água nas descargas e sem ajuste nos ramais, os entupimentos aumentam. Com menos água, o caimento faz ainda mais diferença.</p>

    <h2>Como saber se o cano está deformado ou quebrado?</h2>
    <ul>
      <li>A mola ou o jato <strong>trava sempre no mesmo lugar</strong>, e a sensação é de bater numa parede, não numa sujeira mole.</li>
      <li><strong>Sai terra, areia grossa ou pedaços de cano</strong>: sinal de rachadura ou emenda solta.</li>
      <li>O trecho passa <strong>sob garagem, entrada de carro ou perto de árvore</strong>, ou foi enterrado raso.</li>
      <li>Existe <strong>afundamento ou rachadura no piso</strong> em cima do trajeto do cano.</li>
    </ul>

    <div class="caso">
      <p><span class="rotulo">Caso real (Itaberaí, GO, nov/2026):</span> em um sobradinho, a rede pluvial estava obstruída havia meses. O hidrojato não passava: o encanamento estava achatado e cheio de terra. A passagem foi aberta com sonda rotativa, até a água voltar a escorrer. Contei os detalhes no LinkedIn, em <a href="https://www.linkedin.com/pulse/o-hidrojato-n%C3%A3o-passou-sonda-rotativa-caso-da-rede-pluvial-vieira-hce4f" rel="noopener" target="_blank">O hidrojato não passou. A sonda rotativa passou</a>. A sonda resolveu a urgência, mas um cano achatado continua sendo um ponto estreito, e esse trecho é candidato a troca.</p>
    </div>

    ''' + video("lk54797N6pM", "sonda rotativa em rede pluvial achatada", "Rede pluvial com cano achatado e cheio de terra desobstruída com sonda rotativa",
                "Vídeo (caso real, 41 s): rede pluvial achatada e cheia de terra; o hidrojato não passou e a sonda rotativa abriu a passagem.") + '''

    <h2>Exemplo ilustrativo: quando as causas se juntam</h2>
    <div class="caso">
      <p><span class="rotulo">Exemplo ilustrativo (montado a partir de situações frequentes, não é um atendimento específico):</span> numa casa, a pia da cozinha entope a cada dois meses. Já usaram desentupidor de mercado e chamaram ajuda duas vezes; nas duas, saiu gordura e o problema voltou. Na terceira vez, o técnico anota até onde a mola entra: a obstrução está sempre a uns 6 metros, no trecho que passa sob a entrada da garagem. A câmera mostra água parada num pedaço de uns 2 metros, com gordura grudada só ali. Nesse cenário, a gordura não é a causa principal: ela é consequência da barriga. Limpar resolve por mais dois meses; corrigir o caimento daquele trecho resolve de vez.</p>
    </div>
    <p>O que esse exemplo mostra: anotar <strong>onde</strong> e <strong>de quanto em quanto tempo</strong> o entupimento acontece ajuda muito o diagnóstico.</p>

    <h2>Quando a sonda rotativa resolve e quando é preciso corrigir a tubulação?</h2>
    <div class="tabela-wrap">
      <table>
        <thead><tr><th>Situação</th><th>Sonda rotativa resolve?</th><th>Precisa corrigir o cano?</th></tr></thead>
        <tbody>
          <tr><td>Gordura em placas, cano em bom estado</td><td>Sim (ou hidrojato)</td><td>Não</td></tr>
          <tr><td>Pouco caimento leve, sem barriga</td><td>Alivia; pede manutenção periódica</td><td>Às vezes não, se a limpeza preventiva der conta</td></tr>
          <tr><td>Barriga ou contrapendente</td><td>Só temporariamente</td><td>Sim, refazer o trecho com caimento</td></tr>
          <tr><td>Cano achatado ou com terra</td><td>Abre passagem na urgência</td><td>Sim, trocar o trecho deformado</td></tr>
          <tr><td>Cano quebrado ou emenda solta</td><td>Não deve ser forçada</td><td>Sim</td></tr>
        </tbody>
      </table>
    </div>
    <p>Corrigir não significa quebrar a casa inteira. Na maioria das vezes é um trecho localizado, encontrado pela medição da mola e pela câmera. Veja <a href="../precisa-quebrar-piso-para-desentupir/">quando é preciso quebrar o piso</a>.</p>

    <h2>O que dá para observar em casa?</h2>
    <p>Algumas dicas que encanadores e moradores trocam em fóruns como o Reddit, e que ajudam no diagnóstico:</p>
    <ul>
      <li><strong>Anote as datas</strong> dos entupimentos e qual ponto parou primeiro.</li>
      <li><strong>Abra a caixa de inspeção</strong> algumas horas depois de ninguém usar água. Se tiver água parada, desconfie do caimento depois dela.</li>
      <li><strong>Teste do balde:</strong> jogue um balde de água limpa no ralo ou no vaso e observe a caixa seguinte. A água deve chegar e ir embora; se sobe e demora a baixar, o problema está depois dali.</li>
      <li><strong>Repare no piso:</strong> trinca ou afundamento em cima do trajeto do cano é pista importante.</li>
      <li><strong>Mantenha a caixa de gordura limpa</strong>, para tirar a gordura da lista de suspeitos. Veja <a href="../limpeza-caixa-de-gordura/">de quanto em quanto tempo limpar</a>.</li>
    </ul>
    <ul class="nao">
      <li>Repetir soda cáustica a cada entupimento: não corrige caimento nem cano amassado e endurece a gordura.</li>
      <li>Forçar arame ou vergalhão num ponto que trava sempre: pode furar o cano que já está fragilizado.</li>
      <li>Refazer a rede inteira sem diagnóstico: muitas vezes o problema é um trecho só.</li>
    </ul>

    <h2>Quando chamar um profissional?</h2>
    <ul>
      <li>O entupimento voltou mais de uma vez no mesmo ano.</li>
      <li>A caixa de inspeção vive com água parada.</li>
      <li>Sai terra ou pedaço de cano no desentupimento.</li>
      <li>Há afundamento no piso, mau cheiro constante ou retorno de água.</li>
    </ul>
    <p>Peça que o técnico diga <strong>onde</strong> estava a obstrução e <strong>o que saiu</strong> do cano. Com essas duas informações, já dá para saber se o próximo passo é manutenção ou correção. Para entender a gravidade, veja <a href="../niveis-de-entupimento/">os 4 níveis de entupimento</a>.</p>''',
    faq=[
        ("Por que o meu esgoto entope sempre no mesmo lugar?", "Normalmente porque ali existe um defeito físico: barriga, trecho sem caimento, emenda mal feita ou cano amassado. A sujeira para sempre nesse ponto. Limpar alivia; corrigir o trecho resolve."),
        ("O que é contrapendente no esgoto?", "É quando o cano sobe em algum trecho antes da saída, em vez de descer. A água fica parada ali e os sólidos assentam, causando entupimentos repetidos."),
        ("Qual a inclinação certa do cano de esgoto?", "A NBR 8160 recomenda declividade mínima de 2% para canos de até 75 mm (2 cm por metro) e de 1% para canos de 100 mm ou mais (1 cm por metro), de forma constante."),
        ("Sonda rotativa resolve cano com barriga?", "Resolve a obstrução na hora, mas não corrige o caimento. Com a barriga no lugar, a sujeira volta a se acumular no mesmo ponto."),
        ("Como saber se o cano está amassado sem quebrar o piso?", "Pela medição de onde a ferramenta trava sempre, pelo que sai do cano (terra, pedaços) e, para confirmar, com inspeção por câmera a partir de uma caixa ou ralo."),
    ],
    fontes=["nbr8160", "icesp_decliv", "ufg_moreira", "ufg_gondim", "ufg_reis", "ufg_bucar", "li_sonda", "campo"],
    leia=["gordura-endurecida-no-cano", "precisa-quebrar-piso-para-desentupir", "niveis-de-entupimento"],
)

for a in (REDE, VASO, PISO, PIA, CAIXA, HIDRO, OLEO, RAIZES, CIMENTO, CAIXA_CEGA, HOSPITAL, GORDURA_PEDRA, RECORRENTE):
    gerar(a)

atualizar_listas()
