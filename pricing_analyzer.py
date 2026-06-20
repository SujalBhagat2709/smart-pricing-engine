class PricingAnalyzer:

    def calculate_price(

        self,

        base_price,

        stock,

        sales,

        competitor_price

    ):

        recommended_price = base_price

        demand_score = sales / max(stock, 1)

        if demand_score > 1:

            recommended_price *= 1.20

        elif demand_score > 0.5:

            recommended_price *= 1.10

        if stock < 20:

            recommended_price *= 1.15

        elif stock < 50:

            recommended_price *= 1.05

        if competitor_price > 0:

            if competitor_price < recommended_price:

                recommended_price = (

                    competitor_price + 20

                )

        return round(

            recommended_price,

            2

        )