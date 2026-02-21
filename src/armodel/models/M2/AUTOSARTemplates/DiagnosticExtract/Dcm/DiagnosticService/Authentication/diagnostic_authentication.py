"""DiagnosticAuthentication AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 98)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_Authentication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from abc import ABC, abstractmethod


class DiagnosticAuthentication(DiagnosticServiceInstance, ABC):
    """AUTOSAR DiagnosticAuthentication."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    authentication_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthentication."""
        super().__init__()
        self.authentication_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAuthentication to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAuthentication, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentication_ref
        if self.authentication_ref is not None:
            serialized = ARObject._serialize_item(self.authentication_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTHENTICATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthentication":
        """Deserialize XML element to DiagnosticAuthentication object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthentication object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAuthentication, cls).deserialize(element)

        # Parse authentication_ref
        child = ARObject._find_child_element(element, "AUTHENTICATION-REF")
        if child is not None:
            authentication_ref_value = ARRef.deserialize(child)
            obj.authentication_ref = authentication_ref_value

        return obj



class DiagnosticAuthenticationBuilder:
    """Builder for DiagnosticAuthentication."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthentication = DiagnosticAuthentication()

    def build(self) -> DiagnosticAuthentication:
        """Build and return DiagnosticAuthentication object.

        Returns:
            DiagnosticAuthentication instance
        """
        # TODO: Add validation
        return self._obj
