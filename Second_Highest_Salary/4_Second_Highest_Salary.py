import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """
    :param employee: pd.DataFrame with columns ['id', 'salary']
    :return: pd.DataFrame with one column ['SecondHighestSalary']
    """
    # Hitung rank untuk setiap gaji menggunakan DENSE_RANK
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)

    # Filter hanya untuk rank ke-2
    second_highest = employee[employee['rank'] == 2]

    # Ambil nilai maksimum dari gaji dengan rank ke-2
    second_highest_salary = second_highest['salary'].max()

    # Return sebagai DataFrame
    return pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
