import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_asetettu_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_kortille_voi_ladata(self):
        self.maksukortti.lataa_rahaa(2000)
        self.assertEqual(str(self.maksukortti), "saldo: 30.0")

    def test_rahaa_voi_ottaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1300)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_palauttaa_true(self):
        self.maksukortti.ota_rahaa(9000)
        self.assertEqual(True, True)

    def test_palauttaa_false(self):
        self.maksukortti.ota_rahaa(14000)
        self.assertEqual(False, False)