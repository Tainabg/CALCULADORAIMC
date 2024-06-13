import tkinter as tk
from tkinter import messagebox


class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")

        # Configuração da entrada de peso
        self.label_peso = tk.Label(self.root, text="Peso (kg):")
        self.label_peso.grid(row=0, column=0, padx=10, pady=10)

        self.entry_peso = tk.Entry(self.root)
        self.entry_peso.grid(row=0, column=1, padx=10, pady=10)

        # Configuração da entrada de altura
        self.label_altura = tk.Label(self.root, text="Altura (m):")
        self.label_altura.grid(row=1, column=0, padx=10, pady=10)

        self.entry_altura = tk.Entry(self.root)
        self.entry_altura.grid(row=1, column=1, padx=10, pady=10)

        # Botão para calcular o IMC
        self.botao_calcular = tk.Button(
            self.root, text="Calcular IMC", command=self.calcular_imc)
        self.botao_calcular.grid(row=2, column=0, columnspan=2, pady=10)

        # Labels para exibir o resultado
        self.resultado_imc = tk.StringVar()
        self.label_resultado_imc = tk.Label(
            self.root, textvariable=self.resultado_imc)
        self.label_resultado_imc.grid(row=3, column=0, columnspan=2, pady=10)

        self.resultado_classificacao = tk.StringVar()
        self.label_resultado_classificacao = tk.Label(
            self.root, textvariable=self.resultado_classificacao)
        self.label_resultado_classificacao.grid(
            row=4, column=0, columnspan=2, pady=10)

    def calcular_imc(self):
        try:
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())

            if peso <= 0 or altura <= 0:
                raise ValueError(
                    "Peso e altura devem ser valores positivos maiores que zero.")

            imc = peso / (altura ** 2)
            self.resultado_imc.set(f"Seu IMC é: {imc:.2f}")
            self.show_bmi_category(imc)

        except ValueError as e:
            messagebox.showerror("Erro de Entrada", f"Entrada inválida: {e}")

    def classificar_imc(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc < 24.9:
            return "Peso normal"
        elif imc < 29.9:
            return "Sobrepeso"
        elif imc < 34.9:
            return "Obesidade grau 1"
        elif imc < 39.9:
            return "Obesidade grau 2"
        else:
            return "Obesidade grau 3"

    def show_bmi_category(self, imc):
        classificacao = self.classificar_imc(imc)
        self.resultado_classificacao.set(f"Classificação: {classificacao}")


# Executar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
