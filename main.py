import openpyxl

class FinancialDSL:
    def __init__(self):
        self.variables = {}

    def parse_row(self, name, expression):
        # Ensure both name and expression are valid
        if not name or not expression:
            raise ValueError("Both name and expression must be provided.")
        return name.strip(), str(expression).strip()  # Convert expression to string

    def evaluate_expression(self, expression):
        # Evaluate the expression using the variables dictionary
        try:
            return eval(expression, {}, self.variables)
        except Exception as e:
            raise ValueError(f"Error evaluating expression '{expression}': {e}")

    def execute(self, name, expression):
        value = self.evaluate_expression(expression)
        self.variables[name] = value
        return name, value

    def run_from_excel(self, file_path, name_column="A", value_column="B"):
        # Load Excel file and read the columns
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active

        # Extract data from the specified columns
        names = [cell.value for cell in sheet[name_column] if cell.value]
        values = [cell.value for cell in sheet[value_column] if cell.value]

        if len(names) != len(values):
            raise ValueError("Mismatched number of names and expressions in the specified columns.")

        # Process all rows except the last as variable definitions
        for name, value in zip(names[:-1], values[:-1]):
            name, value = self.parse_row(name, value)
            self.execute(name, value)

        # Process the last row as the final formula
        final_name, final_expression = self.parse_row(names[-1], values[-1])
        key, value = self.execute(final_name, final_expression)

        return key, value


# Example Usage
dsl = FinancialDSL()

# Save the following data in an Excel file:
# Column A (Names):         Column B (Expressions):
# principal                 1000
# rate                      0.05
# years                     10
# future_value              principal * (1 + rate) ** years

file_path = "financial_calculations.xlsx"  # Update this with your Excel file path
result_key, result_value = dsl.run_from_excel(file_path, name_column="A", value_column="B")

print(f"{result_key} = {result_value}")
