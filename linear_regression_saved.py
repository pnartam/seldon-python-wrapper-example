import joblib
from sklearn.linear_model import LinearRegression
from random import randint

TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a + (2*b) + (3*c)
    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(op)


def main():
    predictor = LinearRegression(n_jobs=-1)
    print("Training Model..")
    predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)
    print("Model Trained.!")

    filename_p = 'First.joblib'
    print('Saving model in %s' % filename_p)
    joblib.dump(predictor, filename_p)
    print('Model saved!')


if __name__ == "__main__":
    main()
    pr = joblib.load('First.joblib')
    X_TEST = [[1, 20, 30]]
    outcome = pr.predict(X=X_TEST)
    coefficients = pr.coef_

    print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))
