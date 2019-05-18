from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense

class IrisModel:
    def __init__(self):
        iris = datasets.load_iris()
        self._X = iris.data
        self._Y = iris.target

    def create_model(self):
        X = self._X
        Y = self._Y
        enc = OneHotEncoder()
        Y_1hot = enc.fit_transform(Y.reshape(-1, 1)).toarray()
        model = Sequential()
        model.add(Dense(4, input_dim=4, activation='relu'))
        model.add(Dense(3, activation='softmax'))
        model.compile()

