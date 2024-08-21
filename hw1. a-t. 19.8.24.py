# hw1a:
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
"Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"};

oscar_winners.add("Emma Stone");
print(oscar_winners);
# If "Emma Stone" wasn't already in the set, this line would add her to it.
# Since she is already in the set, this operation won't have any effect.

#hw1b:
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"};
oscar_winners.clear();
print("cleared set is: ", oscar_winners);

#hw1c:
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone",
                 "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"};
oscar_winners_copy = oscar_winners.copy();
print("Copy of the set is: ", oscar_winners_copy);

#hw1d:
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington",
                 "Emma Stone", "Tom Hanks", "Natalie Portman",
                 "Robert De Niro", "Al Pacino"};
oscar_winners.remove("Meryl Streep");

print("The set without Meryl Streep is: ", oscar_winners)

#hw1e:
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"};
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"};

common_actors = titanic_actors.intersection(dark_knight_actors);
print("Actors who appeared in both movies: ", common_actors);

#hw1f:
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"};

common_actors = avengers_actors.intersection(iron_man_actors);
print("Check which actors appear in both movies!:", common_actors);

#hw1g:
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}

winners = actor_list.intersection(oscar_winners);   # finds the common actors between actor_list and oscar_winners.
all_won_oscar = actor_list.issubset(oscar_winners); # checks if all actors in actor_list are also in oscar_winners.

if all_won_oscar:
    print("All actors in actor_list have won an Oscar.")
else:
    print("Not all actors in actor_list have won an Oscar.")
    print("Actors who have won an Oscar:", winners)

#hw1h:
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}

# Check if all actors in actor_list are also in avengers_actors:
are_all_actors_in_avengers = actor_list.issubset(avengers_actors);
print(are_all_actors_in_avengers);

#hw1i:
import random
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}
cast_list = list(movie_cast);  # This conversion is necessary because the random.choice function can only operate on lists, not sets.
# Pick a random actor
actor_to_remove = random.choice(cast_list);
# Remove the actor from the set using discard
movie_cast.discard(actor_to_remove); # The discard method is used to remove actor_to_remove from the movie_cast set.

print(movie_cast)

#hw1j:
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}
movie_cast.discard("Will Smith");
print(movie_cast);

#hw1k:  אילו שחקנים ששיחקו בטיטניק לא זכו באוסקר?
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}

# Find actors from Titanic who haven't won an Oscar:
non_oscar_titanic_actors = titanic_actors.difference(oscar_winners); #or: titanic_actors - oscar_winners
print(non_oscar_titanic_actors);

#hw1l: אילו שחקנים הופיעו רק באחד מהסרטים, טיטניק או האביר האפל?
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"};
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"};

unique_actors = titanic_actors.symmetric_difference(dark_knight_actors);
# This means it returns all elements that are in either of the sets, but not in both.
print(unique_actors);

#hw1m:
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}

# Add Tom Hanks and Natalie Portman:
oscar_winners.update({"Tom Hanks", "Natalie Portman"});
# The update() method adds elements from the specified iterable (in this case, another set {"Tom Hanks", "Natalie Portman"}) to the original set.
# Since sets automatically avoid duplicates, this operation will only add these names if they are not already in the set.
# If they are already there, nothing changes.
print(oscar_winners);

#hw1n:
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"};
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"};

all_actors = titanic_actors.union(dark_knight_actors);

print(all_actors);

#hw1o:
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"};
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"};

# Check if all dark_knight_actors are also in oscar_winners
all_in_oscar_winners = dark_knight_actors <= oscar_winners;
# The <= operator in Python checks if the set on the left-hand side (dark_knight_actors) is a
# subset of the set on the right-hand side (oscar_winners).

print(all_in_oscar_winners);

#hw1p:
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"};
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"};

# Check if all oscar_winners are in legendary_actors
result = oscar_winners <= legendary_actors;
# The subset operator (<=) checks if every element of the first set is also an element of the second set.
print(result);

#hw1q:
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"};
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"};

# שחקנים ששיחקו ב"נוקמים" אך לא ב"איירון מן"
not_in_iron_man = avengers_actors - iron_man_actors;
print(not_in_iron_man);

#hw1r:
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"};
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"};

unique_actors = avengers_actors ^ dark_knight_actors;
# אופרטור ^ מבצע פעולה שנקראת "הפרש סימטרי" (symmetric difference).
# פעולה זו מחזירה קובץ חדש המכיל את כל האלמנטים שמופיעים בדיוק באחד משני הקבצים, אך לא בשניהם.
print(unique_actors);

#hw1s:
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"};
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"};

all_actors = dark_knight_actors | iron_man_actors;  # האופרטור | מבצע איחוד בין שתי הקבוצות.
print(all_actors);

#hw1t:
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
frozen_legendary_actors = frozenset(legendary_actors);
# The frozenset() function takes an iterable (like a set) and returns a new frozenset object,
# which is an immutable version of the set.
# This means you can't add, remove, or change elements in frozen_legendary_actors once it’s created.
print(frozen_legendary_actors);


