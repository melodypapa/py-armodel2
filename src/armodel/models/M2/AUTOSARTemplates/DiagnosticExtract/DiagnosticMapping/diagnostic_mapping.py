"""DiagnosticMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 223)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from abc import ABC, abstractmethod


class DiagnosticMapping(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    provider_ref: Optional[ARRef]
    requester_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticMapping."""
        super().__init__()
        self.provider_ref: Optional[ARRef] = None
        self.requester_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provider_ref
        if self.provider_ref is not None:
            serialized = ARObject._serialize_item(self.provider_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requester_ref
        if self.requester_ref is not None:
            serialized = ARObject._serialize_item(self.requester_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUESTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMapping":
        """Deserialize XML element to DiagnosticMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMapping, cls).deserialize(element)

        # Parse provider_ref
        child = ARObject._find_child_element(element, "PROVIDER-REF")
        if child is not None:
            provider_ref_value = ARRef.deserialize(child)
            obj.provider_ref = provider_ref_value

        # Parse requester_ref
        child = ARObject._find_child_element(element, "REQUESTER-REF")
        if child is not None:
            requester_ref_value = ARRef.deserialize(child)
            obj.requester_ref = requester_ref_value

        return obj



class DiagnosticMappingBuilder:
    """Builder for DiagnosticMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMapping = DiagnosticMapping()

    def build(self) -> DiagnosticMapping:
        """Build and return DiagnosticMapping object.

        Returns:
            DiagnosticMapping instance
        """
        # TODO: Add validation
        return self._obj
