"""DiagnosticDataByIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_data_identifier import (
    DiagnosticAbstractDataIdentifier,
)
from abc import ABC, abstractmethod


class DiagnosticDataByIdentifier(DiagnosticServiceInstance, ABC):
    """AUTOSAR DiagnosticDataByIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    data_identifier: Optional[DiagnosticAbstractDataIdentifier]
    def __init__(self) -> None:
        """Initialize DiagnosticDataByIdentifier."""
        super().__init__()
        self.data_identifier: Optional[DiagnosticAbstractDataIdentifier] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDataByIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDataByIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_identifier
        if self.data_identifier is not None:
            serialized = ARObject._serialize_item(self.data_identifier, "DiagnosticAbstractDataIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataByIdentifier":
        """Deserialize XML element to DiagnosticDataByIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataByIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDataByIdentifier, cls).deserialize(element)

        # Parse data_identifier
        child = ARObject._find_child_element(element, "DATA-IDENTIFIER")
        if child is not None:
            data_identifier_value = ARObject._deserialize_by_tag(child, "DiagnosticAbstractDataIdentifier")
            obj.data_identifier = data_identifier_value

        return obj



class DiagnosticDataByIdentifierBuilder:
    """Builder for DiagnosticDataByIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataByIdentifier = DiagnosticDataByIdentifier()

    def build(self) -> DiagnosticDataByIdentifier:
        """Build and return DiagnosticDataByIdentifier object.

        Returns:
            DiagnosticDataByIdentifier instance
        """
        # TODO: Add validation
        return self._obj
