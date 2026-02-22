"""DiagnosticCapabilityElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 236)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 753)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticAudienceEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DiagRequirementIdString,
    PositiveInteger,
)
from abc import ABC, abstractmethod


class DiagnosticCapabilityElement(ServiceNeeds, ABC):
    """AUTOSAR DiagnosticCapabilityElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    audiences: list[DiagnosticAudienceEnum]
    diag: Optional[DiagRequirementIdString]
    security_access: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticCapabilityElement."""
        super().__init__()
        self.audiences: list[DiagnosticAudienceEnum] = []
        self.diag: Optional[DiagRequirementIdString] = None
        self.security_access: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticCapabilityElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticCapabilityElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize audiences (list to container "AUDIENCES")
        if self.audiences:
            wrapper = ET.Element("AUDIENCES")
            for item in self.audiences:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticAudienceEnum")
                if serialized is not None:
                    child_elem = ET.Element("AUDIENCE")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize diag
        if self.diag is not None:
            serialized = SerializationHelper.serialize_item(self.diag, "DiagRequirementIdString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_access
        if self.security_access is not None:
            serialized = SerializationHelper.serialize_item(self.security_access, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURITY-ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCapabilityElement":
        """Deserialize XML element to DiagnosticCapabilityElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCapabilityElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticCapabilityElement, cls).deserialize(element)

        # Parse audiences (list from container "AUDIENCES")
        obj.audiences = []
        container = SerializationHelper.find_child_element(element, "AUDIENCES")
        if container is not None:
            for child in container:
                # Extract enum value (DiagnosticAudienceEnum)
                child_value = DiagnosticAudienceEnum.deserialize(child)
                if child_value is not None:
                    obj.audiences.append(child_value)

        # Parse diag
        child = SerializationHelper.find_child_element(element, "DIAG")
        if child is not None:
            diag_value = child.text
            obj.diag = diag_value

        # Parse security_access
        child = SerializationHelper.find_child_element(element, "SECURITY-ACCESS")
        if child is not None:
            security_access_value = child.text
            obj.security_access = security_access_value

        return obj



