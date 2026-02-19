"""IdsMgrNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 842)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class IdsMgrNeeds(ServiceNeeds):
    """AUTOSAR IdsMgrNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    use_smart: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize IdsMgrNeeds."""
        super().__init__()
        self.use_smart: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsMgrNeeds":
        """Deserialize XML element to IdsMgrNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsMgrNeeds object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse use_smart
        child = ARObject._find_child_element(element, "USE-SMART")
        if child is not None:
            use_smart_value = child.text
            obj.use_smart = use_smart_value

        return obj



class IdsMgrNeedsBuilder:
    """Builder for IdsMgrNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsMgrNeeds = IdsMgrNeeds()

    def build(self) -> IdsMgrNeeds:
        """Build and return IdsMgrNeeds object.

        Returns:
            IdsMgrNeeds instance
        """
        # TODO: Add validation
        return self._obj
