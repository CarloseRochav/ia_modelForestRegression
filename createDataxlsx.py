import pandas as pd

# Crear la tabla como un DataFrame
data = [
    [2012, 1, 'Primer semestre', None],
    [2012, 1, 'Segundo semestre', None],
    [2012, 1, 'Tercer semestre', None],
    [2012, 1, 'Cuarto semestre', None],
    [2012, 1, 'Quinto semestre', None],
    [2012, 1, 'Sexto semestre', None],
    [2012, 1, 'Séptimo semestre', None],
    [2012, 1, 'Octavo semestre', None],
    [2012, 1, 'Noveno semestre', None],
    [2012, 2, 'Primer semestre', None],
    [2012, 2, 'Segundo semestre', None],
    [2012, 2, 'Tercer semestre', None],
    [2012, 2, 'Cuarto semestre', None],
    [2012, 2, 'Quinto semestre', None],
    [2012, 2, 'Sexto semestre', None],
    [2012, 2, 'Séptimo semestre', None],
    [2012, 2, 'Octavo semestre', None],
    [2012, 2, 'Noveno semestre', None],
    [2013, 1, 'Primer semestre', None],
    [2013, 1, 'Segundo semestre', None],
    [2013, 1, 'Tercer semestre', None],
    [2013, 1, 'Cuarto semestre', None],
    [2013, 1, 'Quinto semestre', None],
    [2013, 1, 'Sexto semestre', None],
    [2013, 1, 'Séptimo semestre', None],
    [2013, 1, 'Octavo semestre', None],
    [2013, 1, 'Noveno semestre', None],
    [2013, 2, 'Primer semestre', None],
    [2013, 2, 'Segundo semestre', None],
    [2013, 2, 'Tercer semestre', None],
    [2013, 2, 'Cuarto semestre', None],
    [2013, 2, 'Quinto semestre', None],
    [2013, 2, 'Sexto semestre', None],
    [2013, 2, 'Séptimo semestre', None],
    [2013, 2, 'Octavo semestre', None],
    [2013, 2, 'Noveno semestre', None],
    [2014, 1, 'Primer semestre', None],
    [2014, 1, 'Segundo semestre', None],
    [2014, 1, 'Tercer semestre', None],
    [2014, 1, 'Cuarto semestre', None],
    [2014, 1, 'Quinto semestre', None],
    [2014, 1, 'Sexto semestre', None],
    [2014, 1, 'Séptimo semestre', None],
    [2014, 1, 'Octavo semestre', None],
    [2014, 1, 'Noveno semestre', None],
    [2014, 2, 'Primer semestre', None],
    [2014, 2, 'Segundo semestre', None],
    [2014, 2, 'Tercer semestre', None],
    [2014, 2, 'Cuarto semestre', None],
    [2014, 2, 'Quinto semestre', None],
    [2014, 2, 'Sexto semestre', None],
    [2014, 2, 'Séptimo semestre', None],
    [2014, 2, 'Octavo semestre', None],
    [2014, 2, 'Noveno semestre', None],
    [2015, 1, 'Primer semestre', None],
    [2015, 1, 'Segundo semestre', None],
    [2015, 1, 'Tercer semestre', None],
    [2015, 1, 'Cuarto semestre', None],
    [2015, 1, 'Quinto semestre', None],
    [2015, 1, 'Sexto semestre', None],
    [2015, 1, 'Séptimo semestre', None],
    [2015, 1, 'Octavo semestre', None],
    [2015, 1, 'Noveno semestre', None],
    [2015, 2, 'Primer semestre', None],
    [2015, 2, 'Segundo semestre', None],
    [2015, 2, 'Tercer semestre', None],
    [2015, 2, 'Cuarto semestre', None],
    [2015, 2, 'Quinto semestre', None],
    [2015, 2, 'Sexto semestre', None],
    [2015, 2, 'Séptimo semestre', None],
    [2015, 2, 'Octavo semestre', None],
    [2015, 2, 'Noveno semestre', None],
    [2016, 1, 'Primer semestre', None],
    [2016, 1, 'Segundo semestre', None],
    [2016, 1, 'Tercer semestre', None],
    [2016, 1, 'Cuarto semestre', None],
    [2016, 1, 'Quinto semestre', None],
    [2016, 1, 'Sexto semestre', None],
    [2016, 1, 'Séptimo semestre', None],
    [2016, 1, 'Octavo semestre', None],
    [2016, 1, 'Noveno semestre', None],
    [2016, 2, 'Primer semestre', None],
    [2016, 2, 'Segundo semestre', None],
    [2016, 2, 'Tercer semestre', None],
    [2016, 2, 'Cuarto semestre', None],
    [2016, 2, 'Quinto semestre', None],
    [2016, 2, 'Sexto semestre', None],
    [2016, 2, 'Séptimo semestre', None],
    [2016, 2, 'Octavo semestre', None],
    [2016, 2, 'Noveno semestre', None],
    [2017, 1, 'Primer semestre', None],
    [2017, 1, 'Segundo semestre', None],
    [2017, 1, 'Tercer semestre', None],
    [2017, 1, 'Cuarto semestre', None],
    [2017, 1, 'Quinto semestre', None],
    [2017, 1, 'Sexto semestre', None],
    [2017, 1, 'Séptimo semestre', None],
    [2017, 1, 'Octavo semestre', None],
    [2017, 1, 'Noveno semestre', None],
    [2017, 2, 'Primer semestre', None],
    [2017, 2, 'Segundo semestre', None],
    [2017, 2, 'Tercer semestre', None],
    [2017, 2, 'Cuarto semestre', None],
    [2017, 2, 'Quinto semestre', None],
    [2017, 2, 'Sexto semestre', None],
    [2017, 2, 'Séptimo semestre', None],
    [2017, 2, 'Octavo semestre', None],
    [2017, 2, 'Noveno semestre', None],
    [2018, 1, 'Primer semestre', None],
    [2018, 1, 'Segundo semestre', None],
    [2018, 1, 'Tercer semestre', None],
    [2018, 1, 'Cuarto semestre', None],
    [2018, 1, 'Quinto semestre', None],
    [2018, 1, 'Sexto semestre', None],
    [2018, 1, 'Séptimo semestre', None],
    [2018, 1, 'Octavo semestre', None],
    [2018, 1, 'Noveno semestre', None],
    [2018, 2, 'Primer semestre', None],
    [2018, 2, 'Segundo semestre', None],
    [2018, 2, 'Tercer semestre', None],
    [2018, 2, 'Cuarto semestre', None],
    [2018, 2, 'Quinto semestre', None],
    [2018, 2, 'Sexto semestre', None],
    [2018, 2, 'Séptimo semestre', None],
    [2018, 2, 'Octavo semestre', None],
    [2018, 2, 'Noveno semestre', None],
    [2019, 1, 'Primer semestre', None],
    [2019, 1, 'Segundo semestre', None],
    [2019, 1, 'Tercer semestre', None],
    [2019, 1, 'Cuarto semestre', None],
    [2019, 1, 'Quinto semestre', None],
    [2019, 1, 'Sexto semestre', None],
    [2019, 1, 'Séptimo semestre', None],
    [2019, 1, 'Octavo semestre', None],
    [2019, 1, 'Noveno semestre', None],
    [2019, 2, 'Primer semestre', None],
    [2019, 2, 'Segundo semestre', None],
    [2019, 2, 'Tercer semestre', None],
    [2019, 2, 'Cuarto semestre', None],
    [2019, 2, 'Quinto semestre', None],
    [2019, 2, 'Sexto semestre', None],
    [2019, 2, 'Séptimo semestre', None],
    [2019, 2, 'Octavo semestre', None],
    [2019, 2, 'Noveno semestre', None],
    [2020, 1, 'Primer semestre', None],
    [2020, 1, 'Segundo semestre', None],
    [2020, 1, 'Tercer semestre', None],
    [2020, 1, 'Cuarto semestre', None],
    [2020, 1, 'Quinto semestre', None],
    [2020, 1, 'Sexto semestre', None],
    [2020, 1, 'Séptimo semestre', None],
    [2020, 1, 'Octavo semestre', None],
    [2020, 1, 'Noveno semestre', None],
    [2020, 2, 'Primer semestre', None],
    [2020, 2, 'Segundo semestre', None],
    [2020, 2, 'Tercer semestre', None],
    [2020, 2, 'Cuarto semestre', None],
    [2020, 2, 'Quinto semestre', None],
    [2020, 2, 'Sexto semestre', None],
    [2020, 2, 'Séptimo semestre', None],
    [2020, 2, 'Octavo semestre', None],
    [2020, 2, 'Noveno semestre', None],
    [2021, 1, 'Primer semestre', None],
    [2021, 1, 'Segundo semestre', None],
    [2021, 1, 'Tercer semestre', None],
    [2021, 1, 'Cuarto semestre', None],
    [2021, 1, 'Quinto semestre', None],
    [2021, 1, 'Sexto semestre', None],
    [2021, 1, 'Séptimo semestre', None],
    [2021, 1, 'Octavo semestre', None],
    [2021, 1, 'Noveno semestre', None],
    [2021, 2, 'Primer semestre', None],
    [2021, 2, 'Segundo semestre', None],
    [2021, 2, 'Tercer semestre', None],
    [2021, 2, 'Cuarto semestre', None],
    [2021, 2, 'Quinto semestre', None],
    [2021, 2, 'Sexto semestre', None],
    [2021, 2, 'Séptimo semestre', None],
    [2021, 2, 'Octavo semestre', None],
    [2021, 2, 'Noveno semestre', None],
    [2022, 1, 'Primer semestre', None],
    [2022, 1, 'Segundo semestre', None],
    [2022, 1, 'Tercer semestre', None],
    [2022, 1, 'Cuarto semestre', None],
    [2022, 1, 'Quinto semestre', None],
    [2022, 1, 'Sexto semestre', None],
    [2022, 1, 'Séptimo semestre', None],
    [2022, 1, 'Octavo semestre', None],
    [2022, 1, 'Noveno semestre', None],
    [2022, 2, 'Primer semestre', None],
    [2022, 2, 'Segundo semestre', None],
    [2022, 2, 'Tercer semestre', None],
    [2022, 2, 'Cuarto semestre', None],
    [2022, 2, 'Quinto semestre', None],
    [2022, 2, 'Sexto semestre', None],
    [2022, 2, 'Séptimo semestre', None],
    [2022, 2, 'Octavo semestre', None],
    [2022, 2, 'Noveno semestre', None],
    [2023, 1, 'Primer semestre', None],
    [2023, 1, 'Segundo semestre', None],
    [2023, 1, 'Tercer semestre', None],
    [2023, 1, 'Cuarto semestre', None],
    [2023, 1, 'Quinto semestre', None],
    [2023, 1, 'Sexto semestre', None],
    [2023, 1, 'Séptimo semestre', None],
    [2023, 1, 'Octavo semestre', None],
    [2023, 1, 'Noveno semestre', None],
    [2023, 2, 'Primer semestre', None],
    [2023, 2, 'Segundo semestre', None],
    [2023, 2, 'Tercer semestre', None],
    [2023, 2, 'Cuarto semestre', None],
    [2023, 2, 'Quinto semestre', None],
    [2023, 2, 'Sexto semestre', None],
    [2023, 2, 'Séptimo semestre', None],
    [2023, 2, 'Octavo semestre', None],
    [2023, 2, 'Noveno semestre', None],
]

columns = ['Año', 'Periodo', 'Grado', 'Número de grupos']

df = pd.DataFrame(data, columns=columns)

# Exportar el DataFrame a un archivo Excel
df.to_excel('tabla_grupos.xlsx', index=False)
