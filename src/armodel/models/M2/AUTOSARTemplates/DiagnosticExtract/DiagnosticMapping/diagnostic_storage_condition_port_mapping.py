"""DiagnosticStorageConditionPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticStorageConditionPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticStorageConditionPortMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_storage_ref: Optional[Any]
    swc_flat_service_ref: Optional[Any]
    swc_service: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionPortMapping."""
        super().__init__()
        self.diagnostic_storage_ref: Optional[Any] = None
        self.swc_flat_service_ref: Optional[Any] = None
        self.swc_service: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticStorageConditionPortMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticStorageConditionPortMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_storage_ref
        if self.diagnostic_storage_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_storage_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-STORAGE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_flat_service_ref
        if self.swc_flat_service_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_flat_service_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-FLAT-SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_service
        if self.swc_service is not None:
            serialized = SerializationHelper.serialize_item(self.swc_service, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageConditionPortMapping":
        """Deserialize XML element to DiagnosticStorageConditionPortMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStorageConditionPortMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticStorageConditionPortMapping, cls).deserialize(element)

        # Parse diagnostic_storage_ref
        child = SerializationHelper.find_child_element(element, "DIAGNOSTIC-STORAGE-REF")
        if child is not None:
            diagnostic_storage_ref_value = ARRef.deserialize(child)
            obj.diagnostic_storage_ref = diagnostic_storage_ref_value

        # Parse swc_flat_service_ref
        child = SerializationHelper.find_child_element(element, "SWC-FLAT-SERVICE-REF")
        if child is not None:
            swc_flat_service_ref_value = ARRef.deserialize(child)
            obj.swc_flat_service_ref = swc_flat_service_ref_value

        # Parse swc_service
        child = SerializationHelper.find_child_element(element, "SWC-SERVICE")
        if child is not None:
            swc_service_value = child.text
            obj.swc_service = swc_service_value

        return obj



class DiagnosticStorageConditionPortMappingBuilder:
    """Builder for DiagnosticStorageConditionPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionPortMapping = DiagnosticStorageConditionPortMapping()

    def build(self) -> DiagnosticStorageConditionPortMapping:
        """Build and return DiagnosticStorageConditionPortMapping object.

        Returns:
            DiagnosticStorageConditionPortMapping instance
        """
        # TODO: Add validation
        return self._obj
