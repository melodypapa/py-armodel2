"""UnitGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 314)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 402)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class UnitGroup(ARElement):
    """AUTOSAR UnitGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    unit_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize UnitGroup."""
        super().__init__()
        self.unit_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize UnitGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UnitGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize unit_refs (list to container "UNIT-REFS")
        if self.unit_refs:
            wrapper = ET.Element("UNIT-REFS")
            for item in self.unit_refs:
                serialized = ARObject._serialize_item(item, "Unit")
                if serialized is not None:
                    child_elem = ET.Element("UNIT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UnitGroup":
        """Deserialize XML element to UnitGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UnitGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(UnitGroup, cls).deserialize(element)

        # Parse unit_refs (list from container "UNIT-REFS")
        obj.unit_refs = []
        container = ARObject._find_child_element(element, "UNIT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.unit_refs.append(child_value)

        return obj



class UnitGroupBuilder:
    """Builder for UnitGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UnitGroup = UnitGroup()

    def build(self) -> UnitGroup:
        """Build and return UnitGroup object.

        Returns:
            UnitGroup instance
        """
        # TODO: Add validation
        return self._obj
