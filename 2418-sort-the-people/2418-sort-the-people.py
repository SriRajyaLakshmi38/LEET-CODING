class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        number_of_people = len(names)

        height_to_name_map = OrderedDict()

        # Populate the OrderedDict with height as key and name as value
        for height, name in zip(heights, names):
            height_to_name_map[height] = name

        # Sort the OrderedDict by height in descending order
        height_to_name_map = OrderedDict(
            sorted(height_to_name_map.items(), reverse=True)
        )

        # Create a list of sorted names based on descending heights
        sorted_names = list(height_to_name_map.values())

        return sorted_names
