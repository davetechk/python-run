# The Python Run

We're working through **CS50P** — Harvard's Introduction to Programming with
Python. One hour a day, six days a week. Lectures 0 to 9, then a final project.


| Precious | heading for AI |
| Ebere | heading for Django |
| Zidyep | heading for Django |

---

## The schedule

| Lecture | Topic                       | Dates          |
|---      |---                          |---             |
| L0      | Functions, Variables        | Sept 2 – 4     |
| L1      | Conditionals                | Sept 5 – 7     |
| L2      | Loops                       | Sept 8 – 10    |
| L3      | Exceptions                  | Sept 11 – 13   |
| L4      | Libraries                   | Sept 14 – 16   |
| L5      | Unit Tests                  | Sept 17 – 20   |
| L6      | File I/O                    | Sept 21 – 24   |
| L7      | Regular Expressions         | Sept 25 – 28   |
| L8      | Object-Oriented Programming | Sept 29 – Oct 2 |
| L9      | Et Cetera                   | Oct 3 – 6      |
| —       | Final project               | Oct 7 – 13     |

Lectures 6 to 9 are much harder than 0 to 4. If we slow down there, that's
normal. We adjust, we don't quit.

---

## The rules

**1. Post your progress in the group, not privately.**
"Done with L2, pset 3 is stressing me" is enough.

**2. Ask each other first.**
If one person is stuck, the other tries before anyone else jumps in.
Nobody here is the teacher.

**3. Sunday evenings we check in.**
Where you are, what's next. Every Sunday.

**And if you miss a day, don't do two hours the next day.** Just do your hour.
Missing one day is fine. Missing two in a row is the thing to avoid.

---

## How the repo works

Everyone has their own folder. Yours is the only one you write in.

```
python-run/
├── precious/
├── ebere/
└── zidyep/
```

**Only open someone else's folder after you've pushed your own.** That way
nobody gets spoiled by accident.

### Where your files go

One folder per problem set. One file per problem.

```
zidyep/
├── pset0/
│   ├── indoor.py
│   ├── playback.py
│   ├── faces.py
│   ├── einstein.py
│   └── tip.py
├── pset1/
│   ├── deep.py
│   ├── bank.py
│   └── ...
└── pset2/
```

**Use the exact filename CS50 gives you on the problem page.** Don't rename
anything — `check50` looks for that specific name and will fail if it's
different.

---

## Git, the short version

Once, to get the repo on your laptop:

```bash
git clone https://github.com/davetechk/python-run.git
cd python-run
```

Every time you finish something:

```bash
git add .
git commit -m "pset0 done"
git push
```

Before you start each day, to pull down what the others pushed:

```bash
git pull
```

If git fights you, send your file in the group and we'll sort the git part
later. Don't let git stop you doing the lecture.

---

## Links

- [Problem sets](https://cs50.harvard.edu/python/psets/)
- [CS50P course page](https://cs50.harvard.edu/python/)
- [Git in 1 hour](https://youtu.be/8JJ101D3knE)