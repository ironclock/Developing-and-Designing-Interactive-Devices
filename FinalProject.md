## Team Members

Shai "The Bacchanalian" Aarons (sla88) 🕺

Ariana "The One Who Sees All" Bhigroog (ab2959) ❤️‍🔥

Jon "The Apparatus" Caceres (jc3569) 🚀

Rachel "The Weaver" Minkowitz (rhm256) 🍄

Amando "The Miracle Worker" Xu (ax45) ✨

## Final Project Big Idea
![PeePass-logos_black](https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/25d9c15c-d581-4b26-b052-30df17db408d)

PeePass is a mobile application that connects users to nearby business restrooms offering clean toilets through an application interface and proprietary locking mechanism on bathroom doors. 

PeePass is a cool mobile app that makes finding a clean restroom a breeze. With a simple interface, it connects users with nearby businesses that offer top-notch toilets. Plus, its seamless integration with a proprietary bathroom security system and locking mechanism adds an extra layer of privacy for an *elite bathroom experience*.

Imagine you're out and about, and suddenly, you need to use the restroom. Public restrooms trigger some sort of a trauma for you. Don't fret. Whip out PeePass, find the closest restroom, scan your QR code and viola sparkling clean toilet for you to use. The app's design is easy to navigate, making your bathroom quest a piece of cake.

But here's the real kicker: PeePass isn't just about finding a restroom; it's about making the whole experience better. The bathroom doors come with this cool proprietary lock. It's not just a lock; it's like your personal VIP entry to a clean and comfy oasis.

So, whether you're in the middle of the city or just exploring, PeePass is your restroom sidekick. It's all about keeping things simple, making sure you find a great restroom without any fuss, and enjoying a bit of extra privacy with that snazzy door lock. Say goodbye to restroom stress and hello to hassle-free pit stops with PeePass!

## Objective

Our objective is to create a 3D miniature bathroom setting with would *simulate* a user journey of someone using PeePass. The model would include a life size lock on the 'door' that would unlock using a prototype version of the PeePass app and QR code connected to our Raspberry Pi. Most importantly, for fun, we plan to include lasers inside the bathroom when the door is locked. The lasers are deactivated when the door is unlocked.

## Deliverables

### Project Plan:

### 1. Conceptualization and Design (Week 1)

- **Designing the App Interface:** Basic functionality for NFC scanning and keypad code entry.
- **3D Bathroom Model Design:** Plan the dimensions, placement of the door lock, and interior details like the toilet and bathtub.
- **Laser System Conceptualization:** Determine the placement and type of lasers and how they will be integrated.

### 2. Development and Procurement (Weeks 2-3)

- **iOS App Development:**
    - Setup a basic user interface.
    - Implement NFC reading functionality.
    - Integrate keypad input with a 4-digit code system.
- **3D Model Printing:**
    - Finalize the design and start 3D printing components.
- **Raspberry Pi Setup:**
    - Program the Pi to respond to NFC scans and keypad inputs.
    - Integrate the electric strike lock.
- **Laser System Setup:**
    - Source the lasers and any necessary wiring (fishing wire or fiber optics).
    - Install and test the laser system within the model.

### 3. Assembly and Testing (Week 4)

- **Assemble the Bathroom Model:**
    - Install the electric strike lock and connect it to the Raspberry Pi.
    - Place the interior model pieces.
    - Set up the laser system.
- **Integration Testing:**
    - Test the iOS app with the NFC reader and keypad on the Raspberry Pi.
    - Ensure the lock mechanism works correctly.
    - Test the visibility and alignment of the laser system.

### 4. Final Adjustments and Presentation (Week 5)

- **Troubleshooting and Adjustments:**
    - Address any issues found during testing.
    - Make adjustments to the hardware or software as necessary.
- **Final Review and Demonstration:**
    - Prepare a demonstration setup.
    - Review the project against initial objectives and specifications.

 ### Functioning Project:

 ### Design Process:

 #### Background
Throughout the semester we were very excited for this Final Project. So much so, that whenever we came up with a good idea we filed it for the final project :) 

A couple of ideas we came up with throughout the semester include:
1. Building on our Bender Security System to be more efficient and robust
2. Creating a wallet that indicates which cards you have on you (i.e. insurance card, credit card A) according to colored lights
3. Smart Mirror - A mirror that displays inspirations quotes and motivating sayings if it detects someone is sad
4. Digital pet rock which responds to different interactions
5. Creating the PeePass lock which functions for Startup Studio

Although there are some cute ideas in this list, we decided to go with option 5 - starting to work on the team's next semester startup studio idea which is PeePass. Because this studio idea is very realistic, we wanted to try to simulate the real life experience of using peepass as much as possible. Ideally, we would have access to a real life bathrooom and door, but since that's not feasible we decided to simulate the experience as much as possible. With that in mind, we wanted to build a mini bathroom with a life size lock that opens via an App and QR code or keypad with proper authentication etc.

#### Initial Sketches

![IMG_12F19BD60560-1](https://github.com/ironclock/Developing-and-Designing-Interactive-Devices/assets/82296790/c7f373de-6605-419f-bf7d-c694d51dec25)

#### Storyboard

#### Development Happenings
We started development with compiling a list of sensors/components needed and buying the various items that we did not have including an NFC Scanner, a lock, a VERY large battery pack, some wood, a larger screen and a lock ---. 

Originally we had planned to use an NFC scanner to validate entrance into the restroom (using iOS NFC tokens). When we started to work on it, we realized this sensor was more complicated than we thought. The NFC scanner that we had was not working as expected and the pi was not complying with our requests. We tried various NFC Scanners (thinking that our scanner came broken at first) 


////to be deleted
3. Functioning project: The finished project should be a device, system, interface, etc. that people can interact with.

4. Documentation of design process
5. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)
6. Video of someone using your project
7. Reflections on process (What have you learned or wish you knew at the start?)
8. Group work distribution questionnaire

## Change of Design

It is fine to change your project goals, but please resubmit the project plan for the new design when you do that.

## Grading rubric

20% Project planning: Allocation of needed resources (time, people, materials, facilities) anticipated well.
20% Design of project: Interaction, hardware and software aspects of projects planned well.
20% Testing of project: Functional or wizarded system tested with people
20% Prototype functionality: System capable of interaction, either through autonomous or wizarded mechanisms
20% Project documentation: Text, video, and photo of project illustratign capability and documenting plans and process

## Teams

You can and are not required to work in teams. Be clear in documentation who contributed what. The total project contributions should reflect the number of people on the project.

## Examples

[Here is a list of good final projects from previous classes.](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/wiki/Previous-Final-Projects)

