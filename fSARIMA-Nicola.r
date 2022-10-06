#imports
library(forecast)
library(astsa)

#exploring the data
salmon
plot(salmon)
acf2(salmon) #appears to be an AR(2) with possible seasonality and diffing

#decomping and diffing
dsalmon <- mstl(salmon)
plot(dsalmon) #slight seasonality (seasonal component will not be 0,0,0)

sasalmon <- dsalmon %>% seasadj()
plot(sasalmon)

sasalmon %>% diff() %>% acf2() #double seasonal difference may be appropriate
salmon %>% diff() %>% acf2() #single difference may be appropriate

#determining SARIMA order
sari_salmon <- salmon %>% Arima(order = c(2,1,0), seasonal = c(2,1,0))
summary(sari_salmon)  #AICc =  151.03, AIC = 150.63, RMSE = .357

sima_salmon <- salmon %>% Arima(order = c(0,1,2), seasonal = c(0,1,2)) 
summary(sima_salmon) #AICc = 153.64, AIC = 153.23, RMSE = .357

sarima_salmon <- salmon %>% Arima(order = c(1,1,1), seasonal = c(1,1,1))
summary(sarima_salmon)  #AICc = 151.03, AIC = 150.63, RMSE = .357

fit <- salmon %>% Arima(order = c(1,1,0), seasonal = c(2,1,1))
summary(fit) #AICc = 149.07, AIC = 148.66, RMSE = 0.354 SELECTING THIS MODEL
forecast(fit, h = 12)

auto_fit = salmon %>% auto.arima()
summary(auto_fit) #AICc = 156.13, AIC = 155.98, RMSE = 0.379

#Holt-Winters
hwa_salmon <- hw(salmon, h = 12, seasonal = "additive")
summary(hwa_salmon) #AICc = 550.72, AIC = 546.59, RMSE = 0.363

hwm_salmon <- hw(salmon, h = 12, seasonal = "multiplicative")
summary(hwm_salmon) #AICc = 511.98, AIC = 507.83, RMSE = 0.343
