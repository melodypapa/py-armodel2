"""HwAttributeDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 26)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate_HwElementCategory.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory.hw_attribute_literal_def import (
    HwAttributeLiteralDef,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class HwAttributeDef(Identifiable):
    """AUTOSAR HwAttributeDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_attributes: list[HwAttributeLiteralDef]
    is_required: Optional[Boolean]
    unit: Optional[Unit]
    def __init__(self) -> None:
        """Initialize HwAttributeDef."""
        super().__init__()
        self.hw_attributes: list[HwAttributeLiteralDef] = []
        self.is_required: Optional[Boolean] = None
        self.unit: Optional[Unit] = None
    def serialize(self) -> ET.Element:
        """Serialize HwAttributeDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwAttributeDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_attributes (list to container "HW-ATTRIBUTES")
        if self.hw_attributes:
            wrapper = ET.Element("HW-ATTRIBUTES")
            for item in self.hw_attributes:
                serialized = ARObject._serialize_item(item, "HwAttributeLiteralDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize is_required
        if self.is_required is not None:
            serialized = ARObject._serialize_item(self.is_required, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-REQUIRED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unit
        if self.unit is not None:
            serialized = ARObject._serialize_item(self.unit, "Unit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwAttributeDef":
        """Deserialize XML element to HwAttributeDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwAttributeDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwAttributeDef, cls).deserialize(element)

        # Parse hw_attributes (list from container "HW-ATTRIBUTES")
        obj.hw_attributes = []
        container = ARObject._find_child_element(element, "HW-ATTRIBUTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_attributes.append(child_value)

        # Parse is_required
        child = ARObject._find_child_element(element, "IS-REQUIRED")
        if child is not None:
            is_required_value = child.text
            obj.is_required = is_required_value

        # Parse unit
        child = ARObject._find_child_element(element, "UNIT")
        if child is not None:
            unit_value = ARObject._deserialize_by_tag(child, "Unit")
            obj.unit = unit_value

        return obj



class HwAttributeDefBuilder:
    """Builder for HwAttributeDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwAttributeDef = HwAttributeDef()

    def build(self) -> HwAttributeDef:
        """Build and return HwAttributeDef object.

        Returns:
            HwAttributeDef instance
        """
        # TODO: Add validation
        return self._obj
