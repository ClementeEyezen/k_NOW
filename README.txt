The [k]NOW project is an attempt to create an AI that can infer and know information about
  my day to day life and provide information that I want to know now, before I think about
  needing it.

For instance, there have been times where I may have walked into a class or meeting and 
  wanted a file that may have been available on a cloud storage service, or even trickier, 
  on the computer at my desk that was not available online.
  Maybe I have the file, but I just want it to be ready and available, without having to go
  searching for it.
  Another similar example is if I have been taking notes on Evernote for instance, and I want
  to access a note, but instead of searching for it, wouldn't it be nice for it to predict
  which notes are most important and provides links/previews of relavant information?

The goal of [k]NOW is to develop an application that learns about the person using it, so that
  it can provide this type of thinking ahead service. I've decided that Google Now is too slow,
  I would like to do one better. This is the project that will do that.

METHODS
 The AI represents knowledge possibly in a number of ways. The first is
  the graph representation, which links similar concepts and has
  different levels for different levels of abstraction via 
  parent-child relations.
  
PLANS
 The next steps for the data storage development are the integration of task and contact 
  access. This will require the development of more specific node extensions, specifically
  one for people and one for actions (tasks/goals, as opposed to passive events). These will
  allow for instant integration of the applicable client libraries, and then the addition of
  methods that generate pre-formatted data, as well as accept google-format data.
 One further step would be email integration, with the aim to automatically consider events,
  contacts, actions and other data points. The first step in that process is to integrate with
  Gmail (my current mail service of choice) via IMAP or SMTP, then to determine a data type 
  that suits mail, perhaps a structured representation that is also a node-extension. Key data
  points include to, from, subject line (tokens?), content, time. It will link (node style) to
  events, actions resulting as well as contacts involved in the email.
 Another area of development is the complete encapsulation of each individual element into one
  program. For that to happen, it is important for each step (access, read, act/update) to be
  aware of what other programs are doing, and that will be achieved through file read-write
  capability, along with direct interaction. Another benefit of having files written between
  steps, at least at this point in development, is the opportunity it presents for easy 
  debugging.
 A third area of development is direct web access/reading through libcurl. This part of the
  project is less about personal integration, and more about collecting extra information to
  augment the information provided by the personal user. Through a html reader, processor and 
  possibly an information display, generic knowledge/connections can be gained from the web.
  The end goal for this portion of the project is to be able to make connections between
  ideas. If the program inputs a starting point that is part of it's current knowledge graph,
  then the web can be used to extend the graph and make more connections to make the knowledge
  more comprehensive and dense, and possibly connect areas that were not previously connected
  through just personal data.

RESOURCES/Libraries
 Currently Used
   cURL (libcurl)
   pycurl
   Google Client Library
    -Calendar
   
 Future Integration  
   Google Client Libraries
    -Tasks
    -Contacts
