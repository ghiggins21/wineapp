# Generated by Django 3.0 on 2021-07-04 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wineapp', '0004_auto_20210704_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='bottle',
            field=models.CharField(choices=[('', 'Bottle Size'), ('Split (187ml)', 'Split (187ml)'), ('Quarter (200ml)', 'Quarter (200ml)'), ('Half (375ml)', 'Half (375ml)'), ('Jennie (500ml)', 'Jennie (500ml)'), ('Clavelin (620ml)', 'Clavelin (620ml)'), ('Standard (750ml)', 'Standard (750ml)'), ('Litre (1L)', 'Litre (1L)'), ('Magnum (1.5L)', 'Magnum (1.5L)'), ('Jeroboam (3L)', 'Jeroboam (3L)'), ('Rehoboam (4.5L)', 'Rehoboam (4.5L)'), ('Methuselah (6L)', 'Methuselah (6L)'), ('Imperial (6L)', 'Imperial (6L)'), ('Salmanazar (9L)', 'Salmanazar (9L)'), ('Balthazar (12L)', 'Balthazar (12L)'), ('Nebuchadnezzar (15L)', 'Nebuchadnezzar (15L)'), ('Melchior (18L)', 'Melchior (18L)'), ('Solomon (20L)', 'Solomon (20L)'), ('Sovereign (26L)', 'Sovereign (26L)'), ('Goliath (27L)', 'Goliath (27L)'), ('Melchizedek (30L)', 'Melchizedek (30L)')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='country',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='wineapp.Country'),
        ),
        migrations.AlterField(
            model_name='wine',
            name='vintage',
            field=models.CharField(choices=[('', 'Vintage'), ('Unknown', 'Unknown'), ('NV', 'NV'), ('MV', 'MV'), ('Solera System', 'Solera System'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014'), ('2013', '2013'), ('2012', '2012'), ('2011', '2011'), ('2010', '2010'), ('2009', '2009'), ('2008', '2008'), ('2007', '2007'), ('2006', '2006'), ('2005', '2005'), ('2004', '2004'), ('2003', '2003'), ('2002', '2002'), ('2001', '2001'), ('2000', '2000'), ('1999', '1999'), ('1998', '1998'), ('1997', '1997'), ('1996', '1996'), ('1995', '1995'), ('1994', '1994'), ('1993', '1993'), ('1992', '1992'), ('1991', '1991'), ('1990', '1990'), ('1989', '1989'), ('1988', '1988'), ('1987', '1987'), ('1986', '1986'), ('1985', '1985'), ('1984', '1984'), ('1983', '1983'), ('1982', '1982'), ('1981', '1981'), ('1980', '1980'), ('1979', '1979'), ('1978', '1978'), ('1977', '1977'), ('1976', '1976'), ('1975', '1975'), ('1974', '1974'), ('1973', '1973'), ('1972', '1972'), ('1971', '1971'), ('1970', '1970'), ('1969', '1969'), ('1968', '1968'), ('1967', '1967'), ('1966', '1966'), ('1965', '1965'), ('1964', '1964'), ('1963', '1963'), ('1962', '1962'), ('1961', '1961'), ('1960', '1960'), ('1959', '1959'), ('1958', '1958'), ('1957', '1957'), ('1956', '1956'), ('1955', '1955'), ('1954', '1954'), ('1953', '1953'), ('1952', '1952'), ('1951', '1951'), ('1950', '1950'), ('1949', '1949'), ('1948', '1948'), ('1947', '1947'), ('1946', '1946'), ('1945', '1945'), ('1944', '1944'), ('1943', '1943'), ('1942', '1942'), ('1941', '1941'), ('1940', '1940'), ('1939', '1939'), ('1938', '1938'), ('1937', '1937'), ('1936', '1936'), ('1935', '1935'), ('1934', '1934'), ('1933', '1933'), ('1932', '1932'), ('1931', '1931'), ('1930', '1930'), ('1929', '1929'), ('1928', '1928'), ('1927', '1927'), ('1926', '1926'), ('1925', '1925'), ('1924', '1924'), ('1923', '1923'), ('1922', '1922'), ('1921', '1921'), ('1920', '1920'), ('1919', '1919'), ('1918', '1918'), ('1917', '1917'), ('1916', '1916'), ('1915', '1915'), ('1914', '1914'), ('1913', '1913'), ('1912', '1912'), ('1911', '1911'), ('1910', '1910'), ('1909', '1909'), ('1908', '1908'), ('1907', '1907'), ('1906', '1906'), ('1905', '1905'), ('1904', '1904'), ('1903', '1903'), ('1902', '1902'), ('1901', '1901'), ('1900', '1900'), ('1899', '1899'), ('1898', '1898'), ('1897', '1897'), ('1896', '1896'), ('1895', '1895'), ('1894', '1894'), ('1893', '1893'), ('1892', '1892'), ('1891', '1891'), ('1890', '1890'), ('1889', '1889'), ('1888', '1888'), ('1887', '1887'), ('1886', '1886'), ('1885', '1885'), ('1884', '1884'), ('1883', '1883'), ('1882', '1882'), ('1881', '1881'), ('1880', '1880'), ('1879', '1879'), ('1878', '1878'), ('1877', '1877'), ('1876', '1876'), ('1875', '1875')], max_length=20),
        ),
    ]
