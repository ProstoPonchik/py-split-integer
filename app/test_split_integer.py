from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    parameters = (33, 6)
    goal = 33
    assert sum(split_integer(*parameters)) == goal


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    parameters = (16, 4)
    goal = [4, 4, 4, 4]
    assert split_integer(*parameters) == goal


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    parameters = (17, 1)
    goal = [17]
    assert split_integer(*parameters) == goal


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    parameters = (33, 6)
    goal = [5, 5, 5, 6, 6, 6]
    assert split_integer(*parameters) == goal


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    parameters = (2, 3)
    goal = [0, 1, 1]
    assert split_integer(*parameters) == goal
