"""DataPrototypeInPortInterfaceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 787)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_prototype_reference import (
    DataPrototypeReference,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInPortInterfaceRef(DataPrototypeReference):
    """AUTOSAR DataPrototypeInPortInterfaceRef."""

    def __init__(self) -> None:
        """Initialize DataPrototypeInPortInterfaceRef."""
        super().__init__()
        self.data_prototype_in: Optional[DataPrototype] = None


class DataPrototypeInPortInterfaceRefBuilder:
    """Builder for DataPrototypeInPortInterfaceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInPortInterfaceRef = DataPrototypeInPortInterfaceRef()

    def build(self) -> DataPrototypeInPortInterfaceRef:
        """Build and return DataPrototypeInPortInterfaceRef object.

        Returns:
            DataPrototypeInPortInterfaceRef instance
        """
        # TODO: Add validation
        return self._obj
