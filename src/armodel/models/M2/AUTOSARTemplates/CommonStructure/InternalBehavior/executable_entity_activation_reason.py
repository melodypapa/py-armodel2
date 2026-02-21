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
from armodel.serialization import SerializationHelper
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

    def serialize(self) -> ET.Element:
        """Serialize ExecutableEntityActivationReason to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExecutableEntityActivationReason, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bit_position
        if self.bit_position is not None:
            serialized = SerializationHelper.serialize_item(self.bit_position, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BIT-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutableEntityActivationReason":
        """Deserialize XML element to ExecutableEntityActivationReason object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutableEntityActivationReason object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExecutableEntityActivationReason, cls).deserialize(element)

        # Parse bit_position
        child = SerializationHelper.find_child_element(element, "BIT-POSITION")
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
