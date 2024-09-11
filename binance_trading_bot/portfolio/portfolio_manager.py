def rebalance_portfolio(assets, target_allocations):
    """Ребалансировка портфеля в соответствии с целевыми долями."""
    current_values = get_current_asset_values(assets)
    total_value = sum(current_values.values())
    for asset, target_allocation in target_allocations.items():
        current_allocation = current_values[asset] / total_value
        if current_allocation > target_allocation:
            sell_asset(asset, amount=(current_allocation - target_allocation) * total_value)
        elif current_allocation < target_allocation:
            def buy_asset(asset, amount):
                # Logic for buying an asset goes here
                print(f"Buying {amount} of {asset}")def sell_asset(asset, amount):
                    # Logic for selling an asset goes here
                    print(f"Selling {amount} of {asset}")def rebalance_portfolio(assets, target_allocations):
                        """Ребалансировка портфеля в соответствии с целевыми долями."""
                        current_values = get_current_asset_values(assets)
                        total_value = sum(current_values.values())
                        
                        def sell_asset(asset, amount):
                            # Logic for selling an asset goes here
                            print(f"Selling {amount} of {asset}")
                        
                        def buy_asset(asset, amount):
                            # Logic for buying an asset goes here
                            print(f"Buying {amount} of {asset}")
                        
                        for asset, target_allocation in target_allocations.items():
                            current_allocation = current_values[asset] / total_value
                            if current_allocation > target_allocation:
                                sell_asset(asset, amount=(current_allocation - target_allocation) * total_value)
                            elif current_allocation < target_allocation:
                                buy_asset(asset, amount=(target_allocation - current_allocation) * total_value)(asset, amount=(target_allocation - current_allocation) * total_value)
