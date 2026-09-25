from typing import NamedTuple


class MotivationalQuote(NamedTuple):
    text: str
    author: str
    source: str


_INKYPI_QUOTE_TEXTS = (
    "A small step today is still a step away from yesterday.",
    "Start before you feel ready; readiness often follows action.",
    "Consistency turns ordinary effort into uncommon results.",
    "You do not need a perfect plan to make meaningful progress.",
    "The work you repeat becomes the person you become.",
    "A difficult chapter is not the end of the story.",
    "Momentum begins with one honest attempt.",
    "Your future is shaped by what you practice today.",
    "Progress counts even when nobody else can see it yet.",
    "Make the next choice one your future self will thank you for.",
    "Courage can be quiet; sometimes it simply says, try again.",
    "You can rest without giving up.",
    "The direction matters more than the speed.",
    "Do the next useful thing, then let momentum help.",
    "Every skill was once something its owner could not do.",
    "A setback can become information instead of a verdict.",
    "Begin with what you have and improve it as you go.",
    "When motivation fades, let commitment carry you one step farther.",
    "Today is a good day to become a little more capable.",
    "The first draft of progress is allowed to be messy.",
    "Keep the promise you made to yourself this morning.",
    "Even a hard hour can hold the choice that changes your direction.",
    "You are closer once you begin.",
    "Let the challenge teach you what comfort never could.",
    "Your pace is valid as long as you keep choosing forward.",
    "Hard days still count toward a meaningful life.",
    "You do not need applause to keep becoming someone you are proud of.",
    "Confidence grows from evidence, so give yourself a small win.",
    "Each time you keep going, you prove that change is possible.",
    "There is no wasted effort when you learn from it.",
    "You can change the plan without abandoning the goal.",
    "What feels slow today may look like transformation later.",
    "Make progress simple enough that you can repeat it tomorrow.",
    "The next beginning does not need permission from the last ending.",
    "Choose improvement over proving yourself.",
    "A calm mind can still carry fierce ambition.",
    "Every moment of attention can move you closer to the life you hope to build.",
    "On days when hope feels distant, let one small action keep it alive.",
    "The mountain becomes manageable one deliberate step at a time.",
    "You have survived every day that once felt impossible.",
    "Good work compounds long before it becomes obvious.",
    "Turn comparison into curiosity, then return to your own path.",
    "Be patient with the version of you that is still learning.",
    "Protecting what matters gives your courage somewhere meaningful to go.",
    "The goal is not perfection; it is honest progress.",
    "Your next attempt gets to know everything the last one taught you.",
    "Create more evidence that you can trust yourself.",
    "Some days the win is simply refusing to quit.",
    "The life you want is built inside ordinary days.",
    "Focus on the action within reach, not the distance remaining.",
    "Growth often feels like uncertainty before it feels like strength.",
    "You are allowed to outgrow an old definition of success.",
    "Give today's effort enough time to become tomorrow's advantage.",
    "The best time to restart is the moment you notice you stopped.",
    "Rest can restore the strength that your next brave step will need.",
    "An imperfect action can teach more than a perfect intention.",
    "Make your standards kind enough to be sustainable.",
    "The next version of you is built by today's repetitions.",
    "Keep going; clarity often arrives while moving.",
    "You never lose the lesson when you choose to learn.",
)


_FAMOUS_QUOTES = (
    MotivationalQuote(
        "The only thing we have to fear is fear itself.",
        "Franklin D. Roosevelt",
        "First Inaugural Address",
    ),
    MotivationalQuote(
        "Nothing great was ever achieved without enthusiasm.",
        "Ralph Waldo Emerson",
        "Essays: Circles",
    ),
    MotivationalQuote(
        "I am the master of my fate: I am the captain of my soul.",
        "William Ernest Henley",
        "Invictus",
    ),
    MotivationalQuote(
        "To strive, to seek, to find, and not to yield.",
        "Alfred, Lord Tennyson",
        "Ulysses",
    ),
    MotivationalQuote(
        "Hope is the thing with feathers that perches in the soul.",
        "Emily Dickinson",
        "Hope",
    ),
    MotivationalQuote(
        "I took the one less traveled by, and that has made all the difference.",
        "Robert Frost",
        "The Road Not Taken",
    ),
    MotivationalQuote(
        "Well done is better than well said.",
        "Benjamin Franklin",
        "Poor Richard's Almanack",
    ),
    MotivationalQuote(
        "The doer is better than the critic.",
        "Theodore Roosevelt",
        "American Ideals",
    ),
    MotivationalQuote(
        "Character is built up on little things - little things well and honourably transacted.",
        "Samuel Smiles",
        "Thrift",
    ),
    MotivationalQuote(
        "Our doubts are traitors, and make us lose the good we oft might win, by fearing to attempt.",
        "William Shakespeare",
        "Measure for Measure",
    ),
    MotivationalQuote(
        "We are all in the gutter, but some of us are looking at the stars.",
        "Oscar Wilde",
        "Lady Windermere's Fan",
    ),
    MotivationalQuote(
        "I am not afraid of storms, for I am learning how to sail my ship.",
        "Louisa May Alcott",
        "Little Women",
    ),
    MotivationalQuote(
        "Lives of great men all remind us we can make our lives sublime.",
        "Henry Wadsworth Longfellow",
        "A Psalm of Life",
    ),
    MotivationalQuote(
        "If there is no struggle, there is no progress.",
        "Frederick Douglass",
        "West India Emancipation speech",
    ),
    MotivationalQuote(
        "Always bear in mind that your own resolution to succeed is more important than any other one thing.",
        "Abraham Lincoln",
        "Letter to Isham Reavis",
    ),
    MotivationalQuote(
        "Success is to be measured not so much by the position that one has reached in life as by the obstacles which he has overcome.",
        "Booker T. Washington",
        "Up from Slavery",
    ),
    MotivationalQuote(
        "Life is either a daring adventure or nothing.",
        "Helen Keller",
        "Let Us Have Faith",
    ),
    MotivationalQuote(
        "You must do the thing you think you cannot do.",
        "Eleanor Roosevelt",
        "You Learn by Living",
    ),
    MotivationalQuote(
        "The time is always right to do what is right.",
        "Martin Luther King Jr.",
        "Oberlin College commencement address",
    ),
    MotivationalQuote(
        "I learned that courage was not the absence of fear, but the triumph over it.",
        "Nelson Mandela",
        "Long Walk to Freedom",
    ),
    MotivationalQuote(
        "One child, one teacher, one book, and one pen can change the world.",
        "Malala Yousafzai",
        "United Nations Youth Assembly speech",
    ),
    MotivationalQuote(
        "You may encounter many defeats, but you must not be defeated.",
        "Maya Angelou",
        "Letter to My Daughter",
    ),
    MotivationalQuote(
        "Not everything that is faced can be changed, but nothing can be changed until it is faced.",
        "James Baldwin",
        "As Much Truth as One Can Bear",
    ),
    MotivationalQuote(
        "I am deliberate and afraid of nothing.",
        "Audre Lorde",
        "New Year's Day",
    ),
    MotivationalQuote(
        "You are your best thing.",
        "Toni Morrison",
        "Beloved",
    ),
    MotivationalQuote(
        "However difficult life may seem, there is always something you can do and succeed at.",
        "Stephen Hawking",
        "Oxford Union speech",
    ),
    MotivationalQuote(
        "Nothing in life is to be feared; it is only to be understood.",
        "Marie Curie",
        "Recalled in Madame Curie",
    ),
    MotivationalQuote(
        "He who has a why to live can bear almost any how.",
        "Friedrich Nietzsche",
        "Twilight of the Idols",
    ),
    MotivationalQuote(
        "When we are no longer able to change a situation, we are challenged to change ourselves.",
        "Viktor E. Frankl",
        "Man's Search for Meaning",
    ),
    MotivationalQuote(
        "In the depth of winter, I finally learned that within me there lay an invincible summer.",
        "Albert Camus",
        "Return to Tipasa",
    ),
    MotivationalQuote(
        "If you can meet with Triumph and Disaster and treat those two impostors just the same.",
        "Rudyard Kipling",
        "If-",
    ),
    MotivationalQuote(
        "Faith is the bird that feels the light and sings when the dawn is still dark.",
        "Rabindranath Tagore",
        "Fireflies",
    ),
    MotivationalQuote(
        "Where there's hope, there's life. It fills us with fresh courage and makes us strong again.",
        "Anne Frank",
        "The Diary of a Young Girl",
    ),
    MotivationalQuote(
        "If one advances confidently in the direction of his dreams, and endeavors to live the life which he has imagined.",
        "Henry David Thoreau",
        "Walden",
    ),
    MotivationalQuote(
        "You must never be fearful about what you are doing when it is right.",
        "Rosa Parks",
        "Rosa Parks: My Story",
    ),
    MotivationalQuote(
        "Do not get lost in a sea of despair. Be hopeful, be optimistic.",
        "John Lewis",
        "Message to young people",
    ),
    MotivationalQuote(
        "Change will not come if we wait for some other person or some other time.",
        "Barack Obama",
        "Super Tuesday speech",
    ),
    MotivationalQuote(
        "Your story is what you have, what you will always have. It is something to own.",
        "Michelle Obama",
        "Becoming",
    ),
    MotivationalQuote(
        "He who is not courageous enough to take risks will accomplish nothing in life.",
        "Muhammad Ali",
        "Press conference, 1977",
    ),
    MotivationalQuote(
        "A life is not important except in the impact it has on other lives.",
        "Jackie Robinson",
        "I Never Had It Made",
    ),
)


MOTIVATIONAL_QUOTES = tuple(
    MotivationalQuote(text, "InkyPi Collection", "Original quote")
    for text in _INKYPI_QUOTE_TEXTS
) + _FAMOUS_QUOTES
