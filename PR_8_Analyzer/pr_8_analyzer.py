import numpy as np

class DataAnalytics:
    """
    A class to encapsulate advanced NumPy array operations, 
    statistical analysis, and matrix manipulations.
    """
    
    def __init__(self, array=None):
        # Instance attribute holding the current active array
        self.array = np.array(array) if array is not None else None

    # --- Private Helper Methods (Internal Computations) ---
    def _has_array(self):
        """Internal check to ensure an array exists before performing operations."""
        if self.array is None:
            print("\nError: No active array found! Please create one first.")
            return False
        return True

    def _parse_input_to_shape(self, elements_str, shape):
        """Converts a space-separated string into a NumPy array of a given shape."""
        try:
            elements = list(map(float, elements_str.strip().split()))
            if len(elements) != np.prod(shape):
                raise ValueError(f"Expected {np.prod(shape)} elements, but got {len(elements)}.")
            return np.array(elements).reshape(shape)
        except ValueError as e:
            print(f"\nInvalid input: {e}")
            return None

    # --- Static & Class Methods ---
    @staticmethod
    def display_welcome():
        """Displays the application header."""
        print("\nWelcome to the NumPy Analyzer!")
        print("===============================")

    @classmethod
    def create_from_list(cls, data_list):
        """Alternative constructor to build the class directly from a standard python list."""
        return cls(np.array(data_list))

    # --- Array Management ---
    def create_array(self, shape, elements_str):
        """Creates and updates the current active array."""
        new_arr = self._parse_input_to_shape(elements_str, shape)
        if new_arr is not None:
            self.array = new_arr
            print("\nArray created successfully:")
            print(self.array)
            return True
        return False

    def access_slice(self, row_slice_str, col_slice_str):
        """Slices the array dynamically based on user-provided 'start:end' formats."""
        if not self._has_array(): return
        
        try:
            # Parse slice strings (e.g., '0:2' -> slice(0, 2))
            r_start, r_end = map(int, row_slice_str.split(':'))
            c_start, c_end = map(int, col_slice_str.split(':'))
            
            sliced = self.array[r_start:r_end, c_start:c_end]
            print("\nSliced Array:")
            print(sliced)
        except Exception as e:
            print(f"\nSlicing error: Make sure format is start:end (e.g., 0:2). Details: {e}")

    # --- Mathematical Operations ---
    def perform_math(self, op_choice, secondary_elements_str):
        """Performs element-wise arithmetic against another user-provided array."""
        if not self._has_array(): return
        
        second_arr = self._parse_input_to_shape(secondary_elements_str, self.array.shape)
        if second_arr is None:
            return

        print("\nOriginal Array:")
        print(self.array)
        print("\nSecond Array:")
        print(second_arr)

        if op_choice == '1':
            result = self.array + second_arr
            print("\nResult of Addition:")
        elif op_choice == '2':
            result = self.array - second_arr
            print("\nResult of Subtraction:")
        elif op_choice == '3':
            result = self.array * second_arr
            print("\nResult of Multiplication:")
        elif op_choice == '4':
            # Avoid divide by zero crash
            with np.errstate(divide='ignore', invalid='ignore'):
                result = self.array / second_arr
            print("\nResult of Division:")
        else:
            print("Invalid operation selection.")
            return

        print(result)

    # --- Combine & Split Arrays ---
    def combine_with(self, secondary_elements_str):
        """Vertically stacks another array of identical dimensions to the current array."""
        if not self._has_array(): return
        
        second_arr = self._parse_input_to_shape(secondary_elements_str, self.array.shape)
        if second_arr is None:
            return

        print("\nOriginal Array:")
        print(self.array)
        print("\nSecond Array:")
        print(second_arr)

        try:
            combined = np.vstack((self.array, second_arr))
            print("\nCombined Array (Vertical Stack):")
            print(combined)
        except Exception as e:
            print(f"Combination failed: {e}")

    def split_array(self, sections=2):
        """Splits the current array vertically along its rows."""
        if not self._has_array(): return
        
        try:
            splits = np.vsplit(self.array, sections)
            print(f"\nArray split into {sections} sections:")
            for idx, part in enumerate(splits, 1):
                print(f"Section {idx}:\n{part}")
        except Exception as e:
            print(f"\nCannot split array evenly: {e}")

    # --- Search, Sort, and Filter ---
    def search_value(self, value):
        """Finds index coordinates of a specific element inside the array."""
        if not self._has_array(): return
        indices = np.argwhere(self.array == value)
        if indices.size > 0:
            print(f"\nValue {value} found at indices:\n{indices}")
        else:
            print(f"\nValue {value} not found in the array.")

    def sort_array(self, order='ascending'):
        """Sorts the array row-wise."""
        if not self._has_array(): return
        
        print("\nOriginal Array:")
        print(self.array)
        
        # NumPy sorts ascending by default; invert if descending is selected
        sorted_arr = np.sort(self.array, axis=-1)
        if order == 'descending':
            sorted_arr = -np.sort(-self.array, axis=-1)
            
        print("\nSorted Array:")
        print(sorted_arr)
        print("(Sorting applied row-wise.)")

    def filter_values(self, threshold, condition='greater'):
        """Filters out elements based on a dynamic greater/lesser condition threshold."""
        if not self._has_array(): return
        
        if condition == 'greater':
            filtered = self.array[self.array > threshold]
        else:
            filtered = self.array[self.array < threshold]
            
        print(f"\nElements {condition} than {threshold}: {filtered}")

    # --- Aggregates and Statistics ---
    def compute_stats(self, stat_choice):
        """Processes statistical summary tools directly from standard NumPy APIs."""
        if not self._has_array(): return
        
        print("\nOriginal Array:")
        print(self.array)

        if stat_choice == '1':
            print(f"\nSum of Array: {np.sum(self.array)}")
        elif stat_choice == '2':
            print(f"\nMean of Array: {np.mean(self.array)}")
        elif stat_choice == '3':
            print(f"\nMedian of Array: {np.median(self.array)}")
        elif stat_choice == '4':
            print(f"\nStandard Deviation of Array: {np.std(self.array)}")
        elif stat_choice == '5':
            print(f"\nVariance of Array: {np.var(self.array)}")
        else:
            print("Invalid statistical choice.")


# --- Main Application Execution Flow (UI Logic) ---
def main():
    analyzer = DataAnalytics()
    
    while True:
        DataAnalytics.display_welcome()
        print("Choose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            print("\nArray Creation:")
            print("Select the type of array to create:")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. Go Back")
            sub_choice = input("Enter your choice: ").strip()
            
            if sub_choice == '3':
                continue
                
            if sub_choice == '1':
                length = int(input("Enter the number of elements: "))
                elements = input(f"Enter {length} elements separated by space: ")
                analyzer.create_array((length,), elements)
            elif sub_choice == '2':
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                elements = input(f"Enter {rows * cols} elements separated by space: ")
                success = analyzer.create_array((rows, cols), elements)
                
                if success:
                    # Array Management Submenu (Indexing / Slicing)
                    print("\nChoose an operation:")
                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. Go back")
                    manage_choice = input("Enter your choice: ").strip()
                    
                    if manage_choice == '2':
                        row_range = input("Enter the row range (start:end): ").strip()
                        col_range = input("Enter the column range (start:end): ").strip()
                        analyzer.access_slice(row_range, col_range)
                        
        elif choice == '2':
            print("\nMathematical Operations:")
            print("Choose a mathematical operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            math_choice = input("Enter your choice: ").strip()
            
            if analyzer.array is not None:
                size = analyzer.array.size
                elements = input(f"Enter the same-size array elements ({size} elements separated by space): ")
                analyzer.perform_math(math_choice, elements)
            else:
                print("\nPlease construct an array first before using operations.")
                
        elif choice == '3':
            print("\nCombine or Split Arrays:")
            print("Choose an option:")
            print("1. Combine Arrays")
            print("2. Split Array")
            combine_choice = input("Enter your choice: ").strip()
            
            if combine_choice == '1':
                if analyzer.array is not None:
                    size = analyzer.array.size
                    elements = input(f"Enter the elements of another array to combine ({size} elements separated by space): ")
                    analyzer.combine_with(elements)
                else:
                    print("\nPlease construct an array first.")
            elif combine_choice == '2':
                sections = int(input("Enter the number of horizontal sections to split array into: "))
                analyzer.split_array(sections)
                
        elif choice == '4':
            print("\nSearch, Sort, or Filter:")
            print("Choose an option:")
            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")
            sf_choice = input("Enter your choice: ").strip()
            
            if sf_choice == '1':
                val = float(input("Enter the value to search: "))
                analyzer.search_value(val)
            elif sf_choice == '2':
                order_choice = input("Sort order? (1. Ascending / 2. Descending): ").strip()
                order = 'descending' if order_choice == '2' else 'ascending'
                analyzer.sort_array(order)
            elif sf_choice == '3':
                threshold = float(input("Enter target comparison value: "))
                cond = input("Condition? (1. Greater than / 2. Less than): ").strip()
                direction = 'less' if cond == '2' else 'greater'
                analyzer.filter_values(threshold, direction)
                
        elif choice == '5':
            print("\nAggregates and Statistics:")
            print("Choose an aggregate/statistical operation:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            stat_choice = input("Enter your choice: ").strip()
            analyzer.compute_stats(stat_choice)
            
        elif choice == '6':
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("\nInvalid choice option selected. Try again.")

if __name__ == "__main__":
    main()


    