# Welcome to this repository
> This project can automate a script to run on your system to send you automated mails of all the internship blogs on InstiApp. I am not a member of InstiApp so this is not any official feature/ function of InstiApp

First of all install all the libraries by pip installing from requirements.txt file by writing this in your terminal

```
pip install -r requirements.txt
```

### Now its time to get your unique headers which will create a session of yours for accessing blog posts.
> Beginners can read this completely. Else if you have some idea of web scraping, just follow the bold texts in this steps.

1. Go to **instiapp website**. [Link](https://www.insti.app/)
2. **Login** and go to any page on this site or remain on the default webpage after login which will be [https://www.insti.app/feed](https://www.insti.app/feed)
3. Press Ctrl+Shift+I (in case of Chrome in Windows) to open **developer tools**. (It may be different for MAC OS so you can instead right click anywhere on the page and click on Developer tools.
4. Click on Network tab which will be in the upper part of the developer tools. By this time your webpage would have already loaded due to which you cant see anything there. Simply reload the page and you will see lots of **network logs** here which are recorded just after reloading the page.
5. Search for the **get-user log**. There will be 2 get-user logs. The one with a gear logo(settings logo) on it is the one which we want. It's type will be **fetch**.
6. Now go to the headers option among the four after clicking get-user log.
7. Scroll down to see **request headers** and copy them completely to data_for_instiapp.py or you can copy responses of all the inner elements one by one. If you are copying complete request headers, make sure that you **remove the colon from the first four elements (eg. :authority will be replaced as authority)**. And also add (") to all elements to convert into strings. Dont forget to add "," after every set to make a proper header dictionary.

### Now your headers are setup. You can always check if your headers are correct or not by sending get request to the same(or any other request URL of insti.app) of this get-user log and see for the status code of the request. (For beginners: Status Code 200 implies request was successful. Status code 4xx, you can check on the internet to find out the reason for failure in request)

### Now you need to enter credentials of the email ID from which you will be sending emails to your primary email ID. I suggest you to create a new email ID for this purpose. After creating it, go to its settings and turn on access to less secure apps. Finally write your primary email ID where you will receive all the mails in data_for_instiapp.py.

## Lots of steps to do right ( ͡° ͜ʖ ͡°) . This is the last one!! Use any inbuilt task scheduler of your system, and schedule it for daily basis for 4 times i.e. 10AM, 2PM, 6PM and 11:59PM. For windows users, I am sharing an import file for the inbuilt task scheduler(dont forget to edit the location of the .py file in this task schedule while importing)




