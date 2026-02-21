"""DiagnosticSecurityLevel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class DiagnosticSecurityLevel(DiagnosticCommonElement):
    """AUTOSAR DiagnosticSecurityLevel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    access_data: Optional[PositiveInteger]
    key_size: Optional[PositiveInteger]
    num_failed: Optional[PositiveInteger]
    security_delay: Optional[TimeValue]
    seed_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticSecurityLevel."""
        super().__init__()
        self.access_data: Optional[PositiveInteger] = None
        self.key_size: Optional[PositiveInteger] = None
        self.num_failed: Optional[PositiveInteger] = None
        self.security_delay: Optional[TimeValue] = None
        self.seed_size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSecurityLevel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSecurityLevel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access_data
        if self.access_data is not None:
            serialized = ARObject._serialize_item(self.access_data, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESS-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_size
        if self.key_size is not None:
            serialized = ARObject._serialize_item(self.key_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize num_failed
        if self.num_failed is not None:
            serialized = ARObject._serialize_item(self.num_failed, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUM-FAILED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_delay
        if self.security_delay is not None:
            serialized = ARObject._serialize_item(self.security_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURITY-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize seed_size
        if self.seed_size is not None:
            serialized = ARObject._serialize_item(self.seed_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEED-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecurityLevel":
        """Deserialize XML element to DiagnosticSecurityLevel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSecurityLevel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSecurityLevel, cls).deserialize(element)

        # Parse access_data
        child = ARObject._find_child_element(element, "ACCESS-DATA")
        if child is not None:
            access_data_value = child.text
            obj.access_data = access_data_value

        # Parse key_size
        child = ARObject._find_child_element(element, "KEY-SIZE")
        if child is not None:
            key_size_value = child.text
            obj.key_size = key_size_value

        # Parse num_failed
        child = ARObject._find_child_element(element, "NUM-FAILED")
        if child is not None:
            num_failed_value = child.text
            obj.num_failed = num_failed_value

        # Parse security_delay
        child = ARObject._find_child_element(element, "SECURITY-DELAY")
        if child is not None:
            security_delay_value = child.text
            obj.security_delay = security_delay_value

        # Parse seed_size
        child = ARObject._find_child_element(element, "SEED-SIZE")
        if child is not None:
            seed_size_value = child.text
            obj.seed_size = seed_size_value

        return obj



class DiagnosticSecurityLevelBuilder:
    """Builder for DiagnosticSecurityLevel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecurityLevel = DiagnosticSecurityLevel()

    def build(self) -> DiagnosticSecurityLevel:
        """Build and return DiagnosticSecurityLevel object.

        Returns:
            DiagnosticSecurityLevel instance
        """
        # TODO: Add validation
        return self._obj
