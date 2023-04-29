from aiogram.dispatcher.filters.state import State, StatesGroup


class BotState(StatesGroup):
    gender = State()
    goal = State()
    weight = State()
    height = State()
    age = State()
    activity = State()


info = 'The calculations are based on the Harris-Benedict formula. Note that the Harris-Benedict formula cannot be ' \
       'apply to very obese people (the formula overestimates their actual caloric needs) and very muscular people' \
       '(the formula underestimates their actual needs). The formula can be used to calculate calories' \
       'for persons over 18 years of age. However, the calculations using the Harris-Benedict equation are an excellent starting point, its performance ' \
       'can form the basis of an effective and balanced diet, it allows you to assess your energy needs,' \
       'to review and adjust the diet in order to ultimately achieve those parameters that everyone considers for ' \
       'to be as acceptable as possible.'

activity_message = 'Enter your activity level:\n\n\n' \
                   '1️⃣ Low or missing\n\n' \
                   '2️⃣ Low activity (1-3 workouts per week)\n\n' \
                   '3️⃣ Moderate activity (3-5 workouts per week)\n\n' \
                   '4️⃣ High activity (6-7 workouts per week)\n\n' \
                   '5️⃣ Extremely high activity (2 or more workouts per day)'

activity_indexes = {
    '1️⃣': 1.2,
    '2️⃣': 1.375,
    '3️⃣': 1.55,
    '4️⃣': 1.725,
    '5️⃣': 1.9
}

goal_indexes = {
    'Slimming': 0.85,
    'Weight Gain': 1.15,
    'Keep in shape': 1
}


def calculator(user_data: dict) -> str:
    if user_data['gender'] == 'Male 👨':
        result = activity_indexes[user_data['activity']] * (
                88.362 + 13.397 * int(user_data['weight']) + 4.799 * int(
            user_data['height']) - 5.677 * int(user_data['age']))
    else:
        result = activity_indexes[user_data['activity']] * (447.593 + 9.247 * int(
            user_data['weight']) + 3.098 * int(
            user_data['height']) - 4.330 * int(
            user_data['age']))

    return f"Your daily calorie intake is {int(goal_indexes[user_data['goal']] * result)} calories"