# **FatSecret Platform API**

####The FatSecret Platform API is the #1 verified food and nutrition database in the world, utilized by more than 10,000 developers, in more than 50 countries. ####Integrate high quality, curated food, nutrition and calorie data into mobile apps, websites, devices and complementary products and services.

#####The following steps provide a way to acquire data using fatsecret platform apis.

#####Step 1:
#####	Create an account on the fatsecret website.
#####	https://platform.fatsecret.com/api/Default.aspx?screen=r

#####Step 2:
#####Activate account , create the application and acquire the keys (client id and client secret)
	
#####Step 3:
#####	Run the following script(or the access_token .js) with the acquired client id and client secret.

#####var request = require("request");
#####clientID = '7dea337a4396475c9449e22756c2fe49'
#####clientSecret = 'b6b53a6e40f24c0cbb6910801a8a7733'
```javascript
var options = {
   method: 'POST',
   url: 'https://oauth.fatsecret.com/connect/token',
   method : 'POST',
   auth : {
      user : clientID,
      password : clientSecret
   },
   headers: { 'content-type': 'application/json'},
   form: {
      'grant_type': 'client_credentials',
      'scope' : 'basic'
   },
   json: true
};

request(options, function (error, response, body) {
   if (error) throw new Error(error);

   console.log(body);
});
```
#####Save and run the script to get the access_token and replace this in the fat_secret.py file.

#####Step 4:
#####	Copy the files food.txt and fat_secret.py to the local folder and replace Bearer token with the access token above and run the script to get the data.json #####file.
#####(You can add additional food items by appending them to the food.txt file)

#####Step 5:
#####	Copy data.ipynb and data.csv to the current folder and run each cell in the jupyter notebook to get the trial.csv file.

#####Step 6:
##### 	Run the data_format.py script in the current folder to get the files food_details.xlsx and nutrient_details.xlsx
