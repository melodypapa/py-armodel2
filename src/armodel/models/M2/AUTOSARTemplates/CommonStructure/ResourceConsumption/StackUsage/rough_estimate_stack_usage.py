"""RoughEstimateStackUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 151)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_StackUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class RoughEstimateStackUsage(StackUsage):
    """AUTOSAR RoughEstimateStackUsage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    memory_consumption: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize RoughEstimateStackUsage."""
        super().__init__()
        self.memory_consumption: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize RoughEstimateStackUsage to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RoughEstimateStackUsage, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize memory_consumption
        if self.memory_consumption is not None:
            serialized = SerializationHelper.serialize_item(self.memory_consumption, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEMORY-CONSUMPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoughEstimateStackUsage":
        """Deserialize XML element to RoughEstimateStackUsage object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoughEstimateStackUsage object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RoughEstimateStackUsage, cls).deserialize(element)

        # Parse memory_consumption
        child = SerializationHelper.find_child_element(element, "MEMORY-CONSUMPTION")
        if child is not None:
            memory_consumption_value = child.text
            obj.memory_consumption = memory_consumption_value

        return obj



class RoughEstimateStackUsageBuilder:
    """Builder for RoughEstimateStackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoughEstimateStackUsage = RoughEstimateStackUsage()

    def build(self) -> RoughEstimateStackUsage:
        """Build and return RoughEstimateStackUsage object.

        Returns:
            RoughEstimateStackUsage instance
        """
        # TODO: Add validation
        return self._obj
