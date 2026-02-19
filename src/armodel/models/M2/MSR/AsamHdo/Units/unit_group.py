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

    units: list[Unit]
    def __init__(self) -> None:
        """Initialize UnitGroup."""
        super().__init__()
        self.units: list[Unit] = []
    def serialize(self) -> ET.Element:
        """Serialize UnitGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UnitGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize units (list to container "UNITS")
        if self.units:
            wrapper = ET.Element("UNITS")
            for item in self.units:
                serialized = ARObject._serialize_item(item, "Unit")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Parse units (list from container "UNITS")
        obj.units = []
        container = ARObject._find_child_element(element, "UNITS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.units.append(child_value)

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
