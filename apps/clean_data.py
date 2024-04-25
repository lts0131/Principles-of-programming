import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from os.path import join, dirname, realpath
from sklearn.model_selection import train_test_split
from apps.until import Until
import xgboost as xgb
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error


class DealData:
    def __init__(self):
        csv = join(dirname(realpath(__file__)), 'data/Env_Data.csv')
        self.df = pd.read_csv(csv)
        self.model = xgb.XGBRegressor(objective='reg:squarederror', seed=42)
        self.model_fit = None

    def doClean(self):
        self.df = (self.df.dropna())

    def build_chart(self):
        sns.pairplot(self.df)
        plt.savefig("./chart1.jpeg")
        corr_mat = self.df.corr()
        plt.subplots(figsize=(18, 10))
        sns.heatmap(corr_mat, annot=True, annot_kws={'size': 12})
        plt.savefig('./chart2.jpeg')
        sns.jointplot(x='air_quality_index', y='wind_speed', data=self.df)
        plt.savefig("./chart3.jpeg")
        chart_images = []
        for i in range(3):
            base64_str = Until.img_base64(f"./chart{i + 1}.jpeg")
            image_obj = {
                'base64_str': f"data:image/jpeg;base64,{base64_str}"
            }
            chart_images.append(image_obj)
        return chart_images

    def train_data(self):
        self.df = self.df.drop('year', axis=1)
        self.df = self.df.drop('month', axis=1)
        self.df = self.df.drop('day', axis=1)
        self.df = self.df.drop('hour', axis=1)
        scaler = MinMaxScaler()
        self.df[['temperature', 'humidity', 'wind_speed', 'noise_level', 'precipitation',
                 'solar_radiation']] = scaler.fit_transform(
            self.df[['temperature', 'humidity', 'wind_speed', 'noise_level', 'precipitation', 'solar_radiation']])
        DV = 'air_quality_index'
        x = self.df.drop(DV, axis=1)
        y = self.df[DV]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=49)
        self.model_fit = self.model.fit(x_train, y_train)
        y_pred = self.model_fit.predict(x_test)
        mse = mean_squared_error(y_test, y_pred)
        accuracy = 'The mse of the predicted data is {} .'.format(mse * 100)
        return f"Train data is finish.{accuracy}"

    def forecasts(self, data_test):
        df = pd.DataFrame(data_test)
        df = df.astype(int)
        y_pred = self.model_fit.predict(df)
        return ''.join(str(x) for x in y_pred)


if __name__ == '__main__':
    c = DealData()
    print(c.build_chart())
