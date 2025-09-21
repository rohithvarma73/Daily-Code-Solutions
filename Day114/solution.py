from typing import List
from collections import defaultdict
from sortedcontainers import SortedList


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        """
        Initialize the movie renting system.
      
        Args:
            n: Number of shops
            entries: List of [shop, movie, price] entries
        """
        # Store unrented movies: movie_id -> sorted list of (price, shop_id)
        self.unrented = defaultdict(SortedList)
      
        # Store price lookup: (shop_id, movie_id) -> price
        self.shop_and_movie_to_price = {}
      
        # Store currently rented movies: sorted list of (price, shop_id, movie_id)
        self.rented = SortedList()
      
        # Process initial entries
        for shop, movie, price in entries:
            self.unrented[movie].add((price, shop))
            self.shop_and_movie_to_price[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        """
        Search for the 5 cheapest shops that have an unrented copy of the given movie.
      
        Args:
            movie: The movie ID to search for
          
        Returns:
            List of up to 5 shop IDs with cheapest prices
        """
        # Return shop IDs from the first 5 (price, shop) tuples
        return [shop for _, shop in self.unrented[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        """
        Rent a movie from a specific shop.
      
        Args:
            shop: The shop ID
            movie: The movie ID to rent
        """
        # Get the price for this shop-movie combination
        price = self.shop_and_movie_to_price[(shop, movie)]
      
        # Remove from unrented inventory
        self.unrented[movie].remove((price, shop))
      
        # Add to rented inventory
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        """
        Return a rented movie to a specific shop.
      
        Args:
            shop: The shop ID
            movie: The movie ID to return
        """
        # Get the price for this shop-movie combination
        price = self.shop_and_movie_to_price[(shop, movie)]
      
        # Add back to unrented inventory
        self.unrented[movie].add((price, shop))
      
        # Remove from rented inventory
        self.rented.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        """
        Get the 5 cheapest rented movies.
      
        Returns:
            List of up to 5 [shop_id, movie_id] pairs
        """
        # Return shop and movie IDs from the first 5 rented entries
        return [[shop, movie] for _, shop, movie in self.rented[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop, movie)
# obj.drop(shop, movie)
# param_4 = obj.report()