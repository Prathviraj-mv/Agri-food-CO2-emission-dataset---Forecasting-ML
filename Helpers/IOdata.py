from sklearn.model_selection import train_test_split
from Helpers.data_extract_and_preprocessing import DATA


class IO:

    def __init__(self):

        data = DATA().return_data()

        X = data.drop("total_emission", axis=1)
        y = data["total_emission"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X,
            y,
            test_size=0.33,
            random_state=42
        )