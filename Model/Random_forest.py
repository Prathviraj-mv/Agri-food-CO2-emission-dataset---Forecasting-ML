from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
import joblib
from Helpers.IOdata import IO


class RF_MODEL:
    def __init__(self):
        pass

    def rf_model(self):
        rf = RandomForestRegressor(random_state=42)

        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [None, 10, 20],
            'min_samples_split': [2, 5],
            'min_samples_leaf': [1, 2],
            'max_features': ['sqrt', 'log2']
        }

        grid = GridSearchCV(
            estimator=rf,
            param_grid=param_grid,
            cv=5,
            scoring="r2",
            n_jobs=-1,
            verbose=2
        )
        io = IO()

        grid.fit(io.X_train, io.y_train)

        prediction = grid.best_estimator_.predict(io.X_test)

        print(r2_score(io.y_test, prediction))

        best_model = grid.best_estimator_

        rmse = mean_squared_error(
            io.y_test,
            prediction,
        )

        r2 = r2_score(
            io.y_test,
            prediction
        )
        print("RMSE :", rmse)
        print("R² :", r2)

        joblib.dump(best_model,"ML_Model/RF/rfr.pkl")

        return None
