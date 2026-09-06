from typing import List


def get_unfulfilled_customers(
    requests: List[List[int]],
    total_inventory: int
) -> List[int]:
    """
    requests[i] = [
        customer_id,
        quantity,
        bid_amount,
        timestamp
    ]

    Return the customer IDs that receive zero items.
    """

    # TODO: Implement your solution
    requests.sort(key=lambda x: x[2], reverse=True)
    bidMap = {}
    for r in requests:
        if r[2] not in bidMap:
            bidMap[r[2]] = [[r[0], r[1], r[3]]]
        else:
            bidMap[r[2]].append([r[0], r[1], r[3]])

    result = []

    for bid in sorted(bidMap.keys(), reverse=True):
        bidItems = bidMap[bid]
        bidItems.sort(key=lambda x: x[2])

        if total_inventory <= 0:
            for b in bidItems:
                result.append(b)
        else:
            if len(bidItems) > 1:

                if total_inventory < len(bidItems):

                    for i in range(len(bidItems) - 1, total_inventory - 1, -1):
                        result.append(bidItems[i])

                    total_inventory = 0

                else:
                    totalQuantity = 0

                    for b in bidItems:
                        totalQuantity += b[1]

                    if totalQuantity > total_inventory:
                        total_inventory = 0
                    else:
                        total_inventory -= totalQuantity

            else:
                total_inventory -= bidItems[0][1]

    output = []
    for r in result:
        output.append(r[0])

    output.sort()
    
    return output   


if __name__ == "__main__":
    requests = [
        [1, 5, 5, 0],
        [2, 7, 8, 1],
        [3, 7, 5, 1],
        [4, 10, 3, 3],
    ]

    # requests = [
    #     [1, 2, 10, 0],
    #     [2, 2, 10, 1],
    #     [3, 2, 10, 2]
    # ]

    # requests = [
    #     [1, 3, 20, 0],
    #     [2, 5, 10, 1],
    #     [3, 2, 5, 2]
    # ]

    total_inventory = 18

    result = get_unfulfilled_customers(
        requests,
        total_inventory
    )

    print(result)

    # Expected:
    # [4]