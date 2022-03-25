import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_rahamaara_ja_lounaiden_maara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullinen_tasaraha(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_toimii_edullinen_ei_tasaraha(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_toimii_edullinen_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(150)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_toimii_maukas_tasaraha(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_toimii_maukas_ei_tasaraha(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_toimii_maukas_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_toimii_edullinen_raha_riittaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(True, True)
        self.assertEqual(kortti.saldo, 760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_edullinen_raha_ei_riita(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(False, False)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_maukas_raha_riittaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(True, True)
        self.assertEqual(kortti.saldo, 600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_maukas_raha_ei_riita(self):
        kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(False, False)
        self.assertEqual(kortti.saldo, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladataan_rahaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(kortti.saldo, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_ladataan_negatiivinen_summa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -10)
        self.assertEqual(kortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

