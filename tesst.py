a = [
        {
            "name": "4-KATE00-WHE-N0-28",
            "title": "Viền 2.8cm Kate Wheat",
            "quantity": 0.0,
            "ordered_quantity": 0.0,
            "need_quantity": 0.0,
            "need_for_outsourcing": 0.0,
            "outsourcing_stock_out": 0.0,
            "temporary_quantity": 0.0,
            "children": [
                {
                    "name": "1-KATE00-WHE-00-AK",
                    "title": "Vải Kate Wheat",
                    "quantity": 0.0,
                    "ordered_quantity": 0.0,
                    "need_quantity": 0.0,
                    "need_for_outsourcing": 0.0,
                    "outsourcing_stock_out": 0.0,
                    "temporary_quantity": 0.0
                }
            ]
        },
        {
            "name": "1-THUNP0-RED-M2-AK",
            "title": "Vải thun poly Jersey Red ép mút 2mm",
            "quantity": 0.0,
            "ordered_quantity": 0.0,
            "need_quantity": 0.0,
            "need_for_outsourcing": 0.0,
            "outsourcing_stock_out": 0.0,
            "temporary_quantity": 0.0,
            "children": [
                {
                    "name": "1-THUNP0-RED-00-AK",
                    "title": "Vải thun poly Jersey Red",
                    "quantity": 7.0,
                    "ordered_quantity": 0.0,
                    "need_quantity": 0.0,
                    "need_for_outsourcing": 0.0,
                    "outsourcing_stock_out": 0.0,
                    "temporary_quantity": 7.0
                }
            ]
        },
        {
            "name": "1-NYN515-WOM-K1-ML",
            "title": "Vải 100% Nylon ML-N515 Wombat ép keo Kate 3044 White",
            "quantity": 0.0,
            "ordered_quantity": 0.0,
            "need_quantity": 0.0,
            "need_for_outsourcing": 0.0,
            "outsourcing_stock_out": 0.0,
            "temporary_quantity": 0.0,
            "children": [
                {
                    "name": "1-NYN515-WOM-00-ML",
                    "title": "Vải 100% Nylon ML-N515 Wombat",
                    "quantity": 0.0,
                    "ordered_quantity": 0.0,
                    "need_quantity": 0.0,
                    "need_for_outsourcing": 0.0,
                    "outsourcing_stock_out": 0.0,
                    "temporary_quantity": 0.0
                }
            ]
        },
        {
            "name": "1-THUNCO-HGR-V2-AK",
            "title": "Vải thun Cotton Heather Gray ép vải Kate White",
            "quantity": 0.0,
            "ordered_quantity": 0.0,
            "need_quantity": 0.0,
            "need_for_outsourcing": 0.0,
            "outsourcing_stock_out": 0.0,
            "temporary_quantity": 0.0,
            "children": [
                {
                    "name": "1-THUNCO-HGR-00-AK",
                    "title": "Vải thun Cotton Heather Gray",
                    "quantity": 20.0,
                    "ordered_quantity": 0.0,
                    "need_quantity": 0.0,
                    "need_for_outsourcing": 0.0,
                    "outsourcing_stock_out": 0.0,
                    "temporary_quantity": 20.0
                },
                {
                    "name": "1-KATE00-BLK-00-HV",
                    "title": "Vải Kate Black",
                    "quantity": 2028.4476,
                    "ordered_quantity": 0.0,
                    "need_quantity": 516.26,
                    "need_for_outsourcing": 3085.010236,
                    "outsourcing_stock_out": 2895.246,
                    "temporary_quantity": 1322.423364
                }
            ]
        },
        {
            "name": "4-P22158-BES-N0-22",
            "title": "Viền 2.2cm TDS22158 = PLY-2B1120 Blue Electric Stripe",
            "quantity": 0.0,
            "ordered_quantity": 0.0,
            "need_quantity": 0.0,
            "need_for_outsourcing": 0.0,
            "outsourcing_stock_out": 0.0,
            "temporary_quantity": 0.0,
            "children": [
                {
                    "name": "1-P22158-BES-00-HG",
                    "title": "Vải 100% polyester TDS22158 = PLY-2B1120 Blue Electric Stripe",
                    "quantity": 370.1,
                    "ordered_quantity": 0.0,
                    "need_quantity": 0.0,
                    "need_for_outsourcing": 0.0,
                    "outsourcing_stock_out": 0.0,
                    "temporary_quantity": 370.1
                }
            ]
        }
    ]

# print(a.loc[a[0]["name"] == "1-THUNP0-RED-M2-AK"])

adult_ages = filter(lambda name: name == "1-THUNP0-RED-M2-AK", a[1])
print(list(adult_ages))
