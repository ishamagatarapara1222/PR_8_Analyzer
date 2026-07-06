import numpy as np


class DataAnalytics:

    def __init__(self):
        self.__array = None

    def __check_array(self):
        if self.__array is None:
            raise ValueError("No array found. Please create an array first.")

    # ── Array Creation ────────────────────────────────────────────────
    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            elements = list(map(int, input("Enter elements separated by space: ").split()))
            self.__array = np.array(elements)

        elif choice == "2":
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            elements = list(map(int, input(f"Enter {rows * cols} elements separated by space: ").split()))
            self.__array = np.array(elements).reshape(rows, cols)

        elif choice == "3":
            depth = int(input("Enter depth: "))
            rows  = int(input("Enter rows: "))
            cols  = int(input("Enter columns: "))
            elements = list(map(int, input(f"Enter {depth * rows * cols} elements separated by space: ").split()))
            self.__array = np.array(elements).reshape(depth, rows, cols)

        else:
            print("Invalid choice.")
            return

        print("\nArray created successfully:")
        print(self.__array)

    # ── Indexing & Slicing ────────────────────────────────────────────
    def index_slice_array(self):
        self.__check_array()
        print("\nOriginal Array:")
        print(self.__array)

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            idx = list(map(int, input("Enter index (space-separated for multi-dim): ").split()))
            print("Element:", self.__array[tuple(idx)])

        elif choice == "2":
            if self.__array.ndim == 1:
                start, end = map(int, input("Enter start and end index (space-separated): ").split())
                print("Sliced Array:", self.__array[start:end])
            else:
                row_range = input("Enter the row range (start:end): ")
                col_range = input("Enter the column range (start:end): ")
                r_start, r_end = map(int, row_range.split(":"))
                c_start, c_end = map(int, col_range.split(":"))
                print("\nSliced Array:")
                print(self.__array[r_start:r_end, c_start:c_end])

        elif choice == "3":
            return
        else:
            print("Invalid choice.")

    # ── Mathematical Operations ───────────────────────────────────────
    def math_operations(self):
        self.__check_array()
        print("\nOriginal Array:")
        print(self.__array)

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter your choice: ").strip()

        if choice in ("1", "2", "3", "4"):
            size = self.__array.size
            elements = list(map(float, input(f"Enter the same-size array elements ({size} elements separated by space): ").split()))
            second = np.array(elements).reshape(self.__array.shape)

            print("\nOriginal Array:")
            print(self.__array)
            print("\nSecond Array:")
            print(second)

            if choice == "1":
                result, label = self.__array + second, "Addition"
            elif choice == "2":
                result, label = self.__array - second, "Subtraction"
            elif choice == "3":
                result, label = self.__array * second, "Multiplication"
            else:
                result, label = self.__array / second, "Division"

            print(f"\nResult of {label}:")
            print(result)
        else:
            print("Invalid choice.")

    @classmethod
    def dot_product(cls, arr1, arr2):
        return np.dot(np.array(arr1), np.array(arr2))

    @staticmethod
    def matrix_multiply(arr1, arr2):
        return np.array(arr1) @ np.array(arr2)

    # ── Combine or Split ──────────────────────────────────────────────
    def combine_split_arrays(self):
        self.__check_array()
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            size = self.__array.size
            elements = list(map(int, input(f"Enter the elements of another array to combine ({size} elements separated by space): ").split()))
            second = np.array(elements).reshape(self.__array.shape)

            print("\nOriginal Array:")
            print(self.__array)
            print("\nSecond Array:")
            print(second)

            combined = np.vstack((self.__array, second))
            print("\nCombined Array (Vertical Stack):")
            print(combined)

        elif choice == "2":
            splits = int(input("Enter number of splits: "))
            result = np.array_split(self.__array, splits)
            print("\nOriginal Array:")
            print(self.__array)
            for i, part in enumerate(result):
                print(f"\nPart {i + 1}:")
                print(part)
        else:
            print("Invalid choice.")

    # ── Search, Sort, Filter ──────────────────────────────────────────
    def search_sort_filter(self):
        self.__check_array()
        print("\nOriginal Array:")
        print(self.__array)

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            val = int(input("Enter value to search: "))
            result = np.where(self.__array == val)
            print(f"Value {val} found at indices:", result)

        elif choice == "2":
            sorted_arr = np.sort(self.__array, axis=-1)
            print("\nSorted Array:")
            print(sorted_arr)
            if self.__array.ndim > 1:
                print("(Sorting applied row-wise.)")

        elif choice == "3":
            threshold = int(input("Enter threshold value (filter elements > threshold): "))
            filtered = self.__array[self.__array > threshold]
            print(f"\nElements greater than {threshold}:")
            print(filtered)
        else:
            print("Invalid choice.")

    # ── Aggregates & Statistics ───────────────────────────────────────
    def compute_aggregates(self):
        self.__check_array()
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        choice = input("Enter your choice: ").strip()

        print("\nOriginal Array:")
        print(self.__array)

        ops = {
            "1": ("Sum",                np.sum),
            "2": ("Mean",               np.mean),
            "3": ("Median of Array",    np.median),
            "4": ("Standard Deviation", np.std),
            "5": ("Variance",           np.var),
        }
        if choice in ops:
            label, func = ops[choice]
            print(f"{label}:", func(self.__array))
        else:
            print("Invalid choice.")

    def statistical_functions(self):
        self.__check_array()
        print("\nStatistical Functions:")
        print("1. Min & Max")
        print("2. Percentiles")
        print("3. Correlation Coefficient")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Minimum:", np.min(self.__array))
            print("Maximum:", np.max(self.__array))

        elif choice == "2":
            p = int(input("Enter percentile value (e.g. 25, 50, 75): "))
            print(f"{p}th Percentile:", np.percentile(self.__array, p))

        elif choice == "3":
            if self.__array.ndim < 2:
                print("Correlation requires a 2D array.")
            else:
                print("Correlation Coefficients:")
                print(np.corrcoef(self.__array))
        else:
            print("Invalid choice.")


# ── Main Menu ─────────────────────────────────────────────────────────
def main():
    print("Welcome to the NumPy Analyzer!")
    print("-" * 40)

    analyzer = DataAnalytics()

    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            analyzer.create_array()

        elif choice == "2":
            analyzer.math_operations()

        elif choice == "3":
            analyzer.combine_split_arrays()

        elif choice == "4":
            analyzer.search_sort_filter()

        elif choice == "5":
            print("\n1. Aggregate Functions")
            print("2. Statistical Functions")
            sub = input("Enter your choice: ").strip()

            if sub == "1":
                analyzer.compute_aggregates()
            elif sub == "2":
                analyzer.statistical_functions()
            else:
                print("Invalid choice.")

        elif choice == "6":
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()