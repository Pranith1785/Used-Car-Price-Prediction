def car_model_selection(selected_CarModel):

    carModellist = [0] * 98

    car_model_dict = {'Car_Name_800': 0 ,'Car_Name_Activa 3g': 1 ,'Car_Name_Activa 4g': 2 ,'Car_Name_Bajaj  ct 100': 3 ,'Car_Name_Bajaj Avenger 150': 4 ,'Car_Name_Bajaj Avenger 150 street': 5 ,'Car_Name_Bajaj Avenger 220': 6 ,'Car_Name_Bajaj Avenger 220 dtsi': 7 ,'Car_Name_Bajaj Avenger Street 220': 8 ,'Car_Name_Bajaj Discover 100': 9 ,'Car_Name_Bajaj Discover 125': 10 ,
                     'Car_Name_Bajaj Dominar 400': 11 ,'Car_Name_Bajaj Pulsar  NS 200': 12 ,'Car_Name_Bajaj Pulsar 135 LS': 13,'Car_Name_Bajaj Pulsar 150': 14 ,'Car_Name_Bajaj Pulsar 220 F': 15 ,'Car_Name_Bajaj Pulsar NS 200': 16 ,'Car_Name_Bajaj Pulsar RS200': 17 ,'Car_Name_Hero  CBZ Xtreme': 18 ,'Car_Name_Hero  Ignitor Disc': 19 ,'Car_Name_Hero Extreme': 20 ,
                     'Car_Name_Hero Glamour': 21 ,'Car_Name_Hero Honda CBZ extreme': 22 ,'Car_Name_Hero Honda Passion Pro': 23 ,'Car_Name_Hero Hunk': 24,'Car_Name_Hero Passion Pro': 25 ,'Car_Name_Hero Passion X pro': 26 ,'Car_Name_Hero Splender Plus': 27 ,'Car_Name_Hero Splender iSmart': 28 ,'Car_Name_Hero Super Splendor': 29,'Car_Name_Honda Activa 125': 30 ,
                     'Car_Name_Honda Activa 4G': 31 ,'Car_Name_Honda CB Hornet 160R': 32 ,'Car_Name_Honda CB Shine': 33 ,'Car_Name_Honda CB Trigger': 34 ,'Car_Name_Honda CB Unicorn': 35 ,'Car_Name_Honda CB twister': 36 ,'Car_Name_Honda CBR 150': 37 ,'Car_Name_Honda Dream Yuga ': 38 , 'Car_Name_Honda Karizma': 39 ,'Car_Name_Hyosung GT250R': 40 ,
                     'Car_Name_KTM 390 Duke ': 41 , 'Car_Name_KTM RC200': 42 ,'Car_Name_KTM RC390': 43 ,'Car_Name_Mahindra Mojo XT300': 44 ,'Car_Name_Royal Enfield Bullet 350': 45 ,'Car_Name_Royal Enfield Classic 350': 46 ,'Car_Name_Royal Enfield Classic 500': 47 ,'Car_Name_Royal Enfield Thunder 350': 48,'Car_Name_Royal Enfield Thunder 500': 49 ,'Car_Name_Suzuki Access 125': 50 ,
                     'Car_Name_TVS Apache RTR 160': 51 ,'Car_Name_TVS Apache RTR 180': 52 ,'Car_Name_TVS Jupyter': 53 ,'Car_Name_TVS Sport ': 54 ,'Car_Name_TVS Wego': 55 ,'Car_Name_UM Renegade Mojave': 56 ,'Car_Name_Yamaha FZ  v 2.0': 57 ,'Car_Name_Yamaha FZ 16': 58 ,'Car_Name_Yamaha FZ S ': 59,'Car_Name_Yamaha FZ S V 2.0': 60 ,
                     'Car_Name_Yamaha Fazer ': 61 ,'Car_Name_alto 800':62 ,
                    'Car_Name_alto k10': 63 ,'Car_Name_amaze': 64 ,'Car_Name_baleno': 65, 'Car_Name_brio': 66 ,
                    'Car_Name_camry': 67 ,'Car_Name_ciaz': 68 ,'Car_Name_city': 69 ,
                    'Car_Name_corolla':70 ,'Car_Name_corolla altis':71 ,'Car_Name_creta': 72 ,'Car_Name_dzire': 73,'Car_Name_elantra': 74 ,'Car_Name_eon': 75 ,'Car_Name_ertiga': 76 ,
                    'Car_Name_etios cross': 77 ,'Car_Name_etios g': 78 ,'Car_Name_etios gd': 79 ,'Car_Name_etios liva': 80 ,
                    'Car_Name_fortuner': 81 ,'Car_Name_grand i10': 82 ,'Car_Name_i10': 83 ,'Car_Name_i20': 84 ,'Car_Name_ignis': 85 ,
                    'Car_Name_innova': 86 ,'Car_Name_jazz': 87 ,'Car_Name_land cruiser': 88 ,'Car_Name_omni': 89 ,'Car_Name_ritz': 90 ,
                    'Car_Name_s cross': 91 ,'Car_Name_swift': 92 ,'Car_Name_sx4': 93 ,'Car_Name_verna': 94 ,
                    'Car_Name_vitara brezza': 95 ,'Car_Name_wagon r': 96 ,'Car_Name_xcent': 97 }

    carModellist[car_model_dict[selected_CarModel]] = 1

    return carModellist


def fuel_type_selection(fuelValue):

    fuelList = [0] * 3

    fuel_type_dict = {"CNG" : 0, "Diesel" : 1, "Petrol" : 2}

    fuelList[fuel_type_dict[fuelValue]] = 1

    return fuelList

def seller_type_selection(sellerTypeValue):

    sellerTypeList = [0] * 2
    seller_type_dict = {"Dealer" : 0, "Individual" : 1}
    sellerTypeList[seller_type_dict[sellerTypeValue]] = 1

    return sellerTypeList

def trans_type_selection(transTypeValue):

    transTypeList = [0] * 2
    trans_type_dict = {"Automatic" : 0, "Manual" : 1}
    transTypeList[trans_type_dict[transTypeValue]] = 1

    return transTypeList

















































car_independent_features = ['Present_Price',
 'Kms_Driven',
 'Owner',
 'No_of_years',
 'Car_Name_800',
 'Car_Name_Activa 3g',
 'Car_Name_Activa 4g',
 'Car_Name_Bajaj  ct 100',
 'Car_Name_Bajaj Avenger 150',
 'Car_Name_Bajaj Avenger 150 street',
 'Car_Name_Bajaj Avenger 220',
 'Car_Name_Bajaj Avenger 220 dtsi',
 'Car_Name_Bajaj Avenger Street 220',
 'Car_Name_Bajaj Discover 100',
 'Car_Name_Bajaj Discover 125',
 'Car_Name_Bajaj Dominar 400',
 'Car_Name_Bajaj Pulsar  NS 200',
 'Car_Name_Bajaj Pulsar 135 LS',
 'Car_Name_Bajaj Pulsar 150',
 'Car_Name_Bajaj Pulsar 220 F',
 'Car_Name_Bajaj Pulsar NS 200',
 'Car_Name_Bajaj Pulsar RS200',
 'Car_Name_Hero  CBZ Xtreme',
 'Car_Name_Hero  Ignitor Disc',
 'Car_Name_Hero Extreme',
 'Car_Name_Hero Glamour',
 'Car_Name_Hero Honda CBZ extreme',
 'Car_Name_Hero Honda Passion Pro',
 'Car_Name_Hero Hunk',
 'Car_Name_Hero Passion Pro',
 'Car_Name_Hero Passion X pro',
 'Car_Name_Hero Splender Plus',
 'Car_Name_Hero Splender iSmart',
 'Car_Name_Hero Super Splendor',
 'Car_Name_Honda Activa 125',
 'Car_Name_Honda Activa 4G',
 'Car_Name_Honda CB Hornet 160R',
 'Car_Name_Honda CB Shine',
 'Car_Name_Honda CB Trigger',
 'Car_Name_Honda CB Unicorn',
 'Car_Name_Honda CB twister',
 'Car_Name_Honda CBR 150',
 'Car_Name_Honda Dream Yuga ',
 'Car_Name_Honda Karizma',
 'Car_Name_Hyosung GT250R',
 'Car_Name_KTM 390 Duke ',
 'Car_Name_KTM RC200',
 'Car_Name_KTM RC390',
 'Car_Name_Mahindra Mojo XT300',
 'Car_Name_Royal Enfield Bullet 350',
 'Car_Name_Royal Enfield Classic 350',
 'Car_Name_Royal Enfield Classic 500',
 'Car_Name_Royal Enfield Thunder 350',
 'Car_Name_Royal Enfield Thunder 500',
 'Car_Name_Suzuki Access 125',
 'Car_Name_TVS Apache RTR 160',
 'Car_Name_TVS Apache RTR 180',
 'Car_Name_TVS Jupyter',
 'Car_Name_TVS Sport ',
 'Car_Name_TVS Wego',
 'Car_Name_UM Renegade Mojave',
 'Car_Name_Yamaha FZ  v 2.0',
 'Car_Name_Yamaha FZ 16',
 'Car_Name_Yamaha FZ S ',
 'Car_Name_Yamaha FZ S V 2.0',
 'Car_Name_Yamaha Fazer ',
 'Car_Name_alto 800',
 'Car_Name_alto k10',
 'Car_Name_amaze',
 'Car_Name_baleno', 
 'Car_Name_brio',
 'Car_Name_camry',
 'Car_Name_ciaz',
 'Car_Name_city',
 'Car_Name_corolla',
 'Car_Name_corolla altis',
 'Car_Name_creta',
 'Car_Name_dzire',
 'Car_Name_elantra',
 'Car_Name_eon',
 'Car_Name_ertiga',
 'Car_Name_etios cross',
 'Car_Name_etios g',
 'Car_Name_etios gd',
 'Car_Name_etios liva',
 'Car_Name_fortuner',
 'Car_Name_grand i10',
 'Car_Name_i10',
 'Car_Name_i20',
 'Car_Name_ignis',
 'Car_Name_innova',
 'Car_Name_jazz',
 'Car_Name_land cruiser',
 'Car_Name_omni',
 'Car_Name_ritz',
 'Car_Name_s cross',
 'Car_Name_swift',
 'Car_Name_sx4',
 'Car_Name_verna',
 'Car_Name_vitara brezza',
 'Car_Name_wagon r',
 'Car_Name_xcent',
 'Fuel_Type_CNG',
 'Fuel_Type_Diesel',
 'Fuel_Type_Petrol',
 'Seller_Type_Dealer',
 'Seller_Type_Individual',
 'Transmission_Automatic',
 'Transmission_Manual']