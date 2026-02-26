"""FlatMap module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.alias_name_set import (
        AliasNameSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.alias_name_assignment import (
        AliasNameAssignment,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
        FlatInstanceDescriptor,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_map import (
        FlatMap,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.rte_plugin_props import (
        RtePluginProps,
    )

__all__ = [
    "AliasNameAssignment",
    "AliasNameSet",
    "FlatInstanceDescriptor",
    "FlatMap",
    "RtePluginProps",
]
