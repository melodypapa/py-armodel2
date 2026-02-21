"""DiagnosticSession AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm import (
    DiagnosticJumpToBootLoaderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class DiagnosticSession(DiagnosticCommonElement):
    """AUTOSAR DiagnosticSession."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    jump_to_boot: Optional[DiagnosticJumpToBootLoaderEnum]
    p2_server_max: Optional[TimeValue]
    p2_star_server: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize DiagnosticSession."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.jump_to_boot: Optional[DiagnosticJumpToBootLoaderEnum] = None
        self.p2_server_max: Optional[TimeValue] = None
        self.p2_star_server: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSession to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSession, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize id
        if self.id is not None:
            serialized = ARObject._serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize jump_to_boot
        if self.jump_to_boot is not None:
            serialized = ARObject._serialize_item(self.jump_to_boot, "DiagnosticJumpToBootLoaderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("JUMP-TO-BOOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize p2_server_max
        if self.p2_server_max is not None:
            serialized = ARObject._serialize_item(self.p2_server_max, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("P2-SERVER-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize p2_star_server
        if self.p2_star_server is not None:
            serialized = ARObject._serialize_item(self.p2_star_server, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("P2-STAR-SERVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSession":
        """Deserialize XML element to DiagnosticSession object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSession object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSession, cls).deserialize(element)

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse jump_to_boot
        child = ARObject._find_child_element(element, "JUMP-TO-BOOT")
        if child is not None:
            jump_to_boot_value = DiagnosticJumpToBootLoaderEnum.deserialize(child)
            obj.jump_to_boot = jump_to_boot_value

        # Parse p2_server_max
        child = ARObject._find_child_element(element, "P2-SERVER-MAX")
        if child is not None:
            p2_server_max_value = child.text
            obj.p2_server_max = p2_server_max_value

        # Parse p2_star_server
        child = ARObject._find_child_element(element, "P2-STAR-SERVER")
        if child is not None:
            p2_star_server_value = child.text
            obj.p2_star_server = p2_star_server_value

        return obj



class DiagnosticSessionBuilder:
    """Builder for DiagnosticSession."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSession = DiagnosticSession()

    def build(self) -> DiagnosticSession:
        """Build and return DiagnosticSession object.

        Returns:
            DiagnosticSession instance
        """
        # TODO: Add validation
        return self._obj
