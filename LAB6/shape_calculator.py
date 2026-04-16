import geometry_utils 


def run_calculator():

    operations = {
        "circle_area": geometry_utils.circle_area,
        "circle_perimeter": geometry_utils.circle_perimeter,
        "rectangle_area": geometry_utils.rectangle_area,
        "rectangle_perimeter": geometry_utils.rectangle_perimeter,
        "triangle_area": geometry_utils.triangle_area
    }

    print("Available shapes: circle, rectangle, triangle")
    print("Available calculations: area, perimeter (e.g., circle_area)")

    op_choice = input("Enter the operation you want to perform: ").lower()

    try:
        if op_choice not in operations:
            print("Invalid operation choice.")
            return

        if "circle" in op_choice:
            r = float(input("Enter radius: "))
            result = operations[op_choice](r)
        elif "rectangle" in op_choice:
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            result = operations[op_choice](w, h)
        elif "triangle" in op_choice:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            result = operations[op_choice](b, h)

        print(f"Result: {result:.2f}")

    except ValueError as e:

        print(f"Input Error: {e}")


if __name__ == "__main__":
    run_calculator()