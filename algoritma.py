import numpy as np 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import os
for dirname, _, filenames in os.walk('/PPS-Datamining/static'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df = pd.read_csv("static/nilai-dataset/data.csv", encoding='ISO-8859-1')
df.head()
df.describe()
df.shape
df.isnull().sum()
df.duplicated().sum()
test_data = df[df['Target'].isna()]
test_data = test_data.drop(columns=['No', 'Nama', 'Target'])

test_data

df.dropna(subset=['Target'], inplace=True)
df.Target=df.Target.astype('category').cat.codes
df['Target'] = df['Target'].replace(0, 99)

df
df.info()



selected_features = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10']
selected_features


X = df[selected_features] # Independent Values
y = df['Target'] # Targeted Values Selection

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

mms = MinMaxScaler()

X_train = mms.fit_transform(X_train)
X_test = mms.transform(X_test)

X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

n_input = X_train.shape[1]
n_output = len(np.unique(y_train))

print('Input Neuron:', n_input)
print('Output Neuron:', n_output)

class LVQ(object):

    def __init__(self, sizeInput, sizeOutput, max_epoch, learning_rate, fungsi_pembelajaran):
        """
        Inisialisasi class (constructor)
        :param sizeInput (int): Banyaknya input neuron sesuai dengan banyaknya parameter (fitur pada data latih)
        :param sizeOutput (int): Banyaknya output neuron sesuai dengan banyaknya label (kelas pada data latih)
        :param max_epoch (int): Maksimal epoch yang diizinkan
        :param alpha (float): learning rate
        """

        self.sizeInput = sizeInput
        self.sizeOutput = sizeOutput
        self.max_epoch = max_epoch
        self.alpha = learning_rate
        self.fungsi_pembelajaran = fungsi_pembelajaran
        self.weight = np.zeros((sizeOutput, sizeInput))

    def getWeight(self):
        """
        Mendapatkan bobot jaringan LVQ setelah proses training

        :return: weight (nilai bobot)
        """

        return self.weight

    def train(self,train_data,train_target):
        """
        Proses pelatihan jaringan LVQ
        :param train_data (numpy array atau pandas dataframe): Matriks yang berisi data latih
        :param train_target (numpy array atau pandas series): Array yang berisi label dari data latih
        :return: bobot dan label dari bobot
        """

        weight_label, label_index = np.unique(train_target, True)

        # Inisialisasi bobot
        self.weight = train_data[label_index].astype(float)

        # Hapus data yang digunakan untuk inisialisasi bobot
        train_data = np.delete(train_data, label_index, axis=0)
        train_target = np.delete(train_target, label_index, axis=0)

        epoch = 0
        iterasi = 0
        
        while epoch <= self.max_epoch:
            epoch += 1
            for data, target in zip(train_data, train_target):
                iterasi += 1
                distance = np.sqrt(np.sum((data - self.weight) ** 2, axis=1))
                idx_min = np.argmin(distance)

                if target == weight_label[idx_min]:
                    self.weight[idx_min] = self.weight[idx_min] + self.alpha * (data - self.weight[idx_min])
                else:
                    self.weight[idx_min] = self.weight[idx_min] - self.alpha * (data - self.weight[idx_min])

            self.alpha = self.alpha - (self.fungsi_pembelajaran * self.alpha)

        weight_class = (self.weight, weight_label)
        return weight_class

    def test(self, test_data, weight_class):
        """
        Proses pengujian jaringan LVQ
        :param test_data (numpy array atau pandas dataframe): Matriks yang berisi data uji
        :param weight_class (tuple): Tuple yang berisi pasangan bobot dan labelnya
        :return: Nilai prediksi label/class
        """

        weight, label = weight_class
        output = []
        for data in test_data:
            distance = np.sqrt(np.sum((data - weight) ** 2, axis=1))
            idx_min = np.argmin(distance)
            output.append(label[idx_min])

        return output
    
lvq = LVQ(sizeInput=n_input, sizeOutput=n_output, max_epoch=3, learning_rate=0.3, fungsi_pembelajaran=0.1)
bobot_dan_label = lvq.train(X_train, y_train)
bobot = lvq.getWeight()

print('Bobot: ', bobot)
print('Ukuran Bobot:', bobot.shape)

y_pred = lvq.test(X_test, bobot_dan_label)
print('Accuracy:', accuracy_score(y_test, y_pred))

print(confusion_matrix(y_pred, y_test))

print(classification_report(y_pred, y_test, zero_division=1))