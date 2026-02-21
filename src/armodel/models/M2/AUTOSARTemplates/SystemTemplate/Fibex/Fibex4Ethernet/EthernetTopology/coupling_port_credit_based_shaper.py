"""CouplingPortCreditBasedShaper AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2013)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortCreditBasedShaper(Identifiable):
    """AUTOSAR CouplingPortCreditBasedShaper."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    idle_slope: Optional[PositiveInteger]
    lower_boundary: Optional[PositiveInteger]
    upper_boundary: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CouplingPortCreditBasedShaper."""
        super().__init__()
        self.idle_slope: Optional[PositiveInteger] = None
        self.lower_boundary: Optional[PositiveInteger] = None
        self.upper_boundary: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CouplingPortCreditBasedShaper to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CouplingPortCreditBasedShaper, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize idle_slope
        if self.idle_slope is not None:
            serialized = ARObject._serialize_item(self.idle_slope, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDLE-SLOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lower_boundary
        if self.lower_boundary is not None:
            serialized = ARObject._serialize_item(self.lower_boundary, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-BOUNDARY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_boundary
        if self.upper_boundary is not None:
            serialized = ARObject._serialize_item(self.upper_boundary, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-BOUNDARY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortCreditBasedShaper":
        """Deserialize XML element to CouplingPortCreditBasedShaper object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CouplingPortCreditBasedShaper object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CouplingPortCreditBasedShaper, cls).deserialize(element)

        # Parse idle_slope
        child = ARObject._find_child_element(element, "IDLE-SLOPE")
        if child is not None:
            idle_slope_value = child.text
            obj.idle_slope = idle_slope_value

        # Parse lower_boundary
        child = ARObject._find_child_element(element, "LOWER-BOUNDARY")
        if child is not None:
            lower_boundary_value = child.text
            obj.lower_boundary = lower_boundary_value

        # Parse upper_boundary
        child = ARObject._find_child_element(element, "UPPER-BOUNDARY")
        if child is not None:
            upper_boundary_value = child.text
            obj.upper_boundary = upper_boundary_value

        return obj



class CouplingPortCreditBasedShaperBuilder:
    """Builder for CouplingPortCreditBasedShaper."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortCreditBasedShaper = CouplingPortCreditBasedShaper()

    def build(self) -> CouplingPortCreditBasedShaper:
        """Build and return CouplingPortCreditBasedShaper object.

        Returns:
            CouplingPortCreditBasedShaper instance
        """
        # TODO: Add validation
        return self._obj
