"""PRPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class PRPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR PRPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provided: Optional[PortInterface]
    def __init__(self) -> None:
        """Initialize PRPortPrototype."""
        super().__init__()
        self.provided: Optional[PortInterface] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PRPortPrototype":
        """Deserialize XML element to PRPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PRPortPrototype object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse provided
        child = ARObject._find_child_element(element, "PROVIDED")
        if child is not None:
            provided_value = ARObject._deserialize_by_tag(child, "PortInterface")
            obj.provided = provided_value

        return obj



class PRPortPrototypeBuilder:
    """Builder for PRPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PRPortPrototype = PRPortPrototype()

    def build(self) -> PRPortPrototype:
        """Build and return PRPortPrototype object.

        Returns:
            PRPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
