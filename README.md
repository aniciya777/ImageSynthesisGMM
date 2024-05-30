# Системы и методы компьютерного моделирования
## Практическое задание №3
Вероятностное моделирование данных

> Восстановление распределений. Смеси гауссовских распределений (GMM) и их применение.
GMM в библиотеке sklearn. Синтез изображений с использованием GMM. Генерация
синтетических данных с использованием GMM.
Необходимо научиться моделировать новые данные на основе распределения исходных
данных. 

**Набор изображений животных**

**Остапчук Анастасия, гр. ПМИ-201**


![64x64 изображения, Компонент GMM: 4](https://raw.githubusercontent.com/aniciya777/ImageSynthesisGMM/master/results/generated_64x64_4_components.png)

Оптимальное количество компонент:

|       Метрика        | Среднее логарифмическое правдоподобие | Информационный критерий Акаике (AIC) | Байесовский информационный критерий (BIC) |
|:--------------------:|:-------------------------------------:|:------------------------------------:|:-----------------------------------------:|
|   n_components = 1   |              -1.615⋅10⁴               |              5.254⋅10⁸               |                 5.897⋅10⁸                 |
|   n_components = 3   |               -7467⋅10³               |              2.855⋅10⁸               |                 4.786⋅10⁸                 |
| **n_components = 4** |            **-5.513⋅10²**             |            **8.452⋅10⁷**             |               **3.419⋅10⁸**               |
|   n_components = 5   |               4.716⋅10³               |            -6.4584020⋅10⁷            |                 2.571⋅10⁸                 |
|  n_components = 10   |               1.394⋅10⁴               |             -2.713⋅10 ⁸              |                 3.722⋅10⁸                 |

Другие примеры:

![64x64 изображения, Компонент GMM: 100](https://raw.githubusercontent.com/aniciya777/ImageSynthesisGMM/master/results/generated_64x64_100_components.png)
![64x64 изображения, Компонент GMM: 1](https://raw.githubusercontent.com/aniciya777/ImageSynthesisGMM/master/results/generated_64x64_1_components.png)
![32x32 изображения, Компонент GMM: 100](https://raw.githubusercontent.com/aniciya777/ImageSynthesisGMM/master/results/generated_32x32_100_components.png)
![32x32 изображения, Компонент GMM: 1](https://raw.githubusercontent.com/aniciya777/ImageSynthesisGMM/master/results/generated_32x32_1_components.png)
