# NOMBRE_DEL_DUEÑO_CODIGO: AliceWonder789
# TEMATICA_DEL_CODIGO: Redes neuronales con Keras
# IEM_ESCUELA_NORMAL_PASTO: IEM Normal de Pasto
# CURSO: Aprendizaje Automático

from keras.models import Sequential
from keras.layers import Dense

# Crear modelo secuencial
model = Sequential()

# Añadir capas
model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# Compilar modelo
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# Entrenar el modelo
