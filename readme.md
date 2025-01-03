# Time to move on from React.

At some point in your frontend development journey, you’ll probably think, "Wait a second, are we making this much harder than it needs to be?" It’s been over 10 years of React, Vue, Angular, and a bunch of other JavaScript frameworks. I think we've had the tools available to us and sometimes think new ones would make our lives easier.

As developers, our job is to deliver solutions that are easy to maintain. That means ensuring they’re simple to update, quick to modify, and straightforward to pass on to anyone with a basic understanding of web fundamentals—like HTML, JavaScript, CSS, and how browsers function.

We've used and learned a lot from Front-End frameworks, Time to move on to something better by going back to the future with HTMX

In this blog I aim to cover how we can use basic things like server generated html through template engines and small libraries like HTMX to enhance our application

### **Table of Contents**

1. **<a href="#intro"> Introduction</a>**

   - The Current State of Web Development
   - Why It’s Time to Rethink React and Heavy Front-End Frameworks

2. **The Problem with Modern Front-End Development**

   - The Complexity of Build Systems
   - Dependency Hell and Upgrade Fatigue
   - Performance Issues: Heavy Frameworks on Lightweight Tasks

3. **The Case for Core Web Technologies**

   - Leveraging the Browser’s Native Power
   - The Timelessness of HTML, CSS, and JavaScript
   - Why Simplicity Beats Complexity

4. **Dynamic HTML with Server-Generated Content**

   - The Role of a Backend Server Like Flask
   - Responding to User Interactions Dynamically
   - Avoiding Over-Engineering

5. **Introducing HTMX and Alpine.js**

   - Enhancing HTML with HTMX
   - Lightweight Interactivity with Alpine.js
   - Comparing HTMX and Alpine.js to React and Vue

6. **No Build Systems, No Problem**

   - The Beauty of a Zero-Build Workflow
   - Writing Code That Just Runs
   - Reducing Development and Deployment Complexity

7. **A Real-World Example**

   - Building a Simple Dynamic Web Application
   - Server-Rendered HTML with HTMX Enhancements
   - Adding Interactivity with Alpine.js

8. **Benefits of This Approach**

   - Better Performance and Reduced Load Times
   - Easier Maintenance and Longevity
   - Accessibility and SEO Advantages

9. **Challenges and Considerations**

   - When to Avoid This Approach
   - The Learning Curve for HTMX and Alpine.js

10. **Conclusion**

    - Embracing Simplicity in Web Development
    - Future-Proofing Your Applications

11. **Call to Action**
    - Encouraging Readers to Experiment
    - Links to Resources, Tutorials, and Example Projects

<h3 id="intro">Introduction</h3>

#### **The Current State of Web Development**

Web development these days feels way more complicated than it needs to be. React, Angular, Vue—these frameworks have taken over, and with them comes a mountain of tools, build steps, and constant updates just to keep things running. Sure, they’re great for some use cases, but let’s be honest: a lot of apps don’t need all that extra baggage.

My view on the current state of web development is that it has become way to too complicated. We have so many front-end frameworks that promise to make our lives so much better. These frameworks comes with a set of instructions how to scaffold, create, structure and build our code. It also needs to be updated all the time.

We feel that the cool kids are doing it, so we have to do it as well. At the end of the day we just want to build an app our client feels comfortable using. The code has to be easy to maintain.

The starting point for any software is that can I build the same thing with the core tools I have. For this specific project, do I really need the lastest version of React, or Vue or Astro or Next, etc. Can I just start with my chosen server technology or node, python, go, rust, deno, .net

Can I find an easy way to generate HTML for my browser. Yes HTML, not JSON. and if I really want to add some flashiness to my page, can't I just use native JS or some small unobtrusive lib like HTMX or AlpineJS. Something that I can replace very easily without ripping the very guts out of my application.

We need to think more of progressive enhancement. To keep on lightly touching the core tech of Hypermedia. The web and all the giants before us has given us something we can and should have continued to use. The Browser, HTML, JS and CSS.

In all fairness, why have we re-invented the wheel around getting data, posting data, routing, styling. It's been there for decades. Why not just use what is already there.

I don't have a problem if we feel we can enhance what is there but what is the obsession with creating HTML and or CSS with JS. This notion of the virtual DOM. Why do we need it.

What does the user say. Is that what the client wants? No, At the end of the day the client doesn't give a flying f\*ck. All he wants is interact with the data he cares about.

Ok so if the client doesn't give a damn, who does then. Maybe the developer does. After all he or his team are the ones that are going to maintain the code. Well, if you're going to maintain the code, then why not just stick to they way we've been doing it for so many years. Yes sure, developers choose tools that make their workflows faster or more reliable. A tool that abstracts complexity can save hours of work. But does it really in the long run. Let's discuss this seeming valid point. Why has the solution be complex, why does the tool abstract. That to me is a problem. We have created an additional problem when trying to solve one in the first place. Ok, maybe it's the strong community that provides support, documentation, learning mediums. Is that why we adopt a technology. Well there is no bigger community than the implicit one that covers core technologies like HTML, CSS and JS when it comes to front-end development.Ok maybe using popular tools is a way of making yourself more marketable. You need that shit on your resume/cv. and you feel like you are missing out if you don't. You won't be hired? you won't get clients. Well, I think if you've worked on your swiss army knife of core web technolody skills to equip you to handle any client request for an application, that should stead you well as all other frameworks and web technologies are built on the very core skills you've come to master.

Well, its the business of software. Getting people to buy into ecosystems that are gonna make them money. Maybe it's the synical asshole in me, but it's because of money. I would like to guess that devs are this noble small group of individuals, but they're not we all in this to make money people. From the dev coding away in a dark room to the blonde haired vlogger that is out there evangelising on what new shit he just found out. We all in it for the dollar.

So it's up to you, yes you to figure it out for yourself. Be picky in what you want to learn, be efficient, be careful and ultimeately be happy that you'll have to share your code, you'll have to revisit you code. Your code is your product

**Something to Think About:**

- Do we really need a 500MB node_modules folder just to display a list of items?
- Are all these build tools fixing problems we don’t even have?
- And seriously—how sustainable is this constant chase for the next big framework?

#### **Why It’s Time to Rethink React and Heavy Front-End Frameworks**

React revolutionized web development, no doubt about it. It introduced component-based design and virtual DOM optimization. But over time, its ecosystem has become bloated, with developers navigating a maze of libraries, state management tools, and endless configurations.

Imagine building web applications with:

- No dependency on massive front-end frameworks.
- No waiting for Webpack, Vite, or any build tool to compile.
- A simpler, more elegant workflow.

This blog explores how we can strip back to the essentials: **HTML**, **CSS**, and **JavaScript**, enhanced by modern but lightweight tools like **HTMX** and **Alpine.js**, powered by the back of your choice.

#### **A Journey Back to the Core**

Think of this as a return to web development’s roots—leveraging the browser’s native power to build applications that are:

- Faster.
- Simpler.
- More maintainable.

This is not about nostalgia but about finding a sustainable way forward in an industry obsessed with the next shiny thing.

### Let's build something

We are going to build a CRM system with Flask, HTML, JS and CSS. We create an admin application for adding customers, products and orders. We'd like to use the application we're building to do CRUD operations on products and customers, we'll link customers to products through orders

### Let's start with our web application

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
```

This is a simple web server written in python using a web application framework called Flask. The code above when called from a browser renders text of "Hello World".

### Render Dynamic HTML pages

```py
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

Before we run this code we need to create the index.html for the route to render in a directory called and should only be called "templates"

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hello World</title>
  </head>

  <body>
    <h3>Hello World</h3>
  </body>
</html>
```

When we now run the code we can navigate to http://localhost:5000/ and we see an html rendered page

### Passing Data to the Template

Static Pages are useless to use when we are creating a web application. We need a way for the server to pass values to the page dynamically based on what the app is required to render. If we want to show a list of products or customers we need a way of displaying this data we've retrieved from the database on the web page.

Before we create a router specific to products, let's organise these routes in a separate routes directory

```
/
├── app.py
├── templates
│   ├── product
│   │   ├── list.html
│   │   └── edit.html
│   ├── customer
│   │   ├── list.html
│   │   └── edit.html
│   ├── order
│   │   ├── list.html
│   │   └── edit.html
│   └── index.html
└── routes
    ├── customer.py
    ├── product.py
    └── order.py
```

```py

```
