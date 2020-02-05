try:
    from collections.abc import Sequence
except ImportError:
    from collections import Sequence
from typing import Any
from typing import Dict
from typing import Iterator
from typing import List

import gcloud.aio.datastore.value


# https://cloud.google.com/datastore/docs/reference/data/rest/v1/projects/runQuery#ArrayValue
class Array(Sequence):

    def __init__(self, items: List[Any]) -> None:
        super(Array, self).__init__()
        self.items = items

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Array):
            return False
        return self.items == other.items

    def __repr__(self) -> str:
        return repr(self.items)

    @classmethod
    def from_repr(cls, data: Dict[str, Any]) -> 'Array':
        return cls([gcloud.aio.datastore.Value.from_repr(x)
                    for x in data['values']])

    def to_repr(self) -> Dict[str, Any]:
        return {'values': [x.to_repr() for x in self]}

    def __iter__(self) -> Iterator:
        return iter(self.items)

    def __getitem__(self, index: Any) -> Any:
        return self.items[index]

    def __len__(self) -> int:
        return len(self.items)
