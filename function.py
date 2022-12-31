import matplotlib.pyplot as plt
import numpy as np
import math

'''
Amplitud de a -> A_a
Amplitud de b -> A_b

Fase de a -> F_a
Fase de b -> F_b

Campos Electricos -> Eo
'''
class Suma():

    def suma_dos_senos(self,A_a, A_b, F_a, F_b):

        potencia1 = (A_a * math.cos(F_a) + A_b * math.cos(F_b))**2
        potencia2 = (A_a * math.sin(F_a) + A_b * math.sin(F_b))**2

        self.amplitud_c = (potencia1 + potencia2)**0.5

        var1 = (math.pi / 2)
        var2 = A_a * math.cos(F_a)
        var3 = A_b * math.cos(F_b)
        var4 = A_a * math.sin(F_a)
        var5 = A_b * math.sin(F_b)

        self.fase_c = var1 - math.atan2(var2 + var3, var4 + var5)

        return [self.amplitud_c, self.fase_c]

    def PatronIntensidad(self, Lambda, D, ÃŸ, M, List_Ren):
        
        self.AmplitudesCuadrado = []

        self.lista_angulos = np.linspace(-ÃŸ, ÃŸ, M)

        self.num_de_onda = (2 * math.pi) / Lambda 

        self.LposicionPuntos = []

        for punto in range(M):

            self.posicion_y = D * math.tan(self.lista_angulos[punto])
            self.LposicionPuntos.append(self.posicion_y)

            self.lista_radios = []

            for pRendija in List_Ren:
                
                self.lista_radios.append(( D**2 + (self.posicion_y - pRendija)**2)**0.5)

            self.lista_Eo = []

            for radio in self.lista_radios:
                
                self.lista_Eo.append([1 / radio, (self.num_de_onda * radio) * -1])

            while len(self.lista_Eo) >= 2:
                self.lista_Eo[0] = self.suma_dos_senos(
                    self.lista_Eo[0][0], self.lista_Eo[1][0],
                    self.lista_Eo[0][1], self.lista_Eo[1][1])
                self.lista_Eo.pop(1)

            self.AmplitudesCuadrado.append((self.lista_Eo[0][0])**2)

        Eje_x = np.linspace(self.LposicionPuntos[0], self.LposicionPuntos[-1],
                        len(self.LposicionPuntos))

        Eje_y = np.array(self.AmplitudesCuadrado)

        fig, ax = plt.subplots()
        ax.plot(Eje_x, Eje_y)
        ax.set_title('A^2 vs h')
        plt.show()

        return self.AmplitudesCuadrado

    def grafico_del_patron(self,LAmplitudesCuadrado):
        Eje_x = np.linspace(0, 1, 200)
        X, Y = np.meshgrid(Eje_x, LAmplitudesCuadrado)

        plt.imshow(Y, cmap='gray')
        plt.show()

mi_funtion = Suma()