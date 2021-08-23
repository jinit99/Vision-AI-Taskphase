from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

boston = datasets.load_boston()

#features / labels
X = boston.data
y = boston.target

print("X")
print(X)
print(X.shape)
print("y")
print(y)
print(y.shape)

# algorithm we are using
l_reg = linear_model.LinearRegression()

# tried other but they were all focused in some area and this one was much scattered
plt.scatter(X.T[5], y)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train
model = l_reg.fit(X_train, y_train)

predictions = model.predict(X_test)
print("predictions: ", predictions)
print("R^2 value: ", l_reg.score(X, y))
# coeff of the x variable of linear regression model
print("coeff: ", l_reg.coef_)
print("intercept: ", l_reg.intercept_)
