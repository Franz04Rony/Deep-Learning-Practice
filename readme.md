# Deep Learning practicing test
In this repository there are some questions to practice Machine Learning and Deep Learning concepts with libraries like pandas and Tensorflow.

## To execute the notebook with the code and possible answers
```
pip install -r requirements.txt
```

## Questions
1) What type of objective functions was the ADAM algorithm designed for?

<details>
<summary>Answer</summary>

ADAM algorithm was created to optimize `Stochastical fuctions`.
</details>

2) what is the number of outliers in dataset1?
<details>
<summary>Answer</summary>

Depends of how you analyze the data. An option could be checks if values are within a some standart desviation from the mean. 
</details>

3. What is the number of companies that obtanied a second credit?
<details>
<summary>Answer</summary>

9889
</details>

4. What is the number of trainable parameters in the follow neural network?
```
model = Sequential([
    Dense(2, activation="relu", input_dim = 8),
    Dense(2**3, activation="relu"),
    Dense(8**4, activation="relu"),
    Dense(2**5, activation="relu"),
    Dense(19**2, activation="relu"),
    Dense(2+56, activation="relu"),
    Dense(12+0, activation="relu"),
    Dense(6**2, activation="relu"),
    Dense(30, activation="relu"),
    Dense(1, activation="relu"),
    Dense(1, activation="sigmoid")
])
```
<details>
<summary>Answer</summary>

203238
</details>

5. What is the value of the interquantile range of the column "MONTO PRÉSTAMO (S/)" in dataset1?
<details>
<summary>Answer</summary>

4990
</details>

6. What is an appropriate function loss for classification problem?

    a. mean_squared_error <br/>
    b. mean_absolute_error <br/>
    c. mean_squared_logarithmic_error <br/>
    d. mean_absolute_percentage_error <br/>
    e. kl_divergence <br/>
<details>
<summary>Answer</summary>

kl_divergence
</details>


7. What is an incorrect activation function in keras?

    a. CategoricalCrossentropy <br/>
    b. softsign <br/>
    c. elu <br/>
    d. log_softmax <br/>
    e. hard_sigmoid <br/>
<details>
<summary>Answer</summary>

CategoricalCrossentropy
</details>

8. How many companies of the economical sector "CONSTRUCCION" are in dataset1?
<details>
<summary>Answer</summary>

27117
</details>
