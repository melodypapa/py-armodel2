"""ExecutableEntityActivationReason AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 315)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 538)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class ExecutableEntityActivationReason(ImplementationProps):
    """AUTOSAR ExecutableEntityActivationReason."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bit_position: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize ExecutableEntityActivationReason."""
        super().__init__()
        self.bit_position: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutableEntityActivationReason":
        """Deserialize XML element to ExecutableEntityActivationReason object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutableEntityActivationReason object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bit_position
        child = ARObject._find_child_element(element, "BIT-POSITION")
        if child is not None:
            bit_position_value = child.text
            obj.bit_position = bit_position_value

        return obj



class ExecutableEntityActivationReasonBuilder:
    """Builder for ExecutableEntityActivationReason."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutableEntityActivationReason = ExecutableEntityActivationReason()

    def build(self) -> ExecutableEntityActivationReason:
        """Build and return ExecutableEntityActivationReason object.

        Returns:
            ExecutableEntityActivationReason instance
        """
        # TODO: Add validation
        return self._obj
