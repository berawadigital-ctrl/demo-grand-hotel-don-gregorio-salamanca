# Contenido de la demo Grand Hotel Don Gregorio (Salamanca) (es/ca/en/fr). Hechos de hoteldongregorio.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble Deluxe','Doble Deluxe Superior','Suite'],
'ca':['Doble Deluxe','Doble Deluxe Superior','Suite'],
'en':['Double Deluxe','Double Deluxe Superior','Suite'],
'fr':['Double Deluxe','Double Deluxe Supérieure','Suite']}
RD={
'es':['Habitaciones de 23 m² con suelo de roble, baño con bañera de hidromasaje o ducha de lluvia y cafetera Nespresso.','Habitaciones de 33 m², superiores por su tamaño o por sus vistas al Convento de San Esteban o a la Torre del Marqués de Villena.','Habitaciones de 54 m² con zona de estar, cama king size, bañera de hidromasaje para dos y ducha de lluvia.'],
'ca':['Habitacions de 23 m² amb sòl de roure, bany amb banyera d\'hidromassatge o dutxa de pluja i cafetera Nespresso.','Habitacions de 33 m², superiors per la seva mida o per les vistes al Convent de Sant Esteve o a la Torre del Marquès de Villena.','Habitacions de 54 m² amb zona d\'estar, llit king size, banyera d\'hidromassatge per a dos i dutxa de pluja.'],
'en':['23 m² rooms with oak floors, a bathroom with a hydromassage bathtub or rain shower, and a Nespresso machine.','33 m² rooms, superior thanks to their size or their views of the Convento de San Esteban or the Torre del Marqués de Villena.','54 m² rooms with a living area, king-size bed, hydromassage bathtub for two and rain shower.'],
'fr':['Chambres de 23 m² avec parquet de chêne, salle de bain avec baignoire d\'hydromassage ou douche à effet pluie et machine Nespresso.','Chambres de 33 m², supérieures par leur taille ou leur vue sur le Convento de San Esteban ou la Torre del Marqués de Villena.','Chambres de 54 m² avec coin salon, lit king size, baignoire d\'hydromassage pour deux et douche à effet pluie.']}
ART={
'hero':('arches',9401,['#f1e2c4','#dfc08a','#b8893a','#7a5a38','#5a3d28']),
'intro':('columns',9402,['#eee0c6','#f5e9d2','#b8893a','#8c6a47','#5a3d28']),
'r1':('arches',9411,['#f0e0c2','#ddbd88','#b3843a','#76563a','#573b27']),
'r2':('columns',9412,['#ecdfc4','#f3e7cf','#be8f3d','#8a6a48','#5d4029']),
'r3':('skyline',9413,['#40384f','#e58d58','#f8cf93','#3f374d','#2e2839','#1e1a26']),
'g1':('arches',9421,['#f2e3c6','#dfc28e','#b98b3c','#7a5a3a','#5a3d28']),
'g2':('hills',9422,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g3':('skyline',9423,['#3a4a68','#e8935f','#fbd9a0','#394967','#2a3955','#1b2536']),
'g4':('columns',9424,['#eee1c8','#f5e9d3','#bb8c3a','#8d6c49','#58402a']),
'g5':('waves',9425,['#f3e0b4','#e8a374','#fff0c6','#7cb4c4','#4a8ba3','#2f6a83','#1d475d']),
'g6':('skyline',9426,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Grand Hotel Don Gregorio · Hotel con spa y restaurante en un palacio del siglo XV, Salamanca',see_rooms='Ver habitaciones',hero_k='Salamanca · Centro histórico',hero_t='Lujo e historia en un antiguo palacio',hero_s='Un hotel con encanto en el corazón de Salamanca, en un palacio del siglo XV.',
 intro_t='Un palacio del siglo XV en pleno centro histórico',intro_p1='Grand Hotel Don Gregorio ocupa un antiguo palacio del siglo XV en la calle San Pablo 80-82, con 14 habitaciones decoradas de manera personalizada.',
 intro_p2='Tiene spa, restaurante Ment, wifi gratuito en todo el edificio y accesos adaptados para personas con movilidad reducida. Para reservar, contacta con el hotel por teléfono o correo.',
 stats=['14 habitaciones','Spa','Restaurante Ment','Wifi gratuito'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de las categorías de habitación del hotel.',
 svcs=['Spa','Restaurante','Recepción 24 horas','Wifi gratuito','Servicio de habitaciones','Accesos adaptados','Consigna de equipajes','Traslado al aeropuerto bajo petición'],
 loc_p='Calle San Pablo 80-82, 37008 Salamanca, en pleno centro histórico.',
 chips=['¿Cuántas habitaciones tiene?','¿Hay spa?','¿Hay restaurante?','¿Cómo se reserva?']),
'ca':dict(title='Grand Hotel Don Gregorio · Hotel amb spa i restaurant en un palau del segle XV, Salamanca',see_rooms='Veure habitacions',hero_k='Salamanca · Centre històric',hero_t='Luxe i història en un antic palau',hero_s='Un hotel amb encant al cor de Salamanca, en un palau del segle XV.',
 intro_t='Un palau del segle XV en ple centre històric',intro_p1='Grand Hotel Don Gregorio ocupa un antic palau del segle XV al carrer San Pablo 80-82, amb 14 habitacions decorades de manera personalitzada.',
 intro_p2='Té spa, restaurant Ment, wifi gratuït a tot l\'edifici i accessos adaptats per a persones amb mobilitat reduïda. Per reservar, contacta amb l\'hotel per telèfon o correu.',
 stats=['14 habitacions','Spa','Restaurant Ment','Wifi gratuït'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres de les categories d\'habitació de l\'hotel.',
 svcs=['Spa','Restaurant','Recepció 24 hores','Wifi gratuït','Servei d\'habitacions','Accessos adaptats','Consigna d\'equipatges','Trasllat a l\'aeroport sota petició'],
 loc_p='Carrer San Pablo 80-82, 37008 Salamanca, en ple centre històric.',
 chips=['Quantes habitacions té?','Hi ha spa?','Hi ha restaurant?','Com es reserva?']),
'en':dict(title='Grand Hotel Don Gregorio · Hotel with spa and restaurant in a 15th-century palace, Salamanca',see_rooms='See the rooms',hero_k='Salamanca · Historic centre',hero_t='Luxury and history in a former palace',hero_s='A charming hotel in the heart of Salamanca, in a 15th-century palace.',
 intro_t='A 15th-century palace in the historic centre',intro_p1='Grand Hotel Don Gregorio occupies a former 15th-century palace on Calle San Pablo 80-82, with 14 individually decorated rooms.',
 intro_p2='It has a spa, the Ment restaurant, free wifi throughout the building and adapted access for people with reduced mobility. To book, contact the hotel by phone or email.',
 stats=['14 rooms','Spa','Ment restaurant','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s room categories.',
 svcs=['Spa','Restaurant','24-hour reception','Free wifi','Room service','Adapted access','Luggage storage','Airport transfer on request'],
 loc_p='Calle San Pablo 80-82, 37008 Salamanca, in the historic centre.',
 chips=['How many rooms does it have?','Is there a spa?','Is there a restaurant?','How do I book?']),
'fr':dict(title='Grand Hotel Don Gregorio · Hôtel avec spa et restaurant dans un palais du XVe siècle, Salamanque',see_rooms='Voir les chambres',hero_k='Salamanque · Centre historique',hero_t='Luxe et histoire dans un ancien palais',hero_s='Un hôtel de charme au cœur de Salamanque, dans un palais du XVe siècle.',
 intro_t='Un palais du XVe siècle en plein centre historique',intro_p1='Le Grand Hotel Don Gregorio occupe un ancien palais du XVe siècle calle San Pablo 80-82, avec 14 chambres décorées de manière personnalisée.',
 intro_p2='Il dispose d\'un spa, du restaurant Ment, du wifi gratuit dans tout le bâtiment et d\'accès adaptés aux personnes à mobilité réduite. Pour réserver, contactez l\'hôtel par téléphone ou e-mail.',
 stats=['14 chambres','Spa','Restaurant Ment','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des catégories de chambre de l\'hôtel.',
 svcs=['Spa','Restaurant','Réception 24 heures','Wifi gratuit','Service en chambre','Accès adaptés','Consigne à bagages','Transfert aéroport sur demande'],
 loc_p='Calle San Pablo 80-82, 37008 Salamanque, en plein centre historique.',
 chips=['Combien de chambres a-t-il ?','Y a-t-il un spa ?','Y a-t-il un restaurant ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='info@hoteldongregorio.com')
D=dict(name='Grand Hotel Don Gregorio',ac='#5a3d28',ac2='#b8893a',ac2_a11y='#6f4a10',book=BOOK,around=[],foot=FOOT,
 address='Calle San Pablo 80-82 · 37008 Salamanca',phones=['923 217 015'],emails=['info@hoteldongregorio.com'],maps='Grand Hotel Don Gregorio, Calle San Pablo 80-82, Salamanca',t=T)
META=dict(repo='demo-grand-hotel-don-gregorio-salamanca',name='Grand Hotel Don Gregorio',legal_name='Protel San Pablo S.L.U.',registry_ids=['CIF B83919092'],
 url='https://www.hoteldongregorio.com/',domain='hoteldongregorio.com',municipality='Salamanca',province='Salamanca',sector='hotel con spa y restaurante en palacio del siglo XV',
 read_at='2026-10-29T04:57:00+01:00',created_at='2026-10-29T04:58:00+01:00',built_at='2026-10-29T05:00:00+01:00',audit_date='2026-10-29T04:58:00+01:00',
 rating=dict(value=4.7,coincide=['telefono','web'],date='2026-10-29T04:54:23+01:00',url='https://www.google.com/maps/place/Grand+Hotel+Don+Gregorio/@40.9603789,-5.6643255,17z/data=!4m9!3m8!1s0xd3f266ad78a0da7:0x73b7645be24b4cc0!5m2!4m1!1i2!8m2!3d40.9603789!4d-5.6643255!16s%2Fg%2F1tx16nf2'),
 book=dict(mode='mail',email='info@hoteldongregorio.com',note='La web del negocio pide contactar por telefono o correo para reservas en sus ofertas y tiene su propio motor; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel con precedente en demos de esta tanda')
QS={
'es':[('¿Cuántas habitaciones tiene?','K01'),('¿Hay minibar y cafetera?','K02'),('¿Hay spa?','K03'),('¿Tiene restaurante?','K04'),('¿Hay desayuno?','K05'),('¿Hay wifi?','K06'),('¿Es accesible?','K07'),('¿Hay parking?','K08'),('¿Dónde está el hotel?','K09'),('¿Qué historia tiene el palacio?','K10'),('¿Cómo reservo?','K11'),('¿Cuál es el teléfono?','K12'),('¿Quién es el titular?','K13'),('¿Admiten mascotas?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K11')],
'ca':[('Quantes habitacions té?','K01'),('Hi ha minibar i cafetera?','K02'),('Hi ha spa?','K03'),('Té restaurant?','K04'),('Hi ha esmorzar?','K05'),('Hi ha wifi?','K06'),('És accessible?','K07'),('Hi ha pàrquing?','K08'),('On és l\'hotel?','K09'),('Quina història té el palau?','K10'),('Com reservo?','K11'),('Quin és el telèfon?','K12'),('Qui és el titular?','K13'),('Admeteu mascotes?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K11')],
'en':[('How many rooms does it have?','K01'),('Is there a minibar and coffee machine?','K02'),('Is there a spa?','K03'),('Does it have a restaurant?','K04'),('Is there breakfast?','K05'),('Is there wifi?','K06'),('Is it accessible?','K07'),('Is there parking?','K08'),('Where is the hotel?','K09'),('What history does the palace have?','K10'),('How do I book?','K11'),('What is the phone number?','K12'),('Who is the owner?','K13'),('Are pets allowed?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K11')],
'fr':[('Combien de chambres a-t-il ?','K01'),('Y a-t-il un minibar et une cafetière ?','K02'),('Y a-t-il un spa ?','K03'),('A-t-il un restaurant ?','K04'),('Y a-t-il un petit-déjeuner ?','K05'),('Y a-t-il du wifi ?','K06'),('Est-il accessible ?','K07'),('Y a-t-il un parking ?','K08'),('Où est l\'hôtel ?','K09'),('Quelle histoire a le palais ?','K10'),('Comment réserver ?','K11'),('Quel est le téléphone ?','K12'),('Qui est le titulaire ?','K13'),('Les animaux sont-ils admis ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K11')]}
