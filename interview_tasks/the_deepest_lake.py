from typing import List


def max_lake_depth(depths: List[int]) -> int:
    try:
        max_depth = 0
        highest_lake_point = depths[0]
        lowest_lake_point = depths[0]
        for idx, depth in enumerate(depths[1:]):
            if depth > highest_lake_point:
                if max_depth < highest_lake_point - lowest_lake_point:
                    max_depth = highest_lake_point - lowest_lake_point
                highest_lake_point = depth
                lowest_lake_point = depth
            elif depth < lowest_lake_point:
                if max_depth < highest_lake_point - lowest_lake_point:
                    max_depth = highest_lake_point - lowest_lake_point
                lowest_lake_point = depth
            elif depth == highest_lake_point:
                if max_depth < highest_lake_point - lowest_lake_point:
                    max_depth = highest_lake_point - lowest_lake_point
                highest_lake_point = depth
                lowest_lake_point = depth
        else:
            if max_depth < highest_lake_point - lowest_lake_point:
                max_depth = highest_lake_point - lowest_lake_point
    except (TypeError, IndexError):
        return 0
    return max_depth
