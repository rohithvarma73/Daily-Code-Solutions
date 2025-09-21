# Day144: Design Movie Rental System

**Solved**  
**Hard**

---

## Problem Statement

You have a movie renting company consisting of `n` shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.

Each movie is given as a 2D integer array `entries` where `entries[i] = [shopi, moviei, pricei]` indicates that there is a copy of movie `moviei` at shop `shopi` with a rental price of `pricei`.  
Each shop carries at most one copy of a movie `moviei`.

The system should support the following functions:

- **Search**  
  Finds the cheapest 5 shops that have an **unrented** copy of a given movie.  
  - Shops should be sorted by **price (ascending order)**.  
  - If tie in price → smaller `shopi` first.  
  - If less than 5 matches → return all.  
  - If no shop has an unrented copy → return empty list.  

- **Rent**  
  Rents an unrented copy of a given movie from a given shop.  

- **Drop**  
  Drops off a previously rented copy of a given movie at a given shop.  

- **Report**  
  Returns the cheapest 5 rented movies (possibly same movie ID) as a 2D list `res` where `res[j] = [shopj, moviej]`.  
  - Sorted by **price ascending**, then **shopj ascending**, then **moviej ascending**.  
  - If fewer than 5 rented movies → return all.  
  - If none → return empty list.  

---

## Class Definition

```text
MovieRentingSystem(int n, int[][] entries)
    Initializes the system with n shops and the movies in entries.

List<Integer> search(int movie)
    Returns a list of shops with an unrented copy of the given movie.

void rent(int shop, int movie)
    Rents the given movie from the given shop.

void drop(int shop, int movie)
    Drops off the previously rented movie at the given shop.

List<List<Integer>> report()
    Returns a list of cheapest rented movies as described.
````

⚠️ **Note**:

* Test cases ensure `rent` is called only if the shop has an unrented copy.
* `drop` is called only if the shop had rented out the movie.

---

## Example 1

**Input**

```
["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
```

**Output**

```
[null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]
```

**Explanation**

```
MovieRentingSystem movieRentingSystem = new MovieRentingSystem(
    3,
    [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]
);

movieRentingSystem.search(1);  
// return [1, 0, 2] (movies of ID 1 available at shops 1, 0, 2).

movieRentingSystem.rent(0, 1);  
// Rent movie 1 from shop 0. Shop 0 now has unrented [2, 3].

movieRentingSystem.rent(1, 2);  
// Rent movie 2 from shop 1. Shop 1 now has unrented [1].

movieRentingSystem.report();  
// return [[0, 1], [1, 2]].

movieRentingSystem.drop(1, 2);  
// Drop movie 2 at shop 1. Shop 1 now has [1, 2].

movieRentingSystem.search(2);  
// return [0, 1] (shop 0 cheaper than shop 1).
```

---

## Example 2

**Input**

```
["MovieRentingSystem", "search", "rent", "report"]
[[2, [[0, 1, 3], [1, 1, 2]]], [1], [1, 1], []]
```

**Output**

```
[null, [1, 0], null, [[1, 1]]]
```

---

## Constraints

* `1 <= n <= 3 * 10^5`
* `1 <= entries.length <= 10^5`
* `0 <= shopi < n`
* `1 <= moviei, pricei <= 10^4`
* Each shop carries at most one copy of a movie `moviei`.
* At most `10^5` calls in total to `search`, `rent`, `drop`, `report`.
