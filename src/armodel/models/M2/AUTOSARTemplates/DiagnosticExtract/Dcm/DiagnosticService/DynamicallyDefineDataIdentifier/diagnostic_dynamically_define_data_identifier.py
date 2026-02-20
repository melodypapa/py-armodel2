"""DiagnosticDynamicallyDefineDataIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 127)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineDataIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_dynamic_data_identifier import (
    DiagnosticDynamicDataIdentifier,
)


class DiagnosticDynamicallyDefineDataIdentifier(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_identifier_ref: Optional[ARRef]
    dynamically_ref: Optional[Any]
    max_source: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifier."""
        super().__init__()
        self.data_identifier_ref: Optional[ARRef] = None
        self.dynamically_ref: Optional[Any] = None
        self.max_source: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDynamicallyDefineDataIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDynamicallyDefineDataIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_identifier_ref
        if self.data_identifier_ref is not None:
            serialized = ARObject._serialize_item(self.data_identifier_ref, "DiagnosticDynamicDataIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-IDENTIFIER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dynamically_ref
        if self.dynamically_ref is not None:
            serialized = ARObject._serialize_item(self.dynamically_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMICALLY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_source
        if self.max_source is not None:
            serialized = ARObject._serialize_item(self.max_source, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDynamicallyDefineDataIdentifier":
        """Deserialize XML element to DiagnosticDynamicallyDefineDataIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDynamicallyDefineDataIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDynamicallyDefineDataIdentifier, cls).deserialize(element)

        # Parse data_identifier_ref
        child = ARObject._find_child_element(element, "DATA-IDENTIFIER-REF")
        if child is not None:
            data_identifier_ref_value = ARRef.deserialize(child)
            obj.data_identifier_ref = data_identifier_ref_value

        # Parse dynamically_ref
        child = ARObject._find_child_element(element, "DYNAMICALLY-REF")
        if child is not None:
            dynamically_ref_value = ARRef.deserialize(child)
            obj.dynamically_ref = dynamically_ref_value

        # Parse max_source
        child = ARObject._find_child_element(element, "MAX-SOURCE")
        if child is not None:
            max_source_value = child.text
            obj.max_source = max_source_value

        return obj



class DiagnosticDynamicallyDefineDataIdentifierBuilder:
    """Builder for DiagnosticDynamicallyDefineDataIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDynamicallyDefineDataIdentifier = DiagnosticDynamicallyDefineDataIdentifier()

    def build(self) -> DiagnosticDynamicallyDefineDataIdentifier:
        """Build and return DiagnosticDynamicallyDefineDataIdentifier object.

        Returns:
            DiagnosticDynamicallyDefineDataIdentifier instance
        """
        # TODO: Add validation
        return self._obj
