# zaznaczyc glowny folder projektu gdzie mieszcza sie wszystkie pliki (zad_5_moduly) - jako Source Code (glowny katalog) - wybieramy folder -> prawy przycisk -> Mark Directory as - Source catalog. Po testach trzeba odznaczyc.
# jest to potrzebne dla PyCharma zeby nie podkreslaw na czerwono wtedy po najechaniu podpowie z jakich sciezek importujemy, a sam - python tego nie potrzebuje, on juz wie skad importowac i nie uwaza to za blad.

from mathematica.algebra.matrices import add_matrices, sub_matrices


def test_add_matrices():
    a = [[1, 2],
         [3, 4]]
    b = [[2, 2],
         [2, 2]]

    expected = [[3, 4],
                [5, 6]]

    assert add_matrices(a, b) == expected


def test_sub_matrices():
    assert sub_matrices() == None
