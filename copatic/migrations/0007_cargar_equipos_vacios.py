# Generated by Django 2.0.5 on 2018-05-29 16:19

from django.db import migrations
from copatic.models.escuela import Escuela
from copatic.models.equipo import Equipo

def cargar_equipos(apps, schema_editor):
    lista_de_equipos = [
        ("60623100","a01","Escuela Secundaria Nº32","La Plata"),
        ("60626100","a02","Escuela Media Nº28","La Plata"),
        ("60882100","a03","Escuela Secundaria Nº34","La Plata"),
        ("60884600","a04","Escuela Secundaria Nº27","La Plata"),
        ("60897700","a05","Escuela Secundaria Nº31","La Plata"),
        ("61771300","a06","Escuela Secundaria Nº44","La Plata"),
        ("61772900","a07","Escuela Secundaria  Nº 67","La Plata"),
        ("61858900","a08","Escuela Secundaria Nº62","La Plata"),
        ("61898000","a09","Escuela Secundaria Nº56","La Plata"),
        ("61097100","a10","Escuela Secundaria Nº18","Avellaneda"),
        ("60766200","a11","Escuela Secundaria Nº11","Lanús"),
        ("61039900","a12","Escuela Secundaria Nº1","La Matanza"),
        ("60917100","a13","Escuela Secundaria Nº6","Esteban Echeverria"),
        ("60765300","a14","Escuela Secundaria Nº2","San Fernando"),
        ("61724200","a15","Escuela Secundaria Nº12","San Fernando"),
        ("61757000","a16","Escuela Secundaria Nº13","San Fernando"),
        ("61894500","a17","Escuela Secundaria Nº14","San Fernando"),
        ("61894700","a18","Escuela Secundaria Nº23","San Fernando"),
        ("61897200","a19","Escuela Secundaria Nº24","San Fernando"),
        ("61982200","a20","Escuela Secundaria Basica Nº14","San Fernando"),
        ("61212500","a21","Escuela Secundaria Nº4","San Isidro"),
        ("61212600","a22","Escuela Secundaria Nº14","San Isidro"),
        ("61227100","a23","Escuela Secundaria Nº2","San Isidro"),
        ("61228200","a24","Escuela Secundaria Nº7","San Isidro"),
        ("61230400","a25","Escuela Secundaria Nº9","San Isidro"),
        ("60781900","a26","Escuela Secundaria Nº7","Tigre"),
        ("61097300","a27","Escuela Técnica Nº1","Tigre"),
        ("61829200","a28","Escuela Secundaria Nº19","Tigre"),
        ("61829400","a29","Escuela Secundaria Basica Nº26","Tigre"),
        ("61901000","a30","Escuela Secundaria Basica Nº2","Tigre"),
        ("62040100","a31","Escuela Secundaria Nº9","Tigre"),
        ("60750700","a32","Escuela Secundaria Nº4","Vicente López"),
        ("60789500","a33","Escuela Secundaria Nº3","Vicente López"),
        ("60045200","a34","Escuela Secundaria Nº22","General San Martín"),
        ("60746900","a35","Escuela Secundaria Nº1","General San Martín"),
        ("60747000","a36","Escuela Técnica Nº3","General San Martín"),
        ("61155400","a37","Escuela Técnica Nº4","General San Martín"),
        ("61793900","a38","Secundaria Basica Nº17 (EES 46)","General San Martín"),
        ("60554600","a39","Escuela Secundaria Nº2","Hurlingham"),
        ("60927800","a40","Escuela Técnica Nº2","Hurlingham"),
        ("61759600","a41","Escuela Secundaria Basica Nº3","Hurlingham"),
        ("61818600","a42","Escuela Secundaria Nº7","Hurlingham"),
        ("61896400","a43","Escuela Secundaria Nº19","Tres de Febrero"),
        ("61181600","a44","Escuela Secundaria Nº7","Merlo"),
        ("61799400","a45","Escuela Secundaria Nº43","Merlo"),
        ("61743000","a46","Escuela Secundaria Basica Nº3","Malvinas Argentinas"),
        ("61889900","a47","Escuela Secundaria Basica Nº19","San Miguel"),
        ("61763900","a48","Escuela Secundaria Nº15","Escobar"),
        ("62026800","a49","Escuela Secundaria Nº13","Escobar"),
        ("61980600","a50","Escuela Secundaria Basica Nº18","Pilar"),
        ("60775400","a51","Escuela Secundaria Nº4","Rojas"),
        ("61886101","a52","Anexo Escuela Secundaria Nº7","Chacabuco"),
        ("61970200","a53","Escuela Secundaria Nº6","Bragado"),
        ("61062000","a54","Escuela Secundaria Nº5","Pehuajó"),
        ("61197100","a55","Escuela Técnica Nº1","Pinamar"),
        ("60714200","a56","Escuela Secundaria Nº3","Bahía Blanca"),
        ("61884100","a57","Escuela Secundaria Nº24","Bahía Blanca"),
        ("62291300","a58","Escuela Secundaria Técnica 1","Monte Hermoso"),
        ("61891700","a59","Escuela Secundaria Nº 3","Las Flores"),
        ("61794900","a60","Escuela Secundaria Nº2","Lobos"),
        ("61813600","a61","Escuela Secundaria Nº5","Lobos"),
        ("61863600","a62","Escuela Secundaria N°33","Florencio Varela"),
        ("62042800","a63","Escuela Secundaria N°20","Luján"),
        ("60738700","a64","Escuela Secundaria Técnica N°4","San Nicolás"),
        ("61986000","a65","Escuela Secundaria N°2","Salliqueló"),
        ("62241800","a66","Escuela Secundaria N°4","General Paz"),
        ("61742200","a67","Escuela Secundaria N°61","General Pueyrredón"),
        ("60677000","a68","Escuela Secundaria N°1","Necochea"),
        ("60597900","a69","Escuela Secundaria N°2","Tres Arroyos"),
        ("62047500","a70","Escuela Secundaria N°2","Carhué"),
        ("62249500","a71","Escuela Secundaria N°13","Olavarría"),
        ("60623100","b01","Escuela Secundaria Nº32","La Plata"),
        ("60626100","b02","Escuela Media Nº28","La Plata"),
        ("60882100","b03","Escuela Secundaria Nº34","La Plata"),
        ("60884600","b04","Escuela Secundaria Nº27","La Plata"),
        ("60897700","b05","Escuela Secundaria Nº31","La Plata"),
        ("61771300","b06","Escuela Secundaria Nº44","La Plata"),
        ("61772900","b07","Escuela Secundaria  Nº 67","La Plata"),
        ("61858900","b08","Escuela Secundaria Nº62","La Plata"),
        ("61898000","b09","Escuela Secundaria Nº56","La Plata"),
        ("61097100","b10","Escuela Secundaria Nº18","Avellaneda"),
        ("60766200","b11","Escuela Secundaria Nº11","Lanús"),
        ("61039900","b12","Escuela Secundaria Nº1","La Matanza"),
        ("60917100","b13","Escuela Secundaria Nº6","Esteban Echeverria"),
        ("60765300","b14","Escuela Secundaria Nº2","San Fernando"),
        ("61724200","b15","Escuela Secundaria Nº12","San Fernando"),
        ("61757000","b16","Escuela Secundaria Nº13","San Fernando"),
        ("61894500","b17","Escuela Secundaria Nº14","San Fernando"),
        ("61894700","b18","Escuela Secundaria Nº23","San Fernando"),
        ("61897200","b19","Escuela Secundaria Nº24","San Fernando"),
        ("61982200","b20","Escuela Secundaria Basica Nº14","San Fernando"),
        ("61212500","b21","Escuela Secundaria Nº4","San Isidro"),
        ("61212600","b22","Escuela Secundaria Nº14","San Isidro"),
        ("61227100","b23","Escuela Secundaria Nº2","San Isidro"),
        ("61228200","b24","Escuela Secundaria Nº7","San Isidro"),
        ("61230400","b25","Escuela Secundaria Nº9","San Isidro"),
        ("60781900","b26","Escuela Secundaria Nº7","Tigre"),
        ("61097300","b27","Escuela Técnica Nº1","Tigre"),
        ("61829200","b28","Escuela Secundaria Nº19","Tigre"),
        ("61829400","b29","Escuela Secundaria Basica Nº26","Tigre"),
        ("61901000","b30","Escuela Secundaria Basica Nº2","Tigre"),
        ("62040100","b31","Escuela Secundaria Nº9","Tigre"),
        ("60750700","b32","Escuela Secundaria Nº4","Vicente López"),
        ("60789500","b33","Escuela Secundaria Nº3","Vicente López"),
        ("60045200","b34","Escuela Secundaria Nº22","General San Martín"),
        ("60746900","b35","Escuela Secundaria Nº1","General San Martín"),
        ("60747000","b36","Escuela Técnica Nº3","General San Martín"),
        ("61155400","b37","Escuela Técnica Nº4","General San Martín"),
        ("61793900","b38","Secundaria Basica Nº17 (EES 46)","General San Martín"),
        ("60554600","b39","Escuela Secundaria Nº2","Hurlingham"),
        ("60927800","b40","Escuela Técnica Nº2","Hurlingham"),
        ("61759600","b41","Escuela Secundaria Basica Nº3","Hurlingham"),
        ("61818600","b42","Escuela Secundaria Nº7","Hurlingham"),
        ("61896400","b43","Escuela Secundaria Nº19","Tres de Febrero"),
        ("61181600","b44","Escuela Secundaria Nº7","Merlo"),
        ("61799400","b45","Escuela Secundaria Nº43","Merlo"),
        ("61743000","b46","Escuela Secundaria Basica Nº3","Malvinas Argentinas"),
        ("61889900","b47","Escuela Secundaria Basica Nº19","San Miguel"),
        ("61763900","b48","Escuela Secundaria Nº15","Escobar"),
        ("62026800","b49","Escuela Secundaria Nº13","Escobar"),
        ("61980600","b50","Escuela Secundaria Basica Nº18","Pilar"),
        ("60775400","b51","Escuela Secundaria Nº4","Rojas"),
        ("61886101","b52","Anexo Escuela Secundaria Nº7","Chacabuco"),
        ("61970200","b53","Escuela Secundaria Nº6","Bragado"),
        ("61062000","b54","Escuela Secundaria Nº5","Pehuajó"),
        ("61197100","b55","Escuela Técnica Nº1","Pinamar"),
        ("60714200","b56","Escuela Secundaria Nº3","Bahía Blanca"),
        ("61884100","b57","Escuela Secundaria Nº24","Bahía Blanca"),
        ("62291300","b58","Escuela Secundaria Técnica 1","Monte Hermoso"),
        ("61891700","b59","Escuela Secundaria Nº 3","Las Flores"),
        ("61794900","b60","Escuela Secundaria Nº2","Lobos"),
        ("61813600","b61","Escuela Secundaria Nº5","Lobos"),
        ("61863600","b62","Escuela Secundaria N°33","Florencio Varela"),
        ("62042800","b63","Escuela Secundaria N°20","Luján"),
        ("60738700","b64","Escuela Secundaria Técnica N°4","San Nicolás"),
        ("61986000","b65","Escuela Secundaria N°2","Salliqueló"),
        ("62241800","b66","Escuela Secundaria N°4","General Paz"),
        ("61742200","b67","Escuela Secundaria N°61","General Pueyrredón"),
        ("60677000","b68","Escuela Secundaria N°1","Necochea"),
        ("60597900","b69","Escuela Secundaria N°2","Tres Arroyos"),
        ("62047500","b70","Escuela Secundaria N°2","Carhué"),
        ("62249500","b71","Escuela Secundaria N°13","Olavarría"),
    ]
    for equipo in lista_de_equipos:
        print("escuela a buscar (CUE):" + equipo[0])
        escuela = Escuela.objects.get(cue=equipo[0])
        print(escuela)
        Equipo.objects.create(eid=equipo[1], escuela=escuela)

class Migration(migrations.Migration):

    dependencies = [
        ('copatic', '0006_auto_20180524_1851'),
    ]

    operations = [
        migrations.RunPython(cargar_equipos, migrations.RunPython.noop),
    ]