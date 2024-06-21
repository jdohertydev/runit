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

### Custom Error Pages

I have created custom error pages for 400, 403, 404, and 500 errors that enhance user experience by offering helpful navigation options, maintaining brand consistency, and reducing frustration through humorous running-related puns. This involved creating custom templates and linking them via the urls.py file and views.py.

url.py

```Python

# Custom error handlers
handler400 = 'myproject.views.custom_400_view'
handler403 = 'myproject.views.custom_403_view'
handler404 = 'myproject.views.custom_404_view'
handler500 = 'myproject.views.custom_500_view'

```
views.py

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

