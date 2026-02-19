"""ComMgrUserNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 711)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    MaxCommModeEnum,
)


class ComMgrUserNeeds(ServiceNeeds):
    """AUTOSAR ComMgrUserNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_comm_mode_enum: Optional[MaxCommModeEnum]
    def __init__(self) -> None:
        """Initialize ComMgrUserNeeds."""
        super().__init__()
        self.max_comm_mode_enum: Optional[MaxCommModeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComMgrUserNeeds":
        """Deserialize XML element to ComMgrUserNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ComMgrUserNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ComMgrUserNeeds, cls).deserialize(element)

        # Parse max_comm_mode_enum
        child = ARObject._find_child_element(element, "MAX-COMM-MODE-ENUM")
        if child is not None:
            max_comm_mode_enum_value = MaxCommModeEnum.deserialize(child)
            obj.max_comm_mode_enum = max_comm_mode_enum_value

        return obj



class ComMgrUserNeedsBuilder:
    """Builder for ComMgrUserNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComMgrUserNeeds = ComMgrUserNeeds()

    def build(self) -> ComMgrUserNeeds:
        """Build and return ComMgrUserNeeds object.

        Returns:
            ComMgrUserNeeds instance
        """
        # TODO: Add validation
        return self._obj
