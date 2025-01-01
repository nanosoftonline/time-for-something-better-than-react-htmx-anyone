# Time for something better than React. HTMX anyone?

There comes a time in your front end development struggles where you will say, "Damn!, aren't we complicating things here?" or "Do we really need React for this project". It's been 10+ years of React and it just seems to be getting more complicated to choose and use the appropriate react framework.

New JS libs or versions of them keep appearing, promising to make our dev experience so much better, while continuing to take us further from what is already have as good enough: The browser, HTML, JS and CSS. For most projects, big or small, all we really need is some web server that serves html dynamically, and once served we can choose to use JS to make it pleasant to interact with.

Let's take a look back to browser routing, form posting, anchor tag linking. We'll then look at other JS libs if needed.

### **Table of Contents**

1. **Introduction**

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

### **1. Introduction**

#### **The Current State of Web Development**

Web development has grown increasingly complex. Frameworks like React, Angular, and Vue dominate the landscape, requiring extensive tooling, build pipelines, and constant upgrades to stay relevant. While these tools have their merits, they often introduce unnecessary complexity for applications that could thrive on simpler foundations.

**Key Questions to Ponder:**

- Do we need a 500MB `node_modules` folder to render a list of items?
- Are build systems solving problems we don't actually have?
- Is this sustainable for the long term?

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
