# Run It! 

"Run It!" is a website dedicated to listing running events. Runners can effortlessly find details about local running events, ask questions, and sign up directly through the platform. Event organisers can also use "Run It!" to post their events and manage their participant lists.

The live version of the website can be viewed at [Run It!](https://runit-jdohertydev-773091e00a18.herokuapp.com/).

![Am I responsive](/readme-images/am-i-responsive.png)

## Table of Contents

- [Run It!](#run-it)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [The Idea](#the-idea)
    - [Target Audiences and the Ideal User](#target-audiences-and-the-ideal-user)
    - [Site Goals](#site-goals)
  - [The Strategy Plane](#the-strategy-plane)
  - [Epics](#epics)
  - [User Stories](#user-stories)
    - [User Stories and Project Metrics](#user-stories-and-project-metrics)
    - [Kanban Board Labels](#kanban-board-labels)
    - [Total Story Points](#total-story-points)
    - [EPIC 1: Event Discovery and Browsing](#epic-1-event-discovery-and-browsing)
    - [EPIC 2: User Registration and Login](#epic-2-user-registration-and-login)
    - [EPIC 3: Event Registration](#epic-3-event-registration)
    - [EPIC 4: Event Management for Organisers](#epic-4-event-management-for-organisers)
    - [EPIC 5: User Engagement and Community](#epic-5-user-engagement-and-community)
  - [The Scope Plane](#the-scope-plane)
    - [Features to be Implemented](#features-to-be-implemented)
  - [The Structure Plane](#the-structure-plane)
    - [Site Maps](#site-maps)
      - [Site Map for Users Logged In](#site-map-for-users-logged-in)
      - [Site Map for Users Not Logged In](#site-map-for-users-not-logged-in)
    - [Database Schema](#database-schema)
  - [Relationships](#relationships)
    - [postevent\_postevent Table](#postevent_postevent-table)
    - [auth\_user Table](#auth_user-table)
  - [The Skeleton Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
      - [Landing Page](#landing-page)
      - [Events](#events)
      - [Events Page Listing](#events-page-listing)
      - [Accounts](#accounts)
      - [Contact](#contact)
  - [The Surface Plane](#the-surface-plane)
    - [Color Palette](#color-palette)
    - [Fonts](#fonts)
  - [Features](#features)
    - [Favicon](#favicon)
    - [Logo and Tagline](#logo-and-tagline)
    - [Header](#header)
    - [Slogan](#slogan)
    - [Dynamic menu items that adapt based on the user's login status](#dynamic-menu-items-that-adapt-based-on-the-users-login-status)
    - [Sticky Navbar](#sticky-navbar)
    - [Custom Error Pages](#custom-error-pages)
      - [url.py](#urlpy)
      - [views.py](#viewspy)
    - [Footer](#footer)
    - [Events List Page](#events-list-page)
      - [Display Only Live Races](#display-only-live-races)
      - [Filter by Race Type](#filter-by-race-type)
      - [Event Card](#event-card)
      - [Shadowbox Effect](#shadowbox-effect)
      - [Navigation options for Next/Previous events based on event status](#navigation-options-for-nextprevious-events-based-on-event-status)
    - [Events Post Page](#events-post-page)
      - [Masthead banner](#masthead-banner)
      - [Event Details](#event-details)
      - [Comments section](#comments-section)
      - [Comments section - not logged in](#comments-section---not-logged-in)
      - [Comments section - logged in](#comments-section---logged-in)
      - [Comments section - awaiting approval](#comments-section---awaiting-approval)
      - [Comments section - approved ny superuser](#comments-section---approved-ny-superuser)
      - [Edit](#edit)
      - [Delete](#delete)
      - [List of Participants](#list-of-participants)
        - [List of particpants - unregistered](#list-of-particpants---unregistered)
        - [List of particpants - registered](#list-of-particpants---registered)
        - [Email template - Sign up](#email-template---sign-up)
        - [Email template - Unregister](#email-template---unregister)
    - [Account Page](#account-page)
      - [Update profile](#update-profile)
        - [Update profile confirmation email](#update-profile-confirmation-email)
        - [Change password](#change-password)
        - [Change password confirmation email](#change-password-confirmation-email)
        - [Delete account](#delete-account)
          - [Delete account modal](#delete-account-modal)
        - [Delete account email confirmation](#delete-account-email-confirmation)
    - [Contact Us Page](#contact-us-page)
      - [Contact us form when user is logged in](#contact-us-form-when-user-is-logged-in)
        - [Contact us form when user is not logged in](#contact-us-form-when-user-is-not-logged-in)
        - [Email message](#email-message)
        - [Django Backend](#django-backend)
    - [Django Admin](#django-admin)
      - [Superuser view of post events](#superuser-view-of-post-events)
      - [Staff user view of post events](#staff-user-view-of-post-events)
      - [Post events - Add post event](#post-events---add-post-event)
      - [Export list of participants](#export-list-of-participants)
      - [View in admin - export csv](#view-in-admin---export-csv)
      - [Screenhot of exported csv file](#screenhot-of-exported-csv-file)
    - [Future Features](#future-features)
  - [Validation, Testing \& Bugs](#validation-testing--bugs)
    - [Validation](#validation)
      - [CI Python Linter Screenshot](#ci-python-linter-screenshot)
      - [HTML Validation](#html-validation)
        - [Example of Django code that throws errors](#example-of-django-code-that-throws-errors)
      - [CSS Validation Results](#css-validation-results)
      - [JS Validation](#js-validation)
      - [Lighthouse](#lighthouse)
    - [Testing](#testing)
      - [User stories testing](#user-stories-testing)
      - [Automated Testing](#automated-testing)
        - [Accounts](#accounts-1)
        - [Contact](#contact-1)
      - [Events Listing](#events-listing)
      - [Test Cases](#test-cases)
      - [Viewport Testing](#viewport-testing)
        - [Screenshot - Desktop](#screenshot---desktop)
        - [Screenshot - Tablet](#screenshot---tablet)
        - [Screenshot - Mobile](#screenshot---mobile)
    - [Compatibility Testing](#compatibility-testing)
      - [Comparing Chrome and Edge](#comparing-chrome-and-edge)
    - [Bugs](#bugs)
  - [Deployment](#deployment)
    - [6.1. Transfer of Progress from IDE](#61-transfer-of-progress-from-ide)
    - [6.2. Offline Cloning](#62-offline-cloning)
    - [6.3.2. ElephantSQL](#632-elephantsql)
    - [6.3.3. Cloudinary](#633-cloudinary)
    - [6.3.4. Settings.py \& File-tree](#634-settingspy--file-tree)
    - [Deployment to Heroku](#deployment-to-heroku)
  - [Technologies Used](#technologies-used)
    - [Requirements.txt](#requirementstxt)
  - [Credits](#credits)

## User Experience (UX)

### The Idea

**Run It!** is designed to be a comprehensive running event listing website. Users can effortlessly find free running events in their area and book their spots. Additionally, they can post questions about specific events, add easily contact the site webmaster.

### Target Audiences and the Ideal User

**Target Audiences:**
- Runners of all levels interested in participating in running events.
- Race Organisers who want to list events and manage bookings through the site admin.

**The Ideal User:**
- Enjoys running and wants to participate in events.
- Desires to manage their registrations.
- Aims to connect with other runners in their community.
- Seeks to promote and manage their events via the platform.

### Site Goals

1. **Facilitate Event Discovery:**
   - Provide a user-friendly interface for runners to easily find and book running events in their area.
2. **Enhance User Engagement:**
   - Enable users to post questions, and interact with other runners and event organisers within the platform.
3. **Streamline Event Management:**
   - Offer race organisers robust tools to list events, manage bookings, and communicate with participants efficiently.
4. **Promote Community Connection:**
   - Foster a community of runners by allowing users to connect, share experiences, and support each other through the platform.
5. **Ensure Smooth Registration Process:**
   - Simplify the registration process for runners, making it easy for them to sign up for events and manage their registrations.
6. **Support Event Promotion:**
   - Provide race organisers with effective ways to promote their events, reaching a wider audience of potential participants.
7. **Maintain High-Quality User Support:**
   - Ensure that users can easily contact the site webmaster for assistance, providing reliable support for both runners and race organisers.

## The Strategy Plane

As a thought process of the strategy plane, 5 epics were created and utilised. Please see below the detailed list of epics with links, or a link to the project's Kanban Board ([GitHub Project Board](https://github.com/users/jdohertydev/projects/4)). These Epics were further sliced into 17 USER STORIES.

## Epics

![Run It! Kanban Board](/readme-images/kanban-board-run-it.png)

- [EPIC 1: Event Discovery and Browsing](https://github.com/jdohertydev/runit/issues/1)
- [EPIC 2: User Registration and Login](https://github.com/jdohertydev/runit/issues/2)
- [EPIC 3: Event Registration](https://github.com/jdohertydev/runit/issues/3)
- [EPIC 4: Event Management for Organisers](https://github.com/jdohertydev/runit/issues/4)
- [EPIC 5: User Engagement and Community](https://github.com/jdohertydev/runit/issues/5)

## User Stories

### User Stories and Project Metrics

User stories were created based on the Epics, utilising the MoSCoW prioritisation technique. Each user story was estimated for relative effort using a sequence inspired by Fibonacci numbers (1, 2, 3, 5, 8, 13, etc.), which helps capture the uncertainty and variability in estimating task complexity. This non-linear sequence was chosen to provide a clear initial size assessment for each user story.

### Kanban Board Labels

Each user story on the Kanban Board is labelled with two key attributes:

- **MoSCoW Prioritisation:**
  - **Must-Have:** Critical requirements that are essential for project success (14 story points).
  - **Should-Have:** Important requirements that significantly add value (3 story points).
  - **Could-Have:** Desirable features that provide additional benefits (0 story points).
  - **Won't-Have:** Features explicitly excluded from the project scope (23 story points).

### Total Story Points

The total estimation for the project is 40 Story Points.

### EPIC 1: Event Discovery and Browsing

<details>
<summary>USER STORY: Event Details Page</summary>

As a runner, I want to view detailed information about an event so that I can decide if I want to participate.

</details>

<details>
<summary>USER STORY: Event Filtering</summary>

As a runner, I want to filter events by categories so that I can narrow down the list to relevant races.

</details>

<details>
<summary>USER STORY: Search Events</summary>

As a runner, I want to search for events based on various criteria so that I can find races that interest me.

</details>

### EPIC 2: User Registration and Login

<details>
<summary>USER STORY: User Login</summary>

As a registered user, I want to log in to the website so that I can access my account.

</details>

<details>
<summary>USER STORY: User Registration</summary>

As a runner, I want to register for an account so that I can access the platform's features.

</details>

<details>
<summary>USER STORY: Update Account Details</summary>

As a site user, I can update my account details and also delete my account.

</details>

### EPIC 3: Event Registration

<details>
<summary>USER STORY: Cancel Registration</summary>

As a registered runner, I want to cancel my registration for an event in case I am unable to attend, so that it can be made available to other runners.

</details>

<details>
<summary>USER STORY: View Remaining Places Available</summary>

As a user, I want to see the number of remaining places for an event so that I can gauge availability and make informed decisions about registering for the event.

</details>

<details>
<summary>USER STORY: Registration Confirmation</summary>

As a runner, I want to receive confirmation emails after successfully registering for events.

</details>

<details>
<summary>USER STORY: Event Sign-Up</summary>

As a registered user, I can sign up for an event by clicking a 'sign-up' button so that I can participate in the race.

</details>

<details>
<summary>USER STORY: Payment Processing</summary>

As a runner, I want to pay for event registration fees securely online.

</details>

### EPIC 4: Event Management for Organisers

<details>
<summary>USER STORY: View Registrations</summary>

As an event organiser, I want to view registrations for my events so that I can manage participant details effectively.

</details>

<details>
<summary>USER STORY: Send Notifications</summary>

As an event organiser, I want to send notifications to participants so that I can communicate important updates or changes.

</details>

<details>
<summary>USER STORY: Manage Event Logistics</summary>

As an event organiser, I want to manage events on the platform so that I can effectively organise and oversee race logistics.

</details>

### EPIC 5: User Engagement and Community

<details>
<summary>USER STORY: Social Media Integration</summary>

As a user, I want to share my event registrations and achievements on social media platforms to celebrate accomplishments with my network.

</details>

<details>
<summary>USER STORY: Discussion Forums</summary>

As a user, I want to participate in discussion forums to connect with other runners and share insights.

</details>

<details>
<summary>USER STORY: Event Reviews</summary>

As a user, I want to share my experiences and provide feedback on events so that others can make informed decisions.

</details>

## The Scope Plane

After determining the strategy, the scope was meticulously defined and planned out.

### Features to be Implemented

- **Update Account Details:** Users can modify their personal information, such as name, email address, and password.
- **Event Details Page:** Users can view comprehensive information about a specific event, including date, time, location, description, and any additional details.
- **User Login:** Registered users can securely log in to their accounts to access personalized features and information.
- **User Registration:** New users (runners) can create an account on the platform to gain access to event listings and other site features.
- **Event Sign-Up:** Registered users can enrol in and confirm their participation for a selected event through the platform.
- **View Registrations:** Event organisers can see a list of participants who have registered for their event, along with relevant details.
- **View Remaining Places Available:** Users can check the number of available slots remaining for an event before registering.
- **Cancel Registration:** Registered runners can withdraw from participating in an event they previously signed up for.
- **Search Events:** Users can conduct searches using various criteria to find specific types of running events that match their interests.
- **Event Filtering:** Users can narrow down the list of events based on specific categories or criteria, helping them find events that align with their preferences.

## The Structure Plane

### Site Maps

#### Site Map for Users Logged In

![Site map for users who are logged in](/readme-images/site-map-logged-in.png)

#### Site Map for Users Not Logged In

![Site map for users who are not logged in](/readme-images/site-map-not-logged-in.png)

### Database Schema

![Database Schema](/readme-images/run-it-database-layout.png)

Created using [DBDDiagram](https://dbdiagram.io/):
```

Table users {
  id integer [primary key]
  username varchar
  role varchar
  created_at timestamp
}

Table post_events {
  id integer [primary key]
  event_name varchar
  slug varchar
  date timestamp
  race_type varchar
  author_id integer [ref: > users.id]
  featured_image varchar
  location varchar
  description text
  max_participants integer
  course_map varchar
  created_on timestamp
  status integer
}

Table comments {
  id integer [primary key]
  post_id integer [ref: > post_events.id]
  author_id integer [ref: > users.id]
  body text
  approved boolean
  created_on timestamp
}

Table event_sign_ups {
  id integer [primary key]
  event_id integer [ref: > post_events.id]
  user_id integer [ref: > users.id]
  signed_up_on timestamp
}

Table contact_messages {
  id integer [primary key]
  name varchar
  email varchar
  message text
  sent_at timestamp
}
```

## Relationships

### postevent_postevent Table

- **postevent_comment:** One-to-many relationship. Each `PostEvent` can have multiple `Comments`. The `post_id` in the `postevent_comment` table references the `id` of `postevent_postevent`.
- **postevent_eventsignup:** One-to-many relationship. Each `PostEvent` can have multiple sign-ups. The `event_id` in the `postevent_eventsignup` table references the `id` of `postevent_postevent`.

### auth_user Table

- **postevent_postevent:** The `author_id` field in the `postevent_postevent` table references the `id` of `auth_user`, linking each `PostEvent` to its author.
- **postevent_comment:** The `author_id` field in the `postevent_comment` table references the `id` of `auth_user`, linking each `Comment` to its author.
- **postevent_eventsignup:** The `user_id` field in the `postevent_eventsignup` table references the `id` of `auth_user`, linking each sign-up (`EventSignUp`) to the user who signed up.

These relationships ensure data integrity and establish connections between related data in the database schema.

## The Skeleton Plane

### Wireframes

#### Landing Page

![Landing Page](/readme-images/wire-frame-landing-page.png)

#### Events

![Events](/readme-images/wire-frame-events.png)

#### Events Page Listing

![Events Page Listing](/readme-images/wire-frame-events-page-listing.png)

#### Accounts

![Accounts](/readme-images/wire-frame-account.png)

#### Contact

![Contact](/readme-images/wire-frame-contact.png)

## The Surface Plane

Once the Strategy, Scope, Structure, and Skeleton Planes were in place, it was time to work on the Surface Plane (Design).

### Color Palette

I decided to use the color palette provided by [Looka](https://looka.com/). I find that the dark grayscale colors enhance the website's aesthetic appeal.

![Color Palette](/readme-images/colour-pallette.png)

### Fonts

**Roboto**

Roboto was chosen for its modern, clean aesthetic and versatility. Designed with a mechanical skeleton and largely geometric forms, Roboto offers a contemporary look that is both visually appealing and highly readable on various screen sizes and resolutions. Its wide range of weights and styles, from thin to black, including italics, makes it a flexible choice for diverse design needs, whether for web, mobile, or print applications. Serif was selected as a fallback font in case the primary font (Roboto) fails to load for any reason, such as network issues or the font not being installed on the user's device. This fallback ensures that the text remains legible and maintains a consistent style.

## Features

### Favicon

I used [Favicon Generator](https://favicon.io/favicon-converter/) to create the favicon and I integrated the corresponding code into base.html:

```HTML
<link rel="icon" type="image/x-icon" href="{% static 'images/favicon/favicon.ico' %}">
```

![Favicon](/readme-images/favicon.png)

### Logo and Tagline

I used [Looka](https://looka.com/) to create the logo used:

![Logo and Tagline ](/readme-images/logo-with-slogan.png)

On the landing page, I decided to keep the design simple and reproduce the logo with CSS animation:

![Logo on landing page](/readme-images/logo-on-landing-page.png)

```CSS
/* Fade-in animation */
@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

/* Pulse effect */
@keyframes pulse {
    0% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.05);
    }

    100% {
        transform: scale(1);
    }
}

/* Add pulse effect on hover */
.logo-landing-page:hover {
    animation: pulse 1s infinite;
    /* Infinite pulse effect */
}
```

### Header

The header code is centralised in base.html, ensuring consistency and facilitating future updates or modifications across the website.

![Header](/readme-images/header.png)

### Slogan

![Slogan](/readme-images/logo-with-slogan.png)

The slogan used serves to support the essence and values of my brand, leaving a memorable impression on visitors while reinforcing its identity and purpose. When viewing the website on smaller viewports, the slogan is removed to optimize screen space.

![Slogan](/readme-images/slogan-hideen-on-mobile-view.png)

```CSS
@media (max-width: 991px) {
    .slogan {
        display: none;
    }
}
```
### Dynamic menu items that adapt based on the user's login status

The user can see if they are logged in or not. Seeing their login status is crucial for users as it enhances their experience by providing context, access to personalized content, security, and seamless navigation on the website.

![Logged in](/readme-images/logged-in.png.png)

![Logged out](/readme-images/not-logged-in.png)

### Sticky Navbar

A sticky navbar enhances the user experience (UX) by providing constant, easy access to navigation options, which facilitates smoother and more efficient browsing. It eliminates the need for users to scroll back to the top of the page to navigate, saving time and effort, especially on smaller viewing ports.

Originally, I manually coded this feature using the following code:

```CSS

/* Make header sticky */

.navbar {
    position: -webkit-sticky; /* For Safari */
    position: sticky;
    top: 0;
    z-index: 1030; /* Ensure it stays on top of other content */
}

```
However, after encountering some issues getting the navbar to stay stuck to the top, I read that I could utilize the power of Bootstrap and simply add the class ```sticky-top```.

### Custom Error Pages

I have created custom error pages for 400, 403, 404, and 500 errors that enhance user experience by offering helpful navigation options, maintaining brand consistency, and reducing frustration through humorous running-related puns. This involved creating custom templates and linking them via the urls.py file and views.py.

#### url.py

```Python

# Custom error handlers
handler400 = 'myproject.views.custom_400_view'
handler403 = 'myproject.views.custom_403_view'
handler404 = 'myproject.views.custom_404_view'
handler500 = 'myproject.views.custom_500_view'

```
#### views.py

```Python

def custom_404_view(request, exception):
    """
    Handle 404 Not Found errors.

    This view renders a custom 404 error page when a page is not found.
    """
    return render(request, '404.html', status=404)

```
![Custom Error Pages](/readme-images/example-of-custom-error-page.png)

### Footer

The consistent footer, embedded in base.html, appears on every page, reinforcing brand identity and ensuring users can easily find social media links anywhere on the site.

![Footer](/readme-images/footer.png)

### Events List Page

#### Display Only Live Races

Within `def get_queryset(self)` (events_listing/views.py), the following code ensures that no events that have already taken place are displayed:

```python
def get_queryset(self):
    """
    Get the queryset for the list of post events.
    """
    current_datetime = timezone.now()
    queryset = PostEvent.objects.filter(date__gte=current_datetime)
```
This method retrieves a queryset of PostEvent objects whose date field is greater than or equal to the current date and time, effectively filtering out past events. I believe this makes for a better user experience.

#### Filter by Race Type

To enhance user experience, users can search for races by type (road, trail, mix) and also use keywords to find events.

![Filter by Race Type full screen](/readme-images/filter-and-search-function.png)

JavaScript was implemented to automatically load results when the user selected a race type, enhancing the user experience.

```javascript
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('race_type').addEventListener('change', function() {
        document.getElementById('filterForm').submit();
    });
});
```
On mobile devices, a media query was utilized to optimize the available space within the viewport.

```css
@media (max-width: 453px) {
    .search-filter-container {
        display: flex;
        flex-direction: column;
        align-items: stretch;
    }

    .search-filter-container .form-inline {
        flex-direction: column;
        align-items: stretch;
    }

    .search-filter-container .form-group {
        width: 100%;
        margin-bottom: 10px;
    }

    .search-filter-container .form-group label {
        display: block;
        margin-bottom: 5px;
    }

    .search-filter-container .form-group select,
    .search-filter-container .form-group input,
    .search-filter-container .form-group button {
        width: 100%;
        box-sizing: border-box;
    }

    .search-filter-container .form-group input {
        margin-bottom: 10px;
    }

    .search-filter-container .form-group button {
        width: 100%;
    }
}

/* Ensure consistent height for select and input elements */
.search-filter-container .form-group select,
.search-filter-container .form-group button,
.search-filter-container .form-group input {
    height: 38px;
}
```
![Filter by Race Type mobile device](/readme-images/resized-filter-and-search.png)

#### Event Card

Although a minor design concern, CSS was employed to standardize the size of all event cards, ensuring that the text adjusts accordingly. This was accomplished using CSS.

```CSS

.col-md-4 {
    display: flex;
    flex-direction: column;
    padding: 0 15px;
    /* Add padding to columns to ensure proper spacing */
}

```
Event Card without styling

![Event Card without styling](/readme-images/event-card-without-styling.png)

Event Card with styling

![Event Card with styling](/readme-images/event-card-resizing-to-be-same-size.png)

#### Shadowbox Effect

The shadow box effect serves to enhance visual appeal and usability by adding depth and dimensionality to elements. It helps users easily identify interactive elements and distinguish them from static content, ensuring a more intuitive browsing experience.

![Shadowbox Effect](/readme-images/event-card-shadow-box.png)

#### Navigation options for Next/Previous events based on event status

Using Python logic, the site will display next and previous buttons based on the number of events currently in the database.

```Python

{% if is_paginated %}
    <nav aria-label="Page navigation">
        <ul class="pagination justify-content-center">
            {% if page_obj.has_previous %}
            <li class="page-item">
                <a href="?page={{ page_obj.previous_page_number }}" class="page-link text-primary">&lt;</a>
            </li>
            {% endif %}
            
            <li class="page-item">
                <span class="page-link text-primary page-display">
                    Page {{ page_obj.number }}
                </span>
            </li>
            
            {% if page_obj.has_next %}
            <li class="page-item">
                <a href="?page={{ page_obj.next_page_number }}" class="page-link text-primary">&gt;</a>
            </li>
            {% endif %}
        </ul>
    </nav>
    {% endif %}

```

![Navigation options for Next/Previous events based on event status](/readme-images/previous-next-nav.png)

### Events Post Page

#### Masthead banner

The masthead banner captures the user's attention by featuring the event name, an event image, and a countdown clock.

![Masthead banner](/readme-images/masthead-image.png)

The countdown clock in JavaScript begins when the DOM content loads. It calculates the time remaining until an event, retrieved from the 'eventDate' element in the HTML, begins. The countdown is updated every second in the 'countdownElement' until the event time elapses. Once the event has passed, it notifies the user that the event has finished. This concept was inspired by [Cronorunner](https://www.cronorunner.com/).

```JavaScript

document.addEventListener("DOMContentLoaded", function() {
    const eventDateElement = document.getElementById('eventDate');
    const eventDate = new Date(eventDateElement.getAttribute('data-event-date')).getTime();
    const countdownElement = document.getElementById('countdown');

    function updateCountdown() {
        const now = new Date().getTime();
        const timeLeft = eventDate - now;

        if (timeLeft < 0) {
            countdownElement.innerHTML = "Event has finished.";
            return;
        }

        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
});

```
#### Event Details 

The event details section effectively prioritizes essential information for the user, following a logic from most to least important.

![Event Details](/readme-images/event-details.png)

#### Comments section

Users will encounter different states based on their login status.

#### Comments section - not logged in

![Comments section - not logged in](/readme-images/comments-not-logged-in.png)

#### Comments section - logged in

![Comments section - logged in](/readme-images/comments-logged-in.png)

To prevent spam or attacks, users need an account to post content, and additionally, the superuser must approve these posts for added security.

#### Comments section - awaiting approval

![Comments section - awaiting approval](/readme-images/alert-waiting-aproval.png)

#### Comments section - approved ny superuser

![Comments section - approved](/readme-images/admin-comment-approved.png)

Full CRUD (Create, Read, Update, Delete) features have been implemented, allowing users to edit and delete their posts as needed.

#### Edit

![Comments section - edit](/readme-images/edit-comment.png)

#### Delete

Extra precaution has been implemented in the form of a modal to confirm if the user wants to delete their post.

```HTML

<div class="modal fade" id="deleteModal" tabindex="-1" aria-labelledby="deleteModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="deleteModalLabel">Delete comment?</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                Are you sure you want to delete your comment? This action cannot be undone.
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <a id="deleteConfirm" href="#" class="btn btn-danger">Delete</a>
            </div>
        </div>
    </div>
</div>

```
![Comments section - delete](/readme-images/delete-comment.png)

#### List of Participants

It is crucial that only registered users can sign up for events to bolster security and prevent potential spam attacks. 

##### List of particpants - unregistered

![List of particpants - unregistered](/readme-images/list-of-participants-unregister.png)

##### List of particpants - registered

![List of particpants - registered](/readme-images/list-of-participants-sign-up.png)

I've chosen to make the list of participants public, which is common in the running community, as it encourages runners to join when they see friends participating. There could potentially be compliance issues with the General Data Protection Regulation (GDPR) that need to be addressed before launching this site live.

When users sign up or unregister, they will receive an automated email to confirm this sending an automatic confirmation email when runners sign up is beneficial because it provides immediate assurance to users that their registration was successful, reduces uncertainty, and helps verify the accuracy of their provided email address.

##### Email template - Sign up

![Email template - Sign up](/readme-images/sign-up-confirmation-email.png)

##### Email template - Unregister

![Email template - Unregister](/readme-images/unregister-confirmation.png)

To do this, I used a free service called [Ethereal](https://ethereal.email) as it offers temporary email addresses that receive emails without needing a real account. It's free, easy to use, and provides a web interface to view received emails, making it ideal for debugging and testing SMTP sending from applications without privacy concerns. The main functionality of this code is configured in the settings.py file:

```Python

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.ethereal.email'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True 

EMAIL_ADMIN_ADDRESS = os.environ.get("EMAIL_ADMIN_ADDRESS")
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_ADMIN_ADDRESS")
SERVER_EMAIL = os.environ.get("EMAIL_ADMIN_ADDRESS")

```
The variables `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, and `EMAIL_ADMIN_ADDRESS` store sensitive information. To enhance security, they were moved to the env.py file and linked using `os.environ.get()`.

A key design feature was ensuring careful management of event capacity. This was achieved by allowing users to sign up only once and restricting signups to not exceed the maximum number of participants set for each event. When a user signs up, the number of places reduces by 1. If all places are allocated, the event is listed as sold out.

![List of participants - full capacity ](/readme-images/list-of-participants-full-capacity.png)

```Python

{% if remaining_places > 0 %}
{% if user_signed_up %}
<button type="button" id="unregisterButton" class="btn btn-danger">Unregister</button>
{% else %}
<button type="button" id="signupButton" class="btn btn-primary">Sign Up</button>
{% endif %}
{% else %}
{% if user_signed_up %}
<button type="button" id="unregisterButton" class="btn btn-danger">Unregister</button>
{% else %}
<p>No more places available</p>
{% endif %}

```
###  Account Page

![Account page ](/readme-images/accounts-page-general.png)

From the account page, users have full CRUD availability, enabling them to change their name and email address, update their password, and delete their account as needed. It was decided not to allow users to change their username to avoid confusion and tracking difficulties in user activity and interactions over time. Email confirmations are sent to verify each user action.

#### Update profile

![Update profile](/readme-images/accounts-update-status.png)

##### Update profile confirmation email

![Update profile confirmation email](/readme-images/account-update-email.png)

##### Change password

![Change password](/readme-images/account-change-password-status.png)

##### Change password confirmation email

![Change password confirmation email](/readme-images/password-changed-email.png)

##### Delete account

Since deleting an account is irreversible, I added an additional layer of protection for the user through a modal box, where the user must enter their current password again.

###### Delete account modal

![Delete account modal](/readme-images/delete-modal.png)

##### Delete account email confirmation

![Delete account email confirmation](/readme-images/delete-account-confirmation-email.png)

### Contact Us Page

The 'Contact Us' page serves as a 'last resort' form where users can easily send a message to the site webmaster. If the user is already logged in, they are not required to enter their name or email address and this information cannot be edited.

#### Contact us form when user is logged in

![Contact us form when user is logged in](/readme-images/contact-us-form-logged-in.png)

##### Contact us form when user is not logged in

![Contact us form when user is not logged in](/readme-images/contact-us-form.png)

Standard validation is employed to ensure that no fields are left blank and that a valid email address has been entered.

The webmaster will receive a copy of the message in their email account, and the message will also be available in Django's backend.

##### Email message

![Email message](/readme-images/contact-form-email.png)

##### Django Backend

![Django Backend](/readme-images/contact-form-email-backend.png)

### Django Admin

The site has been designed so that the superuser manually grants users 'staff status,' enabling them to post running events and manage their own events. It is crucial to ensure that staff users only have access to their own events to uphold privacy and data protection. To achieve this, the following code was used in admin.py:

```Python

    def get_queryset(self, request):
        """
        Limit queryset based on user permissions.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.is_staff:
            return qs.filter(author=request.user)
        return qs.none()

```
#### Superuser view of post events

![Superuser view of post events](/readme-images/post-event-admin-view.png)

#### Staff user view of post events

![Staff user view of post events](/readme-images/post-event-staff-user-view.png)

#### Post events - Add post event

Approved users can post their own events by completing the following form:

![Post events - Add post event](/readme-images/add-post-event-admin-view.png)

By integrating Summernote into Django, it enhances content creation through a user-friendly WYSIWYG editor, simplifies integration, allows for customization, ensures security, improves user experience, and supports scalability for comprehensive content management requirements.

#### Export list of participants

As a race organizer, it's crucial to have easy access to an up-to-date list of participants. To facilitate this, a module named `export_participants` was created in admin.py. This module allows users to export a CSV file by selecting it from a dropdown menu.

```Python

def export_participants(modeladmin, request, queryset):
    """
    Custom admin action to export participants of selected events as a CSV file.
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="participants.csv"'

    writer = csv.writer(response)
    writer.writerow(['Event Name', 'Event Date', 'Participant Number', 'First Name', 'Last Name', 'Signup Date'])

    for event in queryset:
        signups = EventSignUp.objects.filter(event=event).order_by('signed_up_on')
        for index, signup in enumerate(signups, start=1):
            writer.writerow([
                event.event_name, 
                event.date.strftime('%d %B %Y %H:%M'), 
                index, 
                signup.user.first_name, 
                signup.user.last_name,
                signup.signed_up_on.strftime('%d %B %Y %H:%M')
            ])

    return response

export_participants.short_description = "Export participants for selected events"

```
#### View in admin - export csv

![View in admin - export csv](/readme-images/export-participants-list-admin.png)

#### Screenhot of exported csv file

![Screenhot of exported csv file](/readme-images/participants-list-csv.png)

### Future Features

For future releases, I envision incorporating a payment system, which would enhance user experience by allowing seamless transactions. Additionally, integrating social media connectivity will enable users to log in using their social media accounts and effortlessly share the races they participate in.

## Validation, Testing & Bugs

### Validation

To ensure Python files (.py extensions) are PEP8 valid, the following protocol was followed:

1. Installing Black (`$ pip install black`)
2. Update requirements (`$ pip freeze >> requirements.txt`)
3. Run Black (`$ black .`)
4. Run Black to format Python files with a specific line length of 79 characters (`$ black --line-length 79 .`)
5. Manual check all .py files with CI Python Linter. I created `list_py_files.py` to extract the file names of all .py files in the project and tested it only on the files I worked on.

#### CI Python Linter Screenshot

![ci-python-linter-screenshot.png](/readme-images/ci-python-linter-screenshot.png)

Using this method, I successfully validated all my Python code. The only exception I encountered was in the settings.py file*, where the `AUTH_PASSWORD_VALIDATORS` variable exceeded the recommended 79 characters.

<table>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Directory</th>
    <th style="border: 1px solid black; padding: 8px;">File</th>
    <th style="border: 1px solid black; padding: 8px;">Result</th>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">accounts</td>
    <td style="border: 1px solid black; padding: 8px;">forms.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">accounts</td>
    <td style="border: 1px solid black; padding: 8px;">test_forms.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">accounts</td>
    <td style="border: 1px solid black; padding: 8px;">urls.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">accounts</td>
    <td style="border: 1px solid black; padding: 8px;">views.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">contact</td>
    <td style="border: 1px solid black; padding: 8px;">forms.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">contact</td>
    <td style="border: 1px solid black; padding: 8px;">models.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">contact</td>
    <td style="border: 1px solid black; padding: 8px;">test_forms.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">contact</td>
    <td style="border: 1px solid black; padding: 8px;">urls.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">contact</td>
    <td style="border: 1px solid black; padding: 8px;">views.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">admin.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">forms.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">models.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">test_forms.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">urls.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">utils.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">views.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">myproject</td>
    <td style="border: 1px solid black; padding: 8px;">settings.py</td>
    <td style="border: 1px solid black; padding: 8px;">FAIL *</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">myproject</td>
    <td style="border: 1px solid black; padding: 8px;">urls.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">myproject</td>
    <td style="border: 1px solid black; padding: 8px;">views.py</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
</table>

#### HTML Validation

To validate the HTML code, all static files had to be deployed and checked manually (logged out and logged in where appropriate) using the [Markup Validation Service](https://validator.w3.org/). I created list_html_files.py to extract the file names of all .html files in the project and tested it only on the files I worked on.

<table>
  <tr>
    <th style="border: 1px solid black; padding: 8px;">Directory</th>
    <th style="border: 1px solid black; padding: 8px;">File</th>
    <th style="border: 1px solid black; padding: 8px;">Result</th>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">accounts</td>
    <td style="border: 1px solid black; padding: 8px;">account_admin.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">accounts</td>
    <td style="border: 1px solid black; padding: 8px;">account_deleted_email.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">accounts</td>
    <td style="border: 1px solid black; padding: 8px;">account_updated_email.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">accounts</td>
    <td style="border: 1px solid black; padding: 8px;">password_changed_email.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">contact</td>
    <td style="border: 1px solid black; padding: 8px;">contact.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">signup_confirmation_email.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">unregistration_confirmation_email.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">events_list.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">landing_page.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">events_listing</td>
    <td style="border: 1px solid black; padding: 8px;">postevent_detail.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">templates</td>
    <td style="border: 1px solid black; padding: 8px;">400.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">templates</td>
    <td style="border: 1px solid black; padding: 8px;">403.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">templates</td>
    <td style="border: 1px solid black; padding: 8px;">404.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">templates</td>
    <td style="border: 1px solid black; padding: 8px;">500.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">templates</td>
    <td style="border: 1px solid black; padding: 8px;">base.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">templates</td>
    <td style="border: 1px solid black; padding: 8px;">account/login.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">templates</td>
    <td style="border: 1px solid black; padding: 8px;">account/signup.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
  <tr>
    <td style="border: 1px solid black; padding: 8px;">templates</td>
    <td style="border: 1px solid black; padding: 8px;">account/logout.html</td>
    <td style="border: 1px solid black; padding: 8px;">PASS</td>
  </tr>
</table>

Because of the way Django renders code when loading forms, such as `<span class="helptext">`, it is not possible to validate these lines.

##### Example of Django code that throws errors

![Example of Django code that throws errors](/readme-images/django-code-with-html-errors.png)

CSS Validation

To validate the CSS used in the project, I first ran `python manage.py collectstatic` from the command line and deployed the project on Heroku. Then, I selected the 'View Source' option by right-clicking on the webpage, located 'style.css', and opened it in a separate window. Finally, I ran this code through [The W3C CSS Validation Service - Jigsaw](https://jigsaw.w3.org/css-validator/) for validation. The results were as follows:

#### CSS Validation Results

![CSS Validation Results](/readme-images/css-validator-results.png)

#### JS Validation

All JS files are located in 'static/js', making them easy to locate and manually validate using [JS Hint](https://jshint.com/).

![JS Hint Results](/readme-images/screenshot-jshint.png)

| Folder       | File                | Result |
|--------------|---------------------|--------|
| static/js/   | account_admin.js    | PASS   |
| static/js/   | comments.js         | PASS*   |
| static/js/   | countdown.js        | PASS   |
| static/js/   | filter_form.js      | PASS   |
| static/js/   | signup.js           | PASS*   |

All files passed, with two files highlighting `One undefined variable - 27 bootstrap`. I chose to ignore this warning because it's typically harmless if the code functions correctly with Bootstrap. Validators can occasionally misinterpret external dependencies, so it's crucial to grasp the context and ensure proper usage of variables and libraries.

#### Lighthouse

The site performed very well on a Lighthouse test, with overall performance being rated at 99 and accessibility at 95.

![Lighthouse Report](/readme-images/light-house-report.png)

### Testing

#### User stories testing

<table border="1" cellspacing="0" cellpadding="8">
  <tr>
    <th>Epic</th>
    <th>User Story</th>
    <th>Acceptance Criteria</th>
    <th>Result</th>
  </tr>
  <tr>
    <td rowspan="2">EPIC 1: Event Discovery and Browsing</td>
    <td>As a runner, I want to filter events by categories so that I can narrow down the list to relevant races.</td>
    <td>
      <ul>
        <li>Users can filter events by categories such as road race, trail, or mixed.</li>
        <li>Filtered events are displayed correctly according to the selected categories.</li>
      </ul>
    </td>
    <td>PASS</td>
  </tr>
  <tr>
    <td>As a runner, I want to search for events based on various criteria so that I can find races that interest me.</td>
    <td>
      <ul>
        <li>Users can search for events such as keywords, location, date, and event type.</li>
        <li>Search results are filtered accurately based on the user's input.</li>
      </ul>
    </td>
    <td>PASS</td>
  </tr>
  <tr>
    <td>EPIC 1: Event Discovery and Browsing</td>
    <td>As a runner, I want to view detailed information about an event so that I can decide if I want to participate.</td>
    <td>
      <ul>
        <li>Event details page displays accurate information including date, location, distance, and event description.</li>
        <li>Users can navigate to the event details page from the search results or event listings.</li>
      </ul>
    </td>
    <td>PASS</td>
  </tr>
  <tr>
    <td rowspan="3">EPIC 2: User Registration and Login</td>
    <td>As a runner, I want to register for an account so that I can access the platform's features.</td>
    <td>
      <ul>
        <li>Users can register for an account by providing their name, email, username, and password.</li>
        <li>Registration form validates input fields and displays appropriate error messages for invalid entries.</li>
      </ul>
    </td>
    <td>PASS</td>
  </tr>
  <tr>
    <td>As a registered user, I want to log in to the website so that I can access my account.</td>
    <td>
      <ul>
        <li>Registered users can log in using their email/username and password.</li>
        <li>Logged-in users are redirected to the homepage/dashboard after successful authentication.</li>
      </ul>
    </td>
    <td>PASS</td>
  </tr>
  <tr>
    <td>As a site user, I can update my account details and also delete my account.</td>
    <td>
      <ul>
        <li>Account Update:</li>
        <ul>
          <li>Users can access the account update form from their account page.</li>
          <li>The form includes fields for updating personal details (e.g., name, email, password).</li>
          <li>All fields are pre-populated with the user's current information.</li>
          <li>Users can submit the form to save changes.</li>
          <li>Upon successful update, users receive a confirmation message.</li>
          <li>Validation errors are displayed if the form submission is invalid (e.g., email format, required fields).</li>
          <li>Password fields should have proper validation (e.g., minimum length, matching confirmation).</li>
          <li>Users can see the changes reflected immediately on their account page after update.</li>
          <li>This area will not be visible to users not logged in.</li>
        </ul>
        <li>Account Deletion:</li>
        <ul>
          <li>Users can access the account deletion option from their account page.</li>
          <li>A confirmation prompt appears to confirm the deletion action.</li>
          <li>Users must re-enter their password to confirm the deletion.</li>
          <li>Upon successful deletion, the user's account and all associated data are permanently removed.</li>
          <li>Users receive a confirmation message that their account has been deleted.</li>
          <li>Users are redirected to the homepage after account deletion.</li>
        </ul>
      </ul>
    </td>
    <td>PASS</td>
  </tr>
  <tr>
    <td rowspan="2">EPIC 3: Event Registration</td>
    <td>As a registered runner, I want to cancel my registration for an event in case I am unable to attend, so that it can be made available to other runners.</td>
    <td>
      <ul>
        <li>A "Cancel Registration" option is available on the events listing page.</li>
        <li>When selecting the "Cancel Registration" option, the user is prompted to confirm the cancellation to prevent accidental cancellations.</li>
        <li>After confirming the cancellation, the registration is marked as cancelled in the system, and the event's available registration count is incremented accordingly.</li>
        <li>A confirmation message is displayed to the user upon successful cancellation, and the cancelled registration is removed from their list of registered events.</li>
      </ul>
    </td>
    <td>PASS</td>
  </tr>
  <tr>
    <td>As a user, I want to see the number of remaining places for an event so that I can gauge availability and make informed decisions about registering for the event.</td>
    <td>
      <ul>
        <li>On the event details page, the number of remaining places is displayed prominently.</li>
        <li>If all places have been allocated, the message "Remaining places: 0" is displayed instead of the remaining places count.</li>
        <li>The remaining places count is updated in real-time as places are allocated.</li>
      </ul>
    </td>
    <td>PASS</td>
  </tr>
  <tr>
    <td>EPIC 3: User Registration and Login</td>
    <td>As a registered user, I can sign up for an event by clicking a 'sign-up' button so that I can participate in the race.</td>
    <td>
      <ul>
        <li>Users can click button to sign up.</li>
        <li>User's full name is added to participants list.</li>
        <li>User receives an email confirmation of sign-up and unregister.</li>
      </ul>
    </td>
    <td>PASS</td>
  </tr>
  <tr>
    <td>EPIC 4: Event Management for Organizers</td>
    <td>As an event organizer, I want to view registrations for my events so that I can manage participant details effectively.</td>
    <td>
      <ul>
        <li>Organizers can view a list of registered participants for their events.</li>
        <li>Participant list displays accurate registration details including name, email, and registration status.</li>
      </ul>
    </td>
    <td>PASS</td>
  </tr>
</table>

#### Automated Testing

Unit testing was used to implement automated tests on custom `forms.py` files. The `test.py` file was copied and renamed to `test_forms.py` in each directory. The tests were then run via the command prompt using the command `python manage.py test <directory_name>`.

Example of Unittest being run

![Example of Unittest being run](/readme-images/screenshot-automated-test.png)

##### Accounts

The test suite for `CustomUserChangeForm` in the given code includes three main test cases. Firstly, it tests the form with valid data to ensure it validates correctly. Secondly, it tests the form with blank data to verify that required fields trigger appropriate validation errors. Lastly, it checks that the username field is set as read-only, ensuring that this attribute is correctly applied to the form. The tests use a setup method to create a sample user and set initial form data for testing.

Status: **PASS**

##### Contact

The tests for the `ContactForm` class ensure the form's validation logic works correctly. They include verifying that the form is valid when all fields are filled with correct data, checking that the form is invalid when submitted with blank data and confirming that appropriate error messages are displayed for required fields. Additionally, the tests ensure that the form is invalid when an invalid email address is provided, verifying that the correct error message is shown for the email field.

Status: **PASS**

#### Events Listing

The tests for the `CommentForm` and `CustomSignupForm` classes ensure that these forms behave correctly under different scenarios. The `CommentForm` test verifies that the form is valid when submitted with valid data, specifically checking if the form accepts a comment body. On the other hand, the tests for `CustomSignupForm` cover various aspects: the first test validates that the form is valid when provided with matching passwords, and further checks ensure that the form's save method correctly creates a new user instance with the submitted data. The final test for `CustomSignupForm` ensures that the form fails validation when the passwords provided do not match, confirming that the appropriate error message is displayed in such cases. These tests collectively ensure that both forms handle input validation and data saving as expected in their respective contexts.

Status: **PASS**

#### Test Cases

To restrict access to appropriate content, the `@login_required` decorator was implemented. Additionally, staff users can only view events they have created, as managed through Django Admin (see [django-admin](#django-admin)).

#### Viewport Testing

Viewport Testing involved physically testing the project's responsiveness across various devices with different viewports. The test included mobile phones with small and large viewports, as well as tablets. Additionally, testing was conducted on PCs with resolutions of 1366px * 768px (HD) and 1920px * 1080px (Full HD).

##### Screenshot - Desktop
![Screenshot - Desktop](/readme-images/screenshot-desktop.png)

##### Screenshot - Tablet
![Screenshot - Tablet](/readme-images/screenshot-ipad.png)

##### Screenshot - Mobile
![Screenshot - Mobile](/readme-images/screenshot-mobile.png)


The expected outcome was for the project to display correctly without any distortion on all tested devices. The  result confirmed that there were **no issues** or content distortions observed across any of the tested devices. Therefore, the overall result of the viewport testing was deemed successful, with the project passing all criteria without any discrepancies.

### Compatibility Testing

The website was tested on all major browsers, including Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, and Safari. The expected outcome was that the project would function correctly in all these browsers.

#### Comparing Chrome and Edge

![Comparing Chrome and Edge](/readme-images/edge-vs-chrome-screenshot.png)

The result showed that there were no functionality issues, all navigation links worked, and the form responded appropriately to empty fields. 

### Bugs

Bugs were reported on the Kanban board with all bugs being resolved. Two items required attention:

Bugs Screenshot

![Bugs screenshot](/readme-images/bugs-screenshot.png)

| Issue                                                          | Page                        | Solution                                                          |
|----------------------------------------------------------------|-----------------------------|-------------------------------------------------------------------|
| After an event has passed, the option to register/unregister still is useable   | postevents_details.html     | Implement an if statement to check if the date has passed when the page loads. If it has, remove the button accordingly.               |
| Navbar's 'sticky' behaviour obscures main content               | base.html                   | Change from `fixed` to `sticky` class.|

## Deployment 

### 6.1. Transfer of Progress from IDE 

**Task:** Ensure Regular Commits to Avoid Data/Progress Loss.

**Method:**
- Use `git add [filename]` to stage specific files. Alternatively, use `git add .` to stage all changed files.
- Execute `git commit -m "[commit description]"` to queue commits with descriptive messages.
- Utilize `git push` to push all commits to the remote repository on GitHub.

### 6.2. Offline Cloning

**Task:** Use Repository on Local Machine.

**Method:**
1. Navigate to GitHub and locate your repository.
2. Click on "Code" -> "HTTPS" -> Copy button to copy the repository link.
3. Open your local coding environment and type `git clone [copied link]` to clone the repository locally.

### 6.3.2. ElephantSQL

**Task:** Obtain Database URL for Project's Database.

**Method:**
1. Select a database provider (e.g., ElephantSQL).
2. Navigate to [ElephantSQL](https://www.elephantsql.com/) and register a new account.
3. Log in to ElephantSQL with your newly created account credentials.
4. Navigate to "+ Create New Instance".
5. Select Name, Plan, and Region for your database instance.
6. Confirm the instance by clicking "Create Instance".
7. Obtain the database URL in the format `postgres://NAME:PASSKEY@flora.db.elephantsql.com/NAME`.
8. Update `settings.py` in the project directory with the obtained database URL.

### 6.3.3. Cloudinary

**Task:** Obtain Cloudinary URL for Project's Static Storage.

**Method:**
1. Select a static storage provider (e.g., Cloudinary).
2. Navigate to [Cloudinary Console](https://console.cloudinary.com/) and register a new account.
3. Log in to Cloudinary with your newly created account credentials.
4. Navigate to "+ Add a new environment".
5. Confirm your selection.
6. Obtain the Cloudinary URL in the format `cloudinary://USER:PASSKEY@ENVIRONMENT`.
7. Update `settings.py` in the project directory with the obtained Cloudinary URL.

### 6.3.4. Settings.py & File-tree

**Task:** Prepare `settings.py` and file structure for deployment.

**Method:**
1. Create a file named `env.py` to store all sensitive information.
2. Refer to the example of `env.py` file.
3. Add `env.py` to `.gitignore` to prevent it from being uploaded to GitHub.
4. Update `settings.py` with `import os`.
5. For every secured variable, add the code `VARIABLE = os.environ.get("VARIABLE")`.
6. Ensure this process for Gmail, ElephantSQL, Cloudinary, DEBUG, and Django Secret Key.
7. Update default database settings in `settings.py`:
   ```python
   if "DATABASE_URL" in os.environ:
       DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
   else:
       DATABASES = {
           "default": {
               "ENGINE": "django.db.backends.sqlite3",
               "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
           }
       }

8. Update default static settings in settings.py:
```Python
STATIC_URL = "/static/"
STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")
MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
```
9. Update email settings in settings.py:
```Python
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
```
10. Migrate your database models to ElephantSQL using python manage.py migrate command.
11. Create directories ./static and ./templates.
12 Commit and push changes to GitHub.

### Deployment to Heroku

**Task:** Ensure Users Can View Live Version of Aneta's Glimmer Project.

**Method:**
1. Register and log in to [Heroku](https://www.heroku.com/).
2. Navigate to "New" > "Create New App".
3. Select a unique name for your app.
4. Navigate to "Settings" > "Reveal Config Vars".
5. Add all variables from `env.py` to Config Vars of your Heroku App.
6. Add a variable pair `PORT:8000`.
7. For testing deployment, add a variable pair `COLLECT_STATIC:1`.
8. Add the Heroku app URL into `ALLOWED_HOSTS` in `settings.py`.
9. In the root directory, create a file named `Procfile`.
10. Navigate to "Deploy" > "GitHub" > "Connect".
11. Navigate to "Deploy" > "Deploy Branch".
12. Optionally, enable automatic deploys.
13. Check the deployment log - if successful, you will be prompted with an option to view the live page.

(Source: [tomik-z-cech](https://github.com/tomik-z-cech/PP4-Aneta-s-Glimmer/blob/main/README.md#6-deployment))

## Technologies Used

| Technology         | Description                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------|
| Django             | Primary framework used for backend development in the project.                                 |
| Python             | Core backend programming language employed throughout the project.                            |
| HTML               | Markup language utilized for creating frontend templates.                                      |
| CSS                | External stylesheet (`./static/css/style.css`) applied to style the project.                   |
| JavaScript         | Frontend scripting language employed for interactive web elements.                             |
| Bootstrap v. 5.3   | Frontend framework adopted for building responsive, mobile-first web applications.             |
| Heroku             | Cloud platform utilized for deploying the project.                                              |
| Balsamiq           | Software tool utilized for designing wireframes and mockups.                                    |
| Git                | Version control system used to manage changes and project history.                              |
| GitHub             | Hosting service for storing Git repositories and facilitating collaboration.                   |
| Gitpod             | Online IDE initially used for developing the project.                                           |
| Requirements.txt   | File listing Python packages required for the project, facilitating environment setup.         |

### Requirements.txt

The following modules were used in development of the Run it! website:

| Module Name              | Description                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| asgiref==3.8.1           | ASGI specification reference implementation, used for building asynchronous Python web applications. |
| astroid==3.2.2           | Abstract Syntax Tree (AST) manipulation library for Python, used in static analysis tools like pylint. |
| black==24.4.2            | Code formatter for Python, ensuring consistent code style across projects.                     |
| Brotli==1.1.0            | Python bindings for the Brotli compression algorithm, providing lossless data compression.       |
| chardet==5.2.0           | Character encoding auto-detection in Python, used to determine the encoding of text files.       |
| click==8.1.7             | Command line interface creation kit for Python, simplifying the process of writing command line tools. |
| cloudinary==1.36.0       | Python SDK for Cloudinary, a cloud service for managing media assets.                            |
| crispy-bootstrap5==0.7   | Django forms plugin that seamlessly integrates Bootstrap 5 styles with crispy-forms.             |
| cssselect2==0.7.0        | CSS selector library for Python, facilitating the selection of HTML elements using CSS selectors. |
| dj-database-url==0.5.0   | Django utility for utilizing database URLs in configuration, simplifying database connection settings. |
| dj3-cloudinary-storage==0.0.6 | Django storage backend for Cloudinary, allowing seamless integration of Cloudinary with Django projects. |
| Django==4.2.13           | High-level Python web framework that encourages rapid development and clean, pragmatic design.   |
| django-allauth==0.57.2   | Django package for handling authentication, registration, account management, and social authentication. |
| django-crispy-forms==2.1 | Django forms application that helps manage forms rendering in a DRY (Don't Repeat Yourself) manner. |
| django-sendgrid-v5==1.2.3| Django integration with SendGrid API for sending transactional and marketing email.              |
| django-summernote==0.8.20.0 | Django integration with Summernote WYSIWYG editor for text and HTML content editing.             |
| fonttools==4.53.0        | Library for manipulating fonts in Python, used for reading, writing, and converting font files. |
| gunicorn==20.1.0         | Python WSGI HTTP server for UNIX, used to run Python web applications in production environments. |
| html5lib==1.1            | HTML parser library for Python, used for parsing HTML documents and cleaning up markup.          |
| oauthlib==3.2.2          | Library for implementing OAuth 1.0 and OAuth 2.0 in Python, facilitating authentication processes. |
| pathspec==0.12.1         | Library for matching file paths against Unix shell-style patterns, used in git and other tools. |
| pillow==10.3.0           | Python Imaging Library (PIL) fork that adds support for opening, manipulating, and saving many different image file formats. |
| psycopg2==2.9.9          | PostgreSQL adapter for Python, allowing Python to connect to PostgreSQL databases.             |
| pydyf==0.10.0            | Python library for creating and modifying PDF files.                                             |
| PyJWT==2.8.0             | JSON Web Token (JWT) implementation in Python, used for securely transmitting information between parties. |
| pyphen==0.15.0           | Library for hyphenating words in Python, used for text processing and formatting.               |
| python-http-client==3.3.7| Simple HTTP client library for Python, facilitating making HTTP requests.                        |
| python3-openid==3.2.0    | Python 3 implementation of the OpenID Connect protocol for user authentication.                 |
| requests-oauthlib==2.0.0 | OAuth library for Python requests, providing OAuth client support for Python applications.       |
| sqlparse==0.5.0          | Non-validating SQL parser for Python, used for parsing SQL queries and formatting SQL code.      |
| starkbank-ecdsa==2.2.0   | Library for ECDSA cryptography in Python, used for cryptographic operations.                    |
| urllib3==1.26.18         | HTTP client library for Python, used for handling HTTP requests and responses.                  |
| whitenoise==5.3.0        | Simplified static file serving for Python web applications, enhancing Django's static file handling. |
| zopfli==0.2.3            | Compression library for Python, providing higher compression ratios than typical zlib.          |

## Credits

* My mentor, Akshat Garg.
* The CodeStar walkthrough project, which formed the foundation for this project.
* [Cronorunner](https://www.cronorunner.com/), which assisted with various stages of registering for a running event. 
* ChatGPT, which acted as a virtual teacher.
* A fellow Code Institute student, tomik-z-cech, whose readme served as a blueprint for mine.