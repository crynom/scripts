#imports
library(ISLR)
library(glmnet)
library(tidyverse)
library(tidymodels)
library(rsample)
library(dplyr)

#Split into train and test data
set.seed(23)
x <- model.matrix(Apps~.,College)[,-1]
y <- College$Apps
train <- sample(1: nrow(x), nrow(x)*.75)
test <- (-train)
set.seed(23)
College_split <- initial_split(College)
College_train <- training(College_split)
College_test <- testing(College_split)

#Linear Model
lm.fit <- lm(Apps~., data = College, subset = train)
coef(lm.fit)
lm.MSE <- mean((College$Apps - predict(lm.fit, College))[test]^2)
lm.MSE #992281

#Using CV to determine optimal lambda
lambda <- cv.glmnet(x[train,], y[train], alpha = 0)$lambda.min

#Ridge Model
ridge.fit <- glmnet(x[train,], y[train], alpha = 0, lambda = lambda)
coef(ridge.fit)
ridge.MSE <- mean((College$Apps - predict(ridge.fit, x))[test]^2)
ridge.MSE #932226

#Tree Model
tree_spec <- decision_tree() %>% set_engine("rpart") %>% set_mode("regression")
tree.fit <- tree_spec %>% fit(formula = Apps~., data = College_train)
tree.fit
predictions <- predict(tree.fit, new_data = College_test) %>% mutate(actual = College_test$Apps)
predictions
tree.MSE <- mean((predictions$actual - predictions$.pred)^2)
tree.MSE #1989804

