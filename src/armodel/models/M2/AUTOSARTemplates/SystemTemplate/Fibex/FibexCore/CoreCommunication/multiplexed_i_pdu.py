"""MultiplexedIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 408)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dynamic_part import (
    DynamicPart,
)


class MultiplexedIPdu(IPdu):
    """AUTOSAR MultiplexedIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dynamic_part: Optional[DynamicPart]
    selector_field: Optional[Integer]
    unused_bit: Optional[Integer]
    def __init__(self) -> None:
        """Initialize MultiplexedIPdu."""
        super().__init__()
        self.dynamic_part: Optional[DynamicPart] = None
        self.selector_field: Optional[Integer] = None
        self.unused_bit: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiplexedIPdu":
        """Deserialize XML element to MultiplexedIPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiplexedIPdu object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dynamic_part
        child = ARObject._find_child_element(element, "DYNAMIC-PART")
        if child is not None:
            dynamic_part_value = ARObject._deserialize_by_tag(child, "DynamicPart")
            obj.dynamic_part = dynamic_part_value

        # Parse selector_field
        child = ARObject._find_child_element(element, "SELECTOR-FIELD")
        if child is not None:
            selector_field_value = child.text
            obj.selector_field = selector_field_value

        # Parse unused_bit
        child = ARObject._find_child_element(element, "UNUSED-BIT")
        if child is not None:
            unused_bit_value = child.text
            obj.unused_bit = unused_bit_value

        return obj



class MultiplexedIPduBuilder:
    """Builder for MultiplexedIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiplexedIPdu = MultiplexedIPdu()

    def build(self) -> MultiplexedIPdu:
        """Build and return MultiplexedIPdu object.

        Returns:
            MultiplexedIPdu instance
        """
        # TODO: Add validation
        return self._obj
