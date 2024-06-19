# Key Project Information

"Run It!" is a website dedicated to listing running events. Runners can effortlessly find details about local running events, ask questions, and sign up directly through the platform. Event organisers can also use "Run It!" to post their events and manage their participant lists.

The live version of the website can be viewed at: [Run It!](https://runit-jdohertydev-773091e00a18.herokuapp.com/).

![Am I responsive](/readme-images/am-i-responsive.png)

## Table of Contents

***TO BE UPDATED***

## User Experience (UX)

### The Idea

**Run It!** is designed to be a comprehensive running event listing website. Users can effortlessly find free running events in their area and book their spots. Additionally, they can post questions about specific events, add likes, and easily contact the site webmaster.

### The Ideal User

**Target Audiences:**
- Runners of all levels interested in participating in running events.
- Race Organisers who want to list events and manage bookings through the site admin.

**The Ideal User:**
- Enjoys running and wants to participate in events.
- Desires to manage their own registrations.
- Aims to connect with other runners in their community.
- Seeks to promote and manage their events via the platform.

### Site Goals

1. **Facilitate Event Discovery:**
   - Provide a user-friendly interface for runners to easily find and book running events in their area.
2. **Enhance User Engagement:**
   - Enable users to post questions, add likes, and interact with other runners and event organisers within the platform.
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
- **Event Sign-Up:** Registered users can enroll in and confirm their participation for a selected event through the platform.
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

Landing Page

![Landing Page](/readme-images/wire-frame-landing-page.png)

Events

![Events](/readme-images/wire-frame-events.png)

Events Page Listing

![Events Page Listing](/readme-images/wire-frame-events-page-listing.png)

Accounts

![Accounts](/readme-images/wire-frame-account.png)

Contact

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


### Logo and Tagline (Looka)

I used [Looka](https://looka.com/) to create the logo used:

![Logo and Tagline ](/readme-images/logo-with-slogan.png)

### Header

The header code is centralised in base.html, ensuring consistency and facilitating future updates or modifications across the website.

![Header](/readme-images/header.png)

### Slogan

![Slogan](/readme-images/logo-with-slogan.png)

The slogan used serves to support the essence and values of my brand, leaving a memorable impression on visitors while reinforcing its identity and purpose. When viewing the website on mobile viewports, the slogan is removed to optimize screen space.

![Slogan](/readme-images/slogan-hideen-on-mobile-view.png)

```CSS
@media (max-width: 991px) {
    .slogan {
        display: none;
    }
}
```

### Dynamic menu items that adapt based on the user's login status

![Logged in](/readme-images/logged-in.png.png)

![Logged out](/readme-images/not-logged-in.png)


### Login Status

### Custom Error Pages

![Custom Error Pages](/readme-images/example-of-custom-error-page.png)

### Footer

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

#### Navigation options for Next/Previous events based on event status.

![Navigation options for Next/Previous events based on event status](/readme-images/previous-next-nav.png)

### Events Post Page

Masthead banner
- Shows event name, image and countdown lock
Event Details shows all the key information about event.
Comments section
- only registered users can comment
- approval
- edit
- delete

List of Participants
- only registered users can sign up.
- users can sign up / unregister - email confirmation is sent
- When a user signs up, the number of places reduces by 1. If all places are allocated, the event is listed as sold out
- when the event has finished, it is no longer possible to sign up

###  Account Page
- User can update profile
   - not able to change username
- Change password
- Delete account
   - modal - extra security

### Contact Us Page

Autopopulates name and email address if logged in
validates email address and ensures user writes something
response is sent to backend and emails webmaster
- Contact messages

### Django Admin

 Post events
 - Add post event
   - Summer notes
 - Users can export cvs files of participants registered on their event
 - only users who posed the event can see these lists unless superuser

