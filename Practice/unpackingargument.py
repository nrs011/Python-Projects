def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)


nimeshs_data = [27, 20, 0]  # unpacking an argument list

health_calculator(nimeshs_data[0], nimeshs_data[1], nimeshs_data[2])
health_calculator(*nimeshs_data)