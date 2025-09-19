class Spreadsheet:
    def __init__(self, rows: int) -> None:
        """
        Initialize the spreadsheet with a given number of rows.
      
        Args:
            rows: Number of rows in the spreadsheet (currently unused in implementation)
        """
        # Dictionary to store cell values, where key is cell name (e.g., "A1") and value is integer
        self.cells_data = {}

    def setCell(self, cell: str, value: int) -> None:
        """
        Set the value of a specific cell.
      
        Args:
            cell: Cell identifier (e.g., "A1", "B2")
            value: Integer value to store in the cell
        """
        self.cells_data[cell] = value

    def resetCell(self, cell: str) -> None:
        """
        Reset (delete) a cell's value from the spreadsheet.
      
        Args:
            cell: Cell identifier to reset
        """
        # Remove the cell from dictionary if it exists, otherwise do nothing
        self.cells_data.pop(cell, None)

    def getValue(self, formula: str) -> int:
        """
        Calculate and return the value of a formula.
      
        The formula format is "=<expression>" where expression can be:
        - A single number (e.g., "=5")
        - A single cell reference (e.g., "=A1")
        - Sum of numbers and/or cell references separated by "+" (e.g., "=A1+B2+5")
      
        Args:
            formula: Formula string starting with "="
          
        Returns:
            Calculated integer value of the formula
        """
        # Initialize result accumulator
        result = 0
      
        # Remove the leading "=" and split by "+" to get individual terms
        terms = formula[1:].split("+")
      
        # Process each term in the formula
        for term in terms:
            # Check if the term is a number or a cell reference
            if term[0].isdigit():
                # If first character is a digit, treat entire term as a number
                result += int(term)
            else:
                # Otherwise, treat it as a cell reference and get its value (default to 0 if not found)
                result += self.cells_data.get(term, 0)
      
        return result