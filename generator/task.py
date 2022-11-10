# MIT License

# Copyright (c) 2022 Cheng Soon Goh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from dataclasses import dataclass, field
from contextlib import contextmanager

from painter import Painter
from milestone import Milestone


@dataclass(kw_only=True)
class Task:

    text: str
    start: datetime
    end: datetime
    x: int = 0
    y: int = 0
    width: int = 0
    height: int = 0
    font: str = "Arial"
    font_size: int = 12
    font_colour: str = "Black"
    fill_colour: str = "LightGreen"

    def __post_init__(self):
        self.milestones = []
        self.tasks = []

    @contextmanager
    def add_parellel_task(
        self,
        text,
        start,
        end,
        font="Arial",
        font_size=12,
        font_colour="Black",
        fill_colour="LightGreen",
    ):
        """Add a parallel task to this task

        Args:
            text ([type]): [description]
            start ([type]): [description]
            end ([type]): [description]
            font (str, optional): [description]. Defaults to "Arial".
            font_size (int, optional): [description]. Defaults to 12.
            font_colour (str, optional): [description]. Defaults to "Black".
            fill_colour (str, optional): [description]. Defaults to "LightGreen".

        Yields:
            [type]: [description]
        """
        try:
            task = Task(
                text=text,
                start=start,
                end=end,
                font=font,
                font_size=font_size,
                font_colour=font_colour,
                fill_colour=fill_colour,
            )
            self.tasks.append(task)
            yield task
        finally:
            task = None

    def add_milestone(
        self,
        text,
        date,
        font="Arial",
        font_size=12,
        font_colour="Red",
        fill_colour="Red",
    ):
        # print(f"Adding milestone {text}")
        self.milestones.append(
            Milestone(text, date, font, font_size, font_colour, fill_colour)
        )
        # pd(self.milestones)

    def draw(self, painter: Painter):
        pass