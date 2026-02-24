# CICF Week 7

The goals for this week are to

1. Call a web service from the command line
1. Be able to specify HTTP headers with `curl` requests
1. Be able to manipulate JSON files


## Tutorial

This week we will look at web services.

## Flask

<!-- Yaxue start here -->

Flask is a very simple python framework for making web applications.
Here is a Flask app showing how a web server works.
Let's set up the virtual envrionment and run Flask.

    $ source ~/venv/bin/activate
    $ pip install flask
    $ flask --app app run

You will see some text, including that the server is running on "http://127.0.0.1:5000".
This is a special address, in that on any computer in the world, 127.0.0.1 refers to the current computer.
This is also called the "localhost".
The 5000 says the server is listening on port 5000 on the current computer.
Open a web browser and type in the URL `localhost:5000`.
You will see a page showing "Hello World."
This is because in the file `app.py` we match that route and say to return that text.
We also have a route to match any path that begins with `/topic/` so let's try that in the browser.
Enter "localhost:5000/topic/2343453465" in the browser, you will see a page that has the text

    You asked for 2343453465

All web servers follow similar designs: they listen on a port for routes (or pages), and then depending on the page being asked for, run different pieces of code to return a response.


<!-- Yaxue figure out how to make an exercise for this?

maybe start with existing flask app, and alter it to either add a new route, or to do something in addition

-->



## Resources

* [Glue work and systems design](https://apenwarr.ca/log/?m=202012)
* [Building and operating a pretty big storage system](https://www.allthingsdistributed.com/2023/07/building-and-operating-a-pretty-big-storage-system.html)

Software Architecture
* [Software Architects: Do We Need 'em](https://www.bredemeyer.com/who.htm) by Ruth Malan(by the way, this site has many other excellent articles on software architecture).
* [Explaining Software Design](https://explaining.software/)
* [5 essential patterns of software architecture](https://www.redhat.com/architect/5-essential-patterns-software-architecture)
* [List of software architecture styles and patterns](https://en.wikipedia.org/wiki/List_of_software_architecture_styles_and_patterns)
* [Design Patterns, Architectural Patterns](https://cs.nyu.edu/~jcf/classes/g22.2440-001_sp06/slides/session8/g22_2440_001_c82.pdf)
* [14 software architecture design patterns to know](https://www.redhat.com/architect/14-software-architecture-patterns)
* [Roy Fielding's Misappropriated REST Dissertation](https://twobithistory.org/2020/06/28/rest.html) is a great read showing how the term REST was appropriated for what we call REST today.

Jeff Bezos on [two types of decisions](https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm):

> Some decisions are consequential and irreversible or nearly irreversible –
> one-way doors – and these decisions must be made methodically, carefully,
> slowly, with great deliberation and consultation. If you walk through and
> don’t like what you see on the other side, you can’t get back to where you
> were before. We can call these Type 1 decisions. But most decisions aren’t
> like that – they are changeable, reversible – they’re two-way doors. If
> you’ve made a suboptimal Type 2 decision, you don’t have to live with the
> consequences for that long. You can reopen the door and go back through. Type
> 2 decisions can and should be made quickly by high judgment individuals or
> small groups.

* [List of HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
* [List of HTTP Methods](https://en.wikipedia.org/wiki/HTTP#Request_methods)
* JSON [RFC 4627: The application/json Media Type for JavaScript Object Notation (JSON)](https://www.ietf.org/rfc/rfc4627.txt)
* ORCID [API v3.0 Guide](https://github.com/ORCID/orcid-model/blob/master/src/main/resources/record_3.0/README.md)
* Python Flask [minimal application](https://flask.palletsprojects.com/en/3.0.x/quickstart/#a-minimal-application)

