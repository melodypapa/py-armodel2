"""FlexrayNmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 679)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class FlexrayNmEcu(BusspecificNmEcu):
    """AUTOSAR FlexrayNmEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_hw_vote: Optional[Boolean]
    nm_main: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize FlexrayNmEcu."""
        super().__init__()
        self.nm_hw_vote: Optional[Boolean] = None
        self.nm_main: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayNmEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayNmEcu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nm_hw_vote
        if self.nm_hw_vote is not None:
            serialized = ARObject._serialize_item(self.nm_hw_vote, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-HW-VOTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_main
        if self.nm_main is not None:
            serialized = ARObject._serialize_item(self.nm_main, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-MAIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayNmEcu":
        """Deserialize XML element to FlexrayNmEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayNmEcu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayNmEcu, cls).deserialize(element)

        # Parse nm_hw_vote
        child = ARObject._find_child_element(element, "NM-HW-VOTE")
        if child is not None:
            nm_hw_vote_value = child.text
            obj.nm_hw_vote = nm_hw_vote_value

        # Parse nm_main
        child = ARObject._find_child_element(element, "NM-MAIN")
        if child is not None:
            nm_main_value = child.text
            obj.nm_main = nm_main_value

        return obj



class FlexrayNmEcuBuilder:
    """Builder for FlexrayNmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayNmEcu = FlexrayNmEcu()

    def build(self) -> FlexrayNmEcu:
        """Build and return FlexrayNmEcu object.

        Returns:
            FlexrayNmEcu instance
        """
        # TODO: Add validation
        return self._obj
