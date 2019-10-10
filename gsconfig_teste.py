from geoserver.catalog import Catalog
# Conexao com o geoserver
cat = Catalog("http://localhost:8082/geoserver/rest", username="admin", password="geoserver")

# Criando um workspace
#ws = cat.create_workspace('gsc_test','http://localhost:8082/geoserver/testWs')

# Criando um store
ds = cat.create_datastore('bdg_gsc','gsc_test')
#ds.connection_parameters.update(host='localhost', port='5432', database='bdg_gsc', user='user', passwd='user', dbtype='postgis', schema='public')
#cat.save(ds)

# Adicionando layers
#ft = cat.publish_featuretype('mun_pr', ds, 'EPSG:4674', srs='EPSG:4674')
#ft1 = cat.publish_featuretype('escolas_pr', ds, 'EPSG:4674', srs='EPSG:4674')

# Adicionando styles - nao adiciona sld completo
#with open("/home/user/gsc_style.sld") as f:
#   cat.create_style('gsc_style', f.read())

# Atribuindo o estilo a camada
# SLD adicionado no geoserver
style1 = cat.get_style("gsc_test:gsc_style_mun")
layer1 = cat.get_layer("mun_pr")
layer1.default_style = style1
cat.save(layer1)

style2 = cat.get_style("gsc_test:gsc_style_esc")
layer2 = cat.get_layer("escolas_pr")
layer2.default_style = style2
cat.save(layer2)






