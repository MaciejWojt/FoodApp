import random
def call_base(name):
    Tab = {
        'spaget.jpg':'\n\n!SPAGHETTI!\ncebula: 1 sztuka\nczosnek: 2 ząbki\nmarchew: 1 sztuka\nolej: 2 łyzki\npuszka pomidorów: 1 sztuka\nprzecier pomidorowy: 3 łyżki\nsuszone oregano: 2 łyżeczki\nsól, pieprz: b/d\nmakaron spaghetti: 300g\ntarty parmezan: b/d',
        'lazania.jpg':'\n\n!LAZANIA!\npomidory: 400g\ncebula: 150g\nmakaron lasagne: b/d\nparmezan: 100g\nmięso m. wołowe: 300g\nwino: 300g\nmarchew: 50g\nseler: b/d\nczosnek: 10g\nmasło: b/d\noregano: 2g',
        'chilli.jpg':'\n\n!CHILLI SIN CARNE!\nczerwona fasola: 2 puszki\npapryki: 3 sztuki\nczerwone cebule: 2 sztuki\nseler naciowy: 2 łodygi\nprzecier pomidorowy: 1/4 szklanki\nm. kumin, o. papryka: 1,5 łyżeczki\nocet b.,s. i w. papryka: 1 łyżeczka\ncynamon, cukier t.: 1/2 łyżeczki\nsos sojowy: 2 łyżki\nolej, sól, pieprz: kilka łyżek\nryż: 1,5 szkl\nwoda: 3 szkl\ncynamon: 2 laski',
        'curry_fis.jpg':'\n\n!CURRY FISTASZKOWE!\nk. imbiru, cynamon, br. cukier: 1/2 łyzeczki\nm. kumin: 2 łyżeczki\nm. pietruszka: 1 łyżeczka\nmasło orzechowe: 1/2 szkl\nbakłazan, puszka pomidorów: 1\nwoda: 1/2 szkl\nolej, sól, pieprz: kilka łyżek\nsok z cytryny: kilka kropel\nmarchew, cebula: 1 szt.\nczosnek, wiórki kokosowe: 2-3\n',
        'gulasz_warz.jpg':'\n\n!GULASZ Z WARZYWAMI!\npomidory: 1kg\npapryka: 2\nbakłażan: 1\nczerw. cebula: 1\nczosnek: 3 ząbki\no. i s. papryka: 1/2 łyżeczki\ncynamon,sól,pieprz,oliwa: 1/4 łyżeczki\ntofu: 2 kostki\npasta paprykowa wędzona,czosnek: b/d\nmasło orzechowe: 1 łyżka\no. i w. papryka,bazylia,oregano: 1/2 łyżeczki\npulpety: str.237',
        'pierogi_socz.jpg':'\n\n!PIEROGI Z SOCZEWICĄ!\nzielona soczewica: 200g\ncebula: 1\nczosnek: 1 ząbek\nziele angielskie: 2 ziarna\nliście laurowe: 2\ncukier t., majeranek, lubczyk: 1/2 łyżeczki\nmielona kolendra: 1/4 łyżeczki\nsos soj.,sól,olej,pieprz: 2 łyżki\nmąka pszenna: 3 szkl\ngorąca woda: 1 szkl\nolej,sól: 2 łyżki',
        'smaz_soczewica.jpg':'\n\n!SMAŻONA SOCZEWICA!\nczer. soczewica: 1/2 szkl\nkrojone pomidory: 1 puszka\nczerw. cebula: 1\nczosnek: 1 ząbek\ns. i w. papryka: 1/2 łyżeczki\nchili, cynamon: 1/4 łyżeczki\nwoda: 2-3 szkl\noliwa, sól, pieprz: 3 łyżki',
        'zupa_pom.jpg':'\n\n!ZUPA POMIDOROWA!\nryż: 1/2 szkl\nwoda: 1 szkl\nsól: szczypta\npomidory: 1kg\ncebula,marchew: 1\nchili: 5cm\nczosnek: 1 ząbek\nolej: 3 łyżki\nbulion warzywny: 1-2 szkl\nmleko kokosowe: mała puszka\nbr. cukier, sól, pieprz: 1/2 łyżeczki',
        'spaghetti_cukinia.jpg':'\n\n!!SPAGHETTI Z CUKINI!\ncukinie: 2 szt.\nsusz. pomidory: 3/4 szklanki\npraż. pestki dyni: 1/4 szklanki\nsyrop z agawy: 1/4 łyżeczki\noliwa z p. tł.: 1/2 łyżeczki\nchili,sól,pieprz: 1/4 łyżeczki',
        'makaron_n_d.jpg':'\n\n!MAKARON NIEGRZECZNEJ DZIEWCZNY!\nmakaron spaghetti: 400g\nkrojone pomidory: 1 puszka\nwypestkowane papryczki chilli: 4 cm\nczosnek: 2 ząbki\nkapary: 1=2 łyźeczki\noliwa: kilka łyźek\nsól,pieprz: szczypta',
        'spaghetti_pulpety.jpg':'\n\n!SPAGHETTI Z PULPETAMI!\nmakaron spaghetti: 400g\npomidory: 2 puszki\ncebula: 1 szt.\nczosnek: 2 ząbki\nocet balsam.: 1 łyżka\noregano,tymianek: 1/4 łyżeczki',
        'grochówka.jpg':'\n\n!GROCHÓWKA!\ngroch mocz. 1godz.: 2 szklanki\nziemniaki: 2\nmarchewka,cebula: 1\nseler: 1/4\nczosnek: 2 ząbki\nziele ang.: 4 ziarna\nliście laurowe: 4\nmajeranek: 1 łyżka\nw. papryka: 1 łyżeczka\nlubczyk,miel. kolendra: 1/2 łyżeczki\nsos sojowy: 2 łyżki\nolej,sól,pieprz: 4 łyżki'
    }
    return Tab[name]

def call_keys():
    Tab = [
        'spaget.jpg',
        'lazania.jpg',
        'chilli.jpg',
        'curry_fis.jpg',
        'gulasz_warz.jpg',
        'pierogi_socz.jpg',
        'smaz_soczewica.jpg',
        'zupa_pom.jpg',
        'spaghetti_cukinia.jpg',
        'makaron_n_d.jpg',
        'spaghetti_pulpety.jpg',
        'grochówka.jpg'
    ]
    return Tab

