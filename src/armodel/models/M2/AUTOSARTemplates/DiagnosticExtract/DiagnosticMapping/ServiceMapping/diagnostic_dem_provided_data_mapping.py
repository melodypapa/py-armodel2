"""DiagnosticDemProvidedDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 255)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticDemProvidedDataMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticDemProvidedDataMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_element_ref: Optional[ARRef]
    data_provider: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize DiagnosticDemProvidedDataMapping."""
        super().__init__()
        self.data_element_ref: Optional[ARRef] = None
        self.data_provider: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDemProvidedDataMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDemProvidedDataMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = ARObject._serialize_item(self.data_element_ref, "DiagnosticDataElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_provider
        if self.data_provider is not None:
            serialized = ARObject._serialize_item(self.data_provider, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-PROVIDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDemProvidedDataMapping":
        """Deserialize XML element to DiagnosticDemProvidedDataMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDemProvidedDataMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDemProvidedDataMapping, cls).deserialize(element)

        # Parse data_element_ref
        child = ARObject._find_child_element(element, "DATA-ELEMENT-REF")
        if child is not None:
            data_element_ref_value = ARRef.deserialize(child)
            obj.data_element_ref = data_element_ref_value

        # Parse data_provider
        child = ARObject._find_child_element(element, "DATA-PROVIDER")
        if child is not None:
            data_provider_value = child.text
            obj.data_provider = data_provider_value

        return obj



class DiagnosticDemProvidedDataMappingBuilder:
    """Builder for DiagnosticDemProvidedDataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDemProvidedDataMapping = DiagnosticDemProvidedDataMapping()

    def build(self) -> DiagnosticDemProvidedDataMapping:
        """Build and return DiagnosticDemProvidedDataMapping object.

        Returns:
            DiagnosticDemProvidedDataMapping instance
        """
        # TODO: Add validation
        return self._obj
