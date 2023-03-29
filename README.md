# Garden-Generator

Working at a garden center, I took notice the massive quantity of plants brought in to sell each season. Each plant came with a tag that contained data about the plant. With all this unique data available to me, I thought it would be a fun experiment to create a database of plants, giving me an opportunity to play around and gain some SQL experience.

In additon to unloading and displaying the plants, my job involves assisting customers and selling them plants that will thrive in the environment they are going to, in an aesthetically pleasing combination. The garden center is divided into a section for annuals, plants that must be planted each year as they only live for one season, and perennials, plants that will come back every year and bloom for a few weeks at a time. Customers shopping for annuals are looking to either plant beds of flowers in the ground, or to create planters.

There is a formula for creating planters known as "thriller, filler, spiller". "Thrillers" are taller plants that typically act as the centerpiece of a planter. "Fillers" are medium height plants that are often bushy and wide. "Spillers" are plants that get long but not tall, and usually spill out over the side of the planter.

I realized that it would be possible to randomly generate planters based on this formula using a computer program, and that this could be a way to put the plant database to use.

Included in this project folder are the queries I entered to create the SQL database kept in a text file and the Python script used to generate the planters. A separate config file was created to connect with the local database and was not uploaded to the internet.

This is what the program looks like at run time:
![terminalss](https://user-images.githubusercontent.com/78498085/228413194-8269879d-6191-45fe-acac-926077fecb78.PNG)

Beyond serving as an experiment for myself, a scaled up version of this project could be used to help the business I work for. If there was a computer or tablet available for customers that connected to a an inventory database of the plants in stock, customers could run this program to get ideas for themselves. Staff would not need to spend as much time helping customers and could focus more on the work that needs to be done maintaining the garden center. This program wouldn't and shouldn't replace the human customer service altogether, but it would be a useful tool to augment it.

For my own personal gain, this project helped me gain a better understanding of relational databases and how programs can use them.  I was surprised at how much I enjoyed designing and working with the database, and I found myself understanding how multiple programs, each with its own purpose, could use the same database.

Going forward, I have several plans for extending this program. One is creating a feature that generates flower beds in addition to planters. This will require more math and creativity in the Python script than what was needed for the planter generator. Another is to give the program a GUI, with options for more queries to take advantage of the data in the database.

Trying to break into the tech field from a non traditional background, I wanted to come up with a project idea that was unique to my experience, and at the same time to provide an example of how to implement technology in a new way for my current job. The extensibility of the program will keep me learning, engaged, and having fun for some time.

Thanks for reading.
