from pricing_analyzer import (
    PricingAnalyzer
)


def generate_report(

    product,

    base_price,

    stock,

    sales,

    competitor_price,

    recommended_price

):

    html = f"""

    <html>

    <head>

    <title>

    Pricing Report

    </title>

    </head>

    <body>

    <h1>

    Smart Pricing Report

    </h1>

    <hr>

    <p>

    Product:
    {product}

    </p>

    <p>

    Base Price:
    ₹{base_price}

    </p>

    <p>

    Stock:
    {stock}

    </p>

    <p>

    Sales:
    {sales}

    </p>

    <p>

    Competitor Price:
    ₹{competitor_price}

    </p>

    <h2>

    Recommended Price:
    ₹{recommended_price}

    </h2>

    </body>

    </html>

    """

    with open(

        "pricing_report.html",

        "w",

        encoding="utf-8"

    ) as file:

        file.write(html)


def main():

    print(
        "\n========================"
    )

    print(
        "SMART PRICING ENGINE"
    )

    print(
        "========================"
    )

    product = input(
        "\nProduct Name:\n"
    )

    base_price = float(
        input(
            "\nBase Price:\n"
        )
    )

    stock = int(
        input(
            "\nCurrent Stock:\n"
        )
    )

    sales = int(
        input(
            "\nToday's Sales:\n"
        )
    )

    competitor_price = float(
        input(
            "\nCompetitor Price:\n"
        )
    )

    analyzer = PricingAnalyzer()

    recommended_price = (

        analyzer.calculate_price(

            base_price,

            stock,

            sales,

            competitor_price

        )

    )

    print(
        "\n========================"
    )

    print(
        "RESULT"
    )

    print(
        "========================"
    )

    print(
        f"\nRecommended Price: "
        f"₹{recommended_price}"
    )

    generate_report(

        product,

        base_price,

        stock,

        sales,

        competitor_price,

        recommended_price

    )

    print(
        "\nGenerated:"
    )

    print(
        "pricing_report.html"
    )


if __name__ == "__main__":

    main()