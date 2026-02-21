"""DiagnosticServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 69)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommonService.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from abc import ABC, abstractmethod


class DiagnosticServiceInstance(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    access_ref: Optional[ARRef]
    service_class_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticServiceInstance."""
        super().__init__()
        self.access_ref: Optional[ARRef] = None
        self.service_class_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access_ref
        if self.access_ref is not None:
            serialized = SerializationHelper.serialize_item(self.access_ref, "DiagnosticAccessPermission")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_class_ref
        if self.service_class_ref is not None:
            serialized = SerializationHelper.serialize_item(self.service_class_ref, "DiagnosticServiceClass")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-CLASS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceInstance":
        """Deserialize XML element to DiagnosticServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticServiceInstance, cls).deserialize(element)

        # Parse access_ref
        child = SerializationHelper.find_child_element(element, "ACCESS-REF")
        if child is not None:
            access_ref_value = ARRef.deserialize(child)
            obj.access_ref = access_ref_value

        # Parse service_class_ref
        child = SerializationHelper.find_child_element(element, "SERVICE-CLASS-REF")
        if child is not None:
            service_class_ref_value = ARRef.deserialize(child)
            obj.service_class_ref = service_class_ref_value

        return obj



class DiagnosticServiceInstanceBuilder:
    """Builder for DiagnosticServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceInstance = DiagnosticServiceInstance()

    def build(self) -> DiagnosticServiceInstance:
        """Build and return DiagnosticServiceInstance object.

        Returns:
            DiagnosticServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
