# SCAV_BlancaCervera


# Exercise 1

En este ejercicio nuestro objetivo es realizar la conversión de RGB a YUV y viceversa. Para ello, utilizamos las siguientes fórmulas dadas en los vídeos explicados en la teoría de la asignatura.


![Captura de pantalla 2021-11-17 a las 19 56 35](https://user-images.githubusercontent.com/59645708/142264667-3337ed0b-61d2-4ed0-b207-ab32bc4e7886.png)

En el script rgb_yuv.py podemos observar estas dos conversiones. Si en el main llamamos la siguiente línea:

  rgb_to_yuv(255, 0, 255)
  yuv_to_rgb(106, 202, 221)

El output que nos sale es el siguiente:

![Captura de pantalla 2021-11-17 a las 19 58 40](https://user-images.githubusercontent.com/59645708/142264995-9e638cc2-e76d-480d-9261-2ba5a6abab90.png)

# Exercise 2

Para el siguiente ejercicio necesitamos usar el software ffmpeg para reducir la calidad de la foto de Lenna en png. Para ello, abrimos la terminal, entramos donde tenemos repositada la foto (en mi caso, en el Desktop) y ponemos la siguiente línea:

![Captura de pantalla 2021-11-17 a las 20 06 47](https://user-images.githubusercontent.com/59645708/142266368-89fcc71e-050a-41b0-9baa-9dd7b2479913.png)

La fórmula que se ha usado es la siguiente:
"ffmpeg-i original.png -q:v 30 newnameoriginal.jpeg"

Resultado: Primera foto -> Original
           Segunda foto -> Baja calidad

![Lenna](https://user-images.githubusercontent.com/59645708/142266695-33453175-c88d-44bc-bab0-53eeac978cb1.png)![Lenna_lq](https://user-images.githubusercontent.com/59645708/142266721-1d8e6590-28bc-410a-8638-bb2b5a284e2a.jpeg)

# Exercise 3

Este ejercicio es similar al anterior ya que también debíamos usar ffmpeg para realizarlo. Para este, necesitábamos pasar una imagen a blanco y negro. Para ello usamos la siguiente línea en la terminal:

ffmpeg -i Lenna.png -vf format=gray Lenna_Gray.jpeg

Seguidamente le bajamos la calidad de la imagen con la misma línea usada en el ejercicio 2:

ffmpeg -i Lenna_Gray.jpeg -q:v 30 LennaGray_lq.jpeg

Resultado: Primera foto -> B&W
           Segunda foto -> Baja calidad B&W

![Lenna_Gray](https://user-images.githubusercontent.com/59645708/142267386-86021d74-509b-4aad-ac96-7f01e830d43e.jpeg)![LennaGray_lq](https://user-images.githubusercontent.com/59645708/142267391-01b1f2bf-db06-4e77-b39c-f83cbe665b0d.jpeg)

# Exercise 4

En este ejercicio había que hacer un código run_length. Para ello, opté por mirar en internet y encontré la siguiente fuente:
https://gist.github.com/jatinsharrma/ca70db6e889a1c79a736618a7b44dfd4

En el script del repositorio runlength_py tengo puesta mi versión, muy similar a la anterior. En ella contamos las letras consecutivas iguales con tal de detectarlas y así agruparlas en el número de veces repetidas + la letra que es.

Si en el main llamamos la siguiente línea:

  encoded_message = encode("ABBCCCDDDDH")
  print(encoded_message)

El output que nos sale es el siguiente:

![Captura de pantalla 2021-11-17 a las 20 22 31](https://user-images.githubusercontent.com/59645708/142268448-f6c0d6c6-37cb-4991-a89f-47ea1bcbab79.png)

# Exercise 5

En este último ejercicio debíamos crear un script que convirtiera o decodificara (o ambas) un input usando la DCT, es decir, la Discrete Cosine Transform. La DCT es utilizada para image compression. En mi caso, he optado por crear un código muy sencillo en el que importas la dct from scipy.fftpack y después, dada una array como input, le aplicas la dct y la printas en pantalla.

En script dct.py está lo explicado anteriormente, si en el main llamamos la siguiente línea:

    array = np.array([1, 2, 5])
    discrete_function(array)
    
    
El output que sale en pantalla es el siguiente:


![Captura de pantalla 2021-11-17 a las 20 32 48](https://user-images.githubusercontent.com/59645708/142269954-b6de7353-e4e3-4ed3-9484-cbccb8410065.png)

