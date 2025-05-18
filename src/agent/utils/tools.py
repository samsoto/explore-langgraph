import datetime
from langchain_core.tools import tool


@tool
def get_my_name():
    """Get my `MY_NAME`.

    Returns:
        str: my name.
    """

    return "COSMOS"


@tool
def get_power_level(name: str):
    """Get the power level of `name`.

    Returns:
        int: power level.
    """
    if name == "COSMOS":
        return 9000
    else:
        return 0


@tool
def day_of_the_week(year: int = None, month: int = None, day: int = None):
    """Get the day of the week. Call with no arguments to get the current day.

    Returns:
        str: The day of the week.
    """
    date = datetime.date(year, month, day)
    return date.strftime("%A")


tools = [day_of_the_week, get_my_name, get_power_level]
tools_by_name = {tool.name: tool for tool in tools}
