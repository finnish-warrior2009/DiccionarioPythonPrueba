meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Símbolo que representa una carita riéndose. Se usa como respuesta a algo gracioso",
            "CHAMO": "Palabra utilizada en Venezuela para referirse a alguien de manera amistosa"
            "SHITPOST": "Tipo de humor con características absurdas o surreales y hechos a propósito de manera mediocre, incoherente y en baja calidad"
            
            
            
            }
word = input("Escribe una palabra que no entiendas (¡Con Mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Esa palabra no se encuentra en el diccionario")
    
